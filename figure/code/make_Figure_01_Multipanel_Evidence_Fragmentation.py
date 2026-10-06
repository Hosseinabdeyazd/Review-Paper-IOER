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

stage_labels=["S1\nObservation / GeoAI","S2\nMaterial stock","S3\nStock dynamics"]
stage_broad=np.array([878,246,165]); stage_u=np.array([256,44,48]); stage_share=stage_u/stage_broad*100
bridge_labels=["S1→S2","S2→S3","S1→S3","S1→S2→S3"]
bridge_broad=np.array([41,34,6,4]); bridge_u=np.array([9,10,3,1]); bridge_share=bridge_u/bridge_broad*100
ret_labels=["S1→S2\nfrom S1","S2→S3\nfrom S2","Triple\nfrom S1","Triple\nfrom S2","Triple\nfrom S3"]
ret_b=np.array([41/878*100,34/246*100,4/878*100,4/246*100,4/165*100])
ret_u=np.array([9/256*100,10/44*100,1/256*100,1/44*100,1/48*100])
noise_stage=["S1","S2","S3"]; full=np.array([29.2,17.9,29.1]); sens=np.array([28.7,17.5,26.8]); w=.34

fig,ax=plt.subplots(figsize=(6.3,4.7)); x=np.arange(3)
a=ax.bar(x-w/2,stage_broad,w,color=P["broad"],label="Broad (Sb)"); b=ax.bar(x+w/2,stage_u,w,color=P["uncertainty"],label="Uncertainty (Su)")
labels(ax,a); labels(ax,b)
ax.set_xticks(x); ax.set_xticklabels(stage_labels); ax.set_ylabel("Records"); ax.set_title("A  Stage-level evidence base",loc="left",fontweight="bold"); ax.legend(frameon=False,ncol=2); style(ax)
p1=save_panel(fig,"F1_A_stage_counts.png")

fig,ax=plt.subplots(figsize=(6.3,4.7)); x=np.arange(4)
a=ax.bar(x-w/2,bridge_broad,w,color=P["broad"],label="Broad candidates"); b=ax.bar(x+w/2,bridge_u,w,color=P["uncertainty"],label="U-layer candidates")
labels(ax,a); labels(ax,b)
ax.set_xticks(x); ax.set_xticklabels(bridge_labels); ax.set_ylabel("Number of candidate records"); ax.set_title("B  Cross-stage bridge candidates",loc="left",fontweight="bold"); ax.legend(frameon=False); style(ax)
p2=save_panel(fig,"F1_B_bridge_counts.png")

fig,ax=plt.subplots(figsize=(6.3,4.7)); x=np.arange(5)
a=ax.bar(x-w/2,ret_b,w,color=P["broad"],label="Broad retention"); b=ax.bar(x+w/2,ret_u,w,color=P["uncertainty"],label="U retention")
labels(ax,a,"{:.1f}",8); labels(ax,b,"{:.1f}",8)
ax.set_xticks(x); ax.set_xticklabels(ret_labels); ax.set_ylabel("Retention into bridge set (%)"); ax.set_title("C  Retention from stage corpora into bridges",loc="left",fontweight="bold"); ax.legend(frameon=False); style(ax)
p3=save_panel(fig,"F1_C_retention.png")

fig,ax=plt.subplots(figsize=(6.3,4.7)); x=np.arange(3)
a=ax.bar(x-w/2,full,w,color=P["broad"],label="Full corpus"); b=ax.bar(x+w/2,sens,w,color=P["uncertainty"],label="After diagnostic flags removed")
labels(ax,a,"{:.1f}",8); labels(ax,b,"{:.1f}",8)
ax.set_xticks(x); ax.set_xticklabels(noise_stage); ax.set_ylim(0,36); ax.set_ylabel("U/B share (%)"); ax.set_title("D  Sensitivity to diagnostic noise flags",loc="left",fontweight="bold"); ax.legend(frameon=False,fontsize=8); style(ax)
p4=save_panel(fig,"F1_D_noise_sensitivity.png")

compose([p1,p2,p3,p4],FIG/"Figure_01_Multipanel_Evidence_Fragmentation.png","Evidence fragmentation across S1–S3","")
