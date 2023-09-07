# Q2_Results  
----------------------

## Please see the table below

[Tabulated data](/Gradient%20Descent%20with%20JAX%20gradient%20computation%20for%20RIDGE.pdf)


(90, 10)
Batch Gradient Descent with manual gradient computation for unregularized objective :   
 Batch size= 9 , RMSE:  1.7853290067513778  
 Batch size= 9 , MAE:  1.440884854640454  
Time taken  0.2731807231903076  
---------------------------
Batch Gradient Descent with manual gradient computation for Ridge regularization objective :   
 Batch size= 9 , RMSE:  1.0155040049359525  
 Batch size= 9 , MAE:  0.804418858980315  
Time taken  0.22262024879455566  
---------------------------
Batch Gradient Descent with JAX gradient computation for unregularized objective :   
No GPU/TPU found, falling back to CPU. (Set TF_CPP_MIN_LOG_LEVEL=0 and rerun for more info.)  
 Batch size= 9 , RMSE:  1.4106056254032833  
 Batch size= 9 , MAE:  1.1513182572326441  
Time taken  1.3176164627075195  
---------------------------
Batch Gradient Descent with JAX gradient computation for regularized objective LASSO :   
 Batch size= 9 , RMSE:  1.5156732475575057  
 Batch size= 9 , MAE:  1.1717037554127965  
Time taken  2.242830276489258  
---------------------------
Batch Gradient Descent with JAX gradient computation for RIDGE at lr=0.001 and lambda=0.1  
 Batch size= 9 , RMSE:  3.314001060244562  
 Batch size= 9 , MAE:  2.681324870258756  
Time taken  1.8594343662261963  
---------------------------
Batch Gradient Descent with JAX gradient computation for RIDGE at lr=0.01 and lambda=0.1  
 Batch size= 9 , RMSE:  1.4911491795013396  
 Batch size= 9 , MAE:  1.198384478607811  
Time taken  1.4336094856262207  
---------------------------
Batch Gradient Descent with JAX gradient computation for RIDGE at lr=0.1 and lambda=0.1  
 Batch size= 9 , RMSE:  0.9217603663526538  
 Batch size= 9 , MAE:  0.7318958933259078  
Time taken  1.4805946350097656  
---------------------------
Batch Gradient Descent with JAX gradient computation for RIDGE at lr=0.001 and lambda=1  
 Batch size= 9 , RMSE:  2.5656668146126793  
 Batch size= 9 , MAE:  2.054581645005414  
Time taken  1.5079424381256104  
---------------------------
Batch Gradient Descent with JAX gradient computation for RIDGE at lr=0.01 and lambda=1  
 Batch size= 9 , RMSE:  1.3474734515029483  
 Batch size= 9 , MAE:  1.086252723769201  
Time taken  1.4075217247009277  
---------------------------
Batch Gradient Descent with JAX gradient computation for RIDGE at lr=0.1 and lambda=1  
 Batch size= 9 , RMSE:  0.9218650458900396  
 Batch size= 9 , MAE:  0.7310851441595964  
Time taken  1.4911489486694336  
---------------------------
Batch Gradient Descent with JAX gradient computation for RIDGE at lr=0.001 and lambda=10  
 Batch size= 9 , RMSE:  3.665810434571774  
 Batch size= 9 , MAE:  2.8935092155163455  
Time taken  1.453371524810791  
---------------------------
Batch Gradient Descent with JAX gradient computation for RIDGE at lr=0.01 and lambda=10  
 Batch size= 9 , RMSE:  0.9848861915651099  
 Batch size= 9 , MAE:  0.7672203913183792  
Time taken  1.6426382064819336  
---------------------------
Batch Gradient Descent with JAX gradient computation for RIDGE at lr=0.1 and lambda=10  
 Batch size= 9 , RMSE:  0.9315949822843226  
 Batch size= 9 , MAE:  0.7375689416859669  
Time taken  1.4308688640594482  
---------------------------
Batch Gradient Descent with JAX gradient computation for regularized objective RIDGE :   
 Batch size= 1 , RMSE:  1.0047771218609776  
 Batch size= 1 , MAE:  0.7921750572796936  
Time taken  1.8775434494018555  
---------------------------  
Batch Gradient Descent with JAX gradient computation for regularized objective RIDGE with batch size :  10  
 Batch size= 10 , RMSE:  1.8793437389973198  
 Batch size= 10 , MAE:  1.5279358225786834  
Time taken  1.698305368423462  
---------------------------
Batch Gradient Descent with JAX gradient computation for regularized objective RIDGE with batch size :  15  
 Batch size= 15 , RMSE:  2.9734395509741893  
 Batch size= 15 , MAE:  2.3692876298847336  
Time taken  1.0771324634552002  
---------------------------
Batch Gradient Descent with JAX gradient computation for regularized objective RIDGE with batch size :  20  
 Batch size= 20 , RMSE:  1.8433701720957683  
 Batch size= 20 , MAE:  1.4642168226074135  
Time taken  0.954808235168457  
---------------------------
SGD Momemtum with JAX gradient computation for regularized objective RIDGE with momentum :  0.1  
 Batch size= 9 , RMSE:  1.4699483873969783  
 Batch size= 9 , MAE:  1.159449294785491  
Time taken  1.5565354824066162
---------------------------
SGD Momemtum with JAX gradient computation for regularized objective RIDGE with momentum :  0.5  
 Batch size= 9 , RMSE:  0.954917376168867  
 Batch size= 9 , MAE:  0.7579015413881073  
Time taken  1.4115982055664062
---------------------------
SGD Momemtum with JAX gradient computation for regularized objective RIDGE with momentum :  0.9  
 Batch size= 9 , RMSE:  0.9186546626429495  
 Batch size= 9 , MAE:  0.7252929003267249  
Time taken  1.4447081089019775
---------------------------


