atri_dic_min = {'ARGILA':[[150],[150,350],[350,600],[600,1000],[1000,9999999],[9999999,9999999], 'Argila (g/kg)(0-20cm)'], 
    'PH_CACL2':[[4],[4,4.5],[4.5,5.0],[5.0,5.5],[5.5,6],[6], 'pH CaCl2 (0-20cm)'], 
    'AL':[[0.3],[0.3,0.7],[0.8,1.5],[1.6,2.5],[2.5,9999999],[9999999,9999999], 'Aluminio (cmolc/dm³)(0-20cm)'], 
    'CA':[[0.5],[0.5,1],[1,2],[2,6],[6,9999999],[9999999,9999999], 'Cálcio (cmolc/dm³)(0-20cm)'], 
    'MG':[[0.2],[0.2,0.4],[0.5,1],[1.1,2],[2,9999999],[9999999,9999999], 'Magnésio (cmolc/dm³)(0-20cm)'], 
    'M%':[[5],[5,10],[10,20],[20,50],[50,9999999],[9999999,9999999], 'Saturação por Aluminio (M%)(0-20cm)'], 
    'V%':[[20],[20,35],[35,50],[50,70],[79,90],[90], 'Saturação por Bases (V%)(0-20cm)'], 
    'CTC_PH7':[[5],[5,7],[7,14],[14,24],[24,9999999],[9999999,9999999], 'CTC pH 7,0 (cmolc/dm³)(0-20cm)'], 
    'CTC_EFETIV':[[1.1],[1.1,2],[2,4],[4,8],[8,9999999],[9999999,9999999], 'CTC Efetiva (cmolc/dm³)(0-20cm)'], 
    'MOS':[[0.7],[0.7,1.4],[1.4,2.4],[2.4,3.4],[3.4,9999999],[9999999,9999999], 'Matéria Orgânica (g/dm³)(0-20cm)'], 
    'P':[[6,4,3],[6,12,4,8,3,6],[12,18,8,12,6,9],[18,24,12,18,9,12],[24,120,18,90,12,60],[120,90,60], 'Fósforo (mg/dm³)(0-20cm)'], 
    'K':[[0.06],[0.06,0.12],[0.12,0.21],[0.21,0.45],[0.45,9999999],[9999999,9999999], 'Potássio (cmolc/dm³)(0-20cm)'], 
    'S':[[1],[1,2],[2,3],[3,6],[6,9999999],[9999999,9999999], 'Enxofre (mg/dm³)(0-20cm)'], 
    'B':[[0.1],[0.1,0.2],[0.2,0.3],[0.3,0.6],[0.6,2],[2], 'Boro (mg/dm³)(0-20cm)'], 
    'CU':[[0.2],[0.2,0.5],[0.5,0.8],[0.8,3],[3,20],[20], 'Cobre (mg/dm³)(0-20cm)'], 
    'MN':[[5],[5,15],[15,30],[30,100],[100,200],[200], 'Manganês (mg/dm³)(0-20cm)'], 
    'ZN':[[0.4],[0.4,0.8],[0.8,1.2],[1.2,10],[10,30],[30], 'Zinco (mg/dm³)(0-20cm)'], 
    'ARGILA_1':[[150],[150,350],[350,600],[600,1000],[1000,9999999],[9999999,9999999], 'Argila (g/kg)(20-40cm)'], 
    'PH_CACL2_2':[[4],[4,4.4],[4.5,4.0],[5.0,5.5],[5.5,6],[6], 'pH CaCl2 (20-40cm)'], 
    # 'H+AL_2':[[0.3],[0.3,0.7],[0.8,1.5],[1.6,2.5],[2.5],[]], 
    'AL_2':[[0.3],[0.3,0.7],[0.8,1.5],[1.6,2.5],[2.5,9999999],[9999999,9999999], 'Aluminio (cmolc/dm³)(20-40cm)'], 
    'CA_2':[[0.5],[0.5,1],[1,2],[2.1,6],[6,9999999],[9999999,9999999], 'Cálcio (cmolc/dm³)(20-40cm)'], 
    'MG_2':[[0.2],[0.2,0.4],[0.5,1],[1.1,2],[2,9999999],[9999999,9999999], 'Magnésio (cmolc/dm³)(20-40cm)'], 
    'M%_2':[[5],[5,10],[10,20],[20,50],[50,9999999],[9999999,9999999], 'Saturação por Aluminio (M%)(20-40cm)'], 
    'V%_2':[[20],[20,35],[35,50],[50,70],[79,90],[90], 'Saturação por Bases (V%)(20-40cm)'], 
    'CTC_PH7_2':[[5],[5,7],[7,14],[14,24],[24,9999999],[9999999,9999999], 'CTC pH 7,0 (cmolc/dm³)(20-40cm)'], 
    'CTC_EFET_1':[[1.1],[1.1,2],[2,4],[4,8],[8,9999999],[9999999,9999999], 'CTC Efetiva (cmolc/dm³)(20-40cm)'], 
    'MO_2':[[0.7],[0.7,1.4],[1.4,2.4],[2.4,3.4],[3.4,9999999],[9999999,9999999], 'Matéria Orgânica (g/dm³)(20-40cm)'], 
    'P_2':[[6,4,3],[6,12,4,8,3,6],[12,18,8,12,6,9],[18,24,12,18,9,12],[24,120,18,90,12,60],[120,90,60], 'Fósforo (mg/dm³)(20-40cm)'], 
    'K_2':[[0.06],[0.06,0.12],[0.12,0.21],[0.21,0.45],[0.45,9999999],[9999999,9999999], 'Potássio (cmolc/dm³)(20-40cm)'], 
    'S_2':[[3],[3,6],[6,9],[9,12],[12,9999999],[9999999,9999999], 'Enxofre (mg/dm³)(20-40cm)'], 
    'B_2':[[0.1],[0,1,0.2],[0.2,0.3],[0.3,0.6],[0.6,2],[2], 'Boro (mg/dm³)(20-40cm)'], 
    'CU_2':[[0.2],[0.2,0.5],[0.5,0.8],[0.8,3],[3,20],[20], 'Cobre (mg/dm³)(20-40cm)'], 
    'MN_2':[[5],[5,15],[15,30],[30,100],[100,200],[200], 'Manganês (mg/dm³)(20-40cm)'], 
    'ZN_2':[[0.4],[0.4,0.8],[0.8,1.2],[1.2,10],[10,30],[30], 'Zinco (mg/dm³)(20-40cm)'], 
    'C_Superfic':['A','B','C','D','E','ZZZ', 'Classificação Superficie (0-20cm)'], 
    'C_SubSuper':['A','B','C','D','E','ZZZ', 'Classificação Subsuperficie (20-40cm)'], 
    'Class_Fina':['A','B','C','D','E','ZZZ', 'Classificação por ambiente de produção']}

