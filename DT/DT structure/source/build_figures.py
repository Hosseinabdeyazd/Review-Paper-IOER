from pathlib import Path
from html import escape
import math, json, subprocess, os
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor

ROOT=Path(__file__).resolve().parents[1]
FIG=ROOT/'figures'; FIG.mkdir(parents=True,exist_ok=True)
for n,f in [('Serif','times.ttf'),('SerifBold','timesbd.ttf'),('SerifItalic','timesi.ttf')]:
    pdfmetrics.registerFont(TTFont(n,str(Path('C:/Windows/Fonts')/f)))
C={'ink':'#26364A','muted':'#687282','blue':'#355C7D','teal':'#356B70','plum':'#795269','ochre':'#936637','paper':'#FFFFFF','line':'#88929E','pale':'#F4F6F8','bp':'#F0F4F8','tp':'#F0F6F5','pp':'#F7F1F5','op':'#FAF5EF'}

class Figure:
    def __init__(self,name,w,h,width_mm=190):
        self.name=name; self.w=w; self.h=h; self.svg=[]
        self.scale=width_mm*72/25.4/w
        self.pdf=canvas.Canvas(str(FIG/(name+'.pdf')),pagesize=(w*self.scale,h*self.scale),pageCompression=1)
        self.pdf.setTitle(name.replace('_',' ')); self.pdf.setAuthor('Review Paper IOER project')
        self.pdf.scale(self.scale,self.scale)
        self.rect(0,0,w,h,fill='#FFFFFF',stroke=None)
    def style(self,stroke,fill,lw=1,dash=None):
        p=self.pdf; p.setLineWidth(lw); p.setDash(dash or [])
        if stroke:p.setStrokeColor(HexColor(stroke))
        if fill:p.setFillColor(HexColor(fill))
    def rect(self,x,y,w,h,fill='#FFFFFF',stroke=C['line'],lw=1,r=0,dash=None):
        self.style(stroke,fill,lw,dash)
        self.pdf.roundRect(x,self.h-y-h,w,h,r,stroke=int(bool(stroke)),fill=int(bool(fill)))
        self.svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill or "none"}" stroke="{stroke or "none"}" stroke-width="{lw}"'+(f' stroke-dasharray="{",".join(map(str,dash))}"' if dash else '')+'/>' )
    def text(self,x,y,s,size=20,bold=False,color=C['ink'],anchor='start',italic=False):
        font='SerifBold' if bold else ('SerifItalic' if italic else 'Serif')
        self.pdf.setFont(font,size);self.pdf.setFillColor(HexColor(color))
        for i,line in enumerate(s.split('\n')):
            yy=y+i*size*1.22
            if anchor=='middle':self.pdf.drawCentredString(x,self.h-yy-size*.82,line)
            elif anchor=='end':self.pdf.drawRightString(x,self.h-yy-size*.82,line)
            else:self.pdf.drawString(x,self.h-yy-size*.82,line)
            self.svg.append(f'<text x="{x}" y="{yy+size*.82}" font-family="Times New Roman, Liberation Serif, serif" font-size="{size}" font-weight="{"bold" if bold else "normal"}" font-style="{"italic" if italic else "normal"}" text-anchor="{anchor}" fill="{color}">{escape(line)}</text>')
    def poly(self,pts,fill=None,stroke=C['line'],lw=1,dash=None,closed=False):
        self.style(stroke,fill,lw,dash); p=self.pdf.beginPath();p.moveTo(pts[0][0],self.h-pts[0][1])
        for x,y in pts[1:]:p.lineTo(x,self.h-y)
        if closed:p.close()
        self.pdf.drawPath(p,stroke=int(bool(stroke)),fill=int(bool(fill)))
        tag='polygon' if closed else 'polyline'
        self.svg.append(f'<{tag} points="'+ ' '.join(f'{x},{y}' for x,y in pts)+f'" fill="{fill or "none"}" stroke="{stroke or "none"}" stroke-width="{lw}" stroke-linejoin="round"'+(f' stroke-dasharray="{",".join(map(str,dash))}"' if dash else '')+'/>' )
    def arrow(self,pts,color=C['line'],lw=1.6,dash=None,both=False):
        self.poly(pts,stroke=color,lw=lw,dash=dash)
        for a,b in [(pts[-2],pts[-1])]+([(pts[1],pts[0])] if both else []):
            ang=math.atan2(b[1]-a[1],b[0]-a[0]); L=9; W=4
            self.poly([b,(b[0]-L*math.cos(ang)+W*math.sin(ang),b[1]-L*math.sin(ang)-W*math.cos(ang)),(b[0]-L*math.cos(ang)-W*math.sin(ang),b[1]-L*math.sin(ang)+W*math.cos(ang))],fill=color,stroke=None,closed=True)
    def curve(self,x1,y1,x2,y2,color='#A8ADB5',lw=.65):
        dx=(x2-x1)*.45; self.style(color,None,lw)
        p=self.pdf.beginPath();p.moveTo(x1,self.h-y1);p.curveTo(x1+dx,self.h-y1,x2-dx,self.h-y2,x2,self.h-y2);self.pdf.drawPath(p)
        self.svg.append(f'<path d="M{x1},{y1} C{x1+dx},{y1} {x2-dx},{y2} {x2},{y2}" fill="none" stroke="{color}" stroke-width="{lw}"/>')
    def box(self,x,y,w,h,title,body='',color=C['blue'],fill=C['bp'],size=20):
        self.rect(x,y,w,h,fill=fill,stroke=color,lw=1.5,r=3)
        ts=min(size,size*(w-32)/max(1,pdfmetrics.stringWidth(title,'SerifBold',size)))
        self.text(x+16,y+14,title,ts,bold=True,color=color)
        if body:
            bs=size-2
            bs=min(bs,bs*(w-32)/max(pdfmetrics.stringWidth(s,'Serif',bs) for s in body.split('\n')))
            self.text(x+16,y+44,body,bs)
    def diamond(self,x,y,w,h,label,color=C['ochre']):
        self.poly([(x+w/2,y),(x+w,y+h/2),(x+w/2,y+h),(x,y+h/2)],fill=C['op'],stroke=color,lw=1.5,closed=True)
        lines=len(label.split('\n'));self.text(x+w/2,y+h/2-lines*19*1.22/2,label,19,anchor='middle')
    def heading(self,k,title,sub):
        self.text(45,26,k,17,bold=True,color=C['muted']);self.text(45,53,title,30,bold=True)
        self.text(45,94,sub,17,color=C['muted'])
    def save(self):
        self.pdf.save()
        (FIG/(self.name+'.svg')).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="190mm" height="{self.h/self.w*190:.3f}mm" viewBox="0 0 {self.w} {self.h}" role="img"><title>{escape(self.name.replace("_"," "))}</title>'+''.join(self.svg)+'</svg>',encoding='utf-8')

