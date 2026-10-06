from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw

ROOT=Path(__file__).resolve().parents[1]
FIG=ROOT/"figure"
PANELS=FIG/"panels"
FIG.mkdir(parents=True,exist_ok=True)
PANELS.mkdir(parents=True,exist_ok=True)

P={"broad":"#4C78A8","uncertainty":"#72B7B2","highlight":"#9D755D","neutral":"#7F7F7F","soft":"#B8B8B8","grid":"#D9D9D9","text":"#2F2F2F"}

plt.rcParams.update({"font.size":10,"axes.titlesize":12,"axes.labelsize":10,"axes.labelcolor":P["text"],"axes.edgecolor":P["text"],"xtick.color":P["text"],"ytick.color":P["text"],"text.color":P["text"],"legend.fontsize":9})

def style(ax):
    ax.grid(axis="y",color=P["grid"],linewidth=.7)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

def labels(ax,bars,fmt="{:.0f}",fs=9):
    for b in bars:
        h=b.get_height()
        ax.annotate(fmt.format(h),(b.get_x()+b.get_width()/2,h),xytext=(0,3),textcoords="offset points",ha="center",va="bottom",fontsize=fs)

def save_panel(fig,name):
    p=PANELS/name
    fig.savefig(p,dpi=220,bbox_inches="tight",facecolor="white")
    plt.close(fig)
    return p

def compose(paths,out,title,footer):
    ims=[Image.open(p).convert("RGB") for p in paths]
    mw=max(i.width for i in ims); mh=max(i.height for i in ims)
    norm=[]
    for im in ims:
        c=Image.new("RGB",(mw,mh),"white"); c.paste(im,((mw-im.width)//2,(mh-im.height)//2)); norm.append(c)
    gap=20; th=110; fh=90
    c=Image.new("RGB",(mw*2+gap*3,mh*2+gap*3+th+fh),"white")
    xy=[(gap,th+gap),(mw+gap*2,th+gap),(gap,th+mh+gap*2),(mw+gap*2,th+mh+gap*2)]
    for im,pos in zip(norm,xy): c.paste(im,pos)
    d=ImageDraw.Draw(c); d.text((gap,25),title,fill=P["text"]);\n    if footer: d.text((gap,c.height-fh+20),footer,fill=P["text"])
    c.save(out,dpi=(300,300))

exclusive_labels=["S1 only","S2 only","S3 only","S1∩S2 only","S2∩S3 only","S1∩S3 only","All three"]
exclusive=np.array([835,175,129,37,30,2,4])
density_labels=["S1→S2","S2→S3","S1→S3","S1→S2→S3"]; jb=np.array([3.79,9.02,.58,.33]); ju=np.array([3.09,12.05,.99,.30])
periods=["≤2014","2015–2019","2020–2022","2023–2026"]
s12b=[0,0,10,31]; s23b=[1,10,6,17]; s13b=[0,0,1,5]; trib=[0,0,1,3]
s12u=[0,0,4,5]; s23u=[1,3,1,5]; triu=[0,0,1,0]; w=.34

fig,ax=plt.subplots(figsize=(6.5,4.8)); x=np.arange(len(exclusive_labels))
bars=ax.bar(x,exclusive,color=[P["broad"]]*3+[P["highlight"]]*4); labels(ax,bars)
ax.set_yscale("log"); ax.set_xticks(x); ax.set_xticklabels(exclusive_labels,rotation=25,ha="right"); ax.set_ylabel("Records (log)"); ax.set_title("A  Exclusive stage membership",loc="left",fontweight="bold"); style(ax)
p1=save_panel(fig,"F2_A_exclusive_membership.png")

fig,ax=plt.subplots(figsize=(6.5,4.8)); x=np.arange(4)
a=ax.bar(x-w/2,jb,w,color=P["broad"],label="Broad Jaccard"); b=ax.bar(x+w/2,ju,w,color=P["uncertainty"],label="U-layer Jaccard")
labels(ax,a,"{:.2f}",8); labels(ax,b,"{:.2f}",8)
ax.set_xticks(x); ax.set_xticklabels(density_labels); ax.set_ylabel("Jaccard (%)"); ax.set_title("B  Size-adjusted transition density",loc="left",fontweight="bold"); ax.legend(frameon=False); style(ax)
p2=save_panel(fig,"F2_B_jaccard_density.png")

fig,ax=plt.subplots(figsize=(6.5,4.8)); x=np.arange(4); bw=.18
for off,v,n,c in [(-1.5*bw,s12b,"S1→S2",P["broad"]),(-.5*bw,s23b,"S2→S3",P["highlight"]),(.5*bw,s13b,"S1→S3",P["neutral"]),(1.5*bw,trib,"All three",P["soft"])]: ax.bar(x+off,v,bw,label=n,color=c)
ax.set_xticks(x); ax.set_xticklabels(periods); ax.set_ylabel("Bridge records"); ax.set_title("C  Temporal emergence of broad bridges",loc="left",fontweight="bold"); ax.legend(frameon=False,ncol=2); style(ax)
p3=save_panel(fig,"F2_C_temporal_broad_bridges.png")

fig,ax=plt.subplots(figsize=(6.5,4.8)); x=np.arange(4); bw=.24
for off,v,n,c in [(-bw,s12u,"S1→S2",P["uncertainty"]),(0,s23u,"S2→S3",P["highlight"]),(bw,triu,"All three",P["neutral"])]: ax.bar(x+off,v,bw,label=n,color=c)
ax.set_xticks(x); ax.set_xticklabels(periods); ax.set_ylabel("U-layer bridges"); ax.set_title("D  Temporal emergence of uncertainty-oriented bridges",loc="left",fontweight="bold"); ax.legend(frameon=False); style(ax)
p4=save_panel(fig,"F2_D_temporal_uncertainty_bridges.png")

compose([p1,p2,p3,p4],FIG/"Figure_02_Integration_Depth_and_Temporal_Emergence.png","Integration depth and temporal emergence of bridge papers","")