atri_dic = {'ARGILA':[[150],[150,350],[350,600],[600,1000],[1000,9999999],[9999999,9999999], 'ARGILA (g/kg)(0-20cm)'], 
    'PH_CACL2':[[4],[4,4.5],[4.5,5.0],[5.0,5.5],[5.5,6],[6], 'PH CACL2 (0-20cm)'], 
    # 'H+AL':[[0.3],[0.3,0.7],[0.8,1.5],[1.6,2.5],[2.5],[2.5]], 
    'AL':[[0.3],[0.3,0.7],[0.8,1.5],[1.6,2.5],[2.5,9999999],[9999999,9999999], 'ALUMÍNIO (cmolc/dm³)(0-20cm)'], 
    'CA':[[0.5],[0.5,1],[1,2],[2,6],[6,9999999],[9999999,9999999], 'CÁLCIO (cmolc/dm³)(0-20cm)'], 
    'MG':[[0.2],[0.2,0.4],[0.5,1],[1.1,2],[2,9999999],[9999999,9999999], 'MAGNÉSIO (cmolc/dm³)(0-20cm)'], 
    'M%':[[5],[5,10],[10,20],[20,50],[50,9999999],[9999999,9999999], 'SATURAÇÃO POR ALUMÍNIO (M%)(0-20cm)'], 
    'V%':[[20],[20,35],[35,50],[50,70],[79,90],[90], 'SATURAÇÃO POR BASES (V%)(0-20cm)'], 
    'CTC_PH7':[[5],[5,7],[7,14],[14,24],[24,9999999],[9999999,9999999], 'CTC PH 7,0 (cmolc/dm³)(0-20cm)'], 
    'CTC_EFETIV':[[1.1],[1.1,2],[2,4],[4,8],[8,9999999],[9999999,9999999], 'CTC EFETIVA (cmolc/dm³)(0-20cm)'], 
    'MOS':[[0.7],[0.7,1.4],[1.4,2.4],[2.4,3.4],[3.4,9999999],[9999999,9999999], 'MATÉRIA ORGÂNICA (g/dm³)(0-20cm)'], 
    'P':[[6,4,3],[6,12,4,8,3,6],[12,18,8,12,6,9],[18,24,12,18,9,12],[24,120,18,90,12,60],[120,90,60], 'FÓSFORO (mg/dm³)(0-20cm)'], 
    'K':[[0.06],[0.06,0.12],[0.12,0.21],[0.21,0.45],[0.45,9999999],[9999999,9999999], 'POTÁSSIO (cmolc/dm³)(0-20cm)'], 
    'S':[[1],[1,2],[2,3],[3,6],[6,9999999],[9999999,9999999], 'ENXOFRE (mg/dm³)(0-20cm)'], 
    'B':[[0.1],[0.1,0.2],[0.2,0.3],[0.3,0.6],[0.6,2],[2], 'BORO (mg/dm³)(0-20cm)'], 
    'CU':[[0.2],[0.2,0.5],[0.5,0.8],[0.8,3],[3,20],[20], 'COBRE (mg/dm³)(0-20cm)'], 
    'MN':[[5],[5,15],[15,30],[30,100],[100,200],[200], 'MANGANÊS (mg/dm³)(0-20cm)'], 
    'ZN':[[0.4],[0.4,0.8],[0.8,1.2],[1.2,10],[10,30],[30], 'ZINCO (mg/dm³)(0-20cm)'], 
    'ARGILA_1':[[150],[150,350],[350,600],[600,1000],[1000,9999999],[9999999,9999999], 'ARGILA (g/kg)(20-40cm)'], 
    'PH_CACL2_2':[[4],[4,4.5],[4.5,5.0],[5.0,5.5],[5.5,6],[6], 'PH CACL2 (20-40cm)'], 
    'AL_2':[[0.3],[0.3,0.7],[0.8,1.5],[1.6,2.5],[2.5,9999999],[9999999,9999999], 'ALUMÍNIO (cmolc/dm³)(20-40cm)'], 
    'CA_2':[[0.5],[0.5,1],[1,2],[2,6],[6,9999999],[9999999,9999999], 'CÁLCIO (cmolc/dm³)(20-40cm)'], 
    'MG_2':[[0.2],[0.2,0.4],[0.5,1],[1.1,2],[2,9999999],[9999999,9999999], 'MAGNÉSIO (cmolc/dm³)(20-40cm)'], 
    'M%_2':[[5],[5,10],[10,20],[20,50],[50,9999999],[9999999,9999999], 'SATURAÇÃO POR ALUMÍNIO (M%)(20-40cm)'], 
    'V%_2':[[20],[20,35],[35,50],[50,70],[79,90],[90], 'SATURAÇÃO POR BASES (V%)(20-40cm)'], 
    'CTC_PH7_2':[[5],[5,7],[7,14],[14,24],[24,9999999],[9999999,9999999], 'CTC PH 7,0 (cmolc/dm³)(20-40cm)'], 
    'CTC_EFET_1':[[1.1],[1.1,2],[2,4],[4,8],[8,9999999],[9999999,9999999], 'CTC EFETIVA (cmolc/dm³)(20-40cm)'], 
    'MO_2':[[0.7],[0.7,1.4],[1.4,2.4],[2.4,3.4],[3.4,9999999],[9999999,9999999], 'MATÉRIA ORGÂNICA (g/dm³)(20-40cm)'], 
    'P_2':[[6,4,3],[6,12,4,8,3,6],[12,18,8,12,6,9],[18,24,12,18,9,12],[24,120,18,90,12,60],[120,90,60], 'FÓSFORO (mg/dm³)(20-40cm)'], 
    'K_2':[[0.06],[0.06,0.12],[0.12,0.21],[0.21,0.45],[0.45,9999999],[9999999,9999999], 'POTÁSSIO (cmolc/dm³)(20-40cm)'], 
    'S_2':[[3],[3,6],[6,9],[9,12],[12,9999999],[9999999,9999999], 'ENXOFRE (mg/dm³)(20-40cm)'], 
    'B_2':[[0.1],[0.1,0.2],[0.2,0.3],[0.3,0.6],[0.6,2],[2], 'BORO (mg/dm³)(20-40cm)'], 
    'CU_2':[[0.2],[0.2,0.5],[0.5,0.8],[0.8,3],[3,20],[20], 'COBRE (mg/dm³)(20-40cm)'], 
    'MN_2':[[5],[5,15],[15,30],[30,100],[100,200],[200], 'MANGANÊS (mg/dm³)(20-40cm)'], 
    'ZN_2':[[0.4],[0.4,0.8],[0.8,1.2],[1.2,10],[10,30],[30], 'ZINCO (mg/dm³)(20-40cm)'], 
    'C_Superfic':['A','B','C','D','E','ZZZ', 'CLASSIFICAÇÃO SUPERFÍCIE (0-20cm)'], 
    'C_SubSuper':['A','B','C','D','E','ZZZ', 'CLASSIFICAÇÃO SUBSUPERFÍCIE (20-40cm)'], 
    'Class_Fina':['A','B','C','D','E','ZZZ', 'CLASSIFICAÇÃO POR AMBIENTE DE PRODUÇÃO']}