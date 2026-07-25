import os
import json
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

class Dashboard:
    def __init__(self):
        self.output_folder="dashboard"
        os.makedirs(self.output_folder,exist_ok=True)

    def load_latest(self,source):
        p=os.path.join("data",source,"latest.json")
        if not os.path.exists(p): return {}
        with open(p,"r",encoding="utf-8") as f: return json.load(f)

    def load_history(self,source,metric):
        folder=os.path.join("data",source,"history")
        d,v=[],[]
        if not os.path.exists(folder): return d,v
        for fn in sorted(os.listdir(folder)):
            if fn.endswith(".json"):
                with open(os.path.join(folder,fn),"r",encoding="utf-8") as f:
                    obj=json.load(f)
                if metric in obj:
                    try:
                        v.append(float(obj[metric])); d.append(fn.replace(".json",""))
                    except: pass
        return d,v

    def get_change(self,source,metric):
        _,vals=self.load_history(source,metric)
        return 0 if len(vals)<2 else vals[-1]-vals[-2]

    def draw_card(self,ax,title,value,color="#4472C4"):
        ax.set_facecolor(color); ax.set_xticks([]); ax.set_yticks([])
        [s.set_visible(False) for s in ax.spines.values()]
        ax.text(.5,.7,title,ha="center",color="white",fontweight="bold")
        ax.text(.5,.38,str(value),ha="center",color="white",fontsize=20,fontweight="bold")

    def draw_chart(self,ax,source,metric,title):
        d,v=self.load_history(source,metric)
        ax.set_title(title)
        if not v:
            ax.text(.5,.5,"No Data",ha="center"); return
        x=range(len(v))
        ax.plot(x,v,marker="o"); ax.fill_between(x,v,alpha=.2)
        ax.grid(alpha=.3); ax.set_xticks(list(x))
        ax.set_xticklabels([i[:10] for i in d],rotation=30,fontsize=8)

    def create_dashboard(self):
        s=self.load_latest("scholar")
        o=self.load_latest("orcid")
        fig=plt.figure(figsize=(16,10))
        gs=GridSpec(4,4,figure=fig,hspace=.8,wspace=.4)
        fig.suptitle("ACADEMIC TRACKER DASHBOARD",fontsize=24,fontweight="bold")
        fig.text(.5,.95,datetime.now().strftime("Generated: %d %B %Y %H:%M"),ha="center")
        self.draw_card(fig.add_subplot(gs[0,0]),"Citations",s.get("citations",0))
        self.draw_card(fig.add_subplot(gs[0,1]),"h-index",s.get("h_index",0),"#70AD47")
        self.draw_card(fig.add_subplot(gs[0,2]),"i10-index",s.get("i10_index",0),"#ED7D31")
        self.draw_card(fig.add_subplot(gs[0,3]),"Articles",s.get("article_count",0),"#A64D79")
        self.draw_card(fig.add_subplot(gs[1,:]),"ORCID Works",o.get("works",0),"#5B9BD5")
        self.draw_chart(fig.add_subplot(gs[2,:2]),"scholar","citations","Citation History")
        self.draw_chart(fig.add_subplot(gs[2,2:]),"scholar","h_index","h-index History")
        self.draw_chart(fig.add_subplot(gs[3,:2]),"scholar","i10_index","i10-index History")
        self.draw_chart(fig.add_subplot(gs[3,2]),"scholar","article_count","Article History")
        self.draw_chart(fig.add_subplot(gs[3,3]),"orcid","works","ORCID Works")
        fig.tight_layout(rect=[0,0,1,.94])
        fig.savefig(os.path.join(self.output_folder,"academic_dashboard.png"),dpi=300,bbox_inches="tight")
        plt.close(fig)
