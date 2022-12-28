import pandas as pd
import statistics as st
import neurokit2 as nk
import pathlib as pl
from os.path import dirname, join

def feature(path):
    try:
        #filename = join(dirname(__file__), "register/Han.csv")
        filename = join(dirname(__file__), path)
        print(filename)
        a = pd.read_csv(filename)
        signals, info = nk.ecg_process(a['Lead2'], sampling_rate=1000)
        _, peaks = nk.ecg_delineate(signals['ECG_Clean'])
        infos = nk.ecg_findpeaks(signals['ECG_Clean'])

        p_x = []
        p_y = []
        q_x = []
        q_y = []
        r_x = []
        r_y = []
        s_x = []
        s_y = []
        t_x = []
        t_y = []

        for i in range(len(peaks['ECG_Q_Peaks'])):
            if pd.isnull(peaks['ECG_P_Peaks'][i]) != True and pd.isnull(peaks['ECG_Q_Peaks'][i]) != True and pd.isnull(peaks['ECG_S_Peaks'][i]) != True and pd.isnull(peaks['ECG_T_Peaks'][i]) != True and pd.isnull(infos['ECG_R_Peaks'][i]) != True:
                p_x.append(peaks['ECG_P_Peaks'][i])
                p_y.append(signals.iloc[peaks['ECG_P_Peaks'][i], 1])
                q_x.append(peaks['ECG_Q_Peaks'][i])
                q_y.append(signals.iloc[peaks['ECG_Q_Peaks'][i], 1])
                s_x.append(peaks['ECG_S_Peaks'][i])
                s_y.append(signals.iloc[peaks['ECG_S_Peaks'][i], 1])
                t_x.append(peaks['ECG_T_Peaks'][i])
                t_y.append(signals.iloc[peaks['ECG_T_Peaks'][i], 1])
                r_x.append(infos['ECG_R_Peaks'][i])
                r_y.append(signals.iloc[infos['ECG_R_Peaks'][i], 1])

        dis_pr = []
        dis_pt = []
        dis_ps = []
        dis_pq = []
        dis_qr = []
        dis_qs = []
        dis_qt = []
        dis_rs = []
        dis_rt = []

        for i in range(len(p_x)):
            dis_pq.append((float((q_x[i]-p_x[i])**2) +(p_y[i]-q_y[i])*(p_y[i]-q_y[i]))**0.5)
            dis_pr.append((float((r_x[i]-p_x[i])**2) +(r_y[i]-p_y[i])*(r_y[i]-p_y[i]))**0.5)
            dis_ps.append((float((s_x[i]-p_x[i])**2) +(p_y[i]-s_y[i])*(p_y[i]-s_y[i]))**0.5)
            dis_pt.append((float((t_x[i]-p_x[i])**2) +(t_y[i]-p_y[i])*(t_y[i]-p_y[i]))**0.5)
            dis_qr.append((float((r_x[i]-q_x[i])**2) +(r_y[i]-q_y[i])*(r_y[i]-q_y[i]))**0.5)
            dis_qs.append((float((s_x[i]-q_x[i])**2) +(q_y[i]-s_y[i])*(q_y[i]-s_y[i]))**0.5)
            dis_qt.append((float((t_x[i]-q_x[i])**2) +(t_y[i]-q_y[i])*(t_y[i]-q_y[i]))**0.5)
            dis_rs.append((float((s_x[i]-s_x[i])**2) +(r_y[i]-s_y[i])*(r_y[i]-s_y[i]))**0.5)
            dis_rt.append((float((t_x[i]-r_x[i])**2) +(r_y[i]-t_y[i])*(r_y[i]-t_y[i]))**0.5)

        dis_pq_m = st.mean(dis_pq)
        dis_pr_m = st.mean(dis_pr)
        dis_ps_m = st.mean(dis_ps)
        dis_pt_m = st.mean(dis_pt)
        dis_qr_m = st.mean(dis_qr)
        dis_qs_m = st.mean(dis_qs)
        dis_qt_m = st.mean(dis_qt)
        dis_rs_m = st.mean(dis_rs)
        dis_rt_m = st.mean(dis_rt)
        ff = [dis_pq_m, dis_pr_m, dis_ps_m, dis_pt_m, dis_qr_m, dis_qs_m, dis_qt_m, dis_rs_m, dis_rt_m]
        print(ff)
        return ff
    except:
        return 'error'