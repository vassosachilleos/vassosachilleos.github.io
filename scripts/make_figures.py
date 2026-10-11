import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
out=__import__("os").path.join(__import__("os").path.dirname(__file__),"..","content","research")+"/"
plt.rcParams.update({"font.size":13,"axes.spines.top":False,"axes.spines.right":False})
C1,C2,C3="#215CAF","#C0392B","#7F8C8D"

# 1. Hatano-Nelson chain: H_{n+1,n}=t+g, H_{n,n+1}=t-g, open boundaries -> skin modes
N,t,g=40,1.0,0.3
H=np.diag((t+g)*np.ones(N-1),-1)+np.diag((t-g)*np.ones(N-1),1)
E,V=np.linalg.eig(H)
fig,ax=plt.subplots(1,2,figsize=(8,4.5),gridspec_kw={"width_ratios":[1,1.3]})
k=np.linspace(0,2*np.pi,400)
Epbc=(t+g)*np.exp(-1j*k)+(t-g)*np.exp(1j*k)
ax[0].plot(Epbc.real,Epbc.imag,color=C3,lw=2,label="PBC")
ax[0].plot(E.real,E.imag,"o",color=C1,ms=4,label="OBC")
ax[0].set_xlabel(r"Re $E$");ax[0].set_ylabel(r"Im $E$");ax[0].legend(frameon=False,fontsize=11,loc="upper center",ncol=2,bbox_to_anchor=(0.5,1.22))
for j in range(N):
    p=np.abs(V[:,j])**2; ax[1].plot(np.arange(1,N+1),p/p.sum(),color=C1,alpha=.35,lw=1)
ax[1].set_xlabel("site $n$");ax[1].set_ylabel(r"$|\psi_n|^2$")
fig.tight_layout();fig.savefig(out+"skin-effect/featured.png",dpi=150);plt.close()
# check: OBC spectrum real, = 2 sqrt(t^2-g^2) cos(pi m/(N+1))
Ex=np.sort(2*np.sqrt(t*t-g*g)*np.cos(np.pi*np.arange(1,N+1)/(N+1)))
print("OBC max|Im E|",np.abs(E.imag).max()," max dev from analytic",np.abs(np.sort(E.real)-Ex).max())

# 2. PT dimer H=[[w0+i gam, k],[k, w0-i gam]]: eigenvalues w0 ± sqrt(k^2-gam^2), EP at gam=k
kap=1.0; gam=np.linspace(0,2,600); lam=np.sqrt((kap**2-gam**2).astype(complex))
fig,ax=plt.subplots(1,2,figsize=(8,4.5),sharex=True)
for s in (1,-1):
    ax[0].plot(gam,s*lam.real,color=C1,lw=2.5); ax[1].plot(gam,s*lam.imag,color=C2,lw=2.5)
for a,l in zip(ax,[r"Re$(\omega-\omega_0)/\kappa$",r"Im$(\omega-\omega_0)/\kappa$"]):
    a.axvline(1,color=C3,ls="--",lw=1); a.set_xlabel(r"$\gamma/\kappa$"); a.set_ylabel(l)
ax[0].text(1.03,0.6,"EP",color=C3)
fig.tight_layout();fig.savefig(out+"exceptional-points/featured.png",dpi=150);plt.close()

# 3. Two-port resonator, coupling rate g to each port, intrinsic loss g0.
#    Symmetric S-eigenvalue: sigma=(-i D + g0 - 2g)/(-i D + g0 + 2g); CPA at D=0, g0=2g
D=np.linspace(-5,5,800); gc=1.0
fig,ax=plt.subplots(figsize=(8,4.5))
for g0,c,lab in [(1.0,C3,r"$\gamma_0=\gamma$"),(2.0,C2,r"$\gamma_0=2\gamma$ (CPA)"),(4.0,C1,r"$\gamma_0=4\gamma$")]:
    s=(-1j*D+g0-2*gc)/(-1j*D+g0+2*gc); ax.plot(D,np.abs(s)**2,color=c,lw=2.5,label=lab)
ax.set_xlabel(r"$(\omega-\omega_0)/\gamma$"); ax.set_ylabel(r"$|\sigma_{+}|^2$")
ax.legend(frameon=False,ncol=3,loc="upper center",bbox_to_anchor=(0.5,1.2),fontsize=11); fig.tight_layout(); fig.savefig(out+"cpa/featured.png",dpi=150); plt.close()