def main():
    f=Figure('figure_1_design_to_use',1100,1280)
    f.heading('FIGURE 1  |  PROPOSED SYNTHESIS','From digital twin design to evidence-informed decisions','Design choices specify an implementation; model activities act on its data and executable models.')
    f.box(55,137,990,102,'A  Design brief + decision specification','Object and scope | Purpose | Architecture intent | Data needs | Required services\nDecision subject, alternatives, objectives, horizon, evidence and authority. [R1, R2, R5, R6]',size=21)
    f.arrow([(290,239),(290,278)]); f.arrow([(810,239),(810,278)])
    f.box(55,278,440,100,'B  Configuration choices','Composition, architecture, models, coupling,\nagency and timing. See Figure S2.',size=21)
    f.box(605,278,440,100,'C  Functional allocation','Allocate activities to components and people;\ndefine inputs, methods, outputs and timing. [R2, R6]',color=C['plum'],fill=C['pp'],size=21)
    f.arrow([(495,324),(605,324)],both=True);f.text(550,343,'co-design',16,anchor='middle',color=C['muted'])
    f.arrow([(290,378),(290,410),(550,410),(550,447)]);f.poly([(810,378),(810,410),(550,410)],lw=1.6)
    f.text(55,409,'DESIGN ARTIFACTS',16,bold=True,color=C['muted'])
    f.box(55,447,990,102,'Implemented digital twin','Executable models + data pipelines + services + interfaces + assigned roles\nB describes its configuration; C specifies where required activities run. [R1, R2]',color=C['teal'],fill=C['tp'],size=21)
    f.text(635,572,'ASSESS AND MAINTAIN FITNESS\nFOR THE INTENDED USE',17,bold=True,color=C['muted'])
    f.arrow([(185,549),(185,625)]);f.arrow([(485,549),(485,625)])
    f.box(55,625,260,109,'Calibrate, if needed','Fit model parameters\nusing observations.\nBefore or during use. [R3, R11]',color=C['teal'],fill=C['tp'],size=20)
    f.box(365,625,260,109,'Verify and validate','Implementation checks;\nevaluate model adequacy\nwith use-specific evidence. [R12]',color=C['teal'],fill=C['tp'],size=20)
    f.arrow([(315,678),(365,678)]);f.arrow([(625,678),(676,678)])
    f.diamond(676,614,168,128,'Criteria met\nfor this use?')
    f.arrow([(844,678),(890,678)]);f.text(854,655,'No',17,color=C['ochre'])
    f.box(890,625,155,109,'Diagnose','Data, parameters,\nmodel form or\ndesign limitations.',color=C['ochre'],fill=C['op'],size=19)
    f.arrow([(1045,678),(1070,678),(1070,497),(1045,497)],color=C['ochre'])
    f.text(55,759,'Calibration does not establish validity. Reassess after revisions.\nA failed check need not mean recalibration.',16,color=C['muted'])
    f.text(55,807,'USE THE TWIN FOR THE DECISION DEFINED IN A',17,bold=True,color=C['muted'])
    f.arrow([(760,742),(760,847),(190,847),(190,887)],color=C['teal']);f.text(770,772,'Yes: within assessed scope',17,color=C['teal'])
    f.box(55,887,270,110,'Estimate / predict','Observations and models\nproduce decision-relevant\nquantities, when required. [R3]',size=21)
    f.box(415,887,270,110,'Compare / optimize','Evaluate alternatives against\nobjectives and constraints,\nwhen required. [R7-R10, R13]',size=21)
    f.box(775,887,270,110,'Select / approve','Human or delegated role;\napply the authority and\nlimits specified in A. [R6]',color=C['plum'],fill=C['pp'],size=21)
    f.arrow([(325,941),(415,941)]);f.arrow([(685,941),(775,941)])
    f.arrow([(910,997),(910,1030),(550,1030),(550,1060)])
    f.box(55,1060,990,92,'Decision outputs depend on the use case','Design choice | Maintenance or recovery plan | Operating schedule | Recommendation\nPhysical command only where execution is authorized. Observe outcomes after implementation. [R5, R6, R9, R13]',color=C['plum'],fill=C['pp'],size=21)
    f.text(55,1175,'Arrows show the proposed design and evidence relations, not a compulsory lifecycle sequence.',17,color=C['muted'])
    f.text(55,1202,'Monitoring can be an end service. Prediction, optimization and physical control are not mandatory for every use case.',17,color=C['muted'])
    f.text(55,1234,'The layout and A-B-C organization are our synthesis. Reference keys and evidence limits: papers/academic-foundations.md.',16,color=C['muted'])
    f.save()

