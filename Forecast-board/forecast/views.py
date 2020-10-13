from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404
from .models import Fcast
from django.contrib.auth.models import User
#from django.db.models.functions.datetime import datetime
from datetime import datetime 
import pandas as pd
import os
from django.conf import settings
#from django.utils import six
import json
from django.utils.timezone import get_fixed_timezone, utc
from django.db.models import DateTimeField, ExpressionWrapper, F ,Func
# Create your views here.
import joblib
import numpy as np
from keras.models import Sequential
from keras import layers
from keras.models import load_model







base = settings.BASE_DIR



epath = os.path.join(base,'research/modules/NEURAL_DENSE_MODEL3.h5')

#loaded_model =load_model(epath)


def home(request):
	Entry_dict = Fcast.objects.values('utc_timestamp','total_load_consume')
	
	total_load =list()

	
	

	for entry in Entry_dict:

		dlist = [entry['utc_timestamp'].timestamp()*1000 , entry['total_load_consume']]

		total_load.append(dlist)

	return render(request,'home.html',{'total_load':json.dumps(total_load)})
	
	

def gridexp(request):

	Entry_dict1 = Fcast.objects.values('utc_timestamp','grid_export')
	grid_exp = list()

	for entry in Entry_dict1:

		dlist_3 = [entry['utc_timestamp'].timestamp()*1000 , entry['grid_export']]

		grid_exp.append(dlist_3)

	return render(request,'gridexp.html',{'grid_exp':json.dumps(grid_exp)})




def gridimp(request):

	Entry_dict2 = Fcast.objects.values('utc_timestamp','grid_import')

	grid_imp = list()

	for entry in Entry_dict2:

		dlist_2 = [entry['utc_timestamp'].timestamp()*1000 , entry['grid_import']]

		grid_imp.append(dlist_2)

	return render(request,'gridimp.html',{'grid_imp':json.dumps(grid_imp)})


def solar(request):

	Entry_dict3 = Fcast.objects.values('utc_timestamp','pv')
	
	pv = list()

	for entry in Entry_dict3:

		dlist_1 = [entry['utc_timestamp'].timestamp()*1000 , entry['pv']]

		pv.append(dlist_1)

	return render(request,'solar.html',{'pv':json.dumps(pv)})



def create_tensor(float_data,time_steps,step):
        history, target = [],[]
        for j in range(len(float_data) - time_steps - step):
                v = float_data.iloc[j: (j + time_steps),[0,1,2,4]].values
                history.append(v)
                target.append(float_data.iloc[j + time_steps + step][3])
        return np.array(history),np.array(target)




def predict(request):

        Entry_dict4 = Fcast.objects.values('utc_timestamp','total_load_consume')

        view_data = Entry_dict4[0:73946]

        model = joblib.load(os.path.join(base,'research/ARIMA_module.joblib'))

        total_load2 =list()

        for entry in view_data:

                dlist = [entry['utc_timestamp'].timestamp()*1000 , entry['total_load_consume']]

                total_load2.append(dlist)

                last_date=entry['utc_timestamp']

        if last_date.month < 8:
                nxtmonth = '0' + str(last_date.month + 2)

        elif last_date.month > 7 and last_date.month < 11:

                nxtmonth = str(last_date.month + 2)

        elif last_date.month == 11:

                nxtmonth = '01'

        elif last_date.month == 12:

                nxtmonth = '02'

        if last_date.day < 28:

                nxtdy=str(last_date.day)

        elif last_date.day > 27:

                if last_date.month == 12:

                        nxtdy = str(28)

                elif last_date.month in [2,4,7,9]:
                        
                        nxtdy = str(30)

                elif last_date.month in [1,3,5,6,8,10,11]:

                        nxtdy = str(31)

        yr = str(last_date.year)

        end_time = yr + '-' + nxtmonth + '-' + nxtdy + ' ' + '00:00:00'

        pred =model.predict(start= last_date.strftime('%Y-%m-%d %H:%M:%S'),end= end_time,exog=None,typ='levels',dynamic=False)

        pred = pred.reset_index()

        pred = pred.rename(columns ={'index':'timestamp',0:'total_load'})

        pred['timestamp'] = pd.to_datetime(pred['timestamp'])

        pred_list = list()

        for i in range(len(pred)):

                dview =[pred.loc[i,'timestamp'].timestamp()*1000, pred.loc[i,'total_load']]

                pred_list.append(dview)



        return render(request,'predict.html',{'total_load2':total_load2,'predicted':pred_list})






def dense(request):

        Entry_dict5 = Fcast.objects.values('utc_timestamp','datefield','grid_import','grid_export','pv','total_load_consume')

        nw_data = Entry_dict5[0:78266]

        base = settings.BASE_DIR

        epath = os.path.join(base,'research/modules/NEURAL_DENSE_MODEL3.h5')
        loaded_model =load_model(epath)



        total_load_list =list()



        for entry in nw_data:

                total_nw_list = [entry['utc_timestamp'].timestamp()*1000 , entry['total_load_consume']]

                total_load_list.append(total_nw_list)

                


        nw_pd = pd.DataFrame(data =Entry_dict5,columns =['utc_timestamp','datefield','grid_import','grid_export','pv','total_load_consume'])
        aggregate = nw_pd.groupby('datefield')['total_load_consume'].mean()

        aggregate = aggregate.reset_index()

        aggregate = aggregate.rename(columns = {'total_load_consume':'daily_load'})





        nw_join= nw_pd.set_index('datefield').join(aggregate.set_index('datefield'),on='datefield',how ='inner',lsuffix='L',rsuffix='R')
        nw_join =nw_join.reset_index()
        nw_main =nw_join.drop(columns=['datefield'])
        nw_main = nw_main.set_index('utc_timestamp')
        neural_data = nw_main.copy()





        mean = nw_main.mean(axis=0)
        mn = mean[3]

        neural_data -= mean

        std = nw_main.std(axis=0)
        st = std[3]

        neural_data /= std



        neural_data = neural_data[0:78266]
        nw_main = nw_main[0:78266]


        test_d = neural_data[-5021:]
        test_nw =test_d.reset_index()
        test_nw = test_nw.drop(columns=['utc_timestamp'])



        x_test , y_test = create_tensor(test_nw,96,1)




        pred_ld = loaded_model.predict(x_test)
        pred_ld = pred_ld.reshape((len(pred_ld),))
        pred_dn =((pred_ld * std[3])  + mean[3] )




        pred_nw = pd.DataFrame(data={'pred_value':pred_dn},index=nw_main.iloc[-4924:,:].index)

        pred_nw = pred_nw.reset_index()
        pred_nw['utc_timestamp'] = pd.to_datetime(pred_nw['utc_timestamp'])




        neural_pred= list()

        for i in range(len(pred_nw)):
        
                nw_list =[pred_nw.loc[i,'utc_timestamp'].timestamp()*1000, pred_nw.loc[i,'pred_value']]

                neural_pred.append(nw_list)


        return render(request,'dense.html',{'total_load_list':total_load_list,'neural_pred':neural_pred})








