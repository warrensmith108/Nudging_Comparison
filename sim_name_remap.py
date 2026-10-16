
##############################
# This script serves to "match" long (messy) CESM simulation names with shorter (easier to remember)
# names that can be used for naming plots and text labeling
# #############################

remap = \
    {

    ### MAY 2026 SPIN-UP CORRECTIONS: 3hr files

    '2022_M2-weak':'/glade/derecho/scratch/wsmith/archive/FCnudged_f09.carmats16_cesm2.2_2022_M2-3hr/atm/hist/FC*h1*',
    '2022_M2-strong':'/glade/derecho/scratch/wsmith/archive/FCnudged_f09.carmats16_cesm2.2_2022_M2-3hr_rlx-4h/atm/hist/FC*h1*',        
    '2022_E5-strong':'/glade/derecho/scratch/wsmith/archive/FCnudged_f09.carmats16_cesm2.2_2022_E5-1hr/atm/hist/FC*h1*',        
    '2022_E5-weak':'/glade/derecho/scratch/wsmith/archive/FCnudged_f09.carmats16_cesm2.2_2022_E5-3hr/atm/hist/FC*h1*',    
    '2022_E5-weak-0.083':'/glade/derecho/scratch/wsmith/archive/FCnudged_f09.carmats16_cesm2.2_2022_E5-1hr_rlx-12h/atm/hist/FC*h1*', 
    '2022_FreeRun':'/glade/derecho/scratch/wsmith/archive/FCnudged_f09.carmats16_cesm2.2_2022_FreeRun/atm/hist/FC*h1*',         
    '2022_E5-1hr_LNOmod':'/glade/derecho/scratch/wsmith/archive/FCnudged_f09.carmats16_cesm2.2_2022_E5-1hr_LNOmod/atm/hist/FC*h1*',               
    '2022_E5-1hr_Qnudge':'/glade/derecho/scratch/wsmith/archive/FCnudged_f09.carmats16_cesm2.2_2022_E5-1hr_Qnudge/atm/hist/FC*h1*', 
    '2022_E5-1hr_ZMKE':'/glade/derecho/scratch/wsmith/archive/FCnudged_f09.carmats16_cesm2.2_2022_E5-1hr_ZMKE/atm/hist/FC*h1*',      

    'Aug2022_E5-1hr_low-entrain':'/glade/derecho/scratch/wsmith/archive/FCnudged_f09.carmats16_cesm2.2_Aug2022_E5-1hr_low-entrain/atm/hist/FC*h1*',    
 
    ### MAY 2026 SPIN-UP CORRECTIONS: monthly files        

    '2022_M2-weak_h0':'/glade/derecho/scratch/wsmith/archive/FCnudged_f09.carmats16_cesm2.2_2022_M2-3hr/atm/hist/FC*h0*',
    '2022_M2-strong_h0':'/glade/derecho/scratch/wsmith/archive/FCnudged_f09.carmats16_cesm2.2_2022_M2-3hr_rlx-4h/atm/hist/FC*h0*',         
    '2022_E5-strong_h0':'/glade/derecho/scratch/wsmith/archive/FCnudged_f09.carmats16_cesm2.2_2022_E5-1hr/atm/hist/FC*h0*',        
    '2022_E5-weak_h0':'/glade/derecho/scratch/wsmith/archive/FCnudged_f09.carmats16_cesm2.2_2022_E5-3hr/atm/hist/FC*h0*',   
    '2022_E5-weak-0.083_h0':'/glade/derecho/scratch/wsmith/archive/FCnudged_f09.carmats16_cesm2.2_2022_E5-1hr_rlx-12h/atm/hist/FC*h0*', 
    '2022_FreeRun_h0':'/glade/derecho/scratch/wsmith/archive/FCnudged_f09.carmats16_cesm2.2_2022_FreeRun/atm/hist/FC*h0*',           
    '2022_E5-1hr_LNOmod_h0':'/glade/derecho/scratch/wsmith/archive/FCnudged_f09.carmats16_cesm2.2_2022_E5-1hr_LNOmod/atm/hist/FC*h0*',               
    '2022_E5-1hr_Qnudge_h0':'/glade/derecho/scratch/wsmith/archive/FCnudged_f09.carmats16_cesm2.2_2022_E5-1hr_Qnudge/atm/hist/FC*h0*', 
    '2022_E5-1hr_ZMKE_h0':'/glade/derecho/scratch/wsmith/archive/FCnudged_f09.carmats16_cesm2.2_2022_E5-1hr_ZMKE/atm/hist/FC*h0*',      

    # ZMKE sensitivity runs, performed in May 2025
    'MAM4_MEIC_SO2_ZMKE1':'/glade/derecho/scratch/wsmith/archive/FCnudged_f09.carmats16_cesm2.2.carma_trop_strat.2010_2021_cams5.3_so2_meic_withbb_RichConv.002.acclip1/atm/hist/FC*h1.2022-08*',
    'MAM4_MEIC_SO2_pini':'/glade/derecho/scratch/wsmith/archive/FCnudged_f09.carmats16_cesm2.2.carma_trop_strat.2010_2021_cams5.3_so2_meic_withbb_RichConv.002.acclip_pini/atm/hist/FC*h1.2022-08*',
    'MAM4_MEIC_SO2_pe2ke':'/glade/derecho/scratch/wsmith/archive/FCnudged_f09.carmats16_cesm2.2.carma_trop_strat.2010_2021_cams5.3_so2_meic_withbb_RichConv.002.acclip_pe2ke/atm/hist/FC*h1.2022-08*',
    'MAM4_MEIC_SO2_dmpdz':'/glade/derecho/scratch/wsmith/archive/FCnudged_f09.carmats16_cesm2.2.carma_trop_strat.2010_2021_cams5.3_so2_meic_withbb_RichConv.002.acclip_dmpdz/atm/hist/FC*h1.2022-08*',     

    'Aug19_WACCM_init':'/glade/derecho/scratch/wsmith/archive/f.e30_beta05.FWHIST_f09_f09_mg17v1.L70.cam6.001.2022/atm/hist/f.e30*cam.i.*',
    'Aug19_WACCM':'/glade/derecho/scratch/wsmith/archive/f.e30_beta05.FWHIST_f09_f09_mg17v1.L70.cam6.001.2022-Aug19/atm/hist/f.e30*h0i*',  # For comparison with MUSICAv1 ACCLIP test

    #'WACCM_70L':'/glade/derecho/scratch/wsmith/archive/f.e22.FWHIST_BGCslhvbs.f09_f09_mg17.cesm2.2_vsl03.2021_2022.CAMS.FINN.DCOTSS_ACCLIPv01.JJA/atm/hist/f*h1.2022-08-*',
    #'MAM4_MEIC_SO2':'/glade/campaign/acom/acom-climate/wsmith/FCnudged_f09.carmats16_cesm2.2.carma_trop_strat.2010_2021_cams5.3_so2_meic_withbb.acclip/FC*h1.2022-08*',
    #'MAM4_MEIC_SO2_ZMKE':'/glade/derecho/scratch/wsmith/archive/FCnudged_f09.carmats16_cesm2.2.carma_trop_strat.2010_2021_cams5.3_so2_meic_withbb_RichConv.002.acclip/atm/hist/FC*h1.2022-08*',   # Emissions are different in this run        

    'ERA5_f09_32L':'/glade/campaign/cgd/amp/wchapman/Nudging_ERA5/fv_L32_ncl/ERA5_fv09.cam2.i.*',
    'MERRA-2_f09_32L':'/glade/campaign/cesm/cesmdata/inputdata/atm/cam/met/nudging/MERRA2_fv09_32L/2022/MERRA2_fv09.cam2.i.*',
        
    }