def brief():
    f=Figure('figure_S1_design_brief',1100,1270)
    f.heading('FIGURE S1  |  A: DESIGN BRIEF','Define the problem before selecting the configuration','Five framing concerns and a shared decision specification; an adaptation, not a published five-part taxonomy.')
    cards=[('1  Twinning object & scope','What is represented?','Which entity, process or system?\nWhat are its boundaries and interactions?\nWhich states, behaviours and scales matter?','OUTPUT  Counterpart, scope and required detail.','R1, R5',C['blue'],C['bp']),('2  Purpose','Why is the twin needed?','Which problem or decision must it support?\nWho uses it, and what value is expected?\nWhat objectives and constraints define success?','OUTPUT  Intended use and success criteria.','R1, R5',C['ochre'],C['op']),('3  System architecture brief','What solution is envisaged?','Which capabilities, models and components?\nWhich interfaces and deployment constraints?\nWho analyses, selects, approves and executes?','OUTPUT  Architectural intent and responsibilities.','R1, R2, R6',C['plum'],C['pp']),('4  Data requirements','What evidence and information are needed?','Which sources, meanings and quality levels?\nWhat timing, coverage and uncertainty?\nHow are fitting and evaluation data managed?','OUTPUT  Data needs and evidence arrangements.','R1, R3, R12',C['teal'],C['tp'])]
    for i,(title,q,questions,out,refs,col,fill) in enumerate(cards):
        x=55+(i%2)*515;y=145+(i//2)*238
        f.box(x,y,475,215,title,'',color=col,fill=fill,size=23)
        f.text(x+18,y+48,q,19,italic=True,color=C['muted'])
        f.text(x+18,y+81,questions,20)
        f.poly([(x+18,y+162),(x+457,y+162)],stroke='#D5DAE0')
        f.text(x+18,y+177,out,17);f.text(x+457,y+195,'['+refs+']',15,anchor='end',color=C['muted'])
    f.box(55,621,990,150,'5  Service requirements','What must the twin deliver, to whom, and within which performance and authority limits?\nMonitoring | Diagnosis | Prediction | Scenario analysis | Recommendations | Permitted actions\nOUTPUT  Required outputs, recipients, delivery mode and acceptance conditions. [R1, R5, R6]',color=C['blue'],fill=C['bp'],size=23)
    f.text(55,802,'DECISION SPECIFICATION  |  SHARED ACROSS THE FIVE CONCERNS',20,bold=True,color=C['plum'])
    items=[('Subject','Twin design, model credibility,\nor a decision about the target?'),('Alternatives','What may be selected or changed?\nSpecify the decision variables.'),('Objectives & constraints','What is improved, and which\nlimits must be respected?'),('Scope & horizon','Which entities and interactions?\nOver what consequence horizon?'),('Required evidence','Which observations, predictions\nand credibility evidence?'),('Responsibility & authority','Who analyses, chooses, approves\nand implements the decision?')]
    for i,(title,body) in enumerate(items):
        x=55+(i%3)*337;y=843+(i//3)*132
        f.box(x,y,316,112,title,body,color=C['plum'],fill=C['pp'],size=21)
    f.text(55,1131,'A informs both B (configuration choices) and C (functional allocation). Design can be iterated.',19,bold=True,color=C['blue'])
    f.text(55,1172,'The five-card arrangement and six-field decision specification are proposed synthesis.',18,color=C['muted'])
    f.text(55,1200,'Xiong et al. [R1] distinguish object, purpose, architecture, data, modelling and services; these are not B\'s six axes.',17,color=C['muted'])
    f.text(55,1230,'The decision subject, not system size alone, determines evidence needs and appropriate authority. [R5, R6, R13]',17,color=C['muted'])
    f.save()

def configuration():
    f=Figure('figure_S2_configuration_choices',1200,1020)
    f.heading('FIGURE S2  |  B: CONFIGURATION CHOICES','A working vocabulary of digital twin configurations','Six families of descriptors; neither sequential stages nor mutually exclusive classes.')
    columns=[('System\ncomposition',['Single Twin','Aggregate','Composite','Network','Federated','Ecosystem'],['R3','R2, R16','R16','R16','R8, R16','R16'],C['blue'],C['bp']),('Internal\narchitecture',['Layered','Modular','Service-\noriented','Knowledge\ngraph'],['R1','R2, R15','R1, R15','R15'],C['teal'],C['tp']),('Computational\nmodel',['Physics-\nbased','Data-driven','Hybrid','Multiscale *'],['R1, R4','R1, R10','R1, R4','U'],C['blue'],C['bp']),('Coupling &\ncontrol',['One-way *','Bidirectional','Human-\nmediated *','Automated\nclosed-loop'],['R14','R14','R6','R10'],C['ochre'],C['op']),('Agency &\nintelligence',['Rule-based *','Agent-based *','Multi-agent','Agentic AI *'],['U','R8','R8','U'],C['plum'],C['pp']),('Temporal\norganization',['Continuous *','Periodic','Event-driven *','Multi-rate *'],['U','R5','U','U'],C['blue'],C['bp'])]
    positions=[]
    for j,(_,nodes,_,_,_) in enumerate(columns):
        x=45+j*199;ys=[465+(i-(len(nodes)-1)/2)*80 for i in range(len(nodes))];positions.append((x,ys))
    for j in range(5):
        x,ys=positions[j];nx,nys=positions[j+1]
        for y in ys:
            for ny in nys:f.curve(x+122,y,nx,ny,color='#A0A8B2',lw=.75)
    for j,(title,nodes,refs,col,fill) in enumerate(columns):
        x,ys=positions[j];f.text(x+61,156,title,22,anchor='middle',bold=True,color=col)
        f.poly([(x,216),(x+122,216)],stroke='#D4DAE0')
        for label,ref,y in zip(nodes,refs,ys):
            f.rect(x,y-32,122,64,fill=fill,stroke=col,lw=1.5,r=3,dash=[4,3] if ref=='U' else None)
            lines=label.split('\n');size=19 if len(label.replace('\n',''))<17 else 17
            size=min(size,min(110/max(1,pdfmetrics.stringWidth(s,'Serif',size))*size for s in lines))
            f.text(x+61,y-25 if len(lines)>1 else y-17,label,size,anchor='middle')
            f.text(x+61,y+16,'['+ref+']',13,anchor='middle',color=C['muted'])
    f.text(45,723,'HOW TO READ THE CONNECTIONS',19,bold=True)
    f.text(45,755,'Curves enumerate candidate pairings between neighbouring columns for visual exploration only.',20)
    f.text(45,783,'They do not encode execution order, proven compatibility, empirical frequency or a complete dependency graph.',19)
    f.rect(45,829,1110,125,fill=C['pale'],stroke='#D5DAE0',r=3)
    f.text(62,846,'*  Refine before treating these terms as formal categories.',19,bold=True)
    f.text(62,877,'Separate model basis from scale; data direction from authority and feedback; agent roles from simulation models.',18)
    f.text(62,904,'Separate timing guarantees, update triggers and rates. One-way is a Digital Shadow in Kritzinger et al. [R14].',18)
    f.text(62,931,'[U]  Exact descriptor not substantiated in this selected source set. Dashed borders identify these open items.',17,color=C['muted'])
    f.text(45,980,'The six-family arrangement is proposed synthesis. References support terms or examples, not every connecting curve.',17,color=C['muted'])
    f.save()

def allocation():
    f=Figure('figure_S3_functional_allocation',1200,1030)
    f.heading('FIGURE S3  |  C: FUNCTIONAL ALLOCATION','Locate activities in the implemented twin','A specifies the need; B constrains implementation; C allocates the required work. The rows are not stages.')
    xs=[45,215,455,740,1155];y=152
    headers=['Activity','Consumes','Changes / produces','Allocation and links to B']
    for i,t in enumerate(headers):
        f.rect(xs[i],y,xs[i+1]-xs[i],60,fill=C['blue'],stroke='#FFFFFF');f.text(xs[i]+13,y+19,t,21,bold=True,color='#FFFFFF')
    rows=[('Calibration\n[R3, R11]','Observations; model;\nadjustable parameters;\nfit criterion.','Changes model parameters;\nproduces fitted values and\nassociated uncertainty.','Model-update component.\nModel basis, data interfaces,\nupdate timing and coordination.'),('Validation\n[R12]','Model version; evaluation\nevidence; intended use;\nacceptance criteria.','Assesses adequacy for the use;\nproduces evidence and limits.\nDoes not itself tune results.','Evaluation capability and owner.\nModels, interfaces and timing;\nsystem-level interactions.'),('Prediction\n[R3, R10]','Model; current state;\ninputs, scenarios and\nprediction horizon.','Estimates future or unobserved\nquantities, with uncertainty\nwhere characterized.','Inference / simulation service.\nModel choice, computation,\ncoordination and delivery timing.'),('Optimization\n[R7-R10, R13]','Decision variables;\nobjectives; constraints;\na way to evaluate options.','Searches decision alternatives;\nreturns candidates or trade-offs.\nDoes not imply physical action.','Optimization service + decision role.\nModels, architecture, coordination,\nlatency and authority requirements.'),('Control\n[R6, R10]','Observed / estimated state;\nreference or objective;\ncontrol law; allowed actions.','Determines control inputs;\nwhen executed, changes the\nbehaviour of the target.','Controller + execution interface.\nCoupling, feedback, timing,\nresponsibility and limits.')]
    for r,row in enumerate(rows):
        yy=212+r*125
        for i,t in enumerate(row):
            f.rect(xs[i],yy,xs[i+1]-xs[i],125,fill=C['pale'] if r%2==0 else '#FFFFFF',stroke='#DCE1E6',lw=.8)
            f.text(xs[i]+13,yy+22,t,21 if i==0 else 19,bold=i==0,color=C['blue'] if i==0 else C['ink'])
    f.text(45,862,'Verification checks implementation and specified requirements; validation addresses fitness for intended use. [R12]',18)
    f.text(45,895,'Architecture descriptors are not calibrated. Activities operate on models, data or decision variables in an implementation.',18,bold=True)
    f.text(45,929,'Mappings to B are proposed design implications, not a universal allocation matrix. Any family may be affected in context.',18,color=C['muted'])
    f.text(45,961,'The optimization target must be explicit: fitting model parameters differs from choosing a maintenance plan or control input.',18,color=C['muted'])
    f.text(45,994,'Execution may be internal, an external service or a human responsibility. Specify interfaces, triggers, ownership and evidence.',17,color=C['muted'])
    f.save()

if __name__=='__main__':
    main();brief();configuration();allocation()
    print('Created four SVG and four vector PDF figures in',FIG)
