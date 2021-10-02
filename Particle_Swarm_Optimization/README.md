# 手法名
  Particle Swarm Optimization
# 特徴
  生物の行動を参考にして提案された群知能最適化手法．複数の粒子(生物個体)を探索のために利用し，各個体が最適化を行った際に得られる知見を基にして最適値を探索する手法．
# アルゴリズム
  $X_k(t+1) = X_k(t) + V_k(t+1)  $
  $V_k(t+1) = wV_k(t) + c_1r_1 \left( X_k^{pbest}(t) - X_k(t) \right) + c_2r_2 \left( X_k^{gbest}(t) - X_k(t) \right) $
# 参考文献
- (https://www.msi.co.jp/s4/introduction/pso.html)[https://www.msi.co.jp/s4/introduction/pso.html]
  
