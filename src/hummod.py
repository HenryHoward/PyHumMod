from special_functions import *
import math

timervars = []

class System:
    def __init__(self):
        self.InitialX = 0
        self.X = 0
        self.Dx = 0.0003

class Timer:
    def __init__(self, val, state, Dx):
        self.val = val
        self.state = state
        self.Dx = Dx
    
    def count(self):
        if self.state == "OFF":
            pass
        elif self.state == "UP":
            self.val += self.Dx
        elif self.state == "DOWN":
            self.val -= self.Dx
    
    def __lt__(self, other):
        return self.val<other
    
    def __gt__(self, other):
        return self.val>other

class Structure:

    def Context_func(self):
        Context.Calc_func()

    def Parms_func(self):
        Environment.Parms_func()
        Morphology.Parms_func()
        AirSupply_PressureChamber.Calc_func()
        AirSupply_GasTanks.Calc_func()
        AirSupply_InspiredAir.Calc_func()
        Bronchi.Calc_func()
        Environment.FinishParms_func()
        Exercise_Bike.Calc_func()
        Exercise_Treadmill.Parms_func()
        RightHemithorax.Calc_func()
        LeftHemithorax.Calc_func()
        Thorax.Calc_func()
        Ventilator.Calc_func()
        Organs_Vasculature.Parms_func()
        LacPool.Parms_func()
        PT_NH3.Parms_func()
        NephronAldo.Parms_func()
        NephronADH.Parms_func()
        NephronANP.Parms_func()
        MedullaNa.Parms_func()
        MedullaUrea.Parms_func()
        Baroreflex.Parms_func()
        LowPressureReceptors.Parms_func()
        LeftHeart_Infarction.Parms_func()
        RightHeart_Infarction.Parms_func()
        Transfusion.Parms_func()
        Hemorrhage.Parms_func()
        BloodVolume.Parms_func()
        ChemoreceptorAcclimation.Parms_func()
        Anesthesia.Parms_func()
        Drugs.Parms_func()
        ADH.Parms_func()
        ANP.Parms_func()
        EPO.Parms_func()
        Insulin.Parms_func()
        ThyroidGland.Parms_func()
        Renin.Parms_func()
        Catechols.Parms_func()
        Diet.Parms_func()
        Hypothalamus.Parms_func()
        DailyPlannerSchedule.Parms_func()
        DailyPlannerControl.Parms_func()
        OralH2OGlucoseLoad.Parms_func()
        IVDrip.Parms_func()
        Hemodialysis.Parms_func()
        PostureControl.Parms_func()
        Exercise_Control.Parms_func()
        Exercise_Metabolism.Parms_func()
        K.Parms_func()
        GlucosePump.Parms_func()
        KAPump.Parms_func()
        LiverMetabolism.Parms_func()
        RespiratoryMuscle_Insulin.Parms_func()
        SkeletalMuscle_Insulin.Parms_func()
        Kidney_Myogenic.Parms_func()
        CPR.Parms_func()
        SkeletalMuscle_MetabolicVasodilation.Parms_func()
        Leptin.Parms_func()
        HeartValves.Parms_func()
        LH.Parms_func()
        FSH.Parms_func()
        if Gender.IsFemale:
            Ovaries.Parms_func()
        else:
            pass
        Heart_Pacemaker.Parms_func()
        Sweat.Parms_func()

    def Dervs_func(self):
        BloodVolume.CalcVol_func()
        Transfusion.CalcVol_func()
        TissueH2O.CalcVol_func()
        ExternalH2O.CalcVol_func()
        H2O.CalcVol_func()
        SO4Pool.CalcOsmoles_func()
        PO4Pool.CalcOsmoles_func()
        GlucosePool.CalcOsmoles_func()
        Urea.CalcOsmoles_func()
        KAPool.CalcOsmoles_func()
        BVSeq.Calc_func()
        SystemicVeins.CalcVol_func()
        OsmCell.Calc_func()
        OsmECFV.Calc_func()
        OsmBody.Calc_func()
        H2O.Calc_func()
        TissueH2O.Calc_func()
        Organs_Size.Calc_func()
        Weight.Calc_func()
        BMI.Calc_func()
        SurfaceArea.Calc_func()
        Estradiol.Conc_func()
        FSH.Conc_func()
        hCG.Conc_func()
        Inhibin.Conc_func()
        LH.Conc_func()
        Progesterone.Conc_func()
        Testosterone.Conc_func()
        Kidney_NephronCount.Calc_func()
        Heat.CalcTemp_func()
        CellProtein.CalcConc_func()
        Viscosity.Calc_func()
        ArtysVol.Calc_func()
        VeinsVol.Calc_func()
        GILumen.Conc_func()
        Drugs.CalcConc_func()
        NaPool.CalcConc_func()
        K.Conc_func()
        ClPool.CalcConc_func()
        SO4Pool.CalcConc_func()
        PO4Pool.CalcConc_func()
        CellSID.Calc_func()
        Aldosterone.CalcConc_func()
        ADH.CalcConc_func()
        Insulin.CalcConc_func()
        Glucagon.CalcConc_func()
        EPO.CalcConc_func()
        ThyroidGland.CalcConc_func()
        Thyroid.CalcEffect_func()
        Leptin.Conc_func()
        DesglymidodrinePool.CalcConc_func()
        Catechols.CalcConc_func()
        PlasmaProtein.CalcConc_func()
        LacPool.CalcConc_func()
        KAPool.CalcConc_func()
        FAPool.CalcConc_func()
        Triglyceride.Conc_func()
        Triglyceride.Rate_func()
        GlucosePool.CalcConc_func()
        AAPool.CalcConc_func()
        Urea.CalcConc_func()
        Creatine.Calc_func()
        Creatinine.Conc_func()
        GlycerolPool.CalcConc_func()
        BloodIons.CalcSID_func()
        O2.CalcConc_func()
        CO2.CalcConc_func()
        BloodIons.FinishSums_func()
        BloodPh.Calc_func()
        Organs_Lactate.CalcConc_func()
        Organs_Ph.CalcSID_func()
        Organs_CO2.CalcConc_func()
        Organs_Ph.CalcPh_func()
        Exercise_Treadmill.Calc_func()
        Exercise_Metabolism.Dervs_func()
        SkeletalMuscle_Metaboreflex.Calc_func()
        MotorRadiation.Calc_func()
        ExerciseSymps.Calc_func()
        Exercise_MusclePump.Calc_func()
        SkeletalMuscle_MusclePumping.Calc_func()
        Anesthesia.Calc_func()
        BrainInsult.Calc_func()
        Brain_Function.Calc_func()
        GlasgowComaScale.Calc_func()
        Organs_Function.Calc_func()
        Hypothalamus.CalcEffect_func()
        Heat.Cals_func()
        Sweat.Calc_func()
        Diet.Dervs_func()
        ANP.CalcConc_func()
        Hydrostatics.Calc_func()
        Pericardium.Calc_func()
        VascularCompartments.CalcPressure_1_func()
        LegMusclePump.Calc_func()
        RegionalPressure.Calc_func()
        CarotidSinus.Calc_func()
        Baroreflex.Calc_func()
        LowPressureReceptors.Calc_func()
        Mechanoreceptors.Calc_func()
        SympsChemo.Calc_func()
        CushingResponse.Calc_func()
        Renin.CalcConc_func()
        SympsCNS.Calc_func()
        SympsKidy.Calc_func()
        GangliaGeneral.Calc_func()
        GangliaKidney.Calc_func()
        VagusNerve.Calc_func()
        AdrenalNerve.Calc_func()
        SystemicVeins_AlphaReceptors.Calc_func()
        VascularCompartments.CalcPressure_2_func()
        BVSeqArtys.CalcPressure_func()
        BVSeqVeins.CalcPressure_func()
        Peritoneum.Dervs_func()
        Hemodialysis.Dervs_func()
        CO.Calc_func()
        HgbConc.Calc_func()
        HgbTissue.Setup_func()
        HgbLung.Setup_func()
        O2.CalcPO2_func()
        CD_H2OChannels.CalcActive_func()
        Organs_AlphaReceptors.Calc_func()
        Organs_BetaReceptors.Calc_func()
        BloodVolume.CalcV0_func()
        Heart.Calc_func()
        LeftHeartPumping.Dervs_func()
        RightHeartPumping.Dervs_func()
        CardiacOutput.Calc_func()
        SystemicArtys.PulsatilePressure_func()
        PulmArty.PulsatilePressure_func()
        PulmArty.CalcOutflow_func()
        PulmCapys.CalcOutflow_func()
        LungBloodFlow.Calc_func()
        LungArtyO2.Calc_func()
        LungArtyCO2.Calc_func()
        Chemoreceptors.Calc_func()
        RespiratoryCenter.Calc_func()
        Breathing.Calc_func()
        PulmonaryMembrane.Calc_func()
        LungO2.Calc_func()
        LungVeinO2.Calc_func()
        LungCO2.Calc_func()
        LungVeinCO2.Calc_func()
        GasExchangeRatio.Calc_func()
        Organs_Pressure.Calc_func()
        Kidney_ArcuateArtery.CalcConductance_func()
        Kidney_AfferentArtery.Dervs_func()
        Kidney_EfferentArtery.Dervs_func()
        Kidney_Flow.Calc_func()
        Kidney_ArcuateArtery.CalcPressure_func()
        NephronIFP.Calc_func()
        GlomerulusFiltrate.Calc_func()
        NephronANP.Calc_func()
        PT_Na.Calc_func()
        PT_H2O.Calc_func()
        PT_Na.CalcConc_func()
        PT_NH3.Calc_func()
        NephronAldo.Calc_func()
        LH_Na.Calc_func()
        LH_H2O.Calc_func()
        LH_Na.CalcConc_func()
        MD_Na.Calc_func()
        DT_Na.Calc_func()
        NephronADH.Calc_func()
        DT_H2O.Calc_func()
        DT_Na.CalcConc_func()
        DT_K.Calc_func()
        MedullaNa.CalcConc_func()
        MedullaUrea.CalcConc_func()
        Medulla.CalcOsm_func()
        LeftHeart_Work.Calc_func()
        RespiratoryMuscle_Work.Calc_func()
        RightHeart_Work.Calc_func()
        SkeletalMuscle_Work.Calc_func()
        Organs_Metabolism.CalcCals_func()
        Metabolism_CaloriesUsed.Calc_func()
        Metabolism_MetabolicRate.Calc_func()
        HepaticArty.CalcFlow_func()
        SkeletalMuscle_MetabolicVasodilation.Calc_func()
        Organs_Flow.Calc_func()
        OrganFlow.Calc_func()
        Kidney_O2.Calc_func()
        Liver_O2.Calc_func()
        Organs_Metabolism.SplitCals_func()
        SkeletalMuscle_Glycogen.Dervs_func()
        RespiratoryMuscle_Glycogen.Dervs_func()
        Organs_Fuel.Dervs_func()
        NephronGlucose.CalcSpillover_func()
        NephronKetoacids.CalcExcretion_func()
        CollectingDuct.Calc_func()
        VasaRecta.Calc_func()
        Metabolism_FuelUse.Calc_func()
        CNSTrophicFactor.Dervs_func()
        ExcessLungWater.Dervs_func()
        Organs_Structure.Calc_func()
        Organs_Vasculature.Calc_func()
        Organs_CO2.CalcDervs_func()
        IVDrip.Dervs_func()
        Hemorrhage.Dervs_func()
        GILumen.Dervs_func()
        Heat.Dervs_func()
        Sweat.Dervs_func()
        H2O.EarlyDervs_func()
        TissueH2O.Dervs_func()
        NaPool.CalcDervs_func()
        K.Dervs_func()
        ClPool.CalcDervs_func()
        SO4Pool.CalcDervs_func()
        PO4Pool.CalcDervs_func()
        CellProtein.Dervs_func()
        Aldosterone.Dervs_func()
        ADH.Dervs_func()
        ANP.Dervs_func()
        Insulin.Dervs_func()
        Glucagon.Dervs_func()
        EPO.Dervs_func()
        ThyroidGland.Dervs_func()
        RightHeartPumping.Dervs_func()
        LeftHeartPumping.Dervs_func()
        VascularCompartments.Dervs_func()
        SplanchnicCirculation.Calc_func()
        Liver_Fuel.Dervs_func()
        Metabolism_Glucose.Calc_func()
        Metabolism_FattyAcid.Calc_func()
        LiverMetabolism.Dervs_func()
        LipidDeposits.Dervs_func()
        Urea.Dervs_func()
        KADecomposition.Dervs_func()
        KAPool.CalcDervs_func()
        FADecomposition.Dervs_func()
        FAPool.CalcDervs_func()
        Triglyceride.Dervs_func()
        GlucoseDecomposition.Dervs_func()
        GlucosePool.CalcDervs_func()
        AAPool.CalcDervs_func()
        Organs_Lactate.CalcDervs_func()
        LacPool.CalcDervs_func()
        MedullaNa.Dervs_func()
        MedullaUrea.Dervs_func()
        CD_H2OChannels.CalcDervs_func()
        O2.Dervs_func()
        CO2.Dervs_func()
        BVSeqArtys.Dervs_func()
        BVSeqVeins.Dervs_func()
        Bone_Mineral.Dervs_func()
        LeftHeart_ContractileProtein.Dervs_func()
        RightHeart_ContractileProtein.Dervs_func()
        RespiratoryMuscle_ContractileProtein.Dervs_func()
        SkeletalMuscle_ContractileProtein.Dervs_func()
        BrainInsult_PO2.Dervs_func()
        Baroreflex.Dervs_func()
        LeftHeart_Infarction.Dervs_func()
        RightHeart_Infarction.Dervs_func()
        ChemoreceptorAcclimation.Calc_func()
        Anesthesia.Dervs_func()
        Drugs.Dervs_func()
        TGF_Vascular.Dervs_func()
        TGF_Renin.Dervs_func()
        Renin.Dervs_func()
        Catechols.Dervs_func()
        Hypothalamus.Dervs_func()
        OralH2OGlucoseLoad.Dervs_func()
        Exercise_Treadmill.Dervs_func()
        Bladder.Dervs_func()
        Peritoneum.Dervs_func()
        Pericardium.Dervs_func()
        BloodVolume.Dervs_func()
        PlasmaProtein.CalcDervs_func()
        H2O.Dervs_func()
        Creatinine.Dervs_func()
        GlycerolPool.Dervs_func()
        RespiratoryMuscle_Insulin.Dervs_func()
        SkeletalMuscle_Insulin.Dervs_func()
        Kidney_Myogenic.Dervs_func()
        SkeletalMuscle_MetabolicVasodilation.Dervs_func()
        Leptin.Dervs_func()
        if Gender.IsFemale:
            Ovaries.Dervs_func()
            Uterus.Dervs_func()
        else:
            Testes.Dervs_func()
        GnRH.Dervs_func()
        hCG.Dervs_func()
        Estradiol.Dervs_func()
        FSH.Dervs_func()
        Inhibin.Dervs_func()
        LH.Dervs_func()
        Progesterone.Dervs_func()
        Testosterone.Dervs_func()
        CO.Dervs_func()

    def Wrapup_func(self):
        Organs_Function.Wrapup_func()
        Age.Calc_func()
        if Gender.IsFemale:
            Ovaries.Wrapup_func()
        else:
            pass
        Autopsy.Calc_func()
        Seizure.Calc_func()
        Brain_Function.Page_func()
        SystemicArtys.Wrapup_func()
        Drugs.Wrapup_func()
        Catechols.Wrapup_func()
        Status.CheckConscious_func()
        Exercise_Control.Wrapup_func()
        DailyPlannerControl.Wrapup_func()
        Status.Wrapup_func()
        Hemodialysis.Wrapup_func()
        Bladder.Wrapup_func()
        Heart.Wrapup_func()
        CPR.Wrapup_func()
        Heart.Final_func()
        PeripheralResistance.Wrapup_func()
        BodyH2O.Wrapup_func()
        Symptoms.Calc_func()

class ADHPump:
    def __init__(self):
        self.Rate = None
        self.Switch = False
        self.Setting = 0.0

    def Parms_func(self):
        if self.Switch:
            self.Rate = self.Setting
        else:
            self.Rate = 0.0


class ADHPool:
    def __init__(self):
        self.conc_ADH = None
        self.conc_ADH_pMolperL = None
        self.conc_ADH_uUpermL = None
        self.Log10Conc = None
        self.PGTOPMOL = 0.922
        self.PGTOUUNITS = 0.400
        self.Gain = None
        self.Loss = None
        self.Targetconc_ADH = 2.0
        self.InitialMass = None

    def Init_func(self):
        self.InitialMass = self.Targetconc_ADH * ECFV.InitialVol_L
        self.Mass = self.InitialMass

    def Initialize_func(self):
        self.Mass = self.InitialConc * ECFV.Vol_L

    def CalcConc_func(self):
        self.conc_ADH = self.Mass / ECFV.Vol_L
        self.conc_ADH_pMolperL = self.PGTOPMOL * self.conc_ADH
        self.conc_ADH_uUpermL = self.PGTOUUNITS * self.conc_ADH
        if self.conc_ADH > 1.0:
            self.Log10Conc = ( math.log10( self.conc_ADH ) )
        else:
            self.Log10Conc = 0.0

    def Dervs_func(self):
        self.Gain = ADHSecretion.Rate + ADHPump.Rate
        self.Loss = ADHClearance.Total
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.3)


class ADHSecretion:
    def __init__(self):
        self.Rate = None
        self.BaseK = 0.001
        self.Base = None
        self.conc_OsmEffect = None
        self.NeuralEffect = None

    def conc_OsmEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.243, 0.253, 0.263], [0.0, 1.0, 5.0], [0.0, 180.0, 0.0])

    def NeuralEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.5, 1.0, 1.2, 1.5], [0.4, 1.0, 2.0, 20.0], [0.0, 0.4, 5.0, 0.0])

    def Dervs_func(self):
        self.Base = self.BaseK * ADHFastMass.Mass
        self.conc_OsmEffect = self.conc_OsmEffect_curve( OsmBody.conc_Osm_Osmoreceptors )
        self.NeuralEffect = self.NeuralEffect_curve( SympsCNS.PituitaryNA )
        self.Rate = self.Base * self.conc_OsmEffect * self.NeuralEffect

class ADHClearance:
    def __init__(self):
        self.Total = None
        self.Liver = None
        self.Kidney = None
        self.Other = None
        self.LiverK = 0.0005
        self.KidneyK = 0.00059
        self.OtherK = 0.00108

    def Dervs_func(self):
        self.Liver = self.LiverK * GITract_Flow.BloodFlow * ADHPool.conc_ADH
        self.Kidney = self.KidneyK * Kidney_Flow.BloodFlow * ADHPool.conc_ADH
        self.Other = self.OtherK * OtherTissue_Flow.BloodFlow * ADHPool.conc_ADH
        self.Total = self.Liver + self.Kidney + self.Other

class ADH:

    def Parms_func(self):
        ADHPump.Parms_func()

    def CalcConc_func(self):
        ADHPool.CalcConc_func()

    def Dervs_func(self):
        ADHSlowMass.Flux_func()
        ADHFastMass.Flux_func()
        ADHSynthesis.Dervs_func()
        ADHSecretion.Dervs_func()
        ADHSlowMass.Dervs_func()
        ADHFastMass.Dervs_func()
        ADHClearance.Dervs_func()
        ADHPool.Dervs_func()

class ADHSynthesis:
    def __init__(self):
        self.Base = 3.2
        self.Rate = None
        self.Feedback = None

    def Feedback_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 17000.0, 20000.0], [4.0, 1.0, 0.0], [0.0, -0.0003, 0.0])

    def Dervs_func(self):
        self.Feedback = self.Feedback_curve( ADHSlowMass.Mass )
        self.Rate = self.Base * self.Feedback

class ADHFastMass:
    def __init__(self):
        self.FluxK = 0.0043
        self.Flux = None
        self.Mass = 3200.0

    def Flux_func(self):
        self.Flux = self.FluxK * self.Mass

    def Dervs_func(self):
        self.Change = ADHSlowMass.Flux - self.Flux - ADHSecretion.Rate
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 32.0)


class ADHSlowMass:
    def __init__(self):
        self.FluxK = 0.0010
        self.Flux = None
        self.Mass = 17000.0

    def Flux_func(self):
        self.Flux = self.FluxK * self.Mass

    def Dervs_func(self):
        self.Change = ADHSynthesis.Rate + ADHFastMass.Flux - self.Flux
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 170.0)


class ICFV:
    def __init__(self):
        self.Vol = None
        self.InitialVol = None
        self.Vol_L = None
        self.FractBodyH2O = None

    def Initialize_func(self):
        self.FractBodyH2O = 1.0 - ECFV.FractBodyH2O
        self.InitialVol = self.FractBodyH2O * BodyH2O.InitialVol
        self.Vol = self.InitialVol
        self.Vol_L = self.Vol / 1000.0

    def CalcVol_func(self):
        self.Vol = OsmBody.ICFV
        self.Vol_L = self.Vol / 1000.0

class ECFV:
    def __init__(self):
        self.Vol = None
        self.InitialVol = None
        self.Vol_L = None
        self.InitialVol_L = None
        self.FractBodyH2O = 0.35

    def Initialize_func(self):
        self.InitialVol = self.FractBodyH2O * BodyH2O.InitialVol
        self.Vol = self.InitialVol
        self.InitialVol_L = self.InitialVol / 1000.0
        self.Vol_L = self.InitialVol_L

    def CalcVol_func(self):
        self.Vol = OsmBody.ECFV
        self.Vol_L = self.Vol / 1000.0

class H2O:

    def CalcVol_func(self):
        BodyH2O.CalcTotal_func()

    def Calc_func(self):
        ECFV.CalcVol_func()
        ICFV.CalcVol_func()

    def EarlyDervs_func(self):
        MetabolicH2O.Dervs_func()

    def Dervs_func(self):
        ExternalH2O.Dervs_func()
        BodyH2O.Dervs_func()

class ExternalH2O:
    def __init__(self):
        self.Vol = None
        self.InitialVol = None
        self.Vol_L = None
        self.Core = None
        self.InitialCore = None
        self.Core_L = None
        self.Other = None
        self.InitialOther = None
        self.Other_L = None
        self.Change = None

    def Initialize_func(self):
        GILumenVolume.Initialize_func()
        PeritoneumSpace.Initialize_func()
        ExcessLungWater.Initialize_func()
        self.InitialCore = PeritoneumSpace.InitialVolume + ExcessLungWater.InitialVolume
        self.InitialOther = GILumenVolume.InitialMass
        self.InitialVol = self.InitialCore + self.InitialOther

    def CalcVol_func(self):
        self.Core = PeritoneumSpace.Volume + ExcessLungWater.Volume
        self.Core_L = self.Core / 1000.0
        self.Other = GILumenVolume.Mass
        self.Other_L = self.Other / 1000.0
        self.Vol = self.Core + self.Other
        self.Vol_L = self.Vol / 1000.0

    def Dervs_func(self):
        self.Change = GILumenVolume.Change + PeritoneumSpace.Change + ExcessLungWater.Change

class BodyH2O:
    def __init__(self):
        self.Vol = None
        self.InitialVol = None
        self.Vol_L = None
        self.TotalVol = None
        self.InitialTotalVol = None
        self.TotalVol_L = None
        self.Gain = None
        self.Loss = None
        self.Change = None
        self.IntravascularVol = None
        self.IntravascularVol_L = None
        self.ExtravascularVol = None
        self.ExtravascularVol_L = None

    def Initialize_func(self):
        self.InitialVol = TissueH2O.InitialVol + PlasmaVol.InitialVol + RBCH2O.InitialVol + ExternalH2O.InitialCore
        self.InitialTotalVol = self.InitialVol + ExternalH2O.InitialOther

    def CalcTotal_func(self):
        self.Vol = TissueH2O.Vol + PlasmaVol.Vol + RBCH2O.Vol + ExternalH2O.Core
        self.Vol_L = self.Vol / 1000.0
        self.TotalVol = self.Vol + ExternalH2O.Other
        self.TotalVol_L = self.TotalVol / 1000.0

    def Dervs_func(self):
        self.Gain = GILumenVolume.Intake + MetabolicH2O.Rate + IVDrip.H2ORate + Transfusion.Rate
        self.Loss = CD_H2O.Outflow + SweatDuct.H2OOutflow + Hemorrhage.Rate + DialyzerActivity.UltrafiltrationRate + HeatInsensibleSkin.H2O + HeatInsensibleLung.H2O + GILumenVomitus.H2OLoss + GILumenDiarrhea.H2OLoss
        self.Change = self.Gain - self.Loss

    def Wrapup_func(self):
        self.IntravascularVol = PlasmaVol.Vol + RBCH2O.Vol
        self.IntravascularVol_L = self.IntravascularVol / 1000.0
        self.ExtravascularVol = InterstitialWater.Vol + CellH2O.Vol + ExternalH2O.Vol
        self.ExtravascularVol_L = self.ExtravascularVol / 1000.0

class MetabolicH2O:
    def __init__(self):
        self.Rate = None
        self.K = 0.000176

    def Dervs_func(self):
        self.Rate = self.K * Metabolism_CaloriesUsed.Total

class RightHeartPumping_Pumping:
    def __init__(self):
        self.BloodFlow = None
        self.StrokeVolume = None
        self.EjectionFraction = None

    def Calc_func(self):
        self.StrokeVolume = RightHeartPumping_Diastole.EDV - RightHeartPumping_Systole.ESV
        self.BloodFlow = Heart_Ventricles.Rate * self.StrokeVolume
        self.EjectionFraction = self.StrokeVolume / RightHeartPumping_Diastole.EDV

class RightHeartPumping_Diastole:
    def __init__(self):
        self.EDV = None
        self.EDP = None
        self.TMP = None
        self.A_Basic = 0.00026
        self.A = None
        self.n = 2.0
        self.Stiffness = 1.0

    def Calc_func(self):
        self.EDP = RightAtrium.Pressure
        self.TMP = self.EDP - Pericardium_Cavity.Pressure
        self.A = self.Stiffness * self.A_Basic
        self.V_equals_f_P_func()

    def P_equals_f_V_func(self):
        self.TMP = self.A * ( self.EDV ** self.n )

    def V_equals_f_P_func(self):
        self.EDV = ( self.TMP / self.A ) ** ( 1.0 / self.n )

class RightHeartPumping_Systole:
    def __init__(self):
        self.ESV = None
        self.ESP = None
        self.TMP = None
        self.A_Basic = 3.53
        self.A = None
        self.n = 0.5
        self.Contractility_Basic = 1.0
        self.Contractility = None

    def Calc_func(self):
        self.ESP = PulmArty.Pressure + 9.0
        self.TMP = self.ESP - Pericardium_Cavity.Pressure
        self.Contractility = self.Contractility_Basic * RightHeart_BetaReceptors.Activity
        self.A = self.Contractility * self.A_Basic
        self.V_equals_f_P_func()

    def P_equals_f_V_func(self):
        self.TMP = self.A * ( self.ESV ** self.n )

    def V_equals_f_P_func(self):
        self.ESV = ( self.TMP / self.A ) ** ( 1.0 / self.n )

class RightHeartPumping:

    def Dervs_func(self):
        RightHeartPumping_Diastole.Calc_func()
        RightHeartPumping_Systole.Calc_func()
        RightHeartPumping_Pumping.Calc_func()

class RightHeartPumping_Valves:
    def __init__(self):
        pass
    
class GlucosePump:
    def __init__(self):
        self.Rate = None
        self.Switch = False
        self.Setting = 0.0

    def Parms_func(self):
        if self.Switch:
            self.Rate = self.Setting
        else:
            self.Rate = 0.0


class Glucose:
    def __init__(self):
        pass
    
class GlucosePool:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.conc_Glucose = None
        self.conc_Glucose_mGperdL = None
        self.conc_Glucose_mMolperL = None
        self.PER_ML_TO_PER_DL = 100.0
        self.MG_TO_MMOL = 5.551
        self.Osmoles = None
        self.conc_Osm = None
        self.conc_Osm_mOsmperL = None
        self.MW = 180.0
        self.Targetconc_Glucose = 1.10
        self.InitialMass = None

    def CalcOsmoles_func(self):
        self.Osmoles = self.Mass / self.MW

    def Init_func(self):
        self.InitialMass = self.Targetconc_Glucose * ECFV.Vol
        self.Mass = self.InitialMass

    def CalcConc_func(self):
        self.conc_Glucose = self.Mass / ECFV.Vol
        self.conc_Glucose_mGperdL = self.PER_ML_TO_PER_DL * self.conc_Glucose
        self.conc_Glucose_mMolperL = self.MG_TO_MMOL * self.conc_Glucose
        self.conc_Osm = self.Osmoles / ECFV.Vol
        self.conc_Osm_mOsmperL = 1000.0 * self.conc_Osm

    def CalcDervs_func(self):
        self.Gain = GILumenCarbohydrates.Absorption + LM_Glucose.Release + GlucosePump.Rate
        self.Loss = Metabolism_Glucose.TotalUptake + LM_Glucose.Uptake + NephronGlucose.Spillover + GlucoseDecomposition.Rate
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 165.0)


class GlucoseDecomposition:
    def __init__(self):
        self.Rate = None
        self.K = 0.0007

    def Dervs_func(self):
        self.Rate = self.K * GlucosePool.Mass

class ThyroidClearance:
    def __init__(self):
        self.Rate = None
        self.K = 0.000041

    def Dervs_func(self):
        self.Rate = self.K * ThyroidPool.Mass

class ThyroidPump:
    def __init__(self):
        self.Rate = None
        self.Switch = False
        self.Setting = 0.0

    def Parms_func(self):
        if self.Switch:
            self.Rate = self.Setting
        else:
            self.Rate = 0.0


class ThyroidTSH:
    def __init__(self):
        self.conc_TSH = None
        self.conc_T4_T3Effect = None
        self.TemperatureEffect = None
        self.Base = 4.0

    def conc_T4_T3Effect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 8.0, 20.0], [8.0, 1.0, 0.0], [0.0, -0.2, 0.0])

    def Dervs_func(self):
        self.conc_T4_T3Effect = self.conc_T4_T3Effect_curve( ThyroidPool.conc_Total_T4_T3 )
        self.TemperatureEffect = HypothalamusTSH.TemperatureEffect
        self.conc_TSH = self.Base * self.conc_T4_T3Effect * self.TemperatureEffect

class ThyroidGland:

    def Parms_func(self):
        ThyroidPump.Parms_func()

    def CalcConc_func(self):
        ThyroidPool.CalcConc_func()

    def Dervs_func(self):
        ThyroidTSH.Dervs_func()
        ThyroidSecretion.Dervs_func()
        ThyroidClearance.Dervs_func()
        ThyroidPool.Dervs_func()

class ThyroidPool:
    def __init__(self):
        self.conc_Total_T4_T3 = None
        self.conc_Free_T4_T3 = None
        self.ML_TO_DL = 0.01
        self.TOTAL_TO_FREE = 0.5
        self.Gain = None
        self.Loss = None
        self.Targetconc_Total_T4_T3 = 8.0
        self.InitialMass = None

    def Init_func(self):
        self.InitialMass = self.Targetconc_Total_T4_T3 * self.ML_TO_DL * ECFV.InitialVol
        self.Mass = self.InitialMass

    def CalcConc_func(self):
        self.conc_Total_T4_T3 = self.Mass / ( self.ML_TO_DL * ECFV.Vol )
        self.conc_Free_T4_T3 = self.TOTAL_TO_FREE * self.conc_Total_T4_T3

    def Dervs_func(self):
        self.Gain = ThyroidSecretion.Rate + ThyroidPump.Rate
        self.Loss = ThyroidClearance.Rate
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 12.0)


class ThyroidSecretion:
    def __init__(self):
        self.Rate = None
        self.conc_TSHEffect = None
        self.Base = 0.05

    def conc_TSHEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 4.0, 30.0], [0.0, 1.0, 10.0], [0.0, 0.4, 0.0])

    def Dervs_func(self):
        self.conc_TSHEffect = self.conc_TSHEffect_curve( ThyroidTSH.conc_TSH )
        self.Rate = self.Base * self.conc_TSHEffect

class HgbConc:
    def __init__(self):
        self.conc_Total = None
        self.Clamp = False
        self.conc_Level = 0.0
        self.conc_Basic = 0.15
        self.HctEffect = None
        self.conc_Free = None
        self.conc_Carboxy = None
        self.CarboxyPercent = None
        self.GasMaxContent = None
        self.conc_O2Max = None
        self.NORMALHCT = 0.44
        self.O2MAX_MLperG = 1.34
        self.conc_O2 = None
        self.Sat_percent = None

    def Calc_func(self):
        self.HctEffect = BloodVol.Hct / self.NORMALHCT
        if self.Clamp:
            self.conc_Total = self.conc_Level
        else:
            self.conc_Total = self.HctEffect * self.conc_Basic

        self.conc_Carboxy = ( min( ( CO.conc_CO / self.O2MAX_MLperG ), self.conc_Total) )
        if self.conc_Total > 0.0:
            self.CarboxyPercent = 100 * self.conc_Carboxy / self.conc_Total
        else:
            self.CarboxyPercent = 0.0

        self.conc_Free = self.conc_Total - self.conc_Carboxy
        self.GasMaxContent = self.O2MAX_MLperG * self.conc_Total
        self.conc_O2Max = self.O2MAX_MLperG * self.conc_Free

    def Sat_percent_func(self):
        if self.conc_O2 > 0.0:
            self.Sat_percent = 100.0 * self.conc_O2 / self.conc_O2Max
        else:
            self.Sat_percent = 0.0


class HgbTissue:
    def __init__(self):
        self.pO2 = None
        self.conc_O2 = None
        self.pH = None
        self.pCO2 = None
        self.P50 = None
        self.ScaleForSat = None
        self.pHEffect = None
        self.pCO2Effect = None
        self.TempEffect = None
        self.COEffect = None

    def Setup_func(self):
        HgbProps.Temp = HeatCore.Temp_C
        HgbProps.pH = BloodPh.VeinsPh
        HgbProps.pCO2 = CO2Veins.Pressure
        HgbProps.Setup_func()
        self.P50 = HgbProps.P50
        self.ScaleForSat = HgbProps.ScaleForSat
        self.pHEffect = HgbProps.pHEffect
        self.pCO2Effect = HgbProps.pCO2Effect
        self.TempEffect = HgbProps.TempEffect
        self.COEffect = HgbProps.COEffect

    def O2ToPO2_func(self):
        HgbProps.conc_O2 = self.conc_O2
        HgbProps.P50 = self.P50
        HgbProps.ScaleForSat = self.ScaleForSat
        HgbProps.O2ToPO2_func()
        self.pO2 = HgbProps.pO2

    def PO2ToO2_func(self):
        HgbProps.pO2 = self.pO2
        HgbProps.P50 = self.P50
        HgbProps.ScaleForSat = self.ScaleForSat
        HgbProps.PO2ToO2_func()
        self.conc_O2 = HgbProps.conc_O2

class HgbProps:
    def __init__(self):
        self.HILLCONSTANT = 2.3
        self.PO2SATURATED = 120
        self.O2SOLUBILITY = 0.00003
        self.TEMPK = 0.024
        self.PHK = -0.40
        self.PCO2K = 0.06
        self.COK = -0.0067
        self.TEMPNORM = 37.0
        self.PHNORM = 7.40
        self.CO2NORM = 40.0
        self.CONORM = 0.0
        self.pO2 = None
        self.conc_O2 = None
        self.pH = None
        self.pCO2 = None
        self.Temp = None
        self.pHEffect = None
        self.pCO2Effect = None
        self.TempEffect = None
        self.COEffect = None
        self.TempSens = 1.0
        self.pHSens = 1.0
        self.pCO2Sens = 1.0
        self.COSens = 1.0
        self.Del = None
        self.Log = None
        self.P50Basic = 26.6
        self.P50 = None
        self.ScaleForSat = None
        self.Sat = None
        self.S = None
        self.An = None
        self.A = None
        self.K = None

    def Setup_func(self):
        self.Del = self.Temp - self.TEMPNORM
        self.TempEffect = 10 ** ( self.TempSens * self.TEMPK * self.Del )
        self.Del = self.pH - self.PHNORM
        self.pHEffect = 10 ** ( self.pHSens * self.PHK * self.Del )
        if self.pCO2 < 1.0:
            self.Log = 0.0
        else:
            self.Log = ( math.log10( self.pCO2 ) )

        self.Del = self.Log - ( math.log10( self.CO2NORM ) )
        self.pCO2Effect = 10 ** ( self.pCO2Sens * self.PCO2K * self.Del )
        self.Del = HgbConc.CarboxyPercent - self.CONORM
        self.COEffect = 10 ** ( self.COSens * self.COK * self.Del )
        self.P50 = self.P50Basic * self.TempEffect * self.pHEffect * self.pCO2Effect * self.COEffect
        self.An = ( self.PO2SATURATED / self.P50 ) ** self.HILLCONSTANT
        self.ScaleForSat = ( 1.0 + self.An ) / self.An

    def O2ToPO2_func(self):
        if self.conc_O2 <= 0.0:
            self.pO2 = 0.0
        elif self.conc_O2 > HgbConc.conc_O2Max:
            self.pO2 = self.PO2SATURATED + ( ( self.conc_O2 - HgbConc.conc_O2Max ) / self.O2SOLUBILITY )
        elif True:
            self.Sat = self.conc_O2 / HgbConc.conc_O2Max
            self.S = self.Sat / self.ScaleForSat
            self.A = ( self.S / ( 1.0 - self.S ) ) ** ( 1.0 / self.HILLCONSTANT )
            self.pO2 = self.A * self.P50

    def PO2ToO2_func(self):
        if self.pO2 <= 0.0:
            self.conc_O2 = 0.0
        elif self.pO2 >= self.PO2SATURATED:
            self.conc_O2 = HgbConc.conc_O2Max + ( ( self.pO2 - self.PO2SATURATED ) * self.O2SOLUBILITY )
        elif True:
            self.An = ( self.pO2 / self.P50 ) ** self.HILLCONSTANT
            self.Sat = self.ScaleForSat * self.An / ( 1.0 + self.An )
            self.conc_O2 = self.Sat * HgbConc.conc_O2Max

class Hemoglobin:
    def __init__(self):
        pass
    
class HgbLung:
    def __init__(self):
        self.pO2 = None
        self.conc_O2 = None
        self.pH = None
        self.pCO2 = None
        self.P50 = None
        self.ScaleForSat = None
        self.pHEffect = None
        self.pCO2Effect = None
        self.TempEffect = None
        self.COEffect = None

    def Setup_func(self):
        HgbProps.Temp = HeatCore.Temp_C
        HgbProps.pH = BloodPh.ArtysPh
        HgbProps.pCO2 = CO2Artys.Pressure
        HgbProps.Setup_func()
        self.P50 = HgbProps.P50
        self.ScaleForSat = HgbProps.ScaleForSat
        self.pHEffect = HgbProps.pHEffect
        self.pCO2Effect = HgbProps.pCO2Effect
        self.TempEffect = HgbProps.TempEffect
        self.COEffect = HgbProps.COEffect

    def O2ToPO2_func(self):
        HgbProps.conc_O2 = self.conc_O2
        HgbProps.P50 = self.P50
        HgbProps.ScaleForSat = self.ScaleForSat
        HgbProps.O2ToPO2_func()
        self.pO2 = HgbProps.pO2

    def PO2ToO2_func(self):
        HgbProps.pO2 = self.pO2
        HgbProps.P50 = self.P50
        HgbProps.ScaleForSat = self.ScaleForSat
        HgbProps.PO2ToO2_func()
        self.conc_O2 = HgbProps.conc_O2

class Skin_Size:
    def __init__(self):
        self.Vol = None
        self.Mass = None
        self.InitialMass = None
        self.Mass_kG = None
        self.Density = None
        self.LiquidMass = None
        self.LiquidDensity = 1.00
        self.LiquidVol = None
        self.InitialLiquidVol = None
        self.SolidMass = None
        self.InitialSolidMass = None
        self.SolidDensity = 1.36
        self.SolidVol = None
        self.FractTotal = None
        self.IFV = None
        self.InitialIFV = None
        self.CellH2O = None
        self.InitialCellH2O = None
        self.MassFractBase = 0.102
        self.H2OFractMass = 0.67
        self.SolidsFractMass = None

    def Initialize_func(self):
        self.InitialMass = self.MassFractBase * Weight.InitialOtherMass
        self.InitialLiquidVol = self.H2OFractMass * self.InitialMass / self.LiquidDensity
        self.SolidsFractMass = 1.0 - self.H2OFractMass
        self.InitialSolidMass = self.SolidsFractMass * self.InitialMass

    def ScaleH2O_func(self):
        self.FractTotal = self.InitialLiquidVol / TissueH2O.InitialVol
        self.InitialIFV = self.FractTotal * InterstitialWater.InitialVol
        self.InitialCellH2O = self.FractTotal * CellH2O.InitialVol

    def Calc_func(self):
        self.IFV = self.FractTotal * InterstitialWater.Vol
        self.CellH2O = self.FractTotal * CellH2O.Vol
        self.LiquidVol = self.IFV + self.CellH2O
        self.LiquidMass = self.LiquidVol * self.LiquidDensity
        self.SolidMass = self.InitialSolidMass
        self.SolidVol = self.SolidMass / self.SolidDensity
        self.Mass = self.LiquidMass + self.SolidMass
        self.Mass_kG = self.Mass / 1000.0
        self.Vol = self.LiquidVol + self.SolidVol
        self.Density = self.Mass / self.Vol

class Skin_Function:
    def __init__(self):
        self.Failed = False
        self.Effect = None
        self.PhEffect = None
        self.ProteinEffect = None
        self.FuelEffect = None
        self.TemperatureEffect = None

    def PhOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [6.6, 6.7], [0.0, 1.0], [0.0, 0.0])

    def ProteinOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [3000.0, 5200.0], [0.0, 1.0], [0.0, 0.0])

    def FuelOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.9], [0.0, 1.0], [0.0, 0.0])

    def TemperatureOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 29.5, 40.0, 46.0], [0.0, 1.0, 1.5, 0.0], [0.0, 0.12, 0.0, 0.0])

    def Calc_func(self):
        self.PhEffect = self.PhOnFunction_curve( Skin_Ph.Ph )
        self.ProteinEffect = self.ProteinOnFunction_curve( CellProtein.Mass_G )
        self.FuelEffect = self.FuelOnFunction_curve( Skin_Fuel.FractUseDelay )
        self.TemperatureEffect = self.TemperatureOnFunction_curve( HeatSkin.Temp_C )
        self.Effect = self.PhEffect * self.ProteinEffect * self.FuelEffect * self.TemperatureEffect * Skin_Structure.Effect

    def Wrapup_func(self):
        if not self.Failed and ( self.Effect < 0.2 ):
            self.Failed = True
        elif self.Failed and ( self.Effect > 0.4 ):
            self.Failed = False

class Skin_Lactate:
    def __init__(self):
        self.conc_Lac_ = None
        self.conc_Lac__mEqperL = None
        self.conc_Lac__mGperdL = None
        self.DC = 270.0
        self.Made = None
        self.Made_mGperMin = None
        self.Used = None
        self.Used_mGperMin = None
        self.Outflux = None
        self.Outflux_0 = None
        self.K = None
        self.Alpha = None
        self.MEQ_ML_TO_MG_DL = 9008.0
        self.GLUCOSE_TO_LACTATE = 0.99
        self.MG_TO_MEQ = 0.0112
        self.Mass = 1.76

    def CalcConc_func(self):
        self.conc_Lac_ = self.Mass / Skin_Size.LiquidVol
        self.conc_Lac__mEqperL = 1000.0 * self.conc_Lac_
        self.conc_Lac__mGperdL = self.MEQ_ML_TO_MG_DL * self.conc_Lac_

    def CalcDervs_func(self):
        self.Made_mGperMin = self.GLUCOSE_TO_LACTATE * Skin_Fuel.AnaerobicGlucoseUsed_mGperMin
        self.Made = self.MG_TO_MEQ * self.Made_mGperMin
        self.Used_mGperMin = Skin_Fuel.LacUsed_mGperMin
        self.Used = self.MG_TO_MEQ * self.Used_mGperMin
        self.K = self.DC / Skin_Size.LiquidVol
        if System.Dx >=0:
            self.Alpha = 0.0
        elif ( self.K * System.Dx ) >= 100.0:
            self.Alpha = 4E-44
        elif True:
            self.Alpha = ( math.e ** ( - self.K * System.Dx ) )
        self.Outflux_0 = self.DC * ( self.conc_Lac_ - LacPool.conc_Lac_ )
        self.Outflux = ( self.Alpha * self.Outflux_0 ) + ( ( 1 - self.Alpha ) * ( self.Made + self.Used ) )
        self.Change = self.Made - self.Used - self.Outflux
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.018)


class Skin_Pressure:
    def __init__(self):
        self.ArtyPressure = None
        self.VeinPressure = None
        self.PressureGradient = None
        self.PumpSwitch = False
        self.PumpSetting = 0.0

    def Calc_func(self):
        if self.PumpSwitch:
            self.ArtyPressure = self.PumpSetting
        else:
            self.ArtyPressure = SystemicArtys.Pressure

        self.VeinPressure = SystemicVeins.Pressure
        self.PressureGradient = ( max( ( self.ArtyPressure - self.VeinPressure ), 0.0) )

class Skin_Vasculature:
    def __init__(self):
        self.Tau = 30.0
        self.Effect = 1.0

    def PO2OnStimulus_curve(self, x):
        return cubic_hermite_spline(x, [41.0, 51.0, 61.0], [1.2, 1.0, 0.8], [0.0, -0.03, 0.0])

    def Parms_func(self):
        self.K = 1.0 / ( self.Tau * 1440.0 )

    def Calc_func(self):
        if Skin_Function.Failed:
            self.Stimulus = 0.0
        else:
            self.Stimulus = self.PO2OnStimulus_curve( Skin_Flow.PO2 )

        self.Effect = delay( self.K, self.Stimulus, self.Effect, System.Dx, None)


class Skin_Fuel:
    def __init__(self):
        self.FADelivered = None
        self.GlucoseDelivered = None
        self.KR = 0.026
        self.Ratio = None
        self.FAFraction = None
        self.GlucoseFraction = None
        self.FA_GlucoseFraction = None
        self.LacFraction = None
        self.FAUsed_CalperMin = None
        self.AerobicGlucoseUsed_CalperMin = None
        self.AnaerobicGlucoseUsed_CalperMin = None
        self.LacUsed_CalperMin = None
        self.FAUsed_mGperMin = None
        self.AerobicGlucoseUsed_mGperMin = None
        self.AnaerobicGlucoseUsed_mGperMin = None
        self.LacUsed_mGperMin = None
        self.TotalGlucoseUsed_mGperMin = None
        self.AnaerobicGlucoseDelivered = None
        self.FAFractionalDelivery = None
        self.AerobicGlucoseFractionalDelivery = None
        self.AnaerobicGlucoseFractionalDelivery = None
        self.MinimumFractionalDelivery = None
        self.FractUseDelay = 1.0

    def LacFraction_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 100.0], [0.0, 0.3], [0.0, 0.0])

    def Dervs_func(self):
        self.FADelivered = ( max( ( FAPool.conc_FA * Skin_Flow.PlasmaFlow ), 0.0) )
        self.GlucoseDelivered = ( max( ( GlucosePool.conc_Glucose * Skin_Flow.PlasmaFlow ), 0.0) )
        self.LacFraction = self.LacFraction_curve( Skin_Lactate.conc_Lac__mGperdL )
        self.FA_GlucoseFraction = 1.0 - self.LacFraction
        self.Ratio = FAPool.conc_FA_mGperdL / GlucosePool.conc_Glucose_mGperdL
        self.FAFraction = self.FA_GlucoseFraction * ( self.Ratio / ( self.Ratio + self.KR ) )
        self.GlucoseFraction = self.FA_GlucoseFraction - self.FAFraction
        self.FAUsed_CalperMin = self.FAFraction * Skin_Metabolism.AerobicCals
        self.FAUsed_mGperMin = self.FAUsed_CalperMin * Metabolism_Tools.Fat_mGperCal
        self.AerobicGlucoseUsed_CalperMin = self.GlucoseFraction * Skin_Metabolism.AerobicCals
        self.AerobicGlucoseUsed_mGperMin = self.AerobicGlucoseUsed_CalperMin * Metabolism_Tools.CarboAerobic_mGperCal
        self.LacUsed_CalperMin = self.LacFraction * Skin_Metabolism.AerobicCals
        self.LacUsed_mGperMin = self.LacUsed_CalperMin * Metabolism_Tools.Lac__mGperCal
        self.AnaerobicGlucoseDelivered = self.GlucoseDelivered - self.AerobicGlucoseUsed_mGperMin
        self.AnaerobicGlucoseUsed_CalperMin = ( min( Skin_Metabolism.AnaerobicCals, self.AnaerobicGlucoseDelivered) )
        self.AnaerobicGlucoseUsed_mGperMin = self.AnaerobicGlucoseUsed_CalperMin * Metabolism_Tools.CarboAnaerobic_mGperCal
        self.TotalGlucoseUsed_mGperMin = self.AerobicGlucoseUsed_mGperMin + self.AnaerobicGlucoseUsed_mGperMin
        if self.FAUsed_mGperMin > 0.0:
            self.FAFractionalDelivery = ( min( ( self.FADelivered / self.FAUsed_mGperMin ), 1.0) )
        else:
            self.FAFractionalDelivery = 1.0

        if self.AerobicGlucoseUsed_mGperMin > 0.0:
            self.AerobicGlucoseFractionalDelivery = ( min( ( self.GlucoseDelivered / self.AerobicGlucoseUsed_mGperMin ), 1.0) )
        else:
            self.AerobicGlucoseFractionalDelivery = 1.0

        if self.AnaerobicGlucoseUsed_mGperMin > 0.0:
            self.AnaerobicGlucoseFractionalDelivery = ( min( ( self.AnaerobicGlucoseDelivered / self.AnaerobicGlucoseUsed_mGperMin ), 1.0) )
        else:
            self.AnaerobicGlucoseFractionalDelivery = 1.0

        self.MinimumFractionalDelivery = ( min( ( min( self.FAFractionalDelivery, self.AerobicGlucoseFractionalDelivery) ), self.AnaerobicGlucoseFractionalDelivery) )
        self.K = 0.5
        self.DxMax = 1.0
        self.FractUse = self.MinimumFractionalDelivery
        self.FractUseDelay = delay( self.K, self.FractUse, self.FractUseDelay, System.Dx, 0.01)


class Skin_Metabolism:
    def __init__(self):
        self.TotalCalsUsed = None
        self.NormalCalsUsed = None
        self.InitialNormalCalsUsed = None
        self.NormalCalsUsed__CalperMinperG = 0.0137
        self.CalMultiplier = 1.0
        self.AerobicCals = None
        self.AnaerobicCals = None
        self.O2Need = None
        self.O2Lack = None

    def ScaleCals_func(self):
        self.InitialNormalCalsUsed = self.CalMultiplier * self.NormalCalsUsed__CalperMinperG * Skin_Size.InitialMass

    def CalcCals_func(self):
        self.NormalCalsUsed = self.CalMultiplier * self.NormalCalsUsed__CalperMinperG * Skin_Size.Mass
        self.TotalCalsUsed = self.NormalCalsUsed * Thyroid.Effect * HeatMetabolism.Skin * Skin_Structure.Effect
        self.O2Need = Metabolism_Tools.CalToO2 * self.TotalCalsUsed

    def SplitCals_func(self):
        self.O2Lack = self.O2Need - Skin_Flow.O2Use
        self.AerobicCals = Metabolism_Tools.O2ToCal * Skin_Flow.O2Use
        self.AnaerobicCals = Metabolism_Tools.O2ToCal * self.O2Lack

class Skin_CO2:
    def __init__(self):
        self.conc_HCO3 = None
        self.conc_HCO3_mEqperL = None
        self.PCO2 = None
        self.InflowGas = None
        self.InflowBase = None
        self.OutflowBase = None
        self.conc_BloodHCO3 = None
        self.Outflow_0 = None
        self.K = None
        self.Alpha = None
        self.Mass = 28.2

    def CalcConc_func(self):
        self.conc_HCO3 = self.Mass / Skin_Size.LiquidVol
        self.conc_HCO3_mEqperL = 1000.0 * self.conc_HCO3
        Tissue_BaseToGas.conc_HCO3 = self.conc_HCO3
        Tissue_BaseToGas.conc_SID = Skin_Ph.conc_SID
        Tissue_BaseToGas.Calc_func()
        self.PCO2 = Tissue_BaseToGas.pCO2

    def CalcDervs_func(self):
        self.K = Skin_Flow.BloodFlow / Skin_Size.LiquidVol
        if System.Dx >=0:
            self.Alpha = 0.0
        elif ( self.K * System.Dx ) >= 100.0:
            self.Alpha = 4E-44
        elif True:
            self.Alpha = ( math.e ** ( - self.K * System.Dx ) )
        self.InflowGas = Metabolism_RespiratoryQuotient.RQ * Skin_Flow.O2Use
        self.InflowBase = CO2Tools.LitersToMols * self.InflowGas
        Blood_GasToBase.pCO2 = self.PCO2
        Blood_GasToBase.conc_SID = BloodIons.conc_SID
        Blood_GasToBase.Calc_func()
        self.conc_BloodHCO3 = Blood_GasToBase.conc_HCO3
        self.Outflow_0 = Skin_Flow.BloodFlow * ( self.conc_BloodHCO3 - CO2Artys.conc_HCO3 )
        self.OutflowBase = ( self.Alpha * self.Outflow_0 ) + ( ( 1 - self.Alpha ) * self.InflowBase )
        self.Change = self.InflowBase - self.OutflowBase
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.28)


class Skin_Flow:
    def __init__(self):
        self.Conductance = None
        self.BasicConductance = 1.6
        self.A2Effect = None
        self.SympsEffect = None
        self.ADHEffect = None
        self.PO2Effect = None
        self.SympsDilateEffect = None
        self.LocalTempEffect = None
        self.AerobicFraction = None
        self.O2Use = None
        self.conc_O2 = None
        self.BloodFlow = None
        self.PlasmaFlow = None
        self.PO2 = 40.0
    def A2Effect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.3, 3.5], [1.05, 1.0, 0.5], [0.0, -0.08, 0.0])

    def SympsEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.0, 5.0], [0.3, 0.0, -0.9], [0.0, -0.3, 0.0])

    def PO2Effect_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 20.0], [2.0, 1.0], [0.0, 0.0])

    def ADHEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.8, 3.0], [1.0, 0.1], [0.0, 0.0])

    def SympsDilateEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.0, 4.0], [0.3, 1.0, 8.0], [0.0, 2.2, 0.0])

    def LocalTempEffect_curve(self, x):
        return cubic_hermite_spline(x, [10.8, 29.0, 45.0], [-0.8, 0.0, 4.0], [0.0, 0.1, 0.0])

    def LocalTempVsNA_curve(self, x):
        return cubic_hermite_spline(x, [1.2, 1.5], [1.0, 0.0], [0.0, 0.0])

    def PO2OnAerobicFraction_curve(self, x):
        return cubic_hermite_spline(x, [2.0, 20.0], [0.0, 1.0], [0.0, 0.0])

    def Calc_func(self):
        self.A2Effect = self.A2Effect_curve( A2Pool.Log10Conc )
        self.SympsEffect = 1.0 + ( self.SympsEffect_curve( OtherTissue_AlphaReceptors.Activity ) * self.LocalTempVsNA_curve( HypothalamusSkinFlow.NerveActivity ) )
        self.ADHEffect = self.ADHEffect_curve( ADHPool.Log10Conc )
        self.SympsDilateEffect = self.SympsDilateEffect_curve( HypothalamusSkinFlow.NerveActivity )
        self.LocalTempEffect = 1.0 + ( self.LocalTempEffect_curve( HeatSkin.Temp_C ) * self.LocalTempVsNA_curve( HypothalamusSkinFlow.NerveActivity ) )
        self.SearchMax = PO2Artys.Pressure

        def PO2implicitfunc(PO2):
            self.PO2Effect = self.PO2Effect_curve( PO2 )
            self.Conductance = self.BasicConductance * self.A2Effect * self.SympsEffect * self.PO2Effect * self.ADHEffect * Viscosity.ConductanceEffect * Anesthesia.VascularConductance * OtherTissue_Vasculature.Effect * self.SympsDilateEffect * self.LocalTempEffect
            self.BloodFlow = ( max( ( Skin_Pressure.PressureGradient * self.Conductance ), 0.0) )
            self.AerobicFraction = self.PO2OnAerobicFraction_curve( PO2 )
            self.O2Use = Skin_Metabolism.O2Need * self.AerobicFraction
            if self.BloodFlow > 0.0:
                self.conc_O2 = O2Artys.conc_O2 - ( self.O2Use / self.BloodFlow )
            else:
                self.conc_O2 = 0.0

            HgbTissue.conc_O2 = self.conc_O2
            HgbTissue.O2ToPO2_func()
            PO2End = HgbTissue.pO2

            return PO2End
        self.PO2 = impliciteq( PO2implicitfunc, self.PO2, 0.40)
        self.PlasmaFlow = self.BloodFlow * BloodVol.PVCrit

class Skin_Structure:
    def __init__(self):
        self.PhEffect = None
        self.FuelEffect = None
        self.TemperatureEffect = None
        self.Effect = 1.0

    def PhOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [6.5, 6.6], [0.1, 0.0], [0.0, 0.0])

    def FuelOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [0.5, 0.8], [0.05, 0.0], [0.0, 0.0])

    def TemperatureOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [44.0, 46.0], [0.0, 0.05], [0.0, 0.0])

    def Calc_func(self):
        self.PhEffect = self.PhOnStructure_curve( Skin_Ph.Ph )
        self.FuelEffect = self.FuelOnStructure_curve( Skin_Fuel.FractUseDelay )
        self.TemperatureEffect = self.TemperatureOnStructure_curve( HeatSkin.Temp_C )
        self.F1 = 0.0
        self.F2 = self.PhEffect + self.TemperatureEffect + self.FuelEffect
        self.Effect = backwardeuler( self.F1, self.F2, System.Dx, self.Effect, None)


class Skin_AlphaReceptors:
    def __init__(self):
        self.Activity = None
        self.TotalAgonism = None
        self.NeuralAgonism = None
        self.HumoralAgonism = None
        self.Switch = False
        self.Setting = 0.0
        self.NEURALK = 0.333
        self.HUMORALK = 0.5

    def Calc_func(self):
        self.NeuralAgonism = GangliaGeneral.NA_Hz
        self.HumoralAgonism = AlphaPool.Effect
        self.TotalAgonism = ( self.NEURALK * self.NeuralAgonism ) + ( self.HUMORALK * self.HumoralAgonism )
        if self.Switch:
            self.Activity = self.Setting
        else:
            self.Activity = self.TotalAgonism * AlphaBlockade.Effect


class Skin:
    def __init__(self):
        pass
    
class Skin_Ph:
    def __init__(self):
        self.Ph = None
        self.conc_SID = None
        self.conc_SID_mEqperL = None

    def CalcSID_func(self):
        self.conc_SID = KCell.conc_K_ + CellSID.OtherCations - CellSID.StrongAnions - Skin_Lactate.conc_Lac_
        self.conc_SID_mEqperL = 1000.0 * self.conc_SID

    def CalcPh_func(self):
        PhCells.pCO2 = Skin_CO2.PCO2
        PhCells.SID = self.conc_SID_mEqperL
        PhCells.Calc_func()
        self.Ph = PhCells.pH

class CellSID:
    def __init__(self):
        self.WeakAnions = 0.036
        self.StrongAnions = 0.117
        self.OtherCations = 0.012
        self.LessLac = None

    def Calc_func(self):
        self.LessLac = KCell.conc_K_ + self.OtherCations - self.StrongAnions

class Electrolytes:
    def __init__(self):
        pass
    
class PO4Pool:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.conc_PO4__ = None
        self.conc_PO4___mEqperL = None
        self.Osmoles = None
        self.Targetconc_PO4__ = 0.00017
        self.InitialMass = None

    def CalcOsmoles_func(self):
        self.Osmoles = self.Mass / 2.0

    def Init_func(self):
        self.InitialMass = self.Targetconc_PO4__ * ECFV.Vol
        self.Mass = self.InitialMass

    def CalcConc_func(self):
        self.conc_PO4__ = self.Mass / ECFV.Vol
        self.conc_PO4___mEqperL = 1000.0 * self.conc_PO4__

    def CalcDervs_func(self):
        self.Gain = DietIntakeElectrolytes.PO4__mEqperMin
        self.Loss = CD_PO4.Outflow
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.026)


class PO4:
    def __init__(self):
        pass
    
class Na:
    def __init__(self):
        pass
    
class NaPool:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.conc_Na_ = None
        self.conc_Na__mEqperL = None
        self.Targetconc_Na_ = 0.144
        self.InitialMass = None

    def Init_func(self):
        self.InitialMass = self.Targetconc_Na_ * ECFV.Vol
        self.Mass = self.InitialMass

    def CalcConc_func(self):
        self.conc_Na_ = self.Mass / ECFV.Vol
        self.conc_Na__mEqperL = 1000.0 * self.conc_Na_

    def CalcDervs_func(self):
        self.Gain = GILumenSodium.Absorption + IVDrip.NaRate + Transfusion.NaRate
        self.Loss = CD_Na.Outflow + SweatDuct.NaOutflow + Hemorrhage.NaRate + DialyzerActivity.Na_Flux
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 21.7)


class SO4:
    def __init__(self):
        pass
    
class SO4Pool:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.conc_SO4__ = None
        self.conc_SO4___mEqperL = None
        self.Osmoles = None
        self.Targetconc_SO4__ = 0.00028
        self.InitialMass = None

    def CalcOsmoles_func(self):
        self.Osmoles = self.Mass / 2.0

    def Init_func(self):
        self.InitialMass = self.Targetconc_SO4__ * ECFV.Vol
        self.Mass = self.InitialMass

    def CalcConc_func(self):
        self.conc_SO4__ = self.Mass / ECFV.Vol
        self.conc_SO4___mEqperL = 1000.0 * self.conc_SO4__

    def CalcDervs_func(self):
        self.Gain = DietIntakeElectrolytes.SO4__mEqperMin
        self.Loss = CD_SO4.Outflow
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.042)


class ClPool:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.conc_Cl_ = None
        self.conc_Cl__mEqperL = None
        self.Targetconc_Cl_ = 0.106
        self.InitialMass = None

    def Init_func(self):
        self.InitialMass = self.Targetconc_Cl_ * ECFV.Vol
        self.Mass = self.InitialMass

    def CalcConc_func(self):
        self.conc_Cl_ = self.Mass / ECFV.Vol
        self.conc_Cl__mEqperL = 1000.0 * self.conc_Cl_

    def CalcDervs_func(self):
        self.Gain = GILumenChloride.Absorption + IVDrip.ClRate + Transfusion.ClRate
        self.Loss = CD_Cl.Outflow + SweatDuct.ClOutflow + Hemorrhage.ClRate + DialyzerActivity.Cl_Flux
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 16.1)


class Cl:
    def __init__(self):
        pass
    
class KAldoEffect:
    def __init__(self):
        self.Tau = 120.0
        self.Delayed = 1.0

    def Effect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 300.0, 1500.0], [0.9, 1.0, 1.1], [0.0, 0.00025, 0.0])

    def Parms_func(self):
        self.RateConst = ( 1 / self.Tau )

    def Dervs_func(self):
        self.Immediate = self.Effect_curve( AldoPool.conc_Aldo_pMolperL )
        self.Delayed = delay( self.RateConst, self.Immediate, self.Delayed, System.Dx, 0.01)


class K:

    def Parms_func(self):
        KAldoEffect.Parms_func()

    def Conc_func(self):
        KPool.Conc_func()
        KCell.Conc_func()

    def Dervs_func(self):
        KAldoEffect.Dervs_func()
        KFluxToCell.Dervs_func()
        KFluxToPool.Dervs_func()
        KMembrane.Dervs_func()
        KPool.Dervs_func()
        KCell.Dervs_func()

class KFluxToPool:
    def __init__(self):
        self.Rate = None
        self.BasicK = 7.4e-5
        self.K = None

    def Dervs_func(self):
        self.K = self.BasicK
        self.Rate = self.K * ( KCell.Mass - KCell.CaptiveMass )

class KCell:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.conc_K_ = None
        self.conc_K__mEqperL = None
        self.CaptiveMass = 2180.0
        self.Targetconc_K_ = 0.142
        self.InitialMass = None

    def Init_func(self):
        self.InitialMass = self.Targetconc_K_ * ICFV.Vol
        self.Mass = self.InitialMass

    def Conc_func(self):
        self.conc_K_ = self.Mass / CellH2O.Vol
        self.conc_K__mEqperL = 1000.0 * self.conc_K_

    def Dervs_func(self):
        self.Gain = KFluxToCell.Rate
        self.Loss = KFluxToPool.Rate
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 39.8)


class KFluxToCell:
    def __init__(self):
        self.Rate = None
        self.BasicK = 0.002
        self.K = None

    def Dervs_func(self):
        self.K = self.BasicK * KAldoEffect.Delayed
        self.Rate = self.K * KPool.Mass

class KPool:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.conc_K_ = None
        self.conc_K__mEqperL = None
        self.Targetconc_K_ = 0.0044
        self.InitialMass = None

    def Init_func(self):
        self.InitialMass = self.Targetconc_K_ * ECFV.Vol
        self.Mass = self.InitialMass

    def Conc_func(self):
        self.conc_K_ = self.Mass / ECFV.InitialVol
        self.conc_K__mEqperL = 1000.0 * self.conc_K_

    def Dervs_func(self):
        self.Gain = GILumenPotassium.Absorption + KFluxToPool.Rate + IVDrip.KRate + Transfusion.KRate
        self.Loss = CD_K.Outflow + KFluxToCell.Rate + SweatDuct.KOutflow + Hemorrhage.KRate + DialyzerActivity.K_Flux
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.66)


class KMembrane:
    def __init__(self):
        self.MembranePotential = None

    def Dervs_func(self):
        self.MembranePotential = -61.0 * ( math.log10( ( KCell.conc_K_ / KPool.conc_K_ ) ) )

class HeatStorage:
    def __init__(self):
        self.Mass = None
        self.Gain = None
        self.Loss = None
        self.Change = None

    def Calc_func(self):
        self.Mass = HeatCore.Mass + HeatSkeletalMuscle.Mass + HeatSkin.Mass + GILumenTemperature.Mass
        self.Gain = GILumenTemperature.Intake + Metabolism_CaloriesUsed.TotalHeat_kCalperMin + HeatIVDrip.Flux + HeatTransfusion.Flux + HeatShivering.Cals
        self.Loss = HeatUrine.Flux + HeatSweating.Flux + HeatHemorrhage.Flux + HeatDialyzer.Flux + HeatRadiation.Flux + HeatConduction.Flux + HeatInsensibleSkin.Flux + HeatInsensibleLung.Flux + GILumenTemperature.Vomitus + GILumenTemperature.Diarrhea
        self.Change = self.Gain - self.Loss

class HeatMetabolism:
    def __init__(self):
        self.Core = None
        self.Skin = None
        self.SkeletalMuscle = None

    def Core_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 37.0, 40.0, 46.0], [0.0, 1.0, 1.5, 0.0], [0.0, 0.12, 0.0, 0.0])

    def Skin_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 29.5, 40.0, 46.0], [0.0, 1.0, 1.5, 0.0], [0.0, 0.12, 0.0, 0.0])

    def SkeletalMuscle_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 37.1, 40.0, 46.0], [0.0, 1.0, 1.5, 0.0], [0.0, 0.12, 0.0, 0.0])

    def Calc_func(self):
        self.Core = self.Core_curve( HeatCore.Temp_C )
        self.Skin = self.Skin_curve( HeatSkin.Temp_C )
        self.SkeletalMuscle = self.SkeletalMuscle_curve( HeatSkeletalMuscle.Temp_C )

class HeatSweating:
    def __init__(self):
        self.Flux = None

    def Flux_func(self):
        self.Flux = HeatSweatEvaporation.Flux + HeatSweatConvection.Flux

class HeatSkeletalMuscle:
    def __init__(self):
        self.Temp_F = None
        self.Temp_C = None
        self.Temp_K = None
        self.Flux = None
        self.Gain = None
        self.Loss = None
        self.InitialTemp_F = 98.7
        self.InitialTemp_K = None
        self.InitialMass = None

    def Initialize_func(self):
        self.InitialTemp_K = ( 5 / 9 ) * ( self.InitialTemp_F - 32.0 ) + 273.15
        self.InitialMass = SkeletalMuscle_Size.InitialMass * SpecificHeat.Tissue_kCalperG * self.InitialTemp_K
        self.Mass = self.InitialMass

    def CalcTemp_func(self):
        self.Temp_K = self.Mass / ( SkeletalMuscle_Size.Mass_kG * SpecificHeat.Tissue )
        self.Temp_C = self.Temp_K - 273.15
        self.Temp_F = ( 9 / 5 ) * self.Temp_C + 32.0

    def Flux_func(self):
        self.Flux = ( SkeletalMuscle_Flow.BloodFlow / 1000.0 ) * ( HeatSkeletalMuscle.Temp_K - HeatCore.Temp_K ) * SpecificHeat.Blood

    def Dervs_func(self):
        self.Gain = Metabolism_CaloriesUsed.SkeletalMuscleHeat_kCalperMin
        self.Loss = self.Flux
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 70.0)


class HeatIVDrip:
    def __init__(self):
        self.Flux = None

    def Flux_func(self):
        self.Flux = IVDrip.H2ORate * AmbientTemperature.Temp_K * SpecificHeat.Water_kCalperG

class TempTools:
    def __init__(self):
        self.DegF = None
        self.DegC = None
        self.DegK = None
        self.Pres = None
        self.Temp = None
        self.Vapor_CalperG = 580.0
        self.Vapor_kCalperG = 0.580
        self.A = 18.6686
        self.B = 4030.183
        self.C = 235.0

    def FromF_func(self):
        self.DegC = ( 5 / 9 ) * ( self.DegF - 32 )
        self.DegK = self.DegC + 273.15

    def FromC_func(self):
        self.DegF = ( 9 / 5 ) * ( self.DegC + 32 )
        self.DegK = self.DegC + 273.15

    def FromK_func(self):
        self.DegC = self.DegK - 273.15
        self.DegF = ( 9 / 5 ) * ( self.DegC + 32 )

    def TempToSatPres_func(self):
        if self.Temp > 100.0:
            self.Pres = 760.0
        elif self.Temp < -273.15:
            self.Pres = 0.0
        elif True:
            self.Pres = ( math.e ** ( self.A - ( self.B / ( self.Temp + self.C ) ) ) )

    def SatPresToTemp_func(self):
        if self.Pres > 760.0:
            self.Temp = 100.0
        elif self.Pres < 0:
            self.Temp = -273.15
        elif True:
            self.Temp = self.B / ( self.A - ( math.log( ( self.Pres ) ) ) ) - self.C

class HeatRadiation:
    def __init__(self):
        self.Flux = None
        self.ClothesEffect = None
        self.TemperatureDifference = None
        self.K = 0.068

    def ClothesEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 2.0, 4.0], [4.0, 1.0, 0.2], [0.0, -1.2, 0.0])

    def Flux_func(self):
        self.ClothesEffect = self.ClothesEffect_curve( Clothes.Weight )
        self.TemperatureDifference = HeatSkin.Temp_K - AmbientTemperature.Temp_K
        self.Flux = self.K * self.ClothesEffect * self.TemperatureDifference

class Convulsing:
    def __init__(self):
        self.Temp = None
        self.NowConvulsing = None
        self.StoppedConvulsing = None
        self.PastConvulsing = None

    def NowConvulsing_func(self):
        if ( self.Temp > 42.0 ) and ( self.Temp < 44.0 ):
            self.NowConvulsing = True
        else:
            self.NowConvulsing = False


    def StoppedConvulsing_func(self):
        if self.Temp < 41.5:
            self.StoppedConvulsing = True
        else:
            self.StoppedConvulsing = False


    def PastConvulsing_func(self):
        if self.Temp > 44.5:
            self.PastConvulsing = True
        else:
            self.PastConvulsing = False


class HeatSkin:
    def __init__(self):
        self.Temp_F = None
        self.Temp_C = None
        self.Temp_K = None
        self.Flux = None
        self.Gain = None
        self.Loss = None
        self.InitialTemp_F = 84.0
        self.InitialTemp_K = None
        self.InitialMass = None

    def Initialize_func(self):
        self.InitialTemp_K = ( 5 / 9 ) * ( self.InitialTemp_F - 32.0 ) + 273.15
        self.InitialMass = Skin_Size.InitialMass * SpecificHeat.Tissue_kCalperG * self.InitialTemp_K
        self.Mass = self.InitialMass

    def CalcTemp_func(self):
        self.Temp_K = self.Mass / ( Skin_Size.Mass_kG * SpecificHeat.Tissue )
        self.Temp_C = self.Temp_K - 273.15
        self.Temp_F = ( 9 / 5 ) * self.Temp_C + 32.0

    def Flux_func(self):
        self.Flux = HeatRadiation.Flux + HeatConduction.Flux + HeatInsensibleSkin.Flux + HeatSweating.Flux

    def Dervs_func(self):
        self.Gain = Metabolism_CaloriesUsed.SkinHeat_kCalperMin + HeatCore.Flux
        self.Loss = self.Flux
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 7.0)


class HeatShivering:
    def __init__(self):
        self.Cals = None
        self.NerveEffect = None

    def NerveEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 4.0], [0.0, 70.0], [0.0, 0.0])

    def Cals_func(self):
        self.NerveEffect = self.NerveEffect_curve( HypothalamusShivering.NerveActivity )
        self.Cals = self.NerveEffect * SkeletalMuscle_Structure.Effect

class HeatInsensibleLung:
    def __init__(self):
        self.Flux = None
        self.Liquid = None
        self.Vapor = None
        self.Air = None
        self.H2O = None
        self.K = 0.80E-3

    def Flux_func(self):
        self.H2O = self.K * Breathing.TotalVentilation * ( ( 47.0 - RelativeHumidity.VaporPressure ) / Barometer.Pressure )
        self.Liquid = self.H2O * HeatCore.Temp_K * SpecificHeat.Water_kCalperG
        self.Vapor = self.H2O * TempTools.Vapor_kCalperG
        self.Air = Breathing.TotalVentilation * ( HeatCore.Temp_K - AmbientTemperature.Temp_K ) * SpecificHeat.Air_kCalpermL
        self.Flux = self.Liquid + self.Vapor + self.Air

class HeatCore:
    def __init__(self):
        self.Temp_F = None
        self.Temp_C = None
        self.Temp_K = None
        self.Flux = None
        self.Gain = None
        self.Loss = None
        self.InitialTemp_F = 98.6
        self.InitialTemp_K = None
        self.InitialMass = None

    def Initialize_func(self):
        self.InitialTemp_K = ( 5 / 9 ) * ( self.InitialTemp_F - 32.0 ) + 273.15
        self.InitialMass = Weight.InitialCore * SpecificHeat.Tissue_kCalperG * self.InitialTemp_K
        self.Mass = self.InitialMass

    def CalcTemp_func(self):
        self.Temp_K = self.Mass / ( Weight.Core_kG * SpecificHeat.Tissue )
        self.Temp_C = self.Temp_K - 273.15
        self.Temp_F = ( 9 / 5 ) * self.Temp_C + 32.0

    def Flux_func(self):
        self.Flux = ( Skin_Flow.BloodFlow / 1000.0 ) * ( HeatCore.Temp_K - HeatSkin.Temp_K ) * SpecificHeat.Blood

    def Dervs_func(self):
        self.Gain = Metabolism_CaloriesUsed.CoreHeat_kCalperMin + HeatSkeletalMuscle.Flux + GILumenTemperature.Absorption + HeatIVDrip.Flux + HeatTransfusion.Flux
        self.Loss = self.Flux + HeatInsensibleLung.Flux + HeatUrine.Flux + HeatDialyzer.Flux + HeatHemorrhage.Flux
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 123.0)


class HeatInsensibleSkin:
    def __init__(self):
        self.Flux = None
        self.Liquid = None
        self.Vapor = None
        self.H2O = None
        self.Base = 0.37

    def Flux_func(self):
        if Skin_Flow.BloodFlow > 0.0:
            self.H2O = self.Base
        else:
            self.H2O = 0.0

        self.Liquid = self.H2O * HeatSkin.Temp_K * SpecificHeat.Water_kCalperG
        self.Vapor = self.H2O * TempTools.Vapor_kCalperG
        self.Flux = self.Liquid + self.Vapor

class HeatConduction:
    def __init__(self):
        self.Flux = None
        self.ClothesEffect = None
        self.BloodFlowEffect = None
        self.WindEffect = None
        self.TemperatureDifference = None
        self.K = 0.034

    def ClothesEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 2.0, 4.0], [4.0, 1.0, 0.2], [0.0, -1.2, 0.0])

    def BloodFlowEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 250.0, 8000.0], [0.8, 1.0, 8.0], [0.0, 0.001, 0.0])

    def WindEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 20.0], [1.0, 4.0], [0.0, 0.0])

    def Flux_func(self):
        self.ClothesEffect = self.ClothesEffect_curve( Clothes.Weight )
        self.BloodFlowEffect = self.BloodFlowEffect_curve( Skin_Flow.BloodFlow )
        self.WindEffect = self.WindEffect_curve( Wind.MPH )
        self.TemperatureDifference = HeatSkin.Temp_K - AmbientTemperature.Temp_K
        self.Flux = self.K * self.ClothesEffect * self.BloodFlowEffect * self.WindEffect * self.TemperatureDifference

class HeatSweatEvaporation:
    def __init__(self):
        self.Flux = None
        self.VaporPressureSkin = None
        self.VaporPressureGradient = None
        self.WindEffect = None
        self.BasicEvaporation = None
        self.MaximumEvaporation = None
        self.H2OEvaporation = None
        self.H2ODrip = None

    def WindEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 20.0], [1.0, 1.5], [0.0, 0.0])

    def BasicEvaporation_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 40.0], [0.0, 20.0], [0.0, 0.0])

    def Flux_func(self):
        TempTools.Temp = HeatSkin.Temp_C
        TempTools.TempToSatPres_func()
        self.VaporPressureSkin = TempTools.Pres
        self.VaporPressureGradient = ( max( ( self.VaporPressureSkin - RelativeHumidity.VaporPressure ), 0.0) )
        self.WindEffect = self.WindEffect_curve( Wind.MPH )
        self.BasicEvaporation = self.BasicEvaporation_curve( self.VaporPressureGradient )
        self.MaximumEvaporation = self.WindEffect * self.BasicEvaporation
        self.H2OEvaporation = ( min( SweatDuct.H2OOutflow, self.MaximumEvaporation) )
        self.Flux = self.H2OEvaporation * TempTools.Vapor_kCalperG
        self.H2ODrip = SweatDuct.H2OOutflow - self.H2OEvaporation

class HeatTransfusion:
    def __init__(self):
        self.Flux = None

    def Flux_func(self):
        self.Flux = Transfusion.Rate * AmbientTemperature.Temp_K * SpecificHeat.Blood_kCalperG

class HeatSweatConvection:
    def __init__(self):
        self.Flux = None

    def Flux_func(self):
        self.Flux = SweatDuct.H2OOutflow * HeatSkin.Temp_K * SpecificHeat.Water_kCalperG

class HeatDialyzer:
    def __init__(self):
        self.Flux = None

    def Flux_func(self):
        self.Flux = DialyzerActivity.UltrafiltrationRate * HeatCore.Temp_K * SpecificHeat.Water_kCalperG

class HeatHemorrhage:
    def __init__(self):
        self.Flux = None

    def Flux_func(self):
        self.Flux = Hemorrhage.Rate * HeatCore.Temp_K * SpecificHeat.Blood_kCalperG

class Heat:

    def Parms_func(self):
        pass

    def CalcTemp_func(self):
        HeatCore.CalcTemp_func()
        HeatSkin.CalcTemp_func()
        HeatSkeletalMuscle.CalcTemp_func()
        HeatMetabolism.Calc_func()

    def Cals_func(self):
        HeatShivering.Cals_func()

    def Dervs_func(self):
        HeatRadiation.Flux_func()
        HeatConduction.Flux_func()
        HeatInsensibleSkin.Flux_func()
        HeatInsensibleLung.Flux_func()
        HeatSweatEvaporation.Flux_func()
        HeatSweatConvection.Flux_func()
        HeatSweating.Flux_func()
        HeatIVDrip.Flux_func()
        HeatTransfusion.Flux_func()
        HeatHemorrhage.Flux_func()
        HeatDialyzer.Flux_func()
        HeatUrine.Flux_func()
        HeatCore.Flux_func()
        HeatSkin.Flux_func()
        HeatSkeletalMuscle.Flux_func()
        HeatCore.Dervs_func()
        HeatSkin.Dervs_func()
        HeatSkeletalMuscle.Dervs_func()
        HeatStorage.Calc_func()

class SpecificHeat:
    def __init__(self):
        self.Water = 1.00
        self.Water_kCalperG = 0.001
        self.Tissue = 0.83
        self.Tissue_kCalperG = 0.00083
        self.Blood = 0.92
        self.Blood_kCalperG = 0.00092
        self.Air_kCalpermL = 3.1E-7
    
class HeatUrine:
    def __init__(self):
        self.Flux = None

    def Flux_func(self):
        self.Flux = CD_H2O.Outflow * HeatCore.Temp_K * SpecificHeat.Water_kCalperG

class IVEpinephrineInjection:
    def __init__(self):
        self.Dose = 1.0
        self.Timespan = 15.0
        self.TotalInjections = 0
        self.TotalDose = 0.0

    def InjectEpinephrineNow_func(self):
        self.TotalInjections = self.TotalInjections + 1
        self.TotalDose = self.TotalDose + self.Dose

class CellProtein:
    def __init__(self):
        self.conc_Protein = None
        self.Gain = None
        self.Loss = None
        self.Inflow = None
        self.Outflow = None
        self.Degradation = None
        self.InflowK = 464.0
        self.OutflowK = 0.880
        self.DegradationK = 0.0000053
        self.Mass_G = None
        self.Mass = 6000000.0

    def CalcConc_func(self):
        self.conc_Protein = self.Mass / ICFV.Vol
        self.Mass_G = 0.001 * self.Mass

    def Dervs_func(self):
        self.Inflow = self.InflowK * AAPool.conc_AA
        self.Outflow = self.OutflowK * self.conc_Protein
        self.Degradation = self.DegradationK * self.Mass
        self.Gain = self.Inflow
        self.Loss = self.Outflow + self.Degradation
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 60000.0)


class LungArtyO2:
    def __init__(self):
        self.conc_O2 = None
        self.PO2 = None
        self.Saturation = None

    def Calc_func(self):
        self.conc_O2 = O2Veins.conc_O2
        HgbTissue.conc_O2 = self.conc_O2
        HgbTissue.O2ToPO2_func()
        self.PO2 = HgbTissue.pO2
        HgbConc.conc_O2 = self.conc_O2
        HgbConc.Sat_percent_func()
        self.Saturation = HgbConc.Sat_percent

class LungArtyCO2:
    def __init__(self):
        self.conc_CO2 = None
        self.conc_CO2_mEqperL = None
        self.PCO2 = None

    def Calc_func(self):
        self.conc_CO2 = CO2Veins.conc_HCO3
        self.conc_CO2_mEqperL = CO2Veins.conc_HCO3_mEqperL
        self.PCO2 = CO2Veins.Pressure

class RightHemithorax:
    def __init__(self):
        self.Pressure = None
        self.ChestOpen = False
        self.NormalPressure = -4.0
        self.LungInflation = None

    def Calc_func(self):
        if self.ChestOpen:
            self.Pressure = 0.0
            self.LungInflation = 0.0
        else:
            self.Pressure = self.NormalPressure
            self.LungInflation = Thorax.PressureOnInflation_curve( self.Pressure )

class ExcessLungWater:
    def __init__(self):
        self.InitialVolume = None
        self.Perm = 3.0
        self.Grad = None
        self.Flux = None
        self.Lymph = None
        self.Volume_L = None

    def Lymph_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 1000.0], [0.0, 1.0], [0.0, 0.0])

    def Initialize_func(self):
        self.InitialVolume = 0.0
        self.Volume = self.InitialVolume

    def Dervs_func(self):
        self.Volume_L = self.Volume / 1000.0
        if OtherTissue_Function.Failed:
            self.Failed_func()
        else:
            self.NotFailed_func()
        self.Change = self.Flux - self.Lymph
        self.Volume = diffeq( self.Change, System.Dx, self.Volume, 10.0)


    def NotFailed_func(self):
        self.Grad = PulmCapys.Pressure - PlasmaProtein.COP
        self.Flux = ( max( ( self.Perm * self.Grad ), 0.0) )
        self.Lymph = self.Lymph_curve( self.Volume )

    def Failed_func(self):
        self.Grad = 0.0
        self.Flux = 0.0
        self.Lymph = 0.0

class Thorax:
    def __init__(self):
        self.AvePressure = None
        self.LungInflation = None
        self.PressureGradientRightLeft = None
        self.LeftLungFlowFract = None
        self.RightLungFlowFract = None

    def PressureOnInflation_curve(self, x):
        return cubic_hermite_spline(x, [-4.0, 4.0], [1.0, 0.0], [0.0, 0.0])

    def PressureGradientOnFlowDist_curve(self, x):
        return cubic_hermite_spline(x, [-25.0, 0.0, 25.0], [0.0, 0.5, 1.0], [0.0, 0.03, 0.0])

    def Calc_func(self):
        self.AvePressure = 0.5 * ( RightHemithorax.Pressure + LeftHemithorax.Pressure )
        self.LungInflation = 0.5 * ( RightHemithorax.LungInflation + LeftHemithorax.LungInflation )
        self.PressureGradientRightLeft = RightHemithorax.Pressure - LeftHemithorax.Pressure
        self.LeftLungFlowFract = self.PressureGradientOnFlowDist_curve( self.PressureGradientRightLeft )
        self.RightLungFlowFract = 1.0 - self.LeftLungFlowFract

class LungO2:
    def __init__(self):
        self.conc_Alveolar = None
        self.PAlveolar = None
        self.MembraneGradient = None
        self.conc_Capy = None
        self.PCapy = None
        self.CapySat = None
        self.Uptake = 250.0
    def Calc_func(self):
        if Breathing.AlveolarVentilation_STPD > 0.0:
            self.CalcUptake_func()
        else:
            self.Uptake = 0.0
            self.conc_Capy = LungArtyO2.conc_O2
            HgbLung.conc_O2 = self.conc_Capy
            HgbLung.O2ToPO2_func()
            self.PCapy = HgbLung.pO2
            self.PAlveolar = self.PCapy
            self.conc_Alveolar = self.PAlveolar / 760.0
        HgbConc.conc_O2 = self.conc_Capy
        HgbConc.Sat_percent_func()
        self.CapySat = HgbConc.Sat_percent

    def CalcUptake_func(self):

        def Uptakeimplicitfunc(Uptake):
            self.conc_Alveolar = Bronchi.conc_O2 - ( Uptake / Breathing.AlveolarVentilation_STPD )
            self.PAlveolar = self.conc_Alveolar * Barometer.Pressure
            self.MembraneGradient = Uptake / PulmonaryMembrane.Permeability
            self.PCapy = self.PAlveolar - self.MembraneGradient
            HgbLung.pO2 = self.PCapy
            HgbLung.PO2ToO2_func()
            self.conc_Capy = HgbLung.conc_O2
            EndUptake = LungBloodFlow.AlveolarVentilated * ( self.conc_Capy - LungArtyO2.conc_O2 )

            return EndUptake
        self.Uptake = impliciteq( Uptakeimplicitfunc, self.Uptake, 2.5)

class Bronchi:
    def __init__(self):
        self.VaporPressure = 47.0
        self.H2O_percent = None
        self.Dilution = None
        self.Pressure = None
        self.O2_percent = None
        self.conc_O2 = None
        self.PO2 = None
        self.N2_percent = None
        self.conc_N2 = None
        self.PN2 = None
        self.CO2_percent = None
        self.conc_CO2 = None
        self.PCO2 = None
        self.CO_percent = None
        self.conc_CO = None
        self.PCO = None
        self.Anesthetic_percent = None
        self.conc_Anesthetic = None
        self.PAnesthetic = None

    def Calc_func(self):
        self.H2O_percent = 100.0 * ( self.VaporPressure / AirSupply_InspiredAir.Pressure )
        self.Dilution = 1.0 - ( self.VaporPressure / AirSupply_InspiredAir.Pressure )
        self.O2_percent = self.Dilution * AirSupply_InspiredAir.O2_percent
        self.conc_O2 = 0.01 * self.O2_percent
        self.PO2 = self.conc_O2 * AirSupply_InspiredAir.Pressure
        self.N2_percent = self.Dilution * AirSupply_InspiredAir.N2_percent
        self.conc_N2 = 0.01 * self.N2_percent
        self.PN2 = self.conc_N2 * AirSupply_InspiredAir.Pressure
        self.CO2_percent = self.Dilution * AirSupply_InspiredAir.CO2_percent
        self.conc_CO2 = 0.01 * self.CO2_percent
        self.PCO2 = self.conc_CO2 * AirSupply_InspiredAir.Pressure
        self.CO_percent = self.Dilution * AirSupply_InspiredAir.CO_percent
        self.conc_CO = 0.01 * self.CO_percent
        self.PCO = self.conc_CO * AirSupply_InspiredAir.Pressure
        self.Anesthetic_percent = self.Dilution * AirSupply_InspiredAir.Anesthetic_percent
        self.conc_Anesthetic = 0.01 * self.Anesthetic_percent
        self.PAnesthetic = self.conc_Anesthetic * AirSupply_InspiredAir.Pressure

class GasExchangeRatio:
    def __init__(self):
        self.Ratio = None

    def Calc_func(self):
        if LungO2.Uptake > 0.0:
            self.Ratio = LungCO2.Expired / LungO2.Uptake
        else:
            self.Ratio = 0.0


class PulmonaryMembrane:
    def __init__(self):
        self.Permeability = None
        self.DiffusingCapacity = None
        self.DC_TO_PERM = 5.0
        self.ActiveArea = None
        self.TotalArea = 80.0
        self.Recruitment = None
        self.Thickness = None
        self.Thickness_Structure = 0.6
        self.Thickness_H2O = None
        self.DC_SCALER = 0.55

    def Recruitment_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 5500.0, 15000.0], [0.01, 0.3, 1.0], [0.0, 0.0001, 0.0])

    def Calc_func(self):
        self.Thickness_H2O = ExcessLungWater.Volume / self.TotalArea
        self.Recruitment = self.Recruitment_curve( LungBloodFlow.Alveolar )
        self.Thickness = self.Thickness_Structure + self.Thickness_H2O
        self.ActiveArea = self.TotalArea * self.Recruitment
        self.DiffusingCapacity = self.DC_SCALER * self.ActiveArea / self.Thickness
        self.Permeability = self.DC_TO_PERM * self.DiffusingCapacity

class Ventilator:
    def __init__(self):
        self.Switch = False
        self.Rate = 0.0
        self.TidalVolume = 0.0
        self.MinuteVolume = None
        self.MinuteVolume_L = None

    def Calc_func(self):
        if self.Switch:
            self.MinuteVolume = self.TidalVolume * self.Rate
        else:
            self.MinuteVolume = 0.0

        self.MinuteVolume_L = self.MinuteVolume / 1000.0

class LungVeinCO2:
    def __init__(self):
        self.conc_CO2 = None
        self.conc_CO2_mEqperL = None
        self.PCO2 = None

    def Calc_func(self):
        if LungBloodFlow.Total > 0.0:
            self.conc_CO2 = ( ( LungBloodFlow.AlveolarVentilated * LungCO2.conc_Capy ) + ( LungBloodFlow.TotalShunt * LungArtyCO2.conc_CO2 ) ) / LungBloodFlow.Total
        else:
            self.conc_CO2 = 0.0

        self.conc_CO2_mEqperL = 1000.0 * self.conc_CO2
        Blood_BaseToGas.conc_HCO3 = self.conc_CO2
        Blood_BaseToGas.conc_SID = BloodIons.conc_SID
        Blood_BaseToGas.Calc_func()
        self.PCO2 = Blood_BaseToGas.pCO2

class Breathing:
    def __init__(self):
        self.NATURAL = 0
        self.CPR = 1
        self.VENTILATOR = 2
        self.Type = None
        self.TotalVentilation = None
        self.TotalVentilation_L = None
        self.AlveolarVentilation = None
        self.AlveolarVentilation_L = None
        self.RespRate = None
        self.TidalVolume = None
        self.TidalVolumeBasic = None
        self.DeadSpace = None
        self.DeadSpaceFract = None
        self.DeadSpaceSlope = 0.20
        self.DeadSpaceMin = 60.0
        self.AlveolarVolume = None
        self.TotalVentilation_L_STPD = None
        self.AlveolarVentilation_L_STPD = None
        self.TotalVentilation_STPD = None
        self.AlveolarVentilation_STPD = None
        self.TidalVolume_STPD = None
        self.DeadSpace_STPD = None
        self.AlveolarVolume_STPD = None

    def DriveOnTidalVolume_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.0, 10.0], [0.0, 550.0, 2630.0], [0.0, 400.0, 0.0])

    def Calc_func(self):
        if Ventilator.Switch:
            self.Type = self.VENTILATOR
            self.RespRate = Ventilator.Rate
            self.TidalVolumeBasic = Ventilator.TidalVolume
            self.TidalVolume = self.TidalVolumeBasic
        elif CPR_Lungs.Status == CPR_Lungs.ACTIVE:
            self.Type = self.CPR
            self.RespRate = CPR_Lungs.Rate
            self.TidalVolumeBasic = CPR_Lungs.Volume
            self.TidalVolume = self.TidalVolumeBasic
        elif True:
            self.Type = self.NATURAL
            self.RespRate = RespiratoryCenter_Output.Rate
            self.TidalVolumeBasic = self.DriveOnTidalVolume_curve( RespiratoryCenter_Output.MotorNerveActivity ) * Thorax.LungInflation * RespiratoryMuscle_Function.Effect
            self.TidalVolume = ( max( ( self.TidalVolumeBasic - ExcessLungWater.Volume ), 0.0) )
        self.DeadSpace = self.DeadSpaceSlope * self.TidalVolume + self.DeadSpaceMin
        if self.TidalVolume > 0.0:
            self.DeadSpaceFract = self.DeadSpace / self.TidalVolume
        else:
            self.DeadSpaceFract = 0

        self.AlveolarVolume = self.TidalVolume - self.DeadSpace
        self.TotalVentilation = self.RespRate * self.TidalVolume
        self.TotalVentilation_L = self.TotalVentilation / 1000.0
        self.AlveolarVentilation = self.RespRate * self.AlveolarVolume
        self.AlveolarVentilation_L = self.AlveolarVentilation / 1000.0
        BTPS_To_STPD.V1 = self.TidalVolume
        BTPS_To_STPD.Calc_func()
        self.TidalVolume_STPD = BTPS_To_STPD.V2
        BTPS_To_STPD.V1 = self.DeadSpace
        BTPS_To_STPD.Calc_func()
        self.DeadSpace_STPD = BTPS_To_STPD.V2
        self.AlveolarVolume_STPD = self.TidalVolume_STPD - self.DeadSpace_STPD
        self.TotalVentilation_STPD = self.RespRate * self.TidalVolume_STPD
        self.TotalVentilation_L_STPD = self.TotalVentilation_STPD / 1000.0
        self.AlveolarVentilation_STPD = self.RespRate * self.AlveolarVolume_STPD
        self.AlveolarVentilation_L_STPD = self.AlveolarVentilation_STPD / 1000.0

class LeftHemithorax:
    def __init__(self):
        self.Pressure = None
        self.ChestOpen = False
        self.NormalPressure = -4.0
        self.LungInflation = None

    def Calc_func(self):
        if self.ChestOpen:
            self.Pressure = 0.0
            self.LungInflation = 0.0
        else:
            self.Pressure = self.NormalPressure
            self.LungInflation = Thorax.PressureOnInflation_curve( self.Pressure )

class LungCO2:
    def __init__(self):
        self.conc_Alveolar = None
        self.PAlveolar = None
        self.conc_Capy = None
        self.PCapy = None
        self.Expired = 200.0
    def Calc_func(self):
        if Breathing.AlveolarVentilation_STPD > 0.0:
            self.CalcExpired_func()
        else:
            self.CalcNoneExpired_func()

    def CalcExpired_func(self):

        def Expiredimplicitfunc(Expired):
            self.conc_Alveolar = Bronchi.conc_CO2 + ( Expired / Breathing.AlveolarVentilation_STPD )
            self.PAlveolar = self.conc_Alveolar * Barometer.Pressure
            self.PCapy = self.PAlveolar
            Blood_GasToBase.pCO2 = self.PCapy
            Blood_GasToBase.conc_SID = BloodIons.conc_SID
            Blood_GasToBase.Calc_func()
            self.conc_Capy = Blood_GasToBase.conc_HCO3
            EndExpired = LungBloodFlow.AlveolarVentilated * ( LungArtyCO2.conc_CO2 - self.conc_Capy ) * CO2Tools.MolsToLiters

            return EndExpired
        self.Expired = impliciteq( Expiredimplicitfunc, self.Expired, 2.0)

    def CalcNoneExpired_func(self):
        self.Expired = 0.0
        self.conc_Capy = LungArtyCO2.conc_CO2
        self.PCapy = LungArtyCO2.PCO2
        self.PAlveolar = self.PCapy
        self.conc_Alveolar = self.PAlveolar / 760.0

class Lungs:
    def __init__(self):
        pass
    
class LungBloodFlow:
    def __init__(self):
        self.Total = None
        self.Alveolar = None
        self.AlveolarVentilated = None
        self.AlveolarShunt = None
        self.BasicR_LShunt = 220.0
        self.Right_LeftShunt = None
        self.TotalShunt = None
        self.RightLungTotal = None
        self.RightLungVentilated = None
        self.RightLungShunt = None
        self.LeftLungTotal = None
        self.LeftLungVentilated = None
        self.LeftLungShunt = None

    def Calc_func(self):
        self.Total = ( PulmArty.Outflow + PulmCapys.Outflow ) / 2.0
        self.Right_LeftShunt = ( min( self.BasicR_LShunt, self.Total) )
        self.Alveolar = self.Total - self.Right_LeftShunt
        self.RightLungTotal = self.Alveolar * Thorax.RightLungFlowFract
        self.RightLungVentilated = self.RightLungTotal * RightHemithorax.LungInflation
        self.RightLungShunt = self.RightLungTotal - self.RightLungVentilated
        self.LeftLungTotal = self.Alveolar * Thorax.LeftLungFlowFract
        self.LeftLungVentilated = self.LeftLungTotal * LeftHemithorax.LungInflation
        self.LeftLungShunt = self.LeftLungTotal - self.LeftLungVentilated
        self.AlveolarVentilated = self.RightLungVentilated + self.LeftLungVentilated
        self.AlveolarShunt = self.RightLungShunt + self.LeftLungShunt
        self.TotalShunt = self.Right_LeftShunt + self.AlveolarShunt

class LungVeinO2:
    def __init__(self):
        self.conc_O2 = None
        self.PO2 = None
        self.Saturation = None

    def Calc_func(self):
        if LungBloodFlow.Total > 0.0:
            self.conc_O2 = ( ( LungBloodFlow.AlveolarVentilated * LungO2.conc_Capy ) + ( LungBloodFlow.TotalShunt * LungArtyO2.conc_O2 ) ) / LungBloodFlow.Total
        else:
            self.conc_O2 = 0.0

        HgbLung.conc_O2 = self.conc_O2
        HgbLung.O2ToPO2_func()
        self.PO2 = HgbLung.pO2
        HgbConc.conc_O2 = self.conc_O2
        HgbConc.Sat_percent_func()
        self.Saturation = HgbConc.Sat_percent

class BTPS_To_STPD:
    def __init__(self):
        self.V1 = None
        self.V2 = None
        self.P1 = 760.0
        self.P2 = None
        self.T1 = 273.2
        self.T2 = None
        self.VaporPres = None

    def Calc_func(self):
        TempTools.Temp = HeatCore.Temp_C
        TempTools.TempToSatPres_func()
        self.VaporPres = TempTools.Pres
        self.P2 = AirSupply_InspiredAir.Pressure - self.VaporPres
        self.T2 = HeatCore.Temp_K
        self.V2 = self.V1 * ( self.P2 / self.P1 ) * ( self.T1 / self.T2 )

class GasTools:
    def __init__(self):
        pass
    
class STPD_To_BTPS:
    def __init__(self):
        self.V1 = None
        self.V2 = None
        self.P1 = None
        self.P2 = 760.0
        self.T1 = None
        self.T2 = 273.2
        self.VaporPres = None

    def Calc_func(self):
        TempTools.Temp = HeatCore.Temp_C
        TempTools.TempToSatPres_func()
        self.VaporPres = TempTools.Pres
        self.P1 = AirSupply_InspiredAir.Pressure - self.VaporPres
        self.T1 = HeatCore.Temp_K
        self.V2 = self.V1 * ( self.P2 / self.P1 ) * ( self.T1 / self.T2 )

class Posture:
    def __init__(self):
        pass
    
class PostureControl:
    def __init__(self):
        self.NONE = 0.0
        self.LYING = 1.0
        self.SITTING = 2.0
        self.STANDING = 3.0
        self.TILTED = 4.0
        self.Restraint = 0
        self.Request = 1
        self.LastValidRequest = 1

    def Parms_func(self):
        if self.Restraint == self.NONE:
            Status.Posture = self.LastValidRequest
        else:
            Status.Posture = self.Restraint
        if self.Restraint != self.NONE:
            pass
        else:
            if DailyPlannerControl.Switch:
                self.Request = self.LastValidRequest
            else:
                if Brain_Function.Comatose:
                    self.Request = self.LastValidRequest
                else:
                    Status.Posture = self.Request
                    self.LastValidRequest = self.Request

    def RequestChange_func(self):
        if self.Restraint == self.NONE:
            Status.Posture = self.Request
            self.LastValidRequest = self.Request
        else:
            pass

class A2Pool:
    def __init__(self):
        self.conc_A2_pGpermL = None
        self.Log10Conc = None
        self.conc_A2_pMolperL = None
        self.FormationRate = None
        self.EndogenousRate = None
        self.CEActivity = None
        self.Block_percent = 0.0
        self.CEBase = 30.0
        self.A2CONC = 0.3333
        self.PG_TO_PMOL = 0.956

    def CalcConc_func(self):
        self.CEActivity = self.CEBase * ( 1.0 - ( self.Block_percent / 100.0 ) )
        self.EndogenousRate = ReninPool.conc_PRA * self.CEActivity
        self.FormationRate = self.EndogenousRate + A2Pump.Rate
        self.conc_A2_pGpermL = self.A2CONC * self.FormationRate
        self.conc_A2_pMolperL = self.PG_TO_PMOL * self.conc_A2_pGpermL
        if self.conc_A2_pGpermL > 1.0:
            self.Log10Conc = ( math.log10( self.conc_A2_pGpermL ) )
        else:
            self.Log10Conc = 0.0


class ReninSynthesis:
    def __init__(self):
        self.TGFEffect = None
        self.SympsEffect = None
        self.Base = 290.0
        self.Tau = 60.0
        self.Rate = 290.0

    def TGFEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.6, 1.0, 2.0], [10.0, 2.0, 1.0, 0.3], [0.0, -4.0, -1.0, 0.0])

    def SympsEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.0, 2.5], [0.5, 1.0, 4.0], [0.0, 1.0, 0.0])

    def Parms_func(self):
        self.K = ( 1 / self.Tau )

    def Dervs_func(self):
        self.TGFEffect = self.TGFEffect_curve( TGF_Renin.Signal )
        self.SympsEffect = self.SympsEffect_curve( Kidney_BetaReceptors.Activity )
        self.SteadyState = self.Base * self.TGFEffect * self.SympsEffect * Kidney_NephronCount.Total_xNormal * Kidney_Function.Effect
        self.Rate = delay( self.K, self.SteadyState, self.Rate, System.Dx, 2.9)


class ReninClearance:
    def __init__(self):
        self.Rate = None
        self.K = 0.0161

    def Dervs_func(self):
        self.Rate = self.K * ReninPool.Mass

class ReninFree:
    def __init__(self):
        self.Flux = None
        self.FluxK = 0.01
        self.Gain = None
        self.Loss = None
        self.Mass = 87000.0

    def Flux_func(self):
        self.Flux = self.FluxK * self.Mass

    def Dervs_func(self):
        self.Gain = ReninSynthesis.Rate + ReninGranules.Flux
        self.Loss = ReninSecretion.Rate + self.Flux
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 870.0)


class A2Pump:
    def __init__(self):
        self.Rate = None
        self.Switch = False
        self.Setting = 0.0

    def Parms_func(self):
        if self.Switch:
            self.Rate = self.Setting
        else:
            self.Rate = 0.0


class ReninGranules:
    def __init__(self):
        self.Flux = None
        self.FluxK = 0.001
        self.Gain = None
        self.Loss = None
        self.Mass = 870000.0

    def Flux_func(self):
        self.Flux = self.FluxK * self.Mass

    def Dervs_func(self):
        self.Gain = ReninGranules.Flux
        self.Loss = self.Flux
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 8700.0)


class ReninPool:
    def __init__(self):
        self.conc_PRA = None
        self.Log10Conc = None
        self.VOLDIST = 0.60
        self.VolumeDistribution = None
        self.InitialVolumeDistribution = None
        self.Gain = None
        self.Loss = None
        self.Targetconc_PRA = 2.0
        self.InitialMass = None

    def Init_func(self):
        self.InitialVolumeDistribution = self.VOLDIST * ECFV.InitialVol
        self.InitialMass = self.Targetconc_PRA * self.InitialVolumeDistribution
        self.Mass = self.InitialMass

    def CalcConc_func(self):
        self.VolumeDistribution = self.VOLDIST * ECFV.Vol
        self.conc_PRA = self.Mass / self.VolumeDistribution
        if self.conc_PRA > 1.0:
            self.Log10Conc = ( math.log10( self.conc_PRA ) )
        else:
            self.Log10Conc = 0.0


    def Dervs_func(self):
        self.Gain = ReninSecretion.Rate + ReninTumor.Rate
        self.Loss = ReninClearance.Rate
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 90.0)


class ReninSecretion:
    def __init__(self):
        self.Rate = None
        self.TGFEffect = None
        self.SympsEffect = None
        self.Base = 0.0033
        self.Fraction = None

    def TGFEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.5, 1.0, 3.0], [8.0, 2.0, 1.0, 0.5], [0.0, -4.0, -1.0, 0.0])

    def SympsEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.0, 3.0], [0.5, 1.0, 4.0], [0.0, 1.0, 0.0])

    def Dervs_func(self):
        self.TGFEffect = self.TGFEffect_curve( TGF_Renin.Signal )
        self.SympsEffect = self.SympsEffect_curve( Kidney_BetaReceptors.Activity )
        self.Fraction = self.Base * self.TGFEffect * self.SympsEffect
        self.Rate = self.Fraction * ReninFree.Mass

class ReninTumor:
    def __init__(self):
        self.Rate = None
        self.Switch = False
        self.Setting = 0.0

    def Parms_func(self):
        if self.Switch:
            self.Rate = self.Setting
        else:
            self.Rate = 0.0


class Renin:

    def Parms_func(self):
        A2Pump.Parms_func()
        ReninTumor.Parms_func()
        ReninSynthesis.Parms_func()

    def CalcConc_func(self):
        ReninPool.CalcConc_func()
        A2Pool.CalcConc_func()

    def Dervs_func(self):
        ReninFree.Flux_func()
        ReninGranules.Flux_func()
        ReninSecretion.Dervs_func()
        ReninSynthesis.Dervs_func()
        ReninFree.Dervs_func()
        ReninGranules.Dervs_func()
        ReninClearance.Dervs_func()
        ReninPool.Dervs_func()

class LegMusclePump:
    def __init__(self):
        self.Effect = None

    def Calc_func(self):
        self.Effect = 1.0

class Gravity:
    def __init__(self):
        self.Gz = 1.0
    
class FattyAcid:
    def __init__(self):
        pass
    
class FAPool:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.conc_FA = None
        self.conc_FA_mGperdL = None
        self.conc_FA_mMolperL = None
        self.PER_ML_TO_PER_DL = 100.0
        self.MG_TO_MMOL = 3.92
        self.Targetconc_FA = 0.160
        self.InitialMass = None

    def Init_func(self):
        self.InitialMass = self.Targetconc_FA * ECFV.Vol
        self.Mass = self.InitialMass

    def CalcConc_func(self):
        self.conc_FA = self.Mass / ECFV.Vol
        self.conc_FA_mGperdL = self.PER_ML_TO_PER_DL * self.conc_FA
        self.conc_FA_mMolperL = self.MG_TO_MMOL * self.conc_FA

    def CalcDervs_func(self):
        self.Gain = TriglycerideHydrolysis.FattyAcidRate + LipidDeposits_Release.Rate
        self.Loss = Metabolism_FattyAcid.TotalBurn + LipidDeposits_Uptake.Rate + LM_Ketoacids.FattyAcidUptake + FADecomposition.Rate
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 25.0)


class FADecomposition:
    def __init__(self):
        self.Rate = None
        self.K = 0.0007

    def Dervs_func(self):
        self.Rate = self.K * FAPool.Mass

class Pericardium:
    def __init__(self):
        self.TotalVol = None
        self.StressedVol = None
        self.IsOpen = False

    def Calc_func(self):
        self.TotalVol = RightHeart_Size.Vol + RightAtrium.Vol + RightVentricle.Vol + LeftHeart_Size.Vol + LeftAtrium.Vol + LeftVentricle.Vol + Pericardium_Cavity.Vol
        Pericardium_TMP.Calc_func()
        Pericardium_Cavity.Calc_func()

    def Dervs_func(self):
        Pericardium_Drain.Dervs_func()
        Pericardium_Hemorrhage.Dervs_func()
        Pericardium_Cavity.Dervs_func()
        Pericardium_V0.Dervs_func()

class Pericardium_Drain:
    def __init__(self):
        self.Switch = False
        self.Conductance = 0.0
        self.BloodFlow = None
        self.PressureGradient = None
        self.ExternalPressure = 0.0

    def Dervs_func(self):
        self.PressureGradient = Pericardium_Cavity.Pressure - self.ExternalPressure
        self.BloodFlow = ( max( ( self.PressureGradient * self.Conductance ), 0.0) )

class Pericardium_Cavity:
    def __init__(self):
        self.Pressure = None
        self.Vol = 0.0

    def Calc_func(self):
        self.Pressure = Thorax.AvePressure + Pericardium_TMP.Pressure

    def Dervs_func(self):
        self.Change = Pericardium_Hemorrhage.BloodFlow - Pericardium_Drain.BloodFlow
        self.Vol = diffeq( self.Change, System.Dx, self.Vol, 0.1)


class Pericardium_TMP:
    def __init__(self):
        self.Pressure = None
        self.Stiffness = 0.015
        self.Vol = None

    def Calc_func(self):
        self.Vol = Pericardium.TotalVol
        self.CalcTMP_func()

    def CalcTMP_func(self):
        if Pericardium.IsOpen or ( self.Vol < Pericardium_V0.Vol ):
            self.Pressure = 0.0
        else:
            self.Pressure = ( math.e ** ( self.Stiffness * ( self.Vol - Pericardium_V0.Vol ) ) ) - 1.0


class Pericardium_Hemorrhage:
    def __init__(self):
        self.Switch = False
        self.Conductance = 0.0
        self.BloodFlow = None
        self.PressureGradient = None
        self.RBCFlow = None
        self.PlasmaFlow = None

    def Dervs_func(self):
        self.PressureGradient = SystemicArtys.Pressure - Pericardium_Cavity.Pressure
        self.BloodFlow = self.PressureGradient * self.Conductance
        self.RBCFlow = BloodVol.Hct * self.BloodFlow
        self.PlasmaFlow = BloodVol.PVCrit * self.BloodFlow

class Pericardium_V0:
    def __init__(self):
        self.K = 0.0035
        self.NormalTMP = 1.0
        self.PressureGradient = None
        self.Vol = 500.0

    def Dervs_func(self):
        self.PressureGradient = Pericardium_TMP.Pressure - self.NormalTMP
        self.Change = self.K * self.PressureGradient
        self.Vol = diffeq( self.Change, System.Dx, self.Vol, 5.0)


class SkeletalMuscle_ContractileProtein:

    def Initialize_func(self):
        self.Mass = SkeletalMuscle_Size.InitialProteinMass

    def Dervs_func(self):
        self.Change = 0.0
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 29.0)


class SkeletalMuscle_Ph:
    def __init__(self):
        self.Ph = None
        self.conc_SID = None
        self.conc_SID_mEqperL = None

    def CalcSID_func(self):
        self.conc_SID = KCell.conc_K_ + CellSID.OtherCations - CellSID.StrongAnions - SkeletalMuscle_Lactate.conc_Lac_
        self.conc_SID_mEqperL = 1000.0 * self.conc_SID

    def CalcPh_func(self):
        PhCells.pCO2 = SkeletalMuscle_CO2.PCO2
        PhCells.SID = self.conc_SID_mEqperL
        PhCells.Calc_func()
        self.Ph = PhCells.pH

class SkeletalMuscle_Fuel:
    def __init__(self):
        self.FADelivered = None
        self.GlucoseDelivered = None
        self.KR = 0.026
        self.Ratio = None
        self.FAFraction = None
        self.GlucoseFraction = None
        self.FA_GlucoseFraction = None
        self.LacFraction = None
        self.FAUsed_CalperMin = None
        self.AerobicGlucoseUsed_CalperMin = None
        self.AnaerobicGlucoseUsed_CalperMin = None
        self.LacUsed_CalperMin = None
        self.FAUsed_mGperMin = None
        self.AerobicGlucoseUsed_mGperMin = None
        self.AnaerobicGlucoseUsed_mGperMin = None
        self.LacUsed_mGperMin = None
        self.TotalGlucoseUsed_mGperMin = None
        self.FAFractionalDelivery = None
        self.AerobicGlucoseFractionalDelivery = None
        self.AnaerobicGlucoseFractionalDelivery = None
        self.MinimumFractionalDelivery = None
        self.FractUseDelay = 1.0

    def LacFraction_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 100.0], [0.0, 0.3], [0.0, 0.0])

    def Dervs_func(self):
        self.FADelivered = FAPool.conc_FA * SkeletalMuscle_Flow.PlasmaFlow
        self.GlucoseDelivered = GlucosePool.conc_Glucose * SkeletalMuscle_Flow.PlasmaFlow
        self.LacFraction = self.LacFraction_curve( SkeletalMuscle_Lactate.conc_Lac__mGperdL )
        self.FA_GlucoseFraction = 1.0 - self.LacFraction
        self.Ratio = FAPool.conc_FA_mGperdL / GlucosePool.conc_Glucose_mGperdL
        self.FAFraction = self.FA_GlucoseFraction * ( self.Ratio / ( self.Ratio + self.KR ) )
        self.GlucoseFraction = self.FA_GlucoseFraction - self.FAFraction
        self.FAUsed_CalperMin = self.FAFraction * SkeletalMuscle_Metabolism.AerobicCals
        self.AerobicGlucoseUsed_CalperMin = self.GlucoseFraction * SkeletalMuscle_Metabolism.AerobicCals
        self.LacUsed_CalperMin = self.LacFraction * SkeletalMuscle_Metabolism.AerobicCals
        self.AnaerobicGlucoseUsed_CalperMin = SkeletalMuscle_Glycogen.Metabolism_CalperMin
        self.FAUsed_mGperMin = self.FAUsed_CalperMin * Metabolism_Tools.Fat_mGperCal
        self.AerobicGlucoseUsed_mGperMin = self.AerobicGlucoseUsed_CalperMin * Metabolism_Tools.CarboAerobic_mGperCal
        self.LacUsed_mGperMin = self.LacUsed_CalperMin * Metabolism_Tools.Lac__mGperCal
        self.AnaerobicGlucoseUsed_mGperMin = SkeletalMuscle_Glycogen.Metabolism
        self.TotalGlucoseUsed_mGperMin = self.AerobicGlucoseUsed_mGperMin + self.AnaerobicGlucoseUsed_mGperMin
        if self.FAUsed_mGperMin > 0.0:
            self.FAFractionalDelivery = ( min( ( self.FADelivered / self.FAUsed_mGperMin ), 1.0) )
        else:
            self.FAFractionalDelivery = 1.0

        if self.AerobicGlucoseUsed_mGperMin > 0.0:
            self.AerobicGlucoseFractionalDelivery = ( min( ( self.GlucoseDelivered / self.AerobicGlucoseUsed_mGperMin ), 1.0) )
        else:
            self.AerobicGlucoseFractionalDelivery = 1.0

        self.AnaerobicGlucoseFractionalDelivery = SkeletalMuscle_Glycogen.Availability
        self.MinimumFractionalDelivery = ( min( ( ( min( self.FAFractionalDelivery, self.AerobicGlucoseFractionalDelivery) ) ), self.AnaerobicGlucoseFractionalDelivery) )
        self.K = 0.5
        self.DxMax = 1.0
        self.FractUse = self.MinimumFractionalDelivery
        self.FractUseDelay = delay( self.K, self.FractUse, self.FractUseDelay, System.Dx, 0.01)


class SkeletalMuscle:
    def __init__(self):
        pass
    
class SkeletalMuscle_Structure:
    def __init__(self):
        self.PhEffect = None
        self.FuelEffect = None
        self.TemperatureEffect = None
        self.Effect = 1.0

    def PhOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [6.5, 6.6], [0.1, 0.0], [0.0, 0.0])

    def FuelOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [0.5, 0.8], [0.05, 0.0], [0.0, 0.0])

    def TemperatureOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [44.0, 46.0], [0.0, 0.05], [0.0, 0.0])

    def Calc_func(self):
        self.PhEffect = self.PhOnStructure_curve( SkeletalMuscle_Ph.Ph )
        self.FuelEffect = self.FuelOnStructure_curve( SkeletalMuscle_Fuel.FractUseDelay )
        self.TemperatureEffect = self.TemperatureOnStructure_curve( HeatSkeletalMuscle.Temp_C )
        self.F1 = 0.0
        self.F2 = self.PhEffect + self.TemperatureEffect + self.FuelEffect
        self.Effect = backwardeuler( self.F1, self.F2, System.Dx, self.Effect, None)


class SkeletalMuscle_Pressure:
    def __init__(self):
        self.ArtyPressure = None
        self.VeinPressure = None
        self.PressureGradient = None
        self.PumpSwitch = False
        self.PumpSetting = 0.0

    def Calc_func(self):
        if self.PumpSwitch:
            self.ArtyPressure = self.PumpSetting
        else:
            self.ArtyPressure = SystemicArtys.Pressure

        self.VeinPressure = SystemicVeins.Pressure
        self.PressureGradient = ( max( ( self.ArtyPressure - self.VeinPressure ), 0.0) )

class SkeletalMuscle_Work:
    def __init__(self):
        self.MechanicalEfficiency_percent = 30.0
        self.MechanicalEfficiency = None
        self.TotalCals = None
        self.MotionCals = None
        self.HeatCals = None

    def Calc_func(self):
        self.MechanicalEfficiency = self.MechanicalEfficiency_percent / 100.0
        self.MotionCals = Exercise_Metabolism.MotionCals
        self.TotalCals = self.MotionCals / self.MechanicalEfficiency
        self.HeatCals = self.TotalCals - self.MotionCals

class SkeletalMuscle_Lactate:
    def __init__(self):
        self.conc_Lac_ = None
        self.conc_Lac__mEqperL = None
        self.conc_Lac__mGperdL = None
        self.DC = 1875.0
        self.Made = None
        self.Made_mGperMin = None
        self.Used = None
        self.Used_mGperMin = None
        self.Outflux = None
        self.Outflux_0 = None
        self.K = None
        self.Alpha = None
        self.MEQ_ML_TO_MG_DL = 9008.0
        self.GLUCOSE_TO_LACTATE = 0.99
        self.MG_TO_MEQ = 0.0112
        self.Mass = 20.25

    def CalcConc_func(self):
        self.conc_Lac_ = self.Mass / SkeletalMuscle_Size.LiquidVol
        self.conc_Lac__mEqperL = 1000.0 * self.conc_Lac_
        self.conc_Lac__mGperdL = self.MEQ_ML_TO_MG_DL * self.conc_Lac_

    def CalcDervs_func(self):
        self.Made_mGperMin = self.GLUCOSE_TO_LACTATE * SkeletalMuscle_Fuel.AnaerobicGlucoseUsed_mGperMin
        self.Made = self.MG_TO_MEQ * self.Made_mGperMin
        self.Used_mGperMin = SkeletalMuscle_Fuel.LacUsed_mGperMin
        self.Used = self.MG_TO_MEQ * self.Used_mGperMin
        self.K = self.DC / SkeletalMuscle_Size.LiquidVol
        if System.Dx >=0:
            self.Alpha = 0.0
        elif ( self.K * System.Dx ) >= 100.0:
            self.Alpha = 4E-44
        elif True:
            self.Alpha = ( math.e ** ( - self.K * System.Dx ) )
        self.Outflux_0 = self.DC * ( self.conc_Lac_ - LacPool.conc_Lac_ )
        self.Outflux = ( self.Alpha * self.Outflux_0 ) + ( ( 1 - self.Alpha ) * ( self.Made + self.Used ) )
        self.Change = self.Made - self.Used - self.Outflux
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.202)


class SkeletalMuscle_Metabolism:
    def __init__(self):
        self.TotalCalsUsed = None
        self.BasalCalsUsed = None
        self.InitialBasalCalsUsed = None
        self.BasalCalsUsed__CalperMinperG = 0.0052
        self.CalMultiplier = 1.0
        self.PostureCals = None
        self.ShiveringCals = None
        self.AerobicCals = None
        self.AnaerobicCals = None
        self.O2Need = None
        self.O2Lack = None

    def ScaleCals_func(self):
        self.InitialBasalCalsUsed = self.CalMultiplier * self.BasalCalsUsed__CalperMinperG * SkeletalMuscle_Size.InitialMass

    def CalcCals_func(self):
        self.BasalCalsUsed = self.CalMultiplier * self.BasalCalsUsed__CalperMinperG * SkeletalMuscle_Size.Mass
        self.PostureCals = 0.0
        self.ShiveringCals = HeatShivering.Cals
        self.TotalCalsUsed = ( self.BasalCalsUsed * Thyroid.Effect * HeatMetabolism.SkeletalMuscle * SkeletalMuscle_Structure.Effect ) + SkeletalMuscle_Work.TotalCals + self.PostureCals + self.ShiveringCals
        self.O2Need = Metabolism_Tools.CalToO2 * self.TotalCalsUsed

    def SplitCals_func(self):
        self.O2Lack = self.O2Need - SkeletalMuscle_Flow.O2Use
        self.AerobicCals = Metabolism_Tools.O2ToCal * SkeletalMuscle_Flow.O2Use
        self.AnaerobicCals = Metabolism_Tools.O2ToCal * self.O2Lack

class SkeletalMuscle_Size:
    def __init__(self):
        self.Vol = None
        self.Mass = None
        self.Mass_kG = None
        self.InitialMass = None
        self.InitialMass_kG = None
        self.Density = None
        self.LiquidMass = None
        self.LiquidDensity = 1.00
        self.LiquidVol = None
        self.InitialLiquidVol = None
        self.SolidMass = None
        self.InitialSolidMass = None
        self.ContractileProteinMass = None
        self.InitialProteinMass = None
        self.ContractileProteinDensity = 1.17
        self.OtherMass = None
        self.InitialOtherMass = None
        self.OtherDensity = 1.17
        self.ContractileProteinVol = None
        self.OtherVol = None
        self.SolidVol = None
        self.FractTotal = None
        self.IFV = None
        self.InitialIFV = None
        self.CellH2O = None
        self.InitialCellH2O = None
        self.H2OFractMass = 0.79
        self.SolidsFractMass = None
        self.OtherFractSolids = 0.50
        self.ProteinFractSolids = None

    def InitializeMuscleMass_func(self):
        self.InitialMass_kG = Values_Muscularity.Mass_kG

    def Initialize_func(self):
        self.InitialMass = 1000.0 * self.InitialMass_kG
        self.InitialLiquidVol = self.H2OFractMass * self.InitialMass / self.LiquidDensity
        self.SolidsFractMass = 1.0 - self.H2OFractMass
        self.InitialSolidMass = self.SolidsFractMass * self.InitialMass
        self.InitialOtherMass = self.OtherFractSolids * self.InitialSolidMass
        self.ProteinFractSolids = 1.0 - self.OtherFractSolids
        self.InitialProteinMass = self.ProteinFractSolids * self.InitialSolidMass

    def ScaleH2O_func(self):
        self.FractTotal = self.InitialLiquidVol / TissueH2O.InitialVol
        self.InitialIFV = self.FractTotal * InterstitialWater.InitialVol
        self.InitialCellH2O = self.FractTotal * CellH2O.InitialVol

    def Calc_func(self):
        self.IFV = self.FractTotal * InterstitialWater.Vol
        self.CellH2O = self.FractTotal * CellH2O.Vol
        self.LiquidVol = self.IFV + self.CellH2O
        self.LiquidMass = self.LiquidVol * self.LiquidDensity
        self.ContractileProteinMass = SkeletalMuscle_ContractileProtein.Mass
        self.OtherMass = self.InitialOtherMass
        self.SolidMass = self.ContractileProteinMass + self.OtherMass
        self.ContractileProteinVol = self.ContractileProteinMass / self.ContractileProteinDensity
        self.OtherVol = self.OtherMass / self.OtherDensity
        self.SolidVol = self.ContractileProteinVol + self.OtherVol
        self.Mass = self.LiquidMass + self.SolidMass
        self.Mass_kG = self.Mass / 1000.0
        self.Vol = self.LiquidVol + self.SolidVol
        self.Density = self.Mass / self.Vol

class SkeletalMuscle_Metaboreflex:
    def __init__(self):
        self.NerveActivity = None
        self.Clamp = False
        self.Level = 0.0

    def PhOnNerveActivity_curve(self, x):
        return cubic_hermite_spline(x, [6.5, 6.9], [5.0, 0.0], [0.0, 0.0])

    def Calc_func(self):
        if SkeletalMuscle_Function.Failed:
            self.NerveActivity = 0.0
        elif self.Clamp:
            self.NerveActivity = self.Level
        elif True:
            self.NerveActivity = self.PhOnNerveActivity_curve( SkeletalMuscle_Ph.Ph )

class SkeletalMuscle_Function:
    def __init__(self):
        self.Failed = False
        self.Effect = None
        self.PhEffect = None
        self.ProteinEffect = None
        self.FuelEffect = None
        self.TemperatureEffect = None

    def PhOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [6.4, 6.7], [0.0, 1.0], [0.0, 0.0])

    def ProteinOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [3000.0, 5200.0], [0.0, 1.0], [0.0, 0.0])

    def FuelOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.9], [0.0, 1.0], [0.0, 0.0])

    def TemperatureOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 37.1, 40.0, 46.0], [0.0, 1.0, 1.5, 0.0], [0.0, 0.12, 0.0, 0.0])

    def Calc_func(self):
        self.PhEffect = self.PhOnFunction_curve( SkeletalMuscle_Ph.Ph )
        self.ProteinEffect = self.ProteinOnFunction_curve( CellProtein.Mass_G )
        self.FuelEffect = self.FuelOnFunction_curve( SkeletalMuscle_Fuel.FractUseDelay )
        self.TemperatureEffect = self.TemperatureOnFunction_curve( HeatSkeletalMuscle.Temp_C )
        self.Effect = self.PhEffect * self.ProteinEffect * self.FuelEffect * self.TemperatureEffect * SkeletalMuscle_Structure.Effect

    def Wrapup_func(self):
        if not self.Failed and ( self.Effect < 0.2 ):
            self.Failed = True
        elif self.Failed and ( self.Effect > 0.4 ):
            self.Failed = False

class SkeletalMuscle_AlphaReceptors:
    def __init__(self):
        self.Activity = None
        self.TotalAgonism = None
        self.NeuralAgonism = None
        self.HumoralAgonism = None
        self.Switch = False
        self.Setting = 0.0
        self.NEURALK = 0.333
        self.HUMORALK = 0.5

    def Calc_func(self):
        self.NeuralAgonism = GangliaGeneral.NA_Hz
        self.HumoralAgonism = AlphaPool.Effect
        self.TotalAgonism = ( self.NEURALK * self.NeuralAgonism ) + ( self.HUMORALK * self.HumoralAgonism )
        if self.Switch:
            self.Activity = self.Setting
        else:
            self.Activity = self.TotalAgonism * AlphaBlockade.Effect


class SkeletalMuscle_MusclePumping:
    def __init__(self):
        self.Effect = None
        self.IntensityEffect = None
        self.RateEffect = None

    def IntensityEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 300.0], [0.0, 1.0], [0.007, 0.0])

    def RateEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 60.0], [0.0, 1.0], [0.04, 0.0])

    def Calc_func(self):
        self.IntensityEffect = self.IntensityEffect_curve( Exercise_Metabolism.MotionWatts )
        self.RateEffect = self.RateEffect_curve( Exercise_Metabolism.ContractionRate )
        self.Effect = 1.0 + ( self.IntensityEffect * self.RateEffect )

class SkeletalMuscle_CO2:
    def __init__(self):
        self.conc_HCO3 = None
        self.conc_HCO3_mEqperL = None
        self.PCO2 = None
        self.InflowGas = None
        self.InflowBase = None
        self.OutflowBase = None
        self.conc_BloodHCO3 = None
        self.Outflow_0 = None
        self.K = None
        self.Alpha = None
        self.Mass = 323.9

    def CalcConc_func(self):
        self.conc_HCO3 = self.Mass / SkeletalMuscle_Size.LiquidVol
        self.conc_HCO3_mEqperL = 1000.0 * self.conc_HCO3
        Tissue_BaseToGas.conc_HCO3 = self.conc_HCO3
        Tissue_BaseToGas.conc_SID = SkeletalMuscle_Ph.conc_SID
        Tissue_BaseToGas.Calc_func()
        self.PCO2 = Tissue_BaseToGas.pCO2

    def CalcDervs_func(self):
        self.K = SkeletalMuscle_Flow.BloodFlow / SkeletalMuscle_Size.LiquidVol
        if System.Dx >=0:
            self.Alpha = 0.0
        elif ( self.K * System.Dx ) >= 100.0:
            self.Alpha = 4E-44
        elif True:
            self.Alpha = ( math.e ** ( - self.K * System.Dx ) )
        self.InflowGas = Metabolism_RespiratoryQuotient.RQ * SkeletalMuscle_Flow.O2Use
        self.InflowBase = CO2Tools.LitersToMols * self.InflowGas
        Blood_GasToBase.pCO2 = self.PCO2
        Blood_GasToBase.conc_SID = BloodIons.conc_SID
        Blood_GasToBase.Calc_func()
        self.conc_BloodHCO3 = Blood_GasToBase.conc_HCO3
        self.Outflow_0 = SkeletalMuscle_Flow.BloodFlow * ( self.conc_BloodHCO3 - CO2Artys.conc_HCO3 )
        self.OutflowBase = ( self.Alpha * self.Outflow_0 ) + ( ( 1 - self.Alpha ) * self.InflowBase )
        self.Change = self.InflowBase - self.OutflowBase
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 3.24)


class SkeletalMuscle_MetabolicVasodilation:
    def __init__(self):
        self.OnTau = 0.2
        self.OnK = None
        self.OffTau = 1.0
        self.OffK = None
        self.Effect = 1.0

    def SteadyState_curve(self, x):
        return cubic_hermite_spline(x, [50.0, 1000.0, 3000.0], [1.0, 3.5, 5.5], [0.0, 0.003, 0.0])

    def Parms_func(self):
        if self.OnTau > 0.0:
            self.OnK = ( 1 / self.OnTau )
        else:
            self.OnK = self.float("inf")

        if self.OffTau > 0.0:
            self.OffK = ( 1 / self.OffTau )
        else:
            self.OffK = self.float("inf")


    def Calc_func(self):
        self.SteadyState = self.SteadyState_curve( SkeletalMuscle_Metabolism.O2Need )

    def Dervs_func(self):
        if self.Effect <= self.SteadyState:
            self.K = self.OnK
        else:
            self.K = self.OffK

        self.Effect = delay( self.K, self.SteadyState, self.Effect, System.Dx, 0.01)


class SkeletalMuscle_Flow:
    def __init__(self):
        self.Conductance = None
        self.BasicConductance = 7.2
        self.A2Effect = None
        self.SympsEffect = None
        self.ADHEffect = None
        self.PO2Effect = None
        self.AerobicFraction = None
        self.O2Use = None
        self.conc_O2 = None
        self.BloodFlow = None
        self.PlasmaFlow = None
        self.PO2 = 38.0
    def A2OnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.3, 3.5], [1.05, 1.0, 0.5], [0.0, -0.08, 0.0])

    def SympsOnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.0, 4.0], [1.3, 1.0, 0.5], [0.0, -0.2, 0.0])

    def PO2OnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 25.0, 35.0], [4.0, 2.5, 1.0], [0.0, -0.2, 0.0])

    def ADHOnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.8, 3.0], [1.0, 0.1], [0.0, 0.0])

    def PO2OnAerobicFraction_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 15.0, 20.0], [0.0, 0.2, 1.0], [0.0, 0.04, 0.0])

    def Calc_func(self):
        self.A2Effect = self.A2OnConductance_curve( A2Pool.Log10Conc )
        self.SympsEffect = self.SympsOnConductance_curve( SkeletalMuscle_AlphaReceptors.Activity )
        self.ADHEffect = self.ADHOnConductance_curve( ADHPool.Log10Conc )
        self.SearchMax = PO2Artys.Pressure

        def PO2implicitfunc(PO2):
            self.PO2Effect = self.PO2OnConductance_curve( PO2 )
            self.Conductance = self.BasicConductance * self.A2Effect * self.SympsEffect * self.PO2Effect * self.ADHEffect * SkeletalMuscle_MetabolicVasodilation.Effect * Viscosity.ConductanceEffect * Anesthesia.VascularConductance * SkeletalMuscle_Vasculature.Effect * SkeletalMuscle_MusclePumping.Effect
            self.BloodFlow = ( max( ( SkeletalMuscle_Pressure.PressureGradient * self.Conductance ), 0.0) )
            self.AerobicFraction = self.PO2OnAerobicFraction_curve( PO2 )
            self.O2Use = SkeletalMuscle_Metabolism.O2Need * self.AerobicFraction
            if self.BloodFlow > 0.0:
                self.conc_O2 = O2Artys.conc_O2 - ( self.O2Use / self.BloodFlow )
            else:
                self.conc_O2 = 0.0

            HgbTissue.conc_O2 = self.conc_O2
            HgbTissue.O2ToPO2_func()
            PO2End = HgbTissue.pO2

            return PO2End
        self.PO2 = impliciteq( PO2implicitfunc, self.PO2, 0.38)
        self.PlasmaFlow = self.BloodFlow * BloodVol.PVCrit

class SkeletalMuscle_Vasculature:
    def __init__(self):
        self.Tau = 30.0
        self.Effect = 1.0

    def PO2OnStimulus_curve(self, x):
        return cubic_hermite_spline(x, [41.0, 51.0, 61.0], [1.2, 1.0, 0.8], [0.0, -0.03, 0.0])

    def Parms_func(self):
        self.K = 1.0 / ( self.Tau * 1440.0 )

    def Calc_func(self):
        if SkeletalMuscle_Function.Failed:
            self.Stimulus = 0.0
        else:
            self.Stimulus = self.PO2OnStimulus_curve( SkeletalMuscle_Flow.PO2 )

        self.Effect = delay( self.K, self.Stimulus, self.Effect, System.Dx, None)


class SkeletalMuscle_Glycogen:
    def __init__(self):
        self.Synthesis = None
        self.Metabolism = None
        self.BasicSynthesis = 20.0
        self.GlucoseEffect = None
        self.InsulinEffect = None
        self.Space = None
        self.Availability = None
        self.Metabolism_CalperMin = None
        self.MG_TO_G = 0.001
        self.Mass = 500.0

    def GlucoseEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 100.0, 300.0], [0.0, 1.0, 3.0], [0.0, 0.01, 0.0])

    def InsulinEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 20.0, 100.0], [0.0, 1.0, 20.0], [0.0, 0.2, 0.0])

    def Space_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 400.0, 500.0], [4.0, 1.0, 0.0], [0.0, -0.015, 0.0])

    def Availability_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 50.0], [0.0, 1.0], [0.0, 0.0])

    def Dervs_func(self):
        self.GlucoseEffect = self.GlucoseEffect_curve( GlucosePool.conc_Glucose_mGperdL )
        self.InsulinEffect = self.InsulinEffect_curve( SkeletalMuscle_Insulin.conc_InsulinDelayed )
        self.Space = self.Space_curve( self.Mass )
        self.Availability = self.Availability_curve( self.Mass )
        self.Synthesis = self.BasicSynthesis * self.GlucoseEffect * self.InsulinEffect * self.Space
        self.Metabolism_CalperMin = SkeletalMuscle_Metabolism.AnaerobicCals * self.Availability
        self.Metabolism = self.Metabolism_CalperMin * Metabolism_Tools.CarboAnaerobic_mGperCal
        self.Change = self.MG_TO_G * ( self.Synthesis - self.Metabolism )
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 5.3)


class SkeletalMuscle_Insulin:
    def __init__(self):
        self.Tau = 40.0
        self.conc_InsulinDelayed = 20.0

    def Parms_func(self):
        self.K = ( 1 / self.Tau )

    def Dervs_func(self):
        self.conc_Insulin = InsulinPool.conc_Insulin
        self.conc_InsulinDelayed = delay( self.K, self.conc_Insulin, self.conc_InsulinDelayed, System.Dx, 0.2)


class InsulinInjection:
    def __init__(self):
        self.Dose = 0.0
        self.Type = 0
        self.TotalInjections = 0
        self.TotalDose = 0.0

    def InjectInsulinNow_func(self):
        self.TotalInjections = self.TotalInjections + 1
        self.TotalDose = self.TotalDose + self.Dose

class hCG:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.Secretion = None
        self.Degradation = None
        self.TargetConcFemale = 0.5
        self.TargetConcMale = 0.1
        self.TargetConc = None
        self.InitialMass = None
        self.conc_Conc_IUperL = None
        self.PumpSwitch = False
        self.PumpSetting = 0.0
        self.K = 0.0009

    def Init_func(self):
        if Gender.IsFemale:
            self.TargetConc = self.TargetConcFemale
        else:
            self.TargetConc = self.TargetConcMale

        self.InitialMass = self.TargetConc * ECFV.InitialVol_L
        self.Mass = self.InitialMass

    def Conc_func(self):
        self.conc_Conc_IUperL = self.Mass / ECFV.Vol_L

    def Dervs_func(self):
        self.Secretion = 0.009
        self.Degradation = self.K * self.Mass
        self.Gain = self.Secretion + ( self.PumpSetting * self.PumpSwitch )
        self.Loss = self.Degradation
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 1.0)


class Estradiol:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.Secretion = None
        self.Degradation = None
        self.TargetConcFemale = 0.15
        self.TargetConcMale = 0.01
        self.TargetConc = None
        self.InitialMass = None
        self.conc_Conc_nMolperL = None
        self.conc_Conc_nGpermL = None
        self.NMOLperL_TO_NGperML = 0.2724
        self.PumpSwitch = False
        self.PumpSetting = 0.0
        self.K = 0.11

    def Init_func(self):
        if Gender.IsFemale:
            self.TargetConc = self.TargetConcFemale
        else:
            self.TargetConc = self.TargetConcMale

        self.InitialMass = self.TargetConc * ECFV.InitialVol_L
        self.Mass = self.InitialMass

    def Conc_func(self):
        self.conc_Conc_nMolperL = self.Mass / ECFV.Vol_L
        self.conc_Conc_nGpermL = self.conc_Conc_nMolperL * self.NMOLperL_TO_NGperML

    def Dervs_func(self):
        if Gender.IsFemale:
            self.Secretion = Ovaries_Estradiol.Secretion
        else:
            self.Secretion = Testes_Estradiol.Secretion

        self.Degradation = self.K * self.Mass
        self.Gain = self.Secretion + ( self.PumpSetting * self.PumpSwitch )
        self.Loss = self.Degradation
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.01)


class DailyPlannerControl:
    def __init__(self):
        self.Switch = 0.0
        self.WorkLevel = 50.0
        self.WorkDuration = 50.0
        self.AerobicsLevel = 100.0
        self.AerobicsDuration = 30.0
        self.MealsDuration = 30.0
        self.FeedingTime = None
        self.FeedingFraction = None
        self.Status = 0
        self.WaitingTimer = Timer(0, "None", System.Dx)
        timervars.append(self.WaitingTimer)
        self.HourTimer = Timer(0, "None", System.Dx)
        timervars.append(self.HourTimer)
        self.WorkTimer = Timer(0, "None", System.Dx)
        timervars.append(self.WorkTimer)
        self.AerobicsTimer = Timer(0, "None", System.Dx)
        timervars.append(self.AerobicsTimer)
        self.MealsTimer = Timer(0, "None", System.Dx)
        timervars.append(self.MealsTimer)
        self.MinutesIntoDay = None
        self.HoursIntoDay = None
        self.MinutesUntilMidnight = None
        self.Task = None
        self.OFF = 0
        self.STARTNOW = 1
        self.STARTATMIDNIGHT = 2

    def Parms_func(self):
        if self.Switch == self.STARTNOW:
            self.Start_func()
        elif self.Switch == self.STARTATMIDNIGHT:
            self.StartWaiting_func()
        elif True:
            self.Stop_func()
        self.FeedingTime = DailyPlannerSchedule.MealCount * DailyPlannerControl.MealsDuration
        self.FeedingFraction = self.FeedingTime / 1440.0

    def Wrapup_func(self):
        if self.Status == 0:
            pass
        elif self.Status == 1:
            self.Waiting_func()
        elif self.Status == 2:
            self.Active_func()

    def StartWaiting_func(self):
        self.MinutesIntoDay = System.X % 1440.0
        if self.MinutesIntoDay:
            self.Status = 1
            self.WaitingTimer.val = 1440.0 - self.MinutesIntoDay
            self.WaitingTimer.state = "DOWN"
        else:
            self.Start_func()

    def Waiting_func(self):
        if self.WaitingTimer == 0:
            self.Start_func()

    def Active_func(self):
        if self.HourTimer == 0:
            self.NewTask_func()
        if self.WorkTimer == 0:
            self.Resting_func()
        if self.AerobicsTimer == 0:
            self.Resting_func()
        if self.MealsTimer == 0:
            self.Resting_func()

    def Start_func(self):
        self.Status = 2
        self.NewTask_func()

    def Stop_func(self):
        self.Status = 0
        self.WaitingTimer.state = "OFF"
        self.HourTimer.state = "OFF"
        self.WorkTimer.state = "OFF"
        self.AerobicsTimer.state = "OFF"
        self.MealsTimer.state = "OFF"
        Status.Activity = 3
        Status.Exertion = 0
        PostureControl.Request = PostureControl.LYING
        PostureControl.RequestChange_func()
        Status.Nutrition = 2

    def NewTask_func(self):
        self.GetTask_func()
        if self.Task == 0:
            self.StartSleep_func()
        elif self.Task == 1:
            self.StartRest_func()
        elif self.Task == 2:
            self.StartWork_func()
        elif self.Task == 3:
            self.StartAerobics_func()
        elif self.Task == 4:
            self.StartMeals_func()
        self.HourTimer.val = 60.0
        self.HourTimer.state = "DOWN"

    def GetTask_func(self):
        self.HoursIntoDay = self.ROUND ( ( System.X % 1440.0 ) / 60.0 )
        if self.HoursIntoDay == 0:
            self.Task = DailyPlannerSchedule.Hour12AM_1AM
        elif self.HoursIntoDay == 1:
            self.Task = DailyPlannerSchedule.Hour1AM_2AM
        elif self.HoursIntoDay == 2:
            self.Task = DailyPlannerSchedule.Hour2AM_3AM
        elif self.HoursIntoDay == 3:
            self.Task = DailyPlannerSchedule.Hour3AM_4AM
        elif self.HoursIntoDay == 4:
            self.Task = DailyPlannerSchedule.Hour4AM_5AM
        elif self.HoursIntoDay == 5:
            self.Task = DailyPlannerSchedule.Hour5AM_6AM
        elif self.HoursIntoDay == 6:
            self.Task = DailyPlannerSchedule.Hour6AM_7AM
        elif self.HoursIntoDay == 7:
            self.Task = DailyPlannerSchedule.Hour7AM_8AM
        elif self.HoursIntoDay == 8:
            self.Task = DailyPlannerSchedule.Hour8AM_9AM
        elif self.HoursIntoDay == 9:
            self.Task = DailyPlannerSchedule.Hour9AM_10AM
        elif self.HoursIntoDay == 10:
            self.Task = DailyPlannerSchedule.Hour10AM_11AM
        elif self.HoursIntoDay == 11:
            self.Task = DailyPlannerSchedule.Hour11AM_12PM
        elif self.HoursIntoDay == 12:
            self.Task = DailyPlannerSchedule.Hour12PM_1PM
        elif self.HoursIntoDay == 13:
            self.Task = DailyPlannerSchedule.Hour1PM_2PM
        elif self.HoursIntoDay == 14:
            self.Task = DailyPlannerSchedule.Hour2PM_3PM
        elif self.HoursIntoDay == 15:
            self.Task = DailyPlannerSchedule.Hour3PM_4PM
        elif self.HoursIntoDay == 16:
            self.Task = DailyPlannerSchedule.Hour4PM_5PM
        elif self.HoursIntoDay == 17:
            self.Task = DailyPlannerSchedule.Hour5PM_6PM
        elif self.HoursIntoDay == 18:
            self.Task = DailyPlannerSchedule.Hour6PM_7PM
        elif self.HoursIntoDay == 19:
            self.Task = DailyPlannerSchedule.Hour7PM_8PM
        elif self.HoursIntoDay == 20:
            self.Task = DailyPlannerSchedule.Hour8PM_9PM
        elif self.HoursIntoDay == 21:
            self.Task = DailyPlannerSchedule.Hour9PM_10PM
        elif self.HoursIntoDay == 22:
            self.Task = DailyPlannerSchedule.Hour10PM_11PM
        elif self.HoursIntoDay == 23:
            self.Task = DailyPlannerSchedule.Hour11PM_12AM

    def StartSleep_func(self):
        Status.Activity = 0
        Status.Exertion = 0
        PostureControl.Request = PostureControl.LYING
        PostureControl.RequestChange_func()
        Status.Nutrition = 1

    def StopSleep_func(self):
        self.Resting_func()

    def StartRest_func(self):
        self.Resting_func()

    def StartWork_func(self):
        self.WorkTimer.val = self.WorkDuration
        self.WorkTimer.state = "DOWN"
        Status.Activity = 1
        Status.Exertion = 1
        PostureControl.Request = PostureControl.STANDING
        PostureControl.RequestChange_func()
        Status.Nutrition = 1

    def StopWork_func(self):
        self.Resting_func()

    def StartAerobics_func(self):
        self.AerobicsTimer.val = self.AerobicsDuration
        self.AerobicsTimer.state = "DOWN"
        Status.Activity = 1
        Status.Exertion = 2
        PostureControl.Request = PostureControl.STANDING
        PostureControl.RequestChange_func()
        Status.Nutrition = 1

    def StopAerobics_func(self):
        self.Resting_func()

    def StartMeals_func(self):
        self.MealsTimer.val = self.MealsDuration
        self.MealsTimer.state = "DOWN"
        Status.Activity = 1
        Status.Exertion = 0
        PostureControl.Request = PostureControl.SITTING
        PostureControl.RequestChange_func()
        Status.Nutrition = 0

    def StopMeals_func(self):
        self.Resting_func()

    def Resting_func(self):
        Status.Activity = 1
        Status.Exertion = 0
        PostureControl.Request = PostureControl.SITTING
        PostureControl.RequestChange_func()
        Status.Nutrition = 1

class DailyPlanner:
    def __init__(self):
        pass
    
class DailyPlannerSchedule:
    def __init__(self):
        self.Hour12AM_1AM = 0
        self.Hour1AM_2AM = 0
        self.Hour2AM_3AM = 0
        self.Hour3AM_4AM = 0
        self.Hour4AM_5AM = 0
        self.Hour5AM_6AM = 0
        self.Hour6AM_7AM = 1
        self.Hour7AM_8AM = 4
        self.Hour8AM_9AM = 2
        self.Hour9AM_10AM = 2
        self.Hour10AM_11AM = 2
        self.Hour11AM_12PM = 2
        self.Hour12PM_1PM = 4
        self.Hour1PM_2PM = 2
        self.Hour2PM_3PM = 2
        self.Hour3PM_4PM = 2
        self.Hour4PM_5PM = 2
        self.Hour5PM_6PM = 1
        self.Hour6PM_7PM = 4
        self.Hour7PM_8PM = 1
        self.Hour8PM_9PM = 1
        self.Hour9PM_10PM = 1
        self.Hour10PM_11PM = 0
        self.Hour11PM_12AM = 0
        self.MealCount = None

    def Parms_func(self):
        self.MealCount = ( self.Hour12AM_1AM == 4 ) + ( self.Hour1AM_2AM == 4 ) + ( self.Hour2AM_3AM == 4 ) + ( self.Hour3AM_4AM == 4 ) + ( self.Hour4AM_5AM == 4 ) + ( self.Hour5AM_6AM == 4 ) + ( self.Hour6AM_7AM == 4 ) + ( self.Hour7AM_8AM == 4 ) + ( self.Hour8AM_9AM == 4 ) + ( self.Hour9AM_10AM == 4 ) + ( self.Hour10AM_11AM == 4 ) + ( self.Hour11AM_12PM == 4 ) + ( self.Hour12PM_1PM == 4 ) + ( self.Hour1PM_2PM == 4 ) + ( self.Hour2PM_3PM == 4 ) + ( self.Hour3PM_4PM == 4 ) + ( self.Hour4PM_5PM == 4 ) + ( self.Hour5PM_6PM == 4 ) + ( self.Hour6PM_7PM == 4 ) + ( self.Hour7PM_8PM == 4 ) + ( self.Hour8PM_9PM == 4 ) + ( self.Hour9PM_10PM == 4 ) + ( self.Hour10PM_11PM == 4 ) + ( self.Hour11PM_12AM == 4 )

class TiltTable:
    def __init__(self):
        self.Degrees = 0.0
    
class Heart_Tachyarrhythmia:
    def __init__(self):
        self.Effect = None

    def Effect_curve(self, x):
        return cubic_hermite_spline(x, [200.0, 300.0], [1.0, 0.0], [0.0, 0.0])

    def Calc_func(self):
        self.Effect = self.Effect_curve( Heart_Rate.Rate )

class Heart_VFib:
    def __init__(self):
        self.Is_Fibrillating = False
        self.ElapsedTime = Timer(0, "None", System.Dx)
        timervars.append(self.ElapsedTime)

    def Wrapup_func(self):
        if Heart_Asystole.Is_Asystole:
            if self.Is_Fibrillating:
                self.Stop_func()
            else:
                pass
        else:
            self.TestStart_func()

    def TestStart_func(self):
        if LeftHeart_Function.Effect < 0.30:
            self.Start_func()
        elif KPool.conc_K__mEqperL > 10.0:
            self.Start_func()
        elif KPool.conc_K__mEqperL < 2.4:
            self.Start_func()
        elif DigoxinPool.conc_Digoxin > 2.5:
            self.Start_func()

    def RequestStart_func(self):
        if Heart_Asystole.Is_Asystole:
            pass
        else:
            self.Start_func()

    def Start_func(self):
        self.Is_Fibrillating = True
        self.ElapsedTime.val = 0.0
        self.ElapsedTime.state = "UP"

    def Stop_func(self):
        self.Is_Fibrillating = False
        self.ElapsedTime.state = "OFF"

    def ResetElapsedTime_func(self):
        self.ElapsedTime.val = 0.0

class Heart_Asystole:
    def __init__(self):
        self.Is_Asystole = False

    def Wrapup_func(self):
        if LeftHeart_Function.Failed:
            self.Is_Asystole = True
        else:
            self.Is_Asystole = False


class SANode_Rate:
    def __init__(self):
        self.Rate = None
        self.ParasympatheticEffect = None
        self.SympatheticEffect = None
        self.BasicRate = 82.0
        self.Is_SinusRhythm = True

    def ParasympatheticEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 2.0, 8.0], [0.0, -20.0, -40.0], [0.0, -8.0, 0.0])

    def SympatheticEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.0, 5.0], [0.0, 10.0, 120.0], [0.0, 10.0, 0.0])

    def Calc_func(self):
        self.ParasympatheticEffect = self.ParasympatheticEffect_curve( VagusNerve.NA_Hz )
        self.SympatheticEffect = self.SympatheticEffect_curve( SANode_BetaReceptors.Activity )
        self.Rate = self.BasicRate + self.ParasympatheticEffect + self.SympatheticEffect

class LeftHeart_Pain:
    def __init__(self):
        self.HasPain = False
        self.IsIschemic = False
        self.IsAcidic = False
        self.conc_Lac__NoPain = 0.03
        self.conc_Lac__Pain = 0.05

    def Wrapup_func(self):
        self.IsIschemic = LeftHeart_Infarction.IsIschemic
        if LeftHeart_Lactate.conc_Lac_ < self.conc_Lac__NoPain:
            self.IsAcidic = False
        else:
            pass
        if LeftHeart_Lactate.conc_Lac_ > self.conc_Lac__Pain:
            self.IsAcidic = True
        else:
            pass
        if self.IsIschemic or self.IsAcidic:
            self.HasPain = True
        else:
            self.HasPain = False


class Heart_Rhythm:
    def __init__(self):
        self.Is_Sinus = True
        self.Is_Ventricle = False
        self.Is_Paced = False
        self.Is_CPRThumper = False
        self.Is_None = False

    def Wrapup_func(self):
        pass

class Heart_Ventricles:
    def __init__(self):
        self.Rate = None
        self.NotPacedRate = None
        self.AVBlock = False
        self.IntrinsicRate = None
        self.BasicRate = 45.0
        self.Is_VentricularRhythm = False

    def Calc_func(self):
        self.IntrinsicRate = self.BasicRate * LeftHeart_Function.Effect
        SANode_Rate.Is_SinusRhythm = False
        self.Is_VentricularRhythm = False
        if Heart_Asystole.Is_Asystole or Heart_VFib.Is_Fibrillating:
            if CPR_Heart.Status == CPR_Heart.ACTIVE:
                self.Rate = CPR_Heart.ThumperRate
            else:
                self.Rate = 0.0

        else:
            if self.AVBlock:
                self.NotPacedRate = self.IntrinsicRate
                self.Is_VentricularRhythm = True
            else:
                self.NotPacedRate = SANode_Rate.Rate
                SANode_Rate.Is_SinusRhythm = True
            if Heart_Pacemaker.Switch:
                self.Rate = ( max( self.NotPacedRate, Heart_Pacemaker.Rate) )
            else:
                self.Rate = self.NotPacedRate


class Heart_Rate:
    def __init__(self):
        self.Rate = None

    def Calc_func(self):
        self.Rate = Heart_Ventricles.Rate

class Heart_Intervals:
    def __init__(self):
        self.R_R = None
        self.Systolic = None
        self.Diastolic = None
        self.SYSTOLICK = 0.343

    def Calc_func(self):
        if CPR_Heart.Status == CPR_Heart.ACTIVE:
            self.R_R = 60.0 / CPR_Heart.ThumpRate
            self.Systolic = 0.5 * self.R_R
            self.Diastolic = self.R_R - self.Systolic
        elif Heart_Rate.Rate <= 0.0:
            self.R_R = 0.0
            self.Systolic = 0.0
            self.Diastolic = 0.0
        elif True:
            self.R_R = 60.0 / Heart_Rate.Rate
            self.Systolic = self.SYSTOLICK * ( math.sqrt( self.R_R ) )
            self.Diastolic = self.R_R - self.Systolic

class Heart_Pacemaker:
    def __init__(self):
        self.Switch = False
        self.Setting = 0.0
        self.Rate = 0.0

    def Parms_func(self):
        if self.Switch:
            self.Rate = self.Setting
        else:
            self.Rate = 0.0


class RightHeart_Pain:
    def __init__(self):
        self.HasPain = False
        self.IsIschemic = False
        self.IsAcidic = False
        self.conc_Lac__NoPain = 0.03
        self.conc_Lac__Pain = 0.05

    def Wrapup_func(self):
        self.IsIschemic = RightHeart_Infarction.IsIschemic
        if RightHeart_Lactate.conc_Lac_ < self.conc_Lac__NoPain:
            self.IsAcidic = False
        else:
            pass
        if RightHeart_Lactate.conc_Lac_ > self.conc_Lac__Pain:
            self.IsAcidic = True
        else:
            pass
        if self.IsIschemic or self.IsAcidic:
            self.HasPain = True
        else:
            self.HasPain = False


class Heart:

    def Parms_func(self):
        Heart_Pacemaker.Parms_func()

    def Calc_func(self):
        SANode_Rate.Calc_func()
        Heart_Ventricles.Calc_func()
        Heart_Rate.Calc_func()
        Heart_Tachyarrhythmia.Calc_func()
        Heart_Intervals.Calc_func()

    def Dervs_func(self):
        pass

    def Wrapup_func(self):
        Heart_Asystole.Wrapup_func()
        Heart_VFib.Wrapup_func()
        Heart_Pain.Wrapup_func()

    def Final_func(self):
        Heart_ECG.Wrapup_func()

class SANode_BetaReceptors:
    def __init__(self):
        self.Activity = None
        self.TotalAgonism = None
        self.NeuralAgonism = None
        self.HumoralAgonism = None
        self.Switch = False
        self.Setting = 0.0
        self.NEURALK = 0.333
        self.HUMORALK = 0.5

    def Calc_func(self):
        self.NeuralAgonism = GangliaGeneral.NA_Hz
        self.HumoralAgonism = BetaPool.Effect
        self.TotalAgonism = ( self.NEURALK * self.NeuralAgonism ) + ( self.HUMORALK * self.HumoralAgonism )
        if self.Switch:
            self.Activity = self.Setting
        else:
            self.Activity = self.TotalAgonism * BetaBlockade.Effect


class Heart_ECG:
    def __init__(self):
        self.Index = 0
        self.Now = None
        self.NORMAL = 0
        self.PACED = 1
        self.STSHIFT = 2
        self.VFIB = 3
        self.FLAT = 4
        self.Is_OK = True
        self.Is_Paced = False
        self.Is_STShift = False
        self.Is_VFib = False
        self.Is_Flat = False
        self.R_RInterval = None
        self.Q_TInterval = None

    def Wrapup_func(self):
        self.R_RInterval = Heart_Intervals.R_R
        self.Q_TInterval = Heart_Intervals.Systolic
        self.Now = self.NORMAL
        if Heart_Pacemaker.Switch:
            self.Now = self.PACED
        elif Heart_Pain.HasPain:
            self.Now = self.STSHIFT
        elif Heart_VFib.Is_Fibrillating:
            self.Now = self.VFIB
        elif Heart_Asystole.Is_Asystole:
            self.Now = self.FLAT
        if ( self.Index != self.FLAT ) and ( self.Now == self.FLAT ):
            self.Index = self.FLAT
            self.Reset_func()
            self.Is_Flat = True
        elif ( self.Index != self.VFIB ) and ( self.Now == self.VFIB ):
            self.Index = self.VFIB
            self.Reset_func()
            self.Is_VFib = True
        elif ( self.Index != self.STSHIFT ) and ( self.Now == self.STSHIFT ):
            self.Index = self.STSHIFT
            self.Reset_func()
            self.Is_STShift = True
        elif ( self.Index != self.PACED ) and ( self.Now == self.PACED ):
            self.Index = self.PACED
            self.Reset_func()
            self.Is_Paced = True
        elif ( self.Index != self.NORMAL ) and ( self.Now == self.NORMAL ):
            self.Index = self.NORMAL
            self.Reset_func()
            self.Is_OK = True

    def Reset_func(self):
        self.Is_OK = False
        self.Is_Paced = False
        self.Is_STShift = False
        self.Is_VFib = False
        self.Is_Flat = False

class Heart_Defibrillator:
    def __init__(self):
        self.Joules = 100.0
        self.TotalShocks = 0
        self.Probability = 0

    def Joules_Probability_curve(self, x):
        return cubic_hermite_spline(x, [50.0, 100.0], [0.0, 0.8], [0.0, 0.0])

    def ShockNow_func(self):
        if Heart_Asystole.Is_Asystole:
            pass
        else:
            if Heart_Rate.Rate > 0.0:
                pass
            else:
                self.TotalShocks = self.TotalShocks + 1
                self.Probability = LeftHeart_Function.Effect * self.Joules_Probability_curve( self.Joules )
                if System.RANDOM < self.Probability:
                    Heart_VFib.Stop_func()
                else:
                    pass

class Heart_Pain:
    def __init__(self):
        self.HasPain = False

    def Wrapup_func(self):
        RightHeart_Pain.Wrapup_func()
        LeftHeart_Pain.Wrapup_func()
        if self.HasPain:
            if ( not RightHeart_Pain.HasPain ) and ( not LeftHeart_Pain.HasPain ):
                self.HasPain = False
                self.ShowOK_func()
            else:
                pass
        else:
            if ( RightHeart_Pain.HasPain ) or ( LeftHeart_Pain.HasPain ):
                self.HasPain = True
                self.ShowPain_func()
            else:
                pass

    def ShowPain_func(self):
        if not Brain_Function.Comatose:
            pass
        else:
            pass

    def ShowOK_func(self):
        if not Brain_Function.Comatose:
            pass
        else:
            pass

class CPR_Lungs:
    def __init__(self):
        self.INACTIVE = 0.0
        self.READY = 1.0
        self.ACTIVE = 2.0
        self.Switch = False
        self.Status = 0.0
        self.Activate = None
        self.ActivateOnRespiratoryArrest = True
        self.Rate = 10.0
        self.Volume = 400.0

    def Parms_func(self):
        if self.Switch:
            self.Status = self.READY
        else:
            self.Status = self.INACTIVE


    def Wrapup_func(self):
        if not self.Switch:
            pass
        else:
            self.Activate = self.ActivateOnRespiratoryArrest and ( RespiratoryCenter_Output.Rate <= 0.0 )
            if self.Activate:
                self.Status = self.ACTIVE
            else:
                self.Status = self.READY


class CPR_Heart:
    def __init__(self):
        self.INACTIVE = 0.0
        self.READY = 1.0
        self.ACTIVE = 2.0
        self.Switch = False
        self.Status = 0.0
        self.Activate = None
        self.ActivateOnAsystole = True
        self.ActivateOnFibrillation = True
        self.ThumpRate = 100.0
        self.Force = 300.0
        self.Is_Active = False

    def Parms_func(self):
        if self.Switch:
            self.Status = self.READY
        else:
            self.Status = self.INACTIVE


    def Wrapup_func(self):
        if not self.Switch:
            pass
        else:
            self.Activate = ( self.ActivateOnAsystole and Heart_Asystole.Is_Asystole ) or ( self.ActivateOnFibrillation and Heart_VFib.Is_Fibrillating )
            if self.Activate:
                self.Status = self.ACTIVE
            else:
                self.Status = self.READY


class CPR:

    def Parms_func(self):
        CPR_Heart.Parms_func()
        CPR_Lungs.Parms_func()

    def Wrapup_func(self):
        CPR_Heart.Wrapup_func()
        CPR_Lungs.Wrapup_func()

class Drugs:

    def Parms_func(self):
        Chlorothiazide.Parms_func()
        Digoxin.Parms_func()
        Furosemide.Parms_func()
        Midodrine.Parms_func()

    def CalcConc_func(self):
        Chlorothiazide.CalcConc_func()
        Digoxin.CalcConc_func()
        Furosemide.CalcConc_func()
        Midodrine.CalcConc_func()

    def Dervs_func(self):
        Chlorothiazide.Dervs_func()
        Digoxin.Dervs_func()
        Furosemide.Dervs_func()
        Midodrine.Dervs_func()

    def Wrapup_func(self):
        Chlorothiazide.Wrapup_func()
        Digoxin.Wrapup_func()
        Midodrine.Wrapup_func()

class MidodrineSingleDose:
    def __init__(self):
        self.Dose = 0.0
        self.TimeLastDose = 0
        self.TotalDoses = 0.0
        self.CumulativeDose = 0.0

    def TakeDoseNow_func(self):
        MidodrineGILumen.Mass = MidodrineGILumen.Mass + ( 1000.0 * self.Dose )
        self.TimeLastDose = System.X
        self.TotalDoses = self.TotalDoses + 1.0
        self.CumulativeDose = self.CumulativeDose + self.Dose

    def Reset_func(self):
        self.TimeLastDose = 0
        self.TotalDoses = 0.0
        self.CumulativeDose = 0.0

class MidodrinePool:
    def __init__(self):
        self.conc_Midodrine = None
        self.Gain = None
        self.Loss = None
        self.K = 0.02
        self.VolDist = 90.0
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Midodrine = self.Mass / self.VolDist

    def Dervs_func(self):
        self.Gain = MidodrineGILumen.Loss
        self.Loss = self.K * self.Mass
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 20.0)


class MidodrineGILumen:
    def __init__(self):
        self.BIOAVAIL = 0.93
        self.NIPHCL = 0.875
        self.PERM = 0.060
        self.conc_Midodrine = None
        self.Loss = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Midodrine = self.Mass / GILumenVolume.Mass_L

    def Dervs_func(self):
        self.Loss = self.BIOAVAIL * self.NIPHCL * self.PERM * self.Mass
        self.Change = - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 5.0)


class MidodrineDailyDose:
    def __init__(self):
        self.Dose = 0.0
        self.TakeDaily = False
        self.LastTakeDaily = False
        self.TimesADay = 1.0
        self.TimeLastDose = 0
        self.TimeNextDose = 0
        self.TotalDoses = 0.0
        self.CumulativeDose = 0.0
        self.Timer = Timer(0.0, "OFF", System.Dx)
        timervars.append(self.Timer)
        self.IntervalGoal = None
        self.Interval = None
        self.PREPTIME = 10.0

    def Parms_func(self):
        self.IntervalGoal = 1440.0 / self.TimesADay
        if self.TakeDaily == self.LastTakeDaily:
            pass
        else:
            if self.TakeDaily:
                self.Timer.val = 0.0
                self.Timer.state = "UP"
                self.Interval = self.PREPTIME
                self.TimeNextDose = System.X + self.PREPTIME
            else:
                self.Timer.state = "OFF"
                self.TimeNextDose = 0
            self.LastTakeDaily = self.TakeDaily

    def Wrapup_func(self):
        if self.TakeDaily:
            if Timer < self.Interval:
                pass
            else:
                self.Timer.val = 0.0
                self.TimeNextDose = self.TimeNextDose + self.IntervalGoal
                self.TimeLastDose = System.X
                self.Interval = self.TimeNextDose - System.X
                MidodrineGILumen.Mass = MidodrineGILumen.Mass + ( 1000.0 * self.Dose )
                self.TotalDoses = self.TotalDoses + 1.0
                self.CumulativeDose = self.CumulativeDose + self.Dose
        else:
            pass

    def Reset_func(self):
        self.TimeLastDose = 0
        self.TotalDoses = 0.0
        self.CumulativeDose = 0.0

class DesglymidodrinePool:
    def __init__(self):
        self.conc_Desglymidodrine = None
        self.Gain = None
        self.Loss = None
        self.VolDist = 180.0
        self.NIPGLYCINE = 0.705
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Desglymidodrine = self.Mass / self.VolDist

    def Dervs_func(self):
        self.Gain = self.NIPGLYCINE * MidodrinePool.Loss
        self.Loss = DesglymidodrineKidney.UrineLoss
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 40.0)


class DesglymidodrineKidney:
    def __init__(self):
        self.UrineLoss = None
        self.K = 0.0045

    def Dervs_func(self):
        self.UrineLoss = self.K * DesglymidodrinePool.Mass * Kidney_NephronCount.Filtering_xNormal * Kidney_Function.Effect

class Midodrine:

    def Parms_func(self):
        MidodrineDailyDose.Parms_func()

    def CalcConc_func(self):
        MidodrineGILumen.CalcConc_func()
        MidodrinePool.CalcConc_func()
        DesglymidodrinePool.CalcConc_func()

    def Dervs_func(self):
        MidodrineGILumen.Dervs_func()
        DesglymidodrineKidney.Dervs_func()
        MidodrinePool.Dervs_func()
        DesglymidodrinePool.Dervs_func()

    def Wrapup_func(self):
        MidodrineDailyDose.Wrapup_func()

class DigoxinKidney:
    def __init__(self):
        self.UrineLoss = None
        self.FiltLoss = None
        self.SecLoss = None
        self.FiltK = 0.000178
        self.SecK = 0.000118

    def Dervs_func(self):
        self.FiltLoss = 0.001 * DigoxinPool.conc_Digoxin * GlomerulusFiltrate.GFR
        self.SecLoss = self.SecK * DigoxinPool.Mass * Kidney_NephronCount.Filtering_xNormal * Kidney_Function.Effect
        self.UrineLoss = self.FiltLoss + self.SecLoss

class Digoxin:

    def Parms_func(self):
        DigoxinDailyDose.Parms_func()

    def CalcConc_func(self):
        DigoxinGILumen.CalcConc_func()
        DigoxinPool.CalcConc_func()

    def Dervs_func(self):
        DigoxinGILumen.Dervs_func()
        DigoxinKidney.Dervs_func()
        DigoxinPool.Dervs_func()

    def Wrapup_func(self):
        DigoxinDailyDose.Wrapup_func()
        DigoxinPool.Wrapup_func()

class DigoxinSingleDose:
    def __init__(self):
        self.Dose = 0.0
        self.TimeLastDose = 0
        self.TotalDoses = 0.0
        self.CumulativeDose = 0.0

    def TakeDoseNow_func(self):
        DigoxinGILumen.Mass = DigoxinGILumen.Mass + ( 1000.0 * self.Dose )
        self.TimeLastDose = System.X
        self.TotalDoses = self.TotalDoses + 1.0
        self.CumulativeDose = self.CumulativeDose + self.Dose

    def Reset_func(self):
        self.TimeLastDose = 0
        self.TotalDoses = 0.0
        self.CumulativeDose = 0.0

class DigoxinPool:
    def __init__(self):
        self.conc_Digoxin = None
        self.Gain = None
        self.Loss = None
        self.VolDist = 700.0
        self.Nauseated = False
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Digoxin = self.Mass / self.VolDist

    def Dervs_func(self):
        self.Gain = DigoxinGILumen.Loss
        self.Loss = DigoxinKidney.UrineLoss
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.01)


    def Wrapup_func(self):
        if ( not self.Nauseated ) and ( self.conc_Digoxin > 2.0 ):
            self.Nauseated = True
        elif ( self.Nauseated ) and ( self.conc_Digoxin <= 1.5 ):
            self.Nauseated = False

class DigoxinDailyDose:
    def __init__(self):
        self.Dose = 0.0
        self.TakeDaily = False
        self.LastTakeDaily = False
        self.TimesADay = 1.0
        self.TimeLastDose = 0
        self.TimeNextDose = 0
        self.TotalDoses = 0.0
        self.CumulativeDose = 0.0
        self.Timer = Timer(0.0, "OFF", System.Dx)
        timervars.append(self.Timer)
        self.IntervalGoal = None
        self.Interval = None
        self.PREPTIME = 10.0

    def Parms_func(self):
        self.IntervalGoal = 1440.0 / self.TimesADay
        if self.TakeDaily == self.LastTakeDaily:
            pass
        else:
            if self.TakeDaily:
                self.Timer.val = 0.0
                self.Timer.state = "UP"
                self.Interval = self.PREPTIME
                self.TimeNextDose = System.X + self.PREPTIME
            else:
                self.Timer.state = "OFF"
                self.TimeNextDose = 0
            self.LastTakeDaily = self.TakeDaily

    def Wrapup_func(self):
        if self.TakeDaily:
            if Timer < self.Interval:
                pass
            else:
                self.Timer.val = 0.0
                self.TimeNextDose = self.TimeNextDose + self.IntervalGoal
                self.TimeLastDose = System.X
                self.Interval = self.TimeNextDose - System.X
                DigoxinGILumen.Mass = DigoxinGILumen.Mass + self.Dose
                self.TotalDoses = self.TotalDoses + 1.0
                self.CumulativeDose = self.CumulativeDose + self.Dose
        else:
            pass

    def Reset_func(self):
        self.TimeLastDose = 0
        self.TotalDoses = 0.0
        self.CumulativeDose = 0.0

class DigoxinGILumen:
    def __init__(self):
        self.BIOAVAIL = 0.75
        self.PERM = 0.007
        self.conc_Digoxin = None
        self.Loss = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Digoxin = self.Mass / GILumenVolume.Mass_L

    def Dervs_func(self):
        self.Loss = self.BIOAVAIL * self.PERM * self.Mass
        self.Change = - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.01)


class FurosemideSingleDose:
    def __init__(self):
        self.Dose = 0.0
        self.Timespan = 15.0
        self.K = None
        self.Loss = None
        self.TimeLastDose = 0
        self.TotalDoses = 0.0
        self.CumulativeDose = 0.0
        self.Mass = 0.0

    def Parms_func(self):
        self.K = ( 1 / ( 2.0 * ( self.Timespan / 60.0 ) ) )

    def Dervs_func(self):
        self.Loss = self.K * self.Mass
        self.Change = - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 1.0)


    def InjectNow_func(self):
        self.Mass = self.Mass + self.Dose
        self.TimeLastDose = System.X
        self.TotalDoses = self.TotalDoses + 1.0
        self.CumulativeDose = self.CumulativeDose + self.Dose

    def Reset_func(self):
        self.TimeLastDose = 0
        self.TotalDoses = 0.0
        self.CumulativeDose = 0.0

class FurosemideKidney:
    def __init__(self):
        self.UrineLoss = None
        self.K = 0.01

    def Dervs_func(self):
        self.UrineLoss = self.K * FurosemidePool.Mass * Kidney_NephronCount.Filtering_xNormal * Kidney_Function.Effect

class FurosemidePool:
    def __init__(self):
        self.conc_Furosemide = None
        self.Gain = None
        self.Loss = None
        self.NonrenalLoss = None
        self.NONRENALK = 0.01
        self.VolDist = None
        self.VOLDISTK = 0.57
        self.Mass = 0.0

    def CalcConc_func(self):
        self.VolDist = self.VOLDISTK * ECFV.Vol_L
        self.conc_Furosemide = self.Mass / self.VolDist

    def Dervs_func(self):
        self.Gain = FurosemideSingleDose.Loss
        self.NonrenalLoss = self.NONRENALK * self.Mass
        self.Loss = self.NonrenalLoss + FurosemideKidney.UrineLoss
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 1.0)


class Furosemide:

    def Parms_func(self):
        FurosemideSingleDose.Parms_func()

    def CalcConc_func(self):
        FurosemidePool.CalcConc_func()

    def Dervs_func(self):
        FurosemideSingleDose.Dervs_func()
        FurosemideKidney.Dervs_func()
        FurosemidePool.Dervs_func()

class ThiazideKidney:
    def __init__(self):
        self.UrineLoss = None
        self.K = 0.008

    def Dervs_func(self):
        self.UrineLoss = self.K * ThiazidePool.Mass * GlomerulusFiltrate.GFRxNormal * Kidney_Function.Effect

class ThiazideGILumen:
    def __init__(self):
        self.BIOAVAIL = 0.20
        self.PERM = 0.01
        self.conc_Thiazide = None
        self.Loss = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Thiazide = self.Mass / GILumenVolume.Mass_L

    def Dervs_func(self):
        self.Loss = self.BIOAVAIL * self.PERM * self.Mass
        self.Change = - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 1.0)


class Chlorothiazide:

    def Parms_func(self):
        ThiazideDailyDose.Parms_func()

    def CalcConc_func(self):
        ThiazideGILumen.CalcConc_func()
        ThiazidePool.CalcConc_func()

    def Dervs_func(self):
        ThiazideGILumen.Dervs_func()
        ThiazideKidney.Dervs_func()
        ThiazidePool.Dervs_func()

    def Wrapup_func(self):
        ThiazideDailyDose.Wrapup_func()

class ThiazideDailyDose:
    def __init__(self):
        self.Dose = 0.0
        self.TakeDaily = False
        self.LastTakeDaily = False
        self.TimesADay = 1.0
        self.TimeLastDose = 0
        self.TimeNextDose = 0
        self.TotalDoses = 0.0
        self.CumulativeDose = 0.0
        self.Timer = Timer(0.0, "OFF", System.Dx)
        timervars.append(self.Timer)
        self.IntervalGoal = None
        self.Interval = None
        self.PREPTIME = 10.0

    def Parms_func(self):
        self.IntervalGoal = 1440.0 / self.TimesADay
        if self.TakeDaily == self.LastTakeDaily:
            pass
        else:
            if self.TakeDaily:
                self.Timer.val = 0.0
                self.Timer.state = "UP"
                self.Interval = self.PREPTIME
                self.TimeNextDose = System.X + self.PREPTIME
            else:
                self.Timer.state = "OFF"
                self.TimeNextDose = 0
            self.LastTakeDaily = self.TakeDaily

    def Wrapup_func(self):
        if self.TakeDaily:
            if Timer < self.Interval:
                pass
            else:
                self.Timer.val = 0.0
                self.TimeNextDose = self.TimeNextDose + self.IntervalGoal
                self.TimeLastDose = System.X
                self.Interval = self.TimeNextDose - System.X
                ThiazideGILumen.Mass = ThiazideGILumen.Mass + self.Dose
                self.TotalDoses = self.TotalDoses + 1.0
                self.CumulativeDose = self.CumulativeDose + self.Dose
        else:
            pass

    def Reset_func(self):
        self.TimeLastDose = 0
        self.TotalDoses = 0.0
        self.CumulativeDose = 0.0

class ThiazidePool:
    def __init__(self):
        self.conc_Thiazide = None
        self.Gain = None
        self.Loss = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Thiazide = self.Mass / ECFV.Vol_L

    def Dervs_func(self):
        self.Gain = ThiazideGILumen.Loss
        self.Loss = ThiazideKidney.UrineLoss
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 1.0)


class ThiazideSingleDose:
    def __init__(self):
        self.Dose = 0.0
        self.TimeLastDose = 0
        self.TotalDoses = 0.0
        self.CumulativeDose = 0.0

    def TakeDoseNow_func(self):
        ThiazideGILumen.Mass = ThiazideGILumen.Mass + self.Dose
        self.TimeLastDose = System.X
        self.TotalDoses = self.TotalDoses + 1.0
        self.CumulativeDose = self.CumulativeDose + self.Dose

    def Reset_func(self):
        self.TimeLastDose = 0
        self.TotalDoses = 0.0
        self.CumulativeDose = 0.0

class CoronarySinus:

    def Calc_func(self):
        pass

class CardiacOutput:
    def __init__(self):
        self.Flow = None
        self.StrokeVolume = None
        self.Flow_LperMin = None
        self.CardiacIndex = None

    def Calc_func(self):
        self.StrokeVolume = LeftHeartPumping_Pumping.StrokeVolume
        self.Flow = LeftHeartPumping_Pumping.BloodFlow
        self.Flow_LperMin = self.Flow / 1000.0
        self.CardiacIndex = self.Flow_LperMin / SurfaceArea.Area

class Viscosity:
    def __init__(self):
        self.Value = None
        self.ConductanceEffect = None
        self.Clamp = False
        self.Level = 0.0

    def HctOnVisc_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.44, 0.8], [0.5, 1.0, 5.0], [0.8, 3.0, 30.0])

    def Calc_func(self):
        if self.Clamp:
            self.Value = self.Level
        else:
            self.Value = self.HctOnVisc_curve( BloodVol.Hct )

        self.ConductanceEffect = ( 1 / self.Value )

class CarotidSinus:
    def __init__(self):
        self.Pressure = None
        self.Switch = False
        self.Level = 0.0

    def Calc_func(self):
        if self.Switch:
            self.Pressure = self.Level
        else:
            self.Pressure = RegionalPressure.Carotid


class VeinsVol:
    def __init__(self):
        self.Vol = None
        self.Vol_L = None

    def Calc_func(self):
        self.Vol = SystemicVeins.Vol + SplanchnicVeins.Vol + RightAtrium.Vol + RightVentricle.Vol + PulmArty.Vol + BVSeqVeins.Vol
        self.Vol_L = self.Vol / 1000.0

class Circulation:
    def __init__(self):
        pass
    
class OrganFlow:
    def __init__(self):
        self.PeripheralFlow = None
        self.HepaticVeinFlow = None

    def Calc_func(self):
        self.PeripheralFlow = A_VFistula_Flow.BloodFlow + Bone_Flow.BloodFlow + Brain_Flow.BloodFlow + Fat_Flow.BloodFlow + Kidney_Flow.BloodFlow + LeftHeart_Flow.BloodFlow + OtherTissue_Flow.BloodFlow + RespiratoryMuscle_Flow.BloodFlow + RightHeart_Flow.BloodFlow + SkeletalMuscle_Flow.BloodFlow + Skin_Flow.BloodFlow
        self.HepaticVeinFlow = GITract_Flow.BloodFlow + HepaticArty.Flow

class ArtysVol:
    def __init__(self):
        self.Vol = None
        self.Vol_L = None

    def Calc_func(self):
        self.Vol = PulmCapys.Vol + PulmVeins.Vol + LeftAtrium.Vol + LeftVentricle.Vol + SystemicArtys.Vol + BVSeqArtys.Vol
        self.Vol_L = self.Vol / 1000.0

class CircyManager:
    def __init__(self):
        pass
    
class HepaticArty:
    def __init__(self):
        self.PressureGradient = None
        self.Flow = None
        self.Conductance = None
        self.BasicConductance = 2.8

    def CalcFlow_func(self):
        self.PressureGradient = SystemicArtys.Pressure - SplanchnicVeins.Pressure
        self.Conductance = self.BasicConductance
        self.Flow = self.PressureGradient * self.Conductance

class PeripheralResistance:
    def __init__(self):
        self.TPR = None

    def Wrapup_func(self):
        if CardiacOutput.Flow > 0.0:
            self.TPR = ( SystemicArtys.Pressure - RightAtrium.Pressure ) / CardiacOutput.Flow
        else:
            self.TPR = None


class GILumen:

    def Conc_func(self):
        GILumenElectrolytes.Conc_func()
        GILumenFood.Conc_func()
        GILumenH2O.Conc_func()

    def Dervs_func(self):
        GILumenOther.Dervs_func()
        GILumenElectrolytes.Dervs_func()
        GILumenFood.Dervs_func()
        GILumenH2O.Dervs_func()

class GILumenSodium:
    def __init__(self):
        self.Intake = None
        self.Absorption = None
        self.Diarrhea = None
        self.conc_Na_ = None
        self.conc_Na__mEqperL = None
        self.Perm = 0.0015
        self.Mass = 80.0

    def Conc_func(self):
        self.conc_Na_ = self.Mass / GILumenVolume.Mass
        self.conc_Na__mEqperL = 1000.0 * self.conc_Na_

    def Dervs_func(self):
        self.Intake = DietIntakeElectrolytes.Na__mEqperMin
        self.Absorption = self.Perm * self.Mass
        self.Diarrhea = GILumenDiarrhea.Na_Loss
        self.Change = self.Intake - self.Absorption - self.Diarrhea
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.8)


class GILumenPotassium:
    def __init__(self):
        self.Intake = None
        self.Absorption = None
        self.conc_K_ = None
        self.conc_K__mEqperL = None
        self.Perm = 0.002
        self.Mass = 25.0

    def Conc_func(self):
        self.conc_K_ = self.Mass / GILumenVolume.Mass
        self.conc_K__mEqperL = 1000.0 * self.conc_K_

    def Dervs_func(self):
        self.Intake = DietIntakeElectrolytes.K__mEqperMin
        self.Absorption = self.Perm * self.Mass
        self.Change = self.Intake - self.Absorption
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.25)


class GILumenChloride:
    def __init__(self):
        self.Intake = None
        self.Absorption = None
        self.Vomitus = None
        self.conc_Cl_ = None
        self.conc_Cl__mEqperL = None
        self.Perm = 0.0015
        self.Mass = 90.0

    def Conc_func(self):
        self.conc_Cl_ = self.Mass / GILumenVolume.Mass
        self.conc_Cl__mEqperL = 1000.0 * self.conc_Cl_

    def Dervs_func(self):
        self.Intake = DietIntakeElectrolytes.Cl__mEqperMin
        self.Absorption = self.Perm * self.Mass
        self.Vomitus = GILumenVomitus.Cl_Loss
        self.Change = self.Intake - self.Absorption - self.Vomitus
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.9)


class GILumenElectrolytes:

    def Conc_func(self):
        GILumenChloride.Conc_func()
        GILumenPotassium.Conc_func()
        GILumenSodium.Conc_func()

    def Dervs_func(self):
        GILumenChloride.Dervs_func()
        GILumenPotassium.Dervs_func()
        GILumenSodium.Dervs_func()

class GILumenVolume:
    def __init__(self):
        self.InitialMass = None
        self.Mass_L = None
        self.Intake = None
        self.Absorption = None
        self.Vomitus = None
        self.Diarrhea = None
        self.conc_OsmNa = None
        self.conc_OsmK = None
        self.conc_Osm = None
        self.conc_Fiber = 0.043
        self.Perm = 150.0

    def Initialize_func(self):
        self.InitialMass = 1000.0
        self.Mass = self.InitialMass

    def Conc_func(self):
        self.Mass_L = self.Mass / 1000.0

    def Dervs_func(self):
        self.conc_OsmNa = 2 * GILumenSodium.conc_Na_
        self.conc_OsmK = 2 * GILumenPotassium.conc_K_
        self.conc_Osm = self.conc_OsmNa + self.conc_OsmK + self.conc_Fiber
        self.Intake = DietIntakeH2O.Rate_mLperMin
        self.Absorption = self.Perm * ( OsmBody.conc_Osm_CellWall - self.conc_Osm )
        self.Vomitus = GILumenVomitus.H2OLoss
        self.Diarrhea = GILumenDiarrhea.H2OLoss
        self.Change = self.Intake - self.Absorption - self.Vomitus - self.Diarrhea
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 10.0)


class GILumenH2O:

    def Conc_func(self):
        GILumenVolume.Conc_func()
        GILumenTemperature.Conc_func()

    def Dervs_func(self):
        GILumenVolume.Dervs_func()
        GILumenTemperature.Dervs_func()

class GILumenTemperature:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.Intake = None
        self.Absorption = None
        self.Vomitus = None
        self.Diarrhea = None
        self.DegK = None
        self.DegC = None
        self.DegF = None
        self.Conduction = None
        self.Convection = None
        self.Cond = 0.01
        self.Mass = 310.0

    def Conc_func(self):
        self.DegK = 1000.0 * self.Mass / GILumenVolume.Mass
        self.DegC = self.DegK - 273.15
        self.DegF = ( 9 / 5 ) * self.DegC + 32

    def Dervs_func(self):
        self.Conduction = self.Cond * ( self.DegK - HeatCore.Temp_K )
        self.Convection = SpecificHeat.Water_kCalperG * self.DegK * GILumenVolume.Absorption
        self.Intake = SpecificHeat.Water_kCalperG * DietGoalH2O.DegK * GILumenVolume.Intake
        self.Absorption = self.Conduction + self.Convection
        self.Vomitus = GILumenVomitus.HeatLoss
        self.Diarrhea = GILumenDiarrhea.HeatLoss
        self.Gain = self.Intake
        self.Loss = self.Absorption + self.Vomitus + self.Diarrhea
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 1.6)


class GILumenDiarrhea:
    def __init__(self):
        self.H2OTarget = 0.0
        self.H2OLoss = None
        self.Na_Loss = None
        self.HeatLoss = None

    def H2OMassEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 50.0], [0.0, 1.0], [0.0, 0.0])

    def Dervs_func(self):
        self.H2OLoss = self.H2OTarget * self.H2OMassEffect_curve( GILumenVolume.Mass )
        self.Na_Loss = self.H2OLoss * GILumenSodium.conc_Na_
        self.HeatLoss = SpecificHeat.Water_kCalperG * self.H2OLoss * GILumenTemperature.DegK

class GILumenVomitus:
    def __init__(self):
        self.H2OTarget = 0.0
        self.H2OLoss = None
        self.Cl_Loss = None
        self.HeatLoss = None

    def H2OMassEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 50.0], [0.0, 1.0], [0.0, 0.0])

    def Dervs_func(self):
        self.H2OLoss = self.H2OTarget * self.H2OMassEffect_curve( GILumenVolume.Mass )
        self.Cl_Loss = self.H2OLoss * GILumenChloride.conc_Cl_
        self.HeatLoss = SpecificHeat.Water_kCalperG * self.H2OLoss * GILumenTemperature.DegK

class GILumenOther:

    def Dervs_func(self):
        GILumenDiarrhea.Dervs_func()
        GILumenVomitus.Dervs_func()

class GILumenCarbohydrates:
    def __init__(self):
        self.Intake = None
        self.Absorption = None
        self.conc_Carbo = None
        self.Transporter = 1.0
        self.Mass = 1930.0

    def AbsorptionSaturation_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1900.0, 6000.0], [0.0, 150.0, 600.0], [0.0, 0.08, 0.0])

    def Conc_func(self):
        self.conc_Carbo = self.Mass / GILumenVolume.Mass

    def Dervs_func(self):
        self.Intake = DietIntakeNutrition.Carbo_mGperMin
        self.Absorption = self.Transporter * self.AbsorptionSaturation_curve( self.Mass )
        self.Change = self.Intake - self.Absorption
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 19.3)


class GILumenFood:

    def Conc_func(self):
        GILumenCarbohydrates.Conc_func()
        GILumenFat.Conc_func()
        GILumenProtein.Conc_func()

    def Dervs_func(self):
        GILumenCarbohydrates.Dervs_func()
        GILumenFat.Dervs_func()
        GILumenProtein.Dervs_func()

class GILumenProtein:
    def __init__(self):
        self.Intake = None
        self.Absorption = None
        self.conc_Protein = None
        self.Perm = 0.05
        self.Mass = 1600.0

    def Conc_func(self):
        self.conc_Protein = self.Mass / GILumenVolume.Mass

    def Dervs_func(self):
        self.Intake = DietIntakeNutrition.Protein_mGperMin
        self.Absorption = self.Mass * self.Perm
        self.Change = self.Intake - self.Absorption
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 16.0)


class GILumenFat:
    def __init__(self):
        self.Intake = None
        self.Absorption = None
        self.conc_Fat = None
        self.Perm = 0.03
        self.Mass = 1990.0

    def Conc_func(self):
        self.conc_Fat = self.Mass / GILumenVolume.Mass

    def Dervs_func(self):
        self.Intake = DietIntakeNutrition.Fat_mGperMin
        self.Absorption = self.Perm * self.Mass
        self.Change = self.Intake - self.Absorption
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 19.9)


class GITract_Pressure:
    def __init__(self):
        self.ArtyPressure = None
        self.VeinPressure = None
        self.PressureGradient = None
        self.PumpSwitch = False
        self.PumpSetting = 0.0

    def Calc_func(self):
        if self.PumpSwitch:
            self.ArtyPressure = self.PumpSetting
        else:
            self.ArtyPressure = SystemicArtys.Pressure

        self.VeinPressure = SplanchnicVeins.Pressure
        self.PressureGradient = ( max( ( self.ArtyPressure - self.VeinPressure ), 0.0) )

class GITract:
    def __init__(self):
        pass
    
class GITract_Structure:
    def __init__(self):
        self.PhEffect = None
        self.FuelEffect = None
        self.TemperatureEffect = None
        self.Effect = 1.0

    def PhOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [6.5, 6.6], [0.1, 0.0], [0.0, 0.0])

    def FuelOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [0.5, 0.8], [0.05, 0.0], [0.0, 0.0])

    def TemperatureOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [44.0, 46.0], [0.0, 0.05], [0.0, 0.0])

    def Calc_func(self):
        self.PhEffect = self.PhOnStructure_curve( GITract_Ph.Ph )
        self.FuelEffect = self.FuelOnStructure_curve( GITract_Fuel.FractUseDelay )
        self.TemperatureEffect = self.TemperatureOnStructure_curve( HeatCore.Temp_C )
        self.F1 = 0.0
        self.F2 = self.PhEffect + self.TemperatureEffect + self.FuelEffect
        self.Effect = backwardeuler( self.F1, self.F2, System.Dx, self.Effect, None)


class GITract_Metabolism:
    def __init__(self):
        self.TotalCalsUsed = None
        self.NormalCalsUsed = None
        self.InitialNormalCalsUsed = None
        self.NormalCalsUsed__CalperMinperG = 0.0718
        self.CalMultiplier = 1.0
        self.AerobicCals = None
        self.AnaerobicCals = None
        self.O2Need = None
        self.O2Lack = None

    def ScaleCals_func(self):
        self.InitialNormalCalsUsed = self.CalMultiplier * self.NormalCalsUsed__CalperMinperG * GITract_Size.InitialMass

    def CalcCals_func(self):
        self.NormalCalsUsed = self.CalMultiplier * self.NormalCalsUsed__CalperMinperG * GITract_Size.Mass
        self.TotalCalsUsed = self.NormalCalsUsed * Thyroid.Effect * HeatMetabolism.Core * GITract_Structure.Effect
        self.O2Need = Metabolism_Tools.CalToO2 * self.TotalCalsUsed

    def SplitCals_func(self):
        self.O2Lack = self.O2Need - GITract_Flow.O2Use
        self.AerobicCals = Metabolism_Tools.O2ToCal * GITract_Flow.O2Use
        self.AnaerobicCals = Metabolism_Tools.O2ToCal * self.O2Lack

class GITract_CO2:
    def __init__(self):
        self.conc_HCO3 = None
        self.conc_HCO3_mEqperL = None
        self.PCO2 = None
        self.InflowGas = None
        self.InflowBase = None
        self.OutflowBase = None
        self.conc_BloodHCO3 = None
        self.Outflow_0 = None
        self.K = None
        self.Alpha = None
        self.Mass = 17.6

    def CalcConc_func(self):
        self.conc_HCO3 = self.Mass / GITract_Size.LiquidVol
        self.conc_HCO3_mEqperL = 1000.0 * self.conc_HCO3
        Tissue_BaseToGas.conc_HCO3 = self.conc_HCO3
        Tissue_BaseToGas.conc_SID = GITract_Ph.conc_SID
        Tissue_BaseToGas.Calc_func()
        self.PCO2 = Tissue_BaseToGas.pCO2

    def CalcDervs_func(self):
        self.K = GITract_Flow.BloodFlow / GITract_Size.LiquidVol
        if System.Dx >=0:
            self.Alpha = 0.0
        elif ( self.K * System.Dx ) >= 100.0:
            self.Alpha = 4E-44
        elif True:
            self.Alpha = ( math.e ** ( - self.K * System.Dx ) )
        self.InflowGas = Metabolism_RespiratoryQuotient.RQ * GITract_Flow.O2Use
        self.InflowBase = CO2Tools.LitersToMols * self.InflowGas
        Blood_GasToBase.pCO2 = self.PCO2
        Blood_GasToBase.conc_SID = BloodIons.conc_SID
        Blood_GasToBase.Calc_func()
        self.conc_BloodHCO3 = Blood_GasToBase.conc_HCO3
        self.Outflow_0 = GITract_Flow.BloodFlow * ( self.conc_BloodHCO3 - CO2Artys.conc_HCO3 )
        self.OutflowBase = ( self.Alpha * self.Outflow_0 ) + ( ( 1 - self.Alpha ) * self.InflowBase )
        self.Change = self.InflowBase - self.OutflowBase
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.18)


class GITract_Fuel:
    def __init__(self):
        self.FADelivered = None
        self.GlucoseDelivered = None
        self.KR = 0.026
        self.Ratio = None
        self.FAFraction = None
        self.GlucoseFraction = None
        self.FA_GlucoseFraction = None
        self.LacFraction = None
        self.FAUsed_CalperMin = None
        self.AerobicGlucoseUsed_CalperMin = None
        self.AnaerobicGlucoseUsed_CalperMin = None
        self.LacUsed_CalperMin = None
        self.FAUsed_mGperMin = None
        self.AerobicGlucoseUsed_mGperMin = None
        self.AnaerobicGlucoseUsed_mGperMin = None
        self.LacUsed_mGperMin = None
        self.TotalGlucoseUsed_mGperMin = None
        self.AnaerobicGlucoseDelivered = None
        self.FAFractionalDelivery = None
        self.AerobicGlucoseFractionalDelivery = None
        self.AnaerobicGlucoseFractionalDelivery = None
        self.MinimumFractionalDelivery = None
        self.FractUseDelay = 1.0

    def LacFraction_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 100.0], [0.0, 0.3], [0.0, 0.0])

    def Dervs_func(self):
        self.FADelivered = ( max( ( FAPool.conc_FA * GITract_Flow.PlasmaFlow ), 0.0) )
        self.GlucoseDelivered = ( max( ( GlucosePool.conc_Glucose * GITract_Flow.PlasmaFlow ), 0.0) )
        self.LacFraction = self.LacFraction_curve( GITract_Lactate.conc_Lac__mGperdL )
        self.FA_GlucoseFraction = 1.0 - self.LacFraction
        self.Ratio = FAPool.conc_FA_mGperdL / GlucosePool.conc_Glucose_mGperdL
        self.FAFraction = self.FA_GlucoseFraction * ( self.Ratio / ( self.Ratio + self.KR ) )
        self.GlucoseFraction = self.FA_GlucoseFraction - self.FAFraction
        self.FAUsed_CalperMin = self.FAFraction * GITract_Metabolism.AerobicCals
        self.FAUsed_mGperMin = self.FAUsed_CalperMin * Metabolism_Tools.Fat_mGperCal
        self.AerobicGlucoseUsed_CalperMin = self.GlucoseFraction * GITract_Metabolism.AerobicCals
        self.AerobicGlucoseUsed_mGperMin = self.AerobicGlucoseUsed_CalperMin * Metabolism_Tools.CarboAerobic_mGperCal
        self.LacUsed_CalperMin = self.LacFraction * GITract_Metabolism.AerobicCals
        self.LacUsed_mGperMin = self.LacUsed_CalperMin * Metabolism_Tools.Lac__mGperCal
        self.AnaerobicGlucoseDelivered = self.GlucoseDelivered - self.AerobicGlucoseUsed_mGperMin
        self.AnaerobicGlucoseUsed_CalperMin = ( min( GITract_Metabolism.AnaerobicCals, self.AnaerobicGlucoseDelivered) )
        self.AnaerobicGlucoseUsed_mGperMin = self.AnaerobicGlucoseUsed_CalperMin * Metabolism_Tools.CarboAnaerobic_mGperCal
        self.TotalGlucoseUsed_mGperMin = self.AerobicGlucoseUsed_mGperMin + self.AnaerobicGlucoseUsed_mGperMin
        if self.FAUsed_mGperMin > 0.0:
            self.FAFractionalDelivery = ( min( ( self.FADelivered / self.FAUsed_mGperMin ), 1.0) )
        else:
            self.FAFractionalDelivery = 1.0

        if self.AerobicGlucoseUsed_mGperMin > 0.0:
            self.AerobicGlucoseFractionalDelivery = ( min( ( self.GlucoseDelivered / self.AerobicGlucoseUsed_mGperMin ), 1.0) )
        else:
            self.AerobicGlucoseFractionalDelivery = 1.0

        if self.AnaerobicGlucoseUsed_mGperMin > 0.0:
            self.AnaerobicGlucoseFractionalDelivery = ( min( ( self.AnaerobicGlucoseDelivered / self.AnaerobicGlucoseUsed_mGperMin ), 1.0) )
        else:
            self.AnaerobicGlucoseFractionalDelivery = 1.0

        self.MinimumFractionalDelivery = ( min( ( min( self.FAFractionalDelivery, self.AerobicGlucoseFractionalDelivery) ), self.AnaerobicGlucoseFractionalDelivery) )
        self.K = 0.5
        self.DxMax = 1.0
        self.FractUse = self.MinimumFractionalDelivery
        self.FractUseDelay = delay( self.K, self.FractUse, self.FractUseDelay, System.Dx, 0.01)


class GITract_Ph:
    def __init__(self):
        self.Ph = None
        self.conc_SID = None
        self.conc_SID_mEqperL = None

    def CalcSID_func(self):
        self.conc_SID = KCell.conc_K_ + CellSID.OtherCations - CellSID.StrongAnions - GITract_Lactate.conc_Lac_
        self.conc_SID_mEqperL = 1000.0 * self.conc_SID

    def CalcPh_func(self):
        PhCells.pCO2 = GITract_CO2.PCO2
        PhCells.SID = self.conc_SID_mEqperL
        PhCells.Calc_func()
        self.Ph = PhCells.pH

class GITract_Function:
    def __init__(self):
        self.Failed = False
        self.Effect = None
        self.PhEffect = None
        self.ProteinEffect = None
        self.FuelEffect = None
        self.TemperatureEffect = None

    def PhOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [6.6, 6.7], [0.0, 1.0], [0.0, 0.0])

    def ProteinOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [3000.0, 5200.0], [0.0, 1.0], [0.0, 0.0])

    def FuelOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.9], [0.0, 1.0], [0.0, 0.0])

    def TemperatureOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 37.0, 40.0, 46.0], [0.0, 1.0, 1.5, 0.0], [0.0, 0.12, 0.0, 0.0])

    def Calc_func(self):
        self.PhEffect = self.PhOnFunction_curve( GITract_Ph.Ph )
        self.ProteinEffect = self.ProteinOnFunction_curve( CellProtein.Mass_G )
        self.FuelEffect = self.FuelOnFunction_curve( GITract_Fuel.FractUseDelay )
        self.TemperatureEffect = self.TemperatureOnFunction_curve( HeatCore.Temp_C )
        self.Effect = self.PhEffect * self.ProteinEffect * self.FuelEffect * self.TemperatureEffect * GITract_Structure.Effect

    def Wrapup_func(self):
        if not self.Failed and ( self.Effect < 0.2 ):
            self.Failed = True
        elif self.Failed and ( self.Effect > 0.4 ):
            self.Failed = False

class GITract_Size:
    def __init__(self):
        self.Vol = None
        self.Mass = None
        self.InitialMass = None
        self.Density = None
        self.LiquidMass = None
        self.LiquidDensity = 1.00
        self.LiquidVol = None
        self.InitialLiquidVol = None
        self.SolidMass = None
        self.InitialSolidMass = None
        self.SolidDensity = 1.17
        self.SolidVol = None
        self.FractTotal = None
        self.IFV = None
        self.InitialIFV = None
        self.CellH2O = None
        self.InitialCellH2O = None
        self.MassFractBase = 0.0578
        self.H2OFractMass = 0.67
        self.SolidsFractMass = None

    def Initialize_func(self):
        self.InitialMass = self.MassFractBase * Weight.InitialOtherMass
        self.InitialLiquidVol = self.H2OFractMass * self.InitialMass / self.LiquidDensity
        self.SolidsFractMass = 1.0 - self.H2OFractMass
        self.InitialSolidMass = self.SolidsFractMass * self.InitialMass

    def ScaleH2O_func(self):
        self.FractTotal = self.InitialLiquidVol / TissueH2O.InitialVol
        self.InitialIFV = self.FractTotal * InterstitialWater.InitialVol
        self.InitialCellH2O = self.FractTotal * CellH2O.InitialVol

    def Calc_func(self):
        self.IFV = self.FractTotal * InterstitialWater.Vol
        self.CellH2O = self.FractTotal * CellH2O.Vol
        self.LiquidVol = self.IFV + self.CellH2O
        self.LiquidMass = self.LiquidVol * self.LiquidDensity
        self.SolidMass = self.InitialSolidMass
        self.SolidVol = self.SolidMass / self.SolidDensity
        self.Mass = self.LiquidMass + self.SolidMass
        self.Vol = self.LiquidVol + self.SolidVol
        self.Density = self.Mass / self.Vol

class GITract_AlphaReceptors:
    def __init__(self):
        self.Activity = None
        self.TotalAgonism = None
        self.NeuralAgonism = None
        self.HumoralAgonism = None
        self.Switch = False
        self.Setting = 0.0
        self.NEURALK = 0.333
        self.HUMORALK = 0.5

    def Calc_func(self):
        self.NeuralAgonism = GangliaGeneral.NA_Hz
        self.HumoralAgonism = AlphaPool.Effect
        self.TotalAgonism = ( self.NEURALK * self.NeuralAgonism ) + ( self.HUMORALK * self.HumoralAgonism )
        if self.Switch:
            self.Activity = self.Setting
        else:
            self.Activity = self.TotalAgonism * AlphaBlockade.Effect


class GITract_Vasculature:
    def __init__(self):
        self.Tau = 30.0
        self.Effect = 1.0

    def PO2OnStimulus_curve(self, x):
        return cubic_hermite_spline(x, [41.0, 51.0, 61.0], [1.2, 1.0, 0.8], [0.0, -0.03, 0.0])

    def Parms_func(self):
        self.K = 1.0 / ( self.Tau * 1440.0 )

    def Calc_func(self):
        if GITract_Function.Failed:
            self.Stimulus = 0.0
        else:
            self.Stimulus = self.PO2OnStimulus_curve( GITract_Flow.PO2 )

        self.Effect = delay( self.K, self.Stimulus, self.Effect, System.Dx, None)


class GITract_Flow:
    def __init__(self):
        self.Conductance = None
        self.BasicConductance = 11.2
        self.A2Effect = None
        self.SympsEffect = None
        self.ADHEffect = None
        self.PO2Effect = None
        self.AerobicFraction = None
        self.O2Use = None
        self.conc_O2 = None
        self.BloodFlow = None
        self.PlasmaFlow = None
        self.PO2 = 54.0
    def A2OnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.3, 3.5], [1.05, 1.0, 0.5], [0.0, -0.08, 0.0])

    def SympsOnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.0, 5.0], [1.3, 1.0, 0.1], [0.0, -0.3, 0.0])

    def PO2OnConductance_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 30.0], [2.0, 1.0], [0.0, 0.0])

    def ADHOnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.8, 3.0], [1.0, 0.1], [0.0, 0.0])

    def PO2OnAerobicFraction_curve(self, x):
        return cubic_hermite_spline(x, [2.0, 10.0], [0.0, 1.0], [0.0, 0.0])

    def Calc_func(self):
        self.A2Effect = self.A2OnConductance_curve( A2Pool.Log10Conc )
        self.SympsEffect = self.SympsOnConductance_curve( GITract_AlphaReceptors.Activity )
        self.ADHEffect = self.ADHOnConductance_curve( ADHPool.Log10Conc )
        self.SearchMax = PO2Artys.Pressure

        def PO2implicitfunc(PO2):
            self.PO2Effect = self.PO2OnConductance_curve( PO2 )
            self.Conductance = self.BasicConductance * self.A2Effect * self.SympsEffect * self.PO2Effect * self.ADHEffect * Viscosity.ConductanceEffect * Anesthesia.VascularConductance * GITract_Vasculature.Effect
            self.BloodFlow = ( max( ( GITract_Pressure.PressureGradient * self.Conductance ), 0.0) )
            self.AerobicFraction = self.PO2OnAerobicFraction_curve( PO2 )
            self.O2Use = GITract_Metabolism.O2Need * self.AerobicFraction
            if self.BloodFlow > 0.0:
                self.conc_O2 = O2Artys.conc_O2 - ( self.O2Use / self.BloodFlow )
            else:
                self.conc_O2 = 0.0

            HgbTissue.conc_O2 = self.conc_O2
            HgbTissue.O2ToPO2_func()
            PO2End = HgbTissue.pO2

            return PO2End
        self.PO2 = impliciteq( PO2implicitfunc, self.PO2, 0.54)
        self.PlasmaFlow = self.BloodFlow * BloodVol.PVCrit

class GITract_Lactate:
    def __init__(self):
        self.conc_Lac_ = None
        self.conc_Lac__mEqperL = None
        self.conc_Lac__mGperdL = None
        self.DC = 180.0
        self.Made = None
        self.Made_mGperMin = None
        self.Used = None
        self.Used_mGperMin = None
        self.Outflux = None
        self.Outflux_0 = None
        self.K = None
        self.Alpha = None
        self.MEQ_ML_TO_MG_DL = 9008.0
        self.GLUCOSE_TO_LACTATE = 0.99
        self.MG_TO_MEQ = 0.0112
        self.Mass = 1.10

    def CalcConc_func(self):
        self.conc_Lac_ = self.Mass / GITract_Size.LiquidVol
        self.conc_Lac__mEqperL = 1000.0 * self.conc_Lac_
        self.conc_Lac__mGperdL = self.MEQ_ML_TO_MG_DL * self.conc_Lac_

    def CalcDervs_func(self):
        self.Made_mGperMin = self.GLUCOSE_TO_LACTATE * GITract_Fuel.AnaerobicGlucoseUsed_mGperMin
        self.Made = self.MG_TO_MEQ * self.Made_mGperMin
        self.Used_mGperMin = GITract_Fuel.LacUsed_mGperMin
        self.Used = self.MG_TO_MEQ * self.Used_mGperMin
        self.K = self.DC / GITract_Size.LiquidVol
        if System.Dx >=0:
            self.Alpha = 0.0
        elif ( self.K * System.Dx ) >= 100.0:
            self.Alpha = 4E-44
        elif True:
            self.Alpha = ( math.e ** ( - self.K * System.Dx ) )
        self.Outflux_0 = self.DC * ( self.conc_Lac_ - LacPool.conc_Lac_ )
        self.Outflux = ( self.Alpha * self.Outflux_0 ) + ( ( 1 - self.Alpha ) * ( self.Made + self.Used ) )
        self.Change = self.Made - self.Used - self.Outflux
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.011)


class AldoSecretion:
    def __init__(self):
        self.Rate = None
        self.Base = 330.0
        self.conc_A2Effect = None
        self.conc_K_Effect = None
        self.Clamp = False
        self.Level = 0.0

    def conc_A2Effect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.3, 4.0], [0.4, 1.0, 4.0], [0.0, 1.0, 0.0])

    def conc_K_Effect_curve(self, x):
        return cubic_hermite_spline(x, [3.0, 4.4, 6.0], [0.3, 1.0, 3.0], [0.0, 1.0, 0.0])

    def Dervs_func(self):
        self.conc_A2Effect = self.conc_A2Effect_curve( A2Pool.Log10Conc )
        self.conc_K_Effect = self.conc_K_Effect_curve( KPool.conc_K__mEqperL )
        if self.Clamp:
            self.Rate = self.Level
        else:
            self.Rate = ( self.Base * self.conc_A2Effect * self.conc_K_Effect * OtherTissue_Function.Effect ) + AldoTumor.SecretionRate


class AldoDisposal:
    def __init__(self):
        self.Rate = None
        self.Clearance = None
        self.ExtractK = 0.78
        self.Degradation = None
        self.DegradeK = 0.0007

    def Dervs_func(self):
        self.Clearance = self.ExtractK * AldoPool.conc_Aldo * OrganFlow.HepaticVeinFlow
        self.Degradation = self.DegradeK * AldoPool.Mass
        self.Rate = self.Clearance + self.Degradation

class AldoPool:
    def __init__(self):
        self.conc_Aldo = None
        self.conc_Aldo_pMolperL = None
        self.conc_Aldo_nGperdL = None
        self.PMOLTONG = 0.0360
        self.Gain = None
        self.Loss = None
        self.Targetconc_Aldo = 0.330
        self.InitialMass = None

    def Init_func(self):
        self.InitialMass = self.Targetconc_Aldo * BodyH2O.InitialVol
        self.Mass = self.InitialMass

    def CalcConc_func(self):
        self.conc_Aldo = self.Mass / BodyH2O.Vol
        self.conc_Aldo_pMolperL = 1000.0 * self.conc_Aldo
        self.conc_Aldo_nGperdL = self.PMOLTONG * self.conc_Aldo_pMolperL

    def Dervs_func(self):
        self.Gain = AldoSecretion.Rate + AldoPump.Rate
        self.Loss = AldoDisposal.Rate
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 142.0)


class AldoTumor:
    def __init__(self):
        self.SecretionRate = 0.0
    
class AldoPump:
    def __init__(self):
        self.Switch = False
        self.Setting = 0.0
        self.Rate = None

    def Dervs_func(self):
        self.Rate = self.Switch * self.Setting

class Aldosterone:

    def CalcConc_func(self):
        AldoPool.CalcConc_func()

    def Dervs_func(self):
        AldoPump.Dervs_func()
        AldoSecretion.Dervs_func()
        AldoDisposal.Dervs_func()
        AldoPool.Dervs_func()

class PO2Veins:
    def __init__(self):
        self.Pressure = 40.0
        self.Sat_percent = None

    def Calc_func(self):
        HgbTissue.conc_O2 = O2Veins.conc_O2
        HgbTissue.O2ToPO2_func()
        self.Pressure = HgbTissue.pO2
        HgbConc.conc_O2 = O2Veins.conc_O2
        HgbConc.Sat_percent_func()
        self.Sat_percent = HgbConc.Sat_percent

    def ForDisplay_func(self):
        HgbTissue.pO2 = self.Pressure
        HgbTissue.PO2ToO2_func()
        O2Veins.conc_O2 = HgbTissue.conc_O2

class O2Total:
    def __init__(self):
        self.Inflow = None
        self.Outflow = None

    def Dervs_func(self):
        self.Inflow = LungO2.Uptake
        self.Outflow = Bone_Flow.O2Use + Brain_Flow.O2Use + Fat_Flow.O2Use + GITract_Flow.O2Use + Kidney_O2.O2Use + LeftHeart_Flow.O2Use + Liver_O2.O2Use + OtherTissue_Flow.O2Use + RespiratoryMuscle_Flow.O2Use + RightHeart_Flow.O2Use + SkeletalMuscle_Flow.O2Use + Skin_Flow.O2Use

class O2Artys:
    def __init__(self):
        self.Mass = None
        self.conc_O2 = 0.196

    def CalcConc_func(self):
        self.Mass = self.conc_O2 * ArtysVol.Vol

    def Dervs_func(self):
        self.K = 5.0
        self.DxMax = 0.5 * ( ( 1 / self.K ) )
        if CardiacOutput.Flow > 0.0:
            self.conc_O2_SteadyState = O2Veins.conc_O2 + ( O2Total.Inflow / CardiacOutput.Flow )
        else:
            self.conc_O2_SteadyState = 0.0

        self.conc_O2 = delay( self.K, self.conc_O2_SteadyState, self.conc_O2, System.Dx, 0.002)


class PO2Artys:
    def __init__(self):
        self.Pressure = None
        self.Sat_percent = None

    def Calc_func(self):
        HgbLung.conc_O2 = O2Artys.conc_O2
        HgbLung.O2ToPO2_func()
        self.Pressure = HgbLung.pO2
        HgbConc.conc_O2 = O2Artys.conc_O2
        HgbConc.Sat_percent_func()
        self.Sat_percent = HgbConc.Sat_percent

    def ForDisplay_func(self):
        HgbLung.pO2 = self.Pressure
        HgbLung.PO2ToO2_func()
        O2Artys.conc_O2 = HgbLung.conc_O2

class O2Veins:
    def __init__(self):
        self.Mass = None
        self.conc_O2 = 0.157

    def CalcConc_func(self):
        self.Mass = self.conc_O2 * VeinsVol.Vol

    def Dervs_func(self):
        self.K = 5.0
        self.DxMax = 0.5 * ( ( 1 / self.K ) )
        if CardiacOutput.Flow > 0.0:
            self.conc_O2_SteadyState = O2Artys.conc_O2 - ( O2Total.Outflow / CardiacOutput.Flow )
        else:
            self.conc_O2_SteadyState = 0.0

        self.conc_O2 = delay( self.K, self.conc_O2_SteadyState, self.conc_O2, System.Dx, 0.0015)


class O2:

    def CalcConc_func(self):
        O2Artys.CalcConc_func()
        O2Veins.CalcConc_func()

    def CalcPO2_func(self):
        PO2Artys.Calc_func()
        PO2Veins.Calc_func()

    def Dervs_func(self):
        O2Total.Dervs_func()
        O2Artys.Dervs_func()
        O2Veins.Dervs_func()

class SweatDuct:
    def __init__(self):
        self.FractReabBasic = 0.8
        self.FractReab = None
        self.FractReabK = None
        self.AldoEffect = None
        self.H2OInflow = None
        self.H2OReab = None
        self.H2OOutflow = None
        self.NaInflow = None
        self.NaReab = None
        self.NaOutflow = None
        self.KInflow = None
        self.KReab = None
        self.KOutflow = None
        self.ClInflow = None
        self.ClReab = None
        self.ClOutflow = None
        self.conc_Na_In = None
        self.conc_Na_Out = None
        self.conc_K_In = None
        self.conc_K_Out = None
        self.conc_Cl_In = None
        self.conc_Cl_Out = None

    def AldoEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 12.0, 100.0], [0.5, 1.0, 2.0], [0.0, 0.03, 0.0])

    def Parms_func(self):
        self.FractReabK = ( math.log( ( self.FractReabBasic ) ) ) / 15.0

    def FractReab_func(self):
        self.FractReab = ( math.e ** ( self.FractReabK * self.H2OInflow / self.AldoEffect ) )

    def Calc_func(self):
        self.H2OInflow = SweatGland.H2ORate
        self.AldoEffect = self.AldoEffect_curve( AldoPool.conc_Aldo_nGperdL )
        self.FractReab_func()
        self.H2OReab = 0.0
        self.H2OOutflow = self.H2OInflow - self.H2OReab
        self.NaInflow = SweatGland.NaRate
        self.NaReab = self.FractReab * self.NaInflow
        self.NaOutflow = self.NaInflow - self.NaReab
        self.KInflow = SweatGland.KRate
        self.KReab = 0.0
        self.KOutflow = self.KInflow - self.KReab
        self.ClInflow = SweatGland.ClRate
        self.ClReab = self.FractReab * self.ClInflow
        self.ClOutflow = self.ClInflow - self.ClReab
        self.conc_Na_In = SweatGland.conc_Na_
        self.conc_K_In = SweatGland.conc_K_
        self.conc_Cl_In = SweatGland.conc_Cl_
        if self.H2OOutflow > 0.0:
            self.conc_Na_Out = self.NaOutflow / self.H2OOutflow
            self.conc_K_Out = self.KOutflow / self.H2OOutflow
            self.conc_Cl_Out = self.ClOutflow / self.H2OOutflow
        else:
            self.conc_Na_Out = self.conc_Na_In
            self.conc_K_Out = self.conc_K_In
            self.conc_Cl_Out = self.conc_Cl_In

class Sweat:

    def Parms_func(self):
        SweatAcclimation.Parms_func()
        SweatDuct.Parms_func()

    def Calc_func(self):
        SweatGland.Calc_func()
        SweatDuct.Calc_func()

    def Dervs_func(self):
        SweatAcclimation.Dervs_func()
        SweatFuel.Dervs_func()

class SweatGland:
    def __init__(self):
        self.H2ORate = None
        self.H2ORateBasic = 1.0
        self.NaRate = None
        self.KRate = None
        self.ClRate = None
        self.conc_Na_ = None
        self.conc_K_ = None
        self.conc_Cl_ = None
        self.NerveEffect = None
        self.FuelEffect = None
        self.AcclimationEffect = None
        self.SkinFunctionEffect = None
        self.ClampSwitch = False
        self.ClampLevel = 0.0

    def NerveEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 4.0], [0.0, 30.0], [0.0, 0.0])

    def Calc_func(self):
        self.NerveEffect = self.NerveEffect_curve( HypothalamusSweating.NerveActivity )
        self.FuelEffect = SweatFuel.Mass
        self.AcclimationEffect = SweatAcclimation.Effect
        self.SkinFunctionEffect = Skin_Function.Effect
        if self.ClampSwitch:
            self.H2ORate = self.ClampLevel
        else:
            self.H2ORate = self.NerveEffect * self.FuelEffect * self.AcclimationEffect * self.SkinFunctionEffect * self.H2ORateBasic

        self.conc_Na_ = NaPool.conc_Na_
        self.conc_K_ = KPool.conc_K_
        self.conc_Cl_ = ClPool.conc_Cl_
        self.NaRate = self.conc_Na_ * self.H2ORate
        self.KRate = self.conc_K_ * self.H2ORate
        self.ClRate = self.conc_Cl_ * self.H2ORate

class SweatFuel:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.UseK = 0.0004
        self.RefillK = 0.004
        self.MassEffect = None
        self.Mass = 1.0

    def MassEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.9, 1.0], [1.0, 0.0], [0.0, 0.0])

    def Dervs_func(self):
        self.MassEffect = self.MassEffect_curve( self.Mass )
        self.Gain = self.RefillK * self.MassEffect
        self.Loss = self.UseK * SweatGland.H2ORateBasic
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.01)


class SweatAcclimation:
    def __init__(self):
        self.BasicEffect = 1.0
        self.TemperatureEffect = None
        self.Tau = 6.0
        self.Effect = 1.0

    def TemperatureEffect_curve(self, x):
        return cubic_hermite_spline(x, [60.0, 85.0, 100.0], [0.5, 1.0, 2.0], [0.0, 0.05, 0.0])

    def Parms_func(self):
        self.K = ( 1 / ( self.Tau * 1440.0 ) )

    def Dervs_func(self):
        self.TemperatureEffect = self.TemperatureEffect_curve( HeatSkin.Temp_F )
        self.SteadyState = self.BasicEffect * self.TemperatureEffect
        self.Effect = delay( self.K, self.SteadyState, self.Effect, System.Dx, 0.01)


class Kidney_Alpha:
    def __init__(self):
        self.NA = 1.0
        self.PT_NA = 1.0
    
class Kidney_Size:
    def __init__(self):
        self.Vol = None
        self.Mass = None
        self.InitialMass = None
        self.Density = None
        self.LiquidMass = None
        self.LiquidDensity = 1.00
        self.LiquidVol = None
        self.InitialLiquidVol = None
        self.SolidMass = None
        self.InitialSolidMass = None
        self.SolidDensity = 1.17
        self.SolidVol = None
        self.FractTotal = None
        self.IFV = None
        self.InitialIFV = None
        self.CellH2O = None
        self.InitialCellH2O = None
        self.MassFractBase = 0.0116
        self.H2OFractMass = 0.67
        self.SolidsFractMass = None

    def Initialize_func(self):
        self.InitialMass = self.MassFractBase * Weight.InitialOtherMass
        self.InitialLiquidVol = self.H2OFractMass * self.InitialMass / self.LiquidDensity
        self.SolidsFractMass = 1.0 - self.H2OFractMass
        self.InitialSolidMass = self.SolidsFractMass * self.InitialMass

    def ScaleH2O_func(self):
        self.FractTotal = self.InitialLiquidVol / TissueH2O.InitialVol
        self.InitialIFV = self.FractTotal * InterstitialWater.InitialVol
        self.InitialCellH2O = self.FractTotal * CellH2O.InitialVol

    def Calc_func(self):
        self.IFV = self.FractTotal * InterstitialWater.Vol
        self.CellH2O = self.FractTotal * CellH2O.Vol
        self.LiquidVol = self.IFV + self.CellH2O
        self.LiquidMass = self.LiquidVol * self.LiquidDensity
        self.SolidMass = self.InitialSolidMass
        self.SolidVol = self.SolidMass / self.SolidDensity
        self.Mass = self.LiquidMass + self.SolidMass
        self.Vol = self.LiquidVol + self.SolidVol
        self.Density = self.Mass / self.Vol

class Kidney_Lactate:
    def __init__(self):
        self.conc_Lac_ = None
        self.conc_Lac__mEqperL = None
        self.conc_Lac__mGperdL = None
        self.DC = 20.0
        self.Made = None
        self.Made_mGperMin = None
        self.Used = None
        self.Used_mGperMin = None
        self.Outflux = None
        self.Outflux_0 = None
        self.K = None
        self.Alpha = None
        self.MEQ_ML_TO_MG_DL = 9008.0
        self.GLUCOSE_TO_LACTATE = 0.99
        self.MG_TO_MEQ = 0.0112
        self.Mass = 0.18

    def CalcConc_func(self):
        self.conc_Lac_ = self.Mass / Kidney_Size.LiquidVol
        self.conc_Lac__mEqperL = 1000.0 * self.conc_Lac_
        self.conc_Lac__mGperdL = self.MEQ_ML_TO_MG_DL * self.conc_Lac_

    def CalcDervs_func(self):
        self.Made_mGperMin = self.GLUCOSE_TO_LACTATE * Kidney_Fuel.AnaerobicGlucoseUsed_mGperMin
        self.Made = self.MG_TO_MEQ * self.Made_mGperMin
        self.Used_mGperMin = Kidney_Fuel.LacUsed_mGperMin
        self.Used = self.MG_TO_MEQ * self.Used_mGperMin
        self.K = self.DC / Kidney_Size.LiquidVol
        if System.Dx >=0:
            self.Alpha = 0.0
        elif ( self.K * System.Dx ) >= 100.0:
            self.Alpha = 4E-44
        elif True:
            self.Alpha = ( math.e ** ( - self.K * System.Dx ) )
        self.Outflux_0 = self.DC * ( self.conc_Lac_ - LacPool.conc_Lac_ )
        self.Outflux = ( self.Alpha * self.Outflux_0 ) + ( ( 1 - self.Alpha ) * ( self.Made + self.Used ) )
        self.Change = self.Made - self.Used - self.Outflux
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.0026)


class Kidney_O2:
    def __init__(self):
        self.Veinconc_O2 = None
        self.VeinPO2 = None
        self.O2Perm = None
        self.O2PermBasic = 0.9
        self.AerobicFraction = None
        self.HgbOnPerm = None
        self.O2Use = None
        self.TubulePO2 = 35.0
    def HgbOnPerm_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.15, 0.25], [0.4, 1.0, 2.0], [0.0, 8.0, 0.0])

    def PO2OnAerobicFraction_curve(self, x):
        return cubic_hermite_spline(x, [2.0, 20.0], [0.0, 1.0], [0.0, 0.0])

    def Calc_func(self):
        self.HgbOnPerm = self.HgbOnPerm_curve( HgbConc.conc_Free )
        self.O2Perm = self.HgbOnPerm * self.O2PermBasic
        self.SearchMax = PO2Artys.Pressure

        def TubulePO2implicitfunc(TubulePO2):
            self.AerobicFraction = self.PO2OnAerobicFraction_curve( TubulePO2 )
            self.O2Use = Kidney_Metabolism.O2Need * self.AerobicFraction
            if Kidney_Flow.BloodFlow > 0.0:
                self.Veinconc_O2 = O2Artys.conc_O2 - ( self.O2Use / Kidney_Flow.BloodFlow )
            else:
                self.Veinconc_O2 = 0.0

            HgbTissue.conc_O2 = self.Veinconc_O2
            HgbTissue.O2ToPO2_func()
            self.VeinPO2 = HgbTissue.pO2
            TubulePO2End = self.VeinPO2 - ( self.O2Use / self.O2Perm )

            return TubulePO2End
        self.TubulePO2 = impliciteq( TubulePO2implicitfunc, self.TubulePO2, 0.35)

class Kidney_MyogenicDelay:
    def __init__(self):
        self.PressureChange = 0.0

    def Dervs_func(self):
        self.K = 2.0
        self.DxMax = 0.2
        self.PressureChange_Steady_State = Kidney_Myogenic.PressureChange_Steady_State
        self.PressureChange = delay( self.K, self.PressureChange_Steady_State, self.PressureChange, System.Dx, 0.1)


class Kidney_Fuel:
    def __init__(self):
        self.FADelivered = None
        self.GlucoseDelivered = None
        self.KR = 0.026
        self.Ratio = None
        self.FAFraction = None
        self.GlucoseFraction = None
        self.FA_GlucoseFraction = None
        self.LacFraction = None
        self.FAUsed_CalperMin = None
        self.AerobicGlucoseUsed_CalperMin = None
        self.AnaerobicGlucoseUsed_CalperMin = None
        self.LacUsed_CalperMin = None
        self.FAUsed_mGperMin = None
        self.AerobicGlucoseUsed_mGperMin = None
        self.AnaerobicGlucoseUsed_mGperMin = None
        self.LacUsed_mGperMin = None
        self.TotalGlucoseUsed_mGperMin = None
        self.AnaerobicGlucoseDelivered = None
        self.FAFractionalDelivery = None
        self.AerobicGlucoseFractionalDelivery = None
        self.AnaerobicGlucoseFractionalDelivery = None
        self.MinimumFractionalDelivery = None
        self.FractUseDelay = 1.0

    def LacFraction_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 100.0], [0.0, 0.3], [0.0, 0.0])

    def Dervs_func(self):
        self.FADelivered = ( max( ( FAPool.conc_FA * Kidney_Flow.PlasmaFlow ), 0.0) )
        self.GlucoseDelivered = ( max( ( GlucosePool.conc_Glucose * Kidney_Flow.PlasmaFlow ), 0.0) )
        self.LacFraction = self.LacFraction_curve( Kidney_Lactate.conc_Lac__mGperdL )
        self.FA_GlucoseFraction = 1.0 - self.LacFraction
        self.Ratio = FAPool.conc_FA_mGperdL / GlucosePool.conc_Glucose_mGperdL
        self.FAFraction = self.FA_GlucoseFraction * ( self.Ratio / ( self.Ratio + self.KR ) )
        self.GlucoseFraction = self.FA_GlucoseFraction - self.FAFraction
        self.FAUsed_CalperMin = self.FAFraction * Kidney_Metabolism.AerobicCals
        self.FAUsed_mGperMin = self.FAUsed_CalperMin * Metabolism_Tools.Fat_mGperCal
        self.AerobicGlucoseUsed_CalperMin = self.GlucoseFraction * Kidney_Metabolism.AerobicCals
        self.AerobicGlucoseUsed_mGperMin = self.AerobicGlucoseUsed_CalperMin * Metabolism_Tools.CarboAerobic_mGperCal
        self.LacUsed_CalperMin = self.LacFraction * Kidney_Metabolism.AerobicCals
        self.LacUsed_mGperMin = self.LacUsed_CalperMin * Metabolism_Tools.Lac__mGperCal
        self.AnaerobicGlucoseDelivered = self.GlucoseDelivered - self.AerobicGlucoseUsed_mGperMin
        self.AnaerobicGlucoseUsed_CalperMin = ( min( Kidney_Metabolism.AnaerobicCals, self.AnaerobicGlucoseDelivered) )
        self.AnaerobicGlucoseUsed_mGperMin = self.AnaerobicGlucoseUsed_CalperMin * Metabolism_Tools.CarboAnaerobic_mGperCal
        self.TotalGlucoseUsed_mGperMin = self.AerobicGlucoseUsed_mGperMin + self.AnaerobicGlucoseUsed_mGperMin
        if self.FAUsed_mGperMin > 0.0:
            self.FAFractionalDelivery = ( min( ( self.FADelivered / self.FAUsed_mGperMin ), 1.0) )
        else:
            self.FAFractionalDelivery = 1.0

        if self.AerobicGlucoseUsed_mGperMin > 0.0:
            self.AerobicGlucoseFractionalDelivery = ( min( ( self.GlucoseDelivered / self.AerobicGlucoseUsed_mGperMin ), 1.0) )
        else:
            self.AerobicGlucoseFractionalDelivery = 1.0

        if self.AnaerobicGlucoseUsed_mGperMin > 0.0:
            self.AnaerobicGlucoseFractionalDelivery = ( min( ( self.AnaerobicGlucoseDelivered / self.AnaerobicGlucoseUsed_mGperMin ), 1.0) )
        else:
            self.AnaerobicGlucoseFractionalDelivery = 1.0

        self.MinimumFractionalDelivery = ( min( ( min( self.FAFractionalDelivery, self.AerobicGlucoseFractionalDelivery) ), self.AnaerobicGlucoseFractionalDelivery) )
        self.K = 0.5
        self.DxMax = 1.0
        self.FractUse = self.MinimumFractionalDelivery
        self.FractUseDelay = delay( self.K, self.FractUse, self.FractUseDelay, System.Dx, 0.01)


class Kidney:
    def __init__(self):
        pass
    
class Kidney_Ph:
    def __init__(self):
        self.Ph = None
        self.conc_SID = None
        self.conc_SID_mEqperL = None

    def CalcSID_func(self):
        self.conc_SID = KCell.conc_K_ + CellSID.OtherCations - CellSID.StrongAnions - Kidney_Lactate.conc_Lac_
        self.conc_SID_mEqperL = 1000.0 * self.conc_SID

    def CalcPh_func(self):
        PhCells.pCO2 = Kidney_CO2.PCO2
        PhCells.SID = self.conc_SID_mEqperL
        PhCells.Calc_func()
        self.Ph = PhCells.pH

class Kidney_Function:
    def __init__(self):
        self.Failed = False
        self.Effect = None
        self.PhEffect = None
        self.ProteinEffect = None
        self.FuelEffect = None
        self.TemperatureEffect = None

    def PhOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [6.6, 6.7], [0.0, 1.0], [0.0, 0.0])

    def ProteinOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [3000.0, 5200.0], [0.0, 1.0], [0.0, 0.0])

    def FuelOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.9], [0.0, 1.0], [0.0, 0.0])

    def TemperatureOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 37.0, 40.0, 46.0], [0.0, 1.0, 1.5, 0.0], [0.0, 0.12, 0.0, 0.0])

    def Calc_func(self):
        self.PhEffect = self.PhOnFunction_curve( Kidney_Ph.Ph )
        self.ProteinEffect = self.ProteinOnFunction_curve( CellProtein.Mass_G )
        self.FuelEffect = self.FuelOnFunction_curve( Kidney_Fuel.FractUseDelay )
        self.TemperatureEffect = self.TemperatureOnFunction_curve( HeatCore.Temp_C )
        self.Effect = self.PhEffect * self.ProteinEffect * self.FuelEffect * self.TemperatureEffect * Kidney_Structure.Effect

    def Wrapup_func(self):
        if not self.Failed and ( self.Effect < 0.2 ):
            self.Failed = True
        elif self.Failed and ( self.Effect > 0.4 ):
            self.Failed = False

class Kidney_AfferentArtery:
    def __init__(self):
        self.Conductance = None
        self.Basic = 34.0
        self.Clamp = False
        self.Level = 0.0
        self.TGFEffect = None
        self.SympEffect = None
        self.MyogenicEffect = None

    def TGFEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.3, 3.0], [1.2, 1.0, 0.6], [0.0, -0.4, 0.0])

    def SympEffect_curve(self, x):
        return cubic_hermite_spline(x, [1.5, 7.0], [1.0, 0.9], [0.0, 0.0])

    def MyogenicEffect_curve(self, x):
        return cubic_hermite_spline(x, [-20.0, 0.0, 20.0], [1.2, 1.0, 0.8], [0.0, -0.02, 0.0])

    def Dervs_func(self):
        self.TGFEffect = self.TGFEffect_curve( TGF_Vascular.Signal )
        self.SympEffect = self.SympEffect_curve( Kidney_AlphaReceptors.Activity )
        self.MyogenicEffect = self.MyogenicEffect_curve( Kidney_MyogenicDelay.PressureChange )
        if self.Clamp:
            self.Conductance = self.Level
        else:
            self.Conductance = self.Basic * Kidney_NephronCount.Total_xNormal * self.TGFEffect * self.SympEffect * self.MyogenicEffect * Anesthesia.VascularConductance


class Kidney_CO2:
    def __init__(self):
        self.conc_HCO3 = None
        self.conc_HCO3_mEqperL = None
        self.PCO2 = None
        self.InflowGas = None
        self.InflowBase = None
        self.OutflowBase = None
        self.conc_BloodHCO3 = None
        self.Outflow_0 = None
        self.K = None
        self.Alpha = None
        self.Mass = 4.1

    def CalcConc_func(self):
        self.conc_HCO3 = self.Mass / Kidney_Size.LiquidVol
        self.conc_HCO3_mEqperL = 1000.0 * self.conc_HCO3
        Tissue_BaseToGas.conc_HCO3 = self.conc_HCO3
        Tissue_BaseToGas.conc_SID = Kidney_Ph.conc_SID
        Tissue_BaseToGas.Calc_func()
        self.PCO2 = Tissue_BaseToGas.pCO2

    def CalcDervs_func(self):
        self.K = Kidney_Flow.BloodFlow / Kidney_Size.LiquidVol
        if System.Dx >=0:
            self.Alpha = 0.0
        elif ( self.K * System.Dx ) >= 100.0:
            self.Alpha = 4E-44
        elif True:
            self.Alpha = ( math.e ** ( - self.K * System.Dx ) )
        self.InflowGas = Metabolism_RespiratoryQuotient.RQ * Kidney_O2.O2Use
        self.InflowBase = CO2Tools.LitersToMols * self.InflowGas
        Blood_GasToBase.pCO2 = self.PCO2
        Blood_GasToBase.conc_SID = BloodIons.conc_SID
        Blood_GasToBase.Calc_func()
        self.conc_BloodHCO3 = Blood_GasToBase.conc_HCO3
        self.Outflow_0 = Kidney_Flow.BloodFlow * ( self.conc_BloodHCO3 - CO2Artys.conc_HCO3 )
        self.OutflowBase = ( self.Alpha * self.Outflow_0 ) + ( ( 1 - self.Alpha ) * self.InflowBase )
        self.Change = self.InflowBase - self.OutflowBase
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.04)


class Kidney_Structure:
    def __init__(self):
        self.PhEffect = None
        self.FuelEffect = None
        self.TemperatureEffect = None
        self.Effect = 1.0

    def PhOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [6.5, 6.6], [0.1, 0.0], [0.0, 0.0])

    def FuelOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [0.5, 0.8], [0.05, 0.0], [0.0, 0.0])

    def TemperatureOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [44.0, 46.0], [0.0, 0.05], [0.0, 0.0])

    def Calc_func(self):
        self.PhEffect = self.PhOnStructure_curve( Kidney_Ph.Ph )
        self.FuelEffect = self.FuelOnStructure_curve( Kidney_Fuel.FractUseDelay )
        self.TemperatureEffect = self.TemperatureOnStructure_curve( HeatCore.Temp_C )
        self.F1 = 0.0
        self.F2 = self.PhEffect + self.TemperatureEffect + self.FuelEffect
        self.Effect = backwardeuler( self.F1, self.F2, System.Dx, self.Effect, None)


class Kidney_Metabolism:
    def __init__(self):
        self.TotalCalsUsed = None
        self.BasalCalsUsed = None
        self.InitialBasalCalsUsed = None
        self.BasalCalsUsed__CalperMinperG = 0.1420
        self.CalMultiplier = 1.0
        self.ProximalTubuleCals = None
        self.LoopOfHenleCals = None
        self.DistalTubuleCals = None
        self.CalPerNa__MeqperMin = 3.6
        self.AerobicCals = None
        self.AnaerobicCals = None
        self.O2Need = None
        self.O2Lack = None

    def ScaleCals_func(self):
        self.InitialBasalCalsUsed = self.CalMultiplier * self.BasalCalsUsed__CalperMinperG * Kidney_Size.InitialMass

    def CalcCals_func(self):
        self.BasalCalsUsed = self.CalMultiplier * self.BasalCalsUsed__CalperMinperG * Kidney_Size.Mass
        self.ProximalTubuleCals = self.CalPerNa__MeqperMin * PT_Na.Reab
        self.LoopOfHenleCals = self.CalPerNa__MeqperMin * LH_Na.Reab
        self.DistalTubuleCals = self.CalPerNa__MeqperMin * DT_Na.Reab
        self.TotalCalsUsed = ( self.BasalCalsUsed * Thyroid.Effect * HeatMetabolism.Core * Kidney_Structure.Effect ) + self.ProximalTubuleCals + self.LoopOfHenleCals + self.DistalTubuleCals
        self.O2Need = Metabolism_Tools.CalToO2 * self.TotalCalsUsed

    def SplitCals_func(self):
        self.O2Lack = self.O2Need - Kidney_O2.O2Use
        self.AerobicCals = Metabolism_Tools.O2ToCal * Kidney_O2.O2Use
        self.AnaerobicCals = Metabolism_Tools.O2ToCal * self.O2Lack

class Kidney_BetaReceptors:
    def __init__(self):
        self.Activity = None
        self.TotalAgonism = None
        self.NeuralAgonism = None
        self.HumoralAgonism = None
        self.Switch = False
        self.Setting = 0.0
        self.NEURALK = 0.333
        self.HUMORALK = 0.5

    def Calc_func(self):
        self.NeuralAgonism = GangliaKidney.NA_Hz
        self.HumoralAgonism = BetaPool.Effect
        self.TotalAgonism = ( self.NEURALK * self.NeuralAgonism ) + ( self.HUMORALK * self.HumoralAgonism )
        if self.Switch:
            self.Activity = self.Setting
        else:
            self.Activity = self.TotalAgonism * BetaBlockade.Effect


class Kidney_AlphaReceptors:
    def __init__(self):
        self.Activity = None
        self.TotalAgonism = None
        self.NeuralAgonism = None
        self.HumoralAgonism = None
        self.Switch = False
        self.Setting = 0.0
        self.NEURALK = 0.333
        self.HUMORALK = 0.5

    def Calc_func(self):
        self.NeuralAgonism = GangliaKidney.NA_Hz
        self.HumoralAgonism = AlphaPool.Effect
        self.TotalAgonism = ( self.NEURALK * self.NeuralAgonism ) + ( self.HUMORALK * self.HumoralAgonism )
        if self.Switch:
            self.Activity = self.Setting
        else:
            self.Activity = self.TotalAgonism * AlphaBlockade.Effect


class Kidney_EfferentArtery:
    def __init__(self):
        self.Conductance = None
        self.Basic = 23.0
        self.Clamp = False
        self.Level = 0.0
        self.A2Effect = None
        self.SympEffect = None

    def A2Effect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.3, 3.0], [1.2, 1.0, 0.6], [0.0, -0.4, 0.0])

    def SympEffect_curve(self, x):
        return cubic_hermite_spline(x, [1.5, 7.0], [1.0, 0.3], [0.0, 0.0])

    def Dervs_func(self):
        self.A2Effect = self.A2Effect_curve( A2Pool.Log10Conc )
        self.SympEffect = self.SympEffect_curve( Kidney_AlphaReceptors.Activity )
        if self.Clamp:
            self.Conductance = self.Level
        else:
            self.Conductance = self.Basic * Kidney_NephronCount.Total_xNormal * self.A2Effect * self.SympEffect * Anesthesia.VascularConductance


class Kidney_Pressure:
    def __init__(self):
        self.ArtyPressure = None
        self.VeinPressure = None
        self.PressureGradient = None
        self.PumpSwitch = False
        self.PumpSetting = 0.0

    def Calc_func(self):
        if self.PumpSwitch:
            self.ArtyPressure = self.PumpSetting
        else:
            self.ArtyPressure = SystemicArtys.Pressure

        self.VeinPressure = SystemicVeins.Pressure
        self.PressureGradient = ( max( ( self.ArtyPressure - self.VeinPressure ), 0.0) )

class Kidney_ArcuateArtery:
    def __init__(self):
        self.Pressure = None
        self.Conductance = None
        self.BasicConductance = 600.0
        self.Stenosis = 1.0

    def CalcConductance_func(self):
        self.Conductance = self.BasicConductance / self.Stenosis

    def CalcPressure_func(self):
        self.Pressure = Kidney_Pressure.ArtyPressure - ( Kidney_Flow.BloodFlow / self.Conductance )

class Kidney_NephronCount:
    def __init__(self):
        self.Total = 2400000
        self.Total_xNormal = None
        self.Normal = 2400000
        self.Filtering_percent = 100.0
        self.Filtering_xNormal = None

    def Calc_func(self):
        self.Total_xNormal = self.Total / self.Normal
        self.Filtering_xNormal = 0.01 * self.Filtering_percent * self.Total_xNormal

class Kidney_Flow:
    def __init__(self):
        self.Conductance = None
        self.BloodFlow = None
        self.PlasmaFlow = None

    def Calc_func(self):
        self.Conductance = ( 1 / ( ( ( 1 / Kidney_ArcuateArtery.Conductance ) ) + ( ( 1 / Kidney_AfferentArtery.Conductance ) ) + ( ( 1 / Kidney_EfferentArtery.Conductance ) ) ) )
        self.BloodFlow = ( max( ( Kidney_Pressure.PressureGradient * self.Conductance ), 0.0) )
        self.PlasmaFlow = BloodVol.PVCrit * self.BloodFlow

class Kidney_Myogenic:
    def __init__(self):
        self.Tau = 4.0
        self.Clamp = False
        self.Level = 0.0
        self.PressureChange_Steady_State = None
        self.AdaptedPressure = 77.0

    def Parms_func(self):
        self.K = ( 1 / ( 60.0 * self.Tau ) )

    def Dervs_func(self):
        self.InterlobarPressure = ( Kidney_ArcuateArtery.Pressure + GlomerulusFiltrate.Pressure ) / 2.0
        if self.Clamp:
            self.PressureChange_Steady_State = self.Level
        else:
            self.PressureChange_Steady_State = self.InterlobarPressure - self.AdaptedPressure

        Kidney_MyogenicDelay.Dervs_func()
        self.AdaptedPressure = delay( self.K, self.InterlobarPressure, self.AdaptedPressure, System.Dx, 0.1)


class AnesthesiaGasBone:
    def __init__(self):
        self.conc_Tissue = None
        self.pTissue = None
        self.conc_Vein = None
        self.pVein = None
        self.Uptake = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Tissue = self.Mass / Bone_Size.Vol
        self.pTissue = self.conc_Tissue * AnesthesiaGasSolubility.GeneralK
        self.pVein = self.pTissue
        self.conc_Vein = self.pVein / AnesthesiaGasSolubility.BloodK

    def Dervs_func(self):
        self.Uptake = ( AnesthesiaGasArty.conc_Blood - self.conc_Vein ) * Bone_Flow.BloodFlow
        self.Change = self.Uptake
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.02)


class AnesthesiaGas:

    def Parms_func(self):
        AnesthesiaGasSolubility.Parms_func()

    def CalcConc_func(self):
        AnesthesiaGasArty.CalcConc_func()
        AnesthesiaGasVein.CalcConc_func()
        AnesthesiaGasBone.CalcConc_func()
        AnesthesiaGasBrain.CalcConc_func()
        AnesthesiaGasFat.CalcConc_func()
        AnesthesiaGasGITract.CalcConc_func()
        AnesthesiaGasKidney.CalcConc_func()
        AnesthesiaGasLeftHeart.CalcConc_func()
        AnesthesiaGasLiver.CalcConc_func()
        AnesthesiaGasOtherTissue.CalcConc_func()
        AnesthesiaGasRespiratoryMuscle.CalcConc_func()
        AnesthesiaGasRightHeart.CalcConc_func()
        AnesthesiaGasSkeletalMuscle.CalcConc_func()
        AnesthesiaGasSkin.CalcConc_func()

    def Dervs_func(self):
        AnesthesiaGasLung.Dervs_func()
        AnesthesiaGasArty.Dervs_func()
        AnesthesiaGasVein.Dervs_func()
        AnesthesiaGasBone.Dervs_func()
        AnesthesiaGasBrain.Dervs_func()
        AnesthesiaGasFat.Dervs_func()
        AnesthesiaGasGITract.Dervs_func()
        AnesthesiaGasKidney.Dervs_func()
        AnesthesiaGasLeftHeart.Dervs_func()
        AnesthesiaGasLiver.Dervs_func()
        AnesthesiaGasOtherTissue.Dervs_func()
        AnesthesiaGasRespiratoryMuscle.Dervs_func()
        AnesthesiaGasRightHeart.Dervs_func()
        AnesthesiaGasSkeletalMuscle.Dervs_func()
        AnesthesiaGasSkin.Dervs_func()

class AnesthesiaGasBrain:
    def __init__(self):
        self.conc_Tissue = None
        self.pTissue = None
        self.conc_Vein = None
        self.pVein = None
        self.Uptake = None
        self.BrainFunc = None
        self.TidalVol = None
        self.Mass = 0.0

    def BrainFunc_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 4.0, 12.0, 16.0], [1.0, 0.4, 0.2, 0.0], [0.0, -0.02, -0.01, 0.0])

    def TidalVol_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 12.0], [1.0, 0.0], [0.0, 0.0])

    def CalcConc_func(self):
        self.conc_Tissue = self.Mass / Brain_Size.Vol
        self.pTissue = self.conc_Tissue * AnesthesiaGasSolubility.BrainK
        self.pVein = self.pTissue
        self.conc_Vein = self.pVein / AnesthesiaGasSolubility.BloodK
        self.BrainFunc = self.BrainFunc_curve( self.pTissue )
        self.TidalVol = self.TidalVol_curve( self.pTissue )

    def Dervs_func(self):
        self.Uptake = ( AnesthesiaGasArty.conc_Blood - self.conc_Vein ) * Brain_Flow.BloodFlow
        self.Change = self.Uptake
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.02)


class AnesthesiaGasLiver:
    def __init__(self):
        self.conc_Tissue = None
        self.pTissue = None
        self.conc_Vein = None
        self.pVein = None
        self.conc_Arty = None
        self.Uptake = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Tissue = self.Mass / Liver_Size.Vol
        self.pTissue = self.conc_Tissue * AnesthesiaGasSolubility.GeneralK
        self.pVein = self.pTissue
        self.conc_Vein = self.pVein / AnesthesiaGasSolubility.BloodK

    def Dervs_func(self):
        if OrganFlow.HepaticVeinFlow > 0.0:
            self.conc_Arty = ( ( AnesthesiaGasArty.conc_Blood * HepaticArty.Flow ) + ( AnesthesiaGasGITract.conc_Vein * GITract_Flow.BloodFlow ) ) / OrganFlow.HepaticVeinFlow
        else:
            self.conc_Arty = 0.0

        self.Uptake = ( self.conc_Arty - self.conc_Vein ) * OrganFlow.HepaticVeinFlow
        self.Change = self.Uptake
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.02)


class AnesthesiaGasGITract:
    def __init__(self):
        self.conc_Tissue = None
        self.pTissue = None
        self.conc_Vein = None
        self.pVein = None
        self.Uptake = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Tissue = self.Mass / GITract_Size.Vol
        self.pTissue = self.conc_Tissue * AnesthesiaGasSolubility.GeneralK
        self.pVein = self.pTissue
        self.conc_Vein = self.pVein / AnesthesiaGasSolubility.BloodK

    def Dervs_func(self):
        self.Uptake = ( AnesthesiaGasArty.conc_Blood - self.conc_Vein ) * GITract_Flow.BloodFlow
        self.Change = self.Uptake
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.02)


class AnesthesiaGasSkeletalMuscle:
    def __init__(self):
        self.conc_Tissue = None
        self.pTissue = None
        self.conc_Vein = None
        self.pVein = None
        self.Uptake = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Tissue = self.Mass / SkeletalMuscle_Size.Vol
        self.pTissue = self.conc_Tissue * AnesthesiaGasSolubility.GeneralK
        self.pVein = self.pTissue
        self.conc_Vein = self.pVein / AnesthesiaGasSolubility.BloodK

    def Dervs_func(self):
        self.Uptake = ( AnesthesiaGasArty.conc_Blood - self.conc_Vein ) * SkeletalMuscle_Flow.BloodFlow
        self.Change = self.Uptake
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.02)


class AnesthesiaGasFat:
    def __init__(self):
        self.conc_Tissue = None
        self.pTissue = None
        self.conc_Vein = None
        self.pVein = None
        self.Uptake = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Tissue = self.Mass / Fat_Size.Vol
        self.pTissue = self.conc_Tissue * AnesthesiaGasSolubility.AdiposeK
        self.pVein = self.pTissue
        self.conc_Vein = self.pVein / AnesthesiaGasSolubility.BloodK

    def Dervs_func(self):
        self.Uptake = ( AnesthesiaGasArty.conc_Blood - self.conc_Vein ) * Fat_Flow.BloodFlow
        self.Change = self.Uptake
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.02)


class AnesthesiaGasRespiratoryMuscle:
    def __init__(self):
        self.conc_Tissue = None
        self.pTissue = None
        self.conc_Vein = None
        self.pVein = None
        self.Uptake = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Tissue = self.Mass / RespiratoryMuscle_Size.Vol
        self.pTissue = self.conc_Tissue * AnesthesiaGasSolubility.GeneralK
        self.pVein = self.pTissue
        self.conc_Vein = self.pVein / AnesthesiaGasSolubility.BloodK

    def Dervs_func(self):
        self.Uptake = ( AnesthesiaGasArty.conc_Blood - self.conc_Vein ) * RespiratoryMuscle_Flow.BloodFlow
        self.Change = self.Uptake
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.02)


class AnesthesiaGasVein:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.conc_Blood = None
        self.pBlood = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Blood = self.Mass / VeinsVol.Vol
        self.pBlood = self.conc_Blood * AnesthesiaGasSolubility.BloodK

    def Dervs_func(self):
        if RightAtrium.Inflow > 0.0:
            self.DxMax = VeinsVol.Vol / RightAtrium.Inflow
        else:
            self.DxMax = 0.5

        self.Gain = ( AnesthesiaGasArty.conc_Blood * A_VFistula_Flow.BloodFlow ) + ( AnesthesiaGasBone.conc_Vein * Bone_Flow.BloodFlow ) + ( AnesthesiaGasBrain.conc_Vein * Brain_Flow.BloodFlow ) + ( AnesthesiaGasFat.conc_Vein * Fat_Flow.BloodFlow ) + ( AnesthesiaGasGITract.conc_Vein * GITract_Flow.BloodFlow ) + ( AnesthesiaGasKidney.conc_Vein * Kidney_Flow.BloodFlow ) + ( AnesthesiaGasLeftHeart.conc_Vein * LeftHeart_Flow.BloodFlow ) + ( AnesthesiaGasLiver.conc_Vein * OrganFlow.HepaticVeinFlow ) + ( AnesthesiaGasOtherTissue.conc_Vein * OtherTissue_Flow.BloodFlow ) + ( AnesthesiaGasRespiratoryMuscle.conc_Vein * RespiratoryMuscle_Flow.BloodFlow ) + ( AnesthesiaGasRightHeart.conc_Vein * RightHeart_Flow.BloodFlow ) + ( AnesthesiaGasSkeletalMuscle.conc_Vein * SkeletalMuscle_Flow.BloodFlow ) + ( AnesthesiaGasSkin.conc_Vein * Skin_Flow.BloodFlow )
        self.Loss = PulmArty.Outflow * self.conc_Blood
        self.Change = self.Gain - self.Loss

class AnesthesiaGasSkin:
    def __init__(self):
        self.conc_Tissue = None
        self.pTissue = None
        self.conc_Vein = None
        self.pVein = None
        self.Uptake = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Tissue = self.Mass / Skin_Size.Vol
        self.pTissue = self.conc_Tissue * AnesthesiaGasSolubility.GeneralK
        self.pVein = self.pTissue
        self.conc_Vein = self.pVein / AnesthesiaGasSolubility.BloodK

    def Dervs_func(self):
        self.Uptake = ( AnesthesiaGasArty.conc_Blood - self.conc_Vein ) * Skin_Flow.BloodFlow
        self.Change = self.Uptake
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.02)


class AnesthesiaGasLeftHeart:
    def __init__(self):
        self.conc_Tissue = None
        self.pTissue = None
        self.conc_Vein = None
        self.pVein = None
        self.Uptake = None
        self.HrtCont = None
        self.Mass = 0.0

    def HrtCont_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 4.0, 12.0], [1.0, 0.5, 0.0], [0.0, -0.2, 0.0])

    def CalcConc_func(self):
        self.conc_Tissue = self.Mass / LeftHeart_Size.Vol
        self.pTissue = self.conc_Tissue * AnesthesiaGasSolubility.GeneralK
        self.pVein = self.pTissue
        self.conc_Vein = self.pVein / AnesthesiaGasSolubility.BloodK
        self.HrtCont = self.HrtCont_curve( self.pTissue )

    def Dervs_func(self):
        self.Uptake = ( AnesthesiaGasArty.conc_Blood - self.conc_Vein ) * LeftHeart_Flow.BloodFlow
        self.Change = self.Uptake
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.02)


class AnesthesiaGasLung:
    def __init__(self):
        self.conc_Alv = None
        self.pAlv = None
        self.conc_Capy = None
        self.pCapy = None
        self.Uptake = None
        self.N = None
        self.D = None

    def Dervs_func(self):
        self.N = ( Breathing.AlveolarVentilation_STPD * Bronchi.conc_Anesthetic ) + ( LungBloodFlow.AlveolarVentilated * AnesthesiaGasVein.conc_Blood )
        self.D = ( Breathing.AlveolarVentilation_STPD / 760.0 ) + ( LungBloodFlow.AlveolarVentilated / AnesthesiaGasSolubility.BloodK )
        if self.D > 0.0:
            self.pAlv = self.N / self.D
        else:
            self.pAlv = 0.0

        self.conc_Alv = self.pAlv / 760.0
        self.pCapy = self.pAlv
        self.conc_Capy = self.pCapy / AnesthesiaGasSolubility.BloodK
        self.Uptake = Breathing.AlveolarVentilation_STPD * ( Bronchi.conc_Anesthetic - self.conc_Alv )

class AnesthesiaGasSolubility:
    def __init__(self):
        self.Blood = 1.4
        self.BloodK = None
        self.General = 4.2
        self.GeneralK = None
        self.Brain = 3.6
        self.BrainK = None
        self.Adipose = 63.0
        self.AdiposeK = None

    def Parms_func(self):
        self.BloodK = 760.0 / self.Blood
        self.GeneralK = 760.0 / self.General
        self.BrainK = 760.0 / self.Brain
        self.AdiposeK = 760.0 / self.Adipose

class AnesthesiaGasArty:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.conc_Blood = None
        self.pBlood = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Blood = self.Mass / ArtysVol.Vol
        self.pBlood = self.conc_Blood * AnesthesiaGasSolubility.BloodK

    def Dervs_func(self):
        if SystemicArtys.Outflow > 0.0:
            self.DxMax = ArtysVol.Vol / SystemicArtys.Outflow
        else:
            self.DxMax = 0.1

        self.Gain = ( AnesthesiaGasLung.conc_Capy * LungBloodFlow.AlveolarVentilated ) + ( AnesthesiaGasVein.conc_Blood * LungBloodFlow.TotalShunt )
        self.Loss = SystemicArtys.Outflow * self.conc_Blood
        self.Change = self.Gain - self.Loss

class AnesthesiaGasOtherTissue:
    def __init__(self):
        self.conc_Tissue = None
        self.pTissue = None
        self.conc_Vein = None
        self.pVein = None
        self.Uptake = None
        self.VascCond = None
        self.Mass = 0.0

    def VascCond_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 5.0], [1.0, 2.0], [0.0, 0.0])

    def CalcConc_func(self):
        self.conc_Tissue = self.Mass / OtherTissue_Size.Vol
        self.pTissue = self.conc_Tissue * AnesthesiaGasSolubility.GeneralK
        self.pVein = self.pTissue
        self.conc_Vein = self.pVein / AnesthesiaGasSolubility.BloodK
        self.VascCond = self.VascCond_curve( self.pTissue )

    def Dervs_func(self):
        self.Uptake = ( AnesthesiaGasArty.conc_Blood - self.conc_Vein ) * OtherTissue_Flow.BloodFlow
        self.Change = self.Uptake
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.02)


class AnesthesiaGasKidney:
    def __init__(self):
        self.conc_Tissue = None
        self.pTissue = None
        self.conc_Vein = None
        self.pVein = None
        self.Uptake = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Tissue = self.Mass / Kidney_Size.Vol
        self.pTissue = self.conc_Tissue * AnesthesiaGasSolubility.GeneralK
        self.pVein = self.pTissue
        self.conc_Vein = self.pVein / AnesthesiaGasSolubility.BloodK

    def Dervs_func(self):
        self.Uptake = ( AnesthesiaGasArty.conc_Blood - self.conc_Vein ) * Kidney_Flow.BloodFlow
        self.Change = self.Uptake
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.02)


class AnesthesiaGasRightHeart:
    def __init__(self):
        self.conc_Tissue = None
        self.pTissue = None
        self.conc_Vein = None
        self.pVein = None
        self.Uptake = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Tissue = self.Mass / RightHeart_Size.Vol
        self.pTissue = self.conc_Tissue * AnesthesiaGasSolubility.GeneralK
        self.pVein = self.pTissue
        self.conc_Vein = self.pVein / AnesthesiaGasSolubility.BloodK

    def Dervs_func(self):
        self.Uptake = ( AnesthesiaGasArty.conc_Blood - self.conc_Vein ) * RightHeart_Flow.BloodFlow
        self.Change = self.Uptake
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.02)


class CO:
    def __init__(self):
        self.conc_CO = None
        self.pCO = None
        self.HaldaneFactor = 230.0
        self.EndogenousProduction = 0.007
        self.ExtravascularSpaceFraction = 0.16
        self.ExtravascularSpace = None
        self.VolumeDistribution = None
        self.Permeability = None
        self.CO_O2Ratio = 0.81
        self.Gradient = None
        self.conc_CO_Lung = None
        self.pCO_Lung = None
        self.Mass = 4.9
        self.Uptake = -0.007
    def Calc_func(self):
        self.ExtravascularSpace = self.ExtravascularSpaceFraction * BloodVol.Vol
        self.VolumeDistribution = BloodVol.Vol + self.ExtravascularSpace
        self.conc_CO = self.Mass / self.VolumeDistribution

    def Dervs_func(self):
        self.pCO = ( self.conc_CO * LungO2.PCapy ) / ( self.HaldaneFactor * LungO2.conc_Capy )
        self.Permeability = self.CO_O2Ratio * PulmonaryMembrane.Permeability

        def Uptakeimplicitfunc(Uptake):
            if Breathing.AlveolarVentilation_STPD > 0.0:
                self.conc_CO_Lung = Bronchi.conc_CO - ( Uptake / Breathing.AlveolarVentilation_STPD )
            else:
                self.conc_CO_Lung = self.conc_CO

            self.pCO_Lung = self.conc_CO_Lung * Barometer.Pressure
            self.Gradient = self.pCO_Lung - self.pCO
            EndUptake = self.Gradient * self.Permeability

            return EndUptake
        self.Uptake = impliciteq( Uptakeimplicitfunc, self.Uptake, 0.01)
        self.Change = self.Uptake + self.EndogenousProduction
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 10.0)


class PhCells:
    def __init__(self):
        self.pH = None
        self.pK = 7.15
        self.pCO2 = None
        self.SID = None
        self.H_ = None

    def Calc_func(self):
        PhGeneral.pK = self.pK
        PhGeneral.pCO2 = self.pCO2
        PhGeneral.SID = self.SID
        PhGeneral.Calc_func()
        self.pH = PhGeneral.pH
        self.H_ = PhGeneral.H_

class PhBlood:
    def __init__(self):
        self.pH = None
        self.pK = 7.42
        self.pCO2 = None
        self.SID = None
        self.H_ = None

    def Calc_func(self):
        PhGeneral.pK = self.pK
        PhGeneral.pCO2 = self.pCO2
        PhGeneral.SID = self.SID
        PhGeneral.Calc_func()
        self.pH = PhGeneral.pH
        self.H_ = PhGeneral.H_

class BloodPh:
    def __init__(self):
        self.ArtysPh = None
        self.Artysconc_H_ = None
        self.VeinsPh = None
        self.Veinsconc_H_ = None

    def Calc_func(self):
        PhBlood.pCO2 = CO2Artys.Pressure
        PhBlood.SID = BloodIons.conc_SID_mEqperL
        PhBlood.Calc_func()
        self.ArtysPh = PhBlood.pH
        self.Artysconc_H_ = PhBlood.H_
        PhBlood.pCO2 = CO2Veins.Pressure
        PhBlood.SID = BloodIons.conc_SID_mEqperL
        PhBlood.Calc_func()
        self.VeinsPh = PhBlood.pH
        self.Veinsconc_H_ = PhBlood.H_

class PhGeneral:
    def __init__(self):
        self.pH = None
        self.pK = None
        self.pCO2 = None
        self.SID = None
        self.H_ = None

    def Calc_func(self):
        if self.pCO2 <= 0.0:
            self.pH = self.pK + 3
        elif ( self.SID / self.pCO2 ) < 1e-3:
            self.pH = self.pK - 3
        elif True:
            self.pH = self.pK + ( math.log10( ( self.SID / self.pCO2 ) ) )
        self.H_ = 10 ** ( 9.0 - self.pH )

class AcidBase:
    def __init__(self):
        pass
    
class InsulinSecretion:
    def __init__(self):
        self.Rate = None
        self.GlucoseEffect = None
        self.KAEffect = None
        self.BasicFraction = 0.0085
        self.Fraction = None

    def GlucoseEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 105.0, 600.0], [0.0, 1.0, 50.0], [0.0, 0.01, 0.0])

    def KAEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.5, 50.0], [0.6, 1.0, 2.0], [0.0, 0.05, 0.0])

    def Dervs_func(self):
        self.GlucoseEffect = self.GlucoseEffect_curve( GlucosePool.conc_Glucose_mGperdL )
        self.KAEffect = self.KAEffect_curve( KAPool.conc_KA_mGperdL )
        self.Fraction = self.BasicFraction * self.GlucoseEffect * self.KAEffect * GITract_Function.Effect
        self.Rate = self.Fraction * InsulinStorage.Mass

class InsulinSynthesis:
    def __init__(self):
        self.Tau = 20.0
        self.MassEffect = None
        self.Base = 0.67
        self.Rate = 17.0

    def MassEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 2000.0, 3000.0], [200.0, 17.0, 0.0], [0.0, -0.02, 0.0])

    def Parms_func(self):
        self.K = ( 1 / self.Tau )

    def Dervs_func(self):
        self.MassEffect = self.MassEffect_curve( InsulinStorage.Mass )
        self.SteadyState = self.MassEffect
        self.Rate = delay( self.K, self.SteadyState, self.Rate, System.Dx, 0.17)


class InsulinPump:
    def __init__(self):
        self.Rate = None
        self.Switch = False
        self.Setting = 0.0

    def Parms_func(self):
        if self.Switch:
            self.Rate = self.Setting
        else:
            self.Rate = 0.0


class InsulinClearance:
    def __init__(self):
        self.Rate = None
        self.K = 0.057

    def Dervs_func(self):
        self.Rate = self.K * InsulinPool.Mass

class InsulinPool:
    def __init__(self):
        self.conc_Insulin = None
        self.Gain = None
        self.Loss = None
        self.Targetconc_Insulin = 20.0
        self.InitialMass = None

    def Init_func(self):
        self.InitialMass = self.Targetconc_Insulin * ECFV.InitialVol_L
        self.Mass = self.InitialMass

    def CalcConc_func(self):
        self.conc_Insulin = self.Mass / ECFV.Vol_L

    def Dervs_func(self):
        self.Gain = InsulinSecretion.Rate + InsulinPump.Rate
        self.Loss = InsulinClearance.Rate
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 1.0)


class Insulin:

    def Parms_func(self):
        InsulinPump.Parms_func()
        InsulinSynthesis.Parms_func()

    def CalcConc_func(self):
        InsulinPool.CalcConc_func()

    def Dervs_func(self):
        InsulinSynthesis.Dervs_func()
        InsulinSecretion.Dervs_func()
        InsulinClearance.Dervs_func()
        InsulinStorage.Dervs_func()
        InsulinPool.Dervs_func()

class InsulinStorage:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.Mass = 2000.0

    def Dervs_func(self):
        self.Gain = InsulinSynthesis.Rate
        self.Loss = InsulinSecretion.Rate
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 20.0)


class LeftHeartPumping_Valves:
    def __init__(self):
        pass
    
class LeftHeartPumping_Systole:
    def __init__(self):
        self.ESV = None
        self.ESP = None
        self.TMP = None
        self.A_Basic = 17.39
        self.A = None
        self.n = 0.5
        self.Contractility_Basic = 1.0
        self.Contractility = None
        self.Switch = 0
        self.Failure = None
        self.Degree = 1

    def Calc_func(self):
        self.ESP = SystemicArtys.Pressure + 24.0
        self.TMP = self.ESP - Pericardium_Cavity.Pressure
        if self.Switch:
            self.Failure = System.X
        else:
            self.Failure = 0
        self.Contractility = ( self.Contractility_Basic * LeftHeart_BetaReceptors.Activity ) - ( self.Failure * self.Degree / 144000 )
        self.A = self.Contractility * self.A_Basic
        self.V_equals_f_P_func()

    def P_equals_f_V_func(self):
        self.TMP = self.A * ( self.ESV ** self.n )

    def V_equals_f_P_func(self):
        self.ESV = ( self.TMP / self.A ) ** ( 1.0 / self.n )

class LeftHeartPumping_Diastole:
    def __init__(self):
        self.EDV = None
        self.EDP = None
        self.TMP = None
        self.A_Basic = 0.00051
        self.A = None
        self.n = 2.0
        self.Stiffness = 1.0

    def Calc_func(self):
        self.EDP = LeftAtrium.Pressure
        self.TMP = self.EDP - Pericardium_Cavity.Pressure
        self.A = self.Stiffness * self.A_Basic
        self.V_equals_f_P_func()

    def P_equals_f_V_func(self):
        self.TMP = self.A * ( self.EDV ** self.n )

    def V_equals_f_P_func(self):
        self.EDV = ( self.TMP / self.A ) ** ( 1.0 / self.n )

class LeftHeartPumping_Pumping:
    def __init__(self):
        self.BloodFlow = None
        self.StrokeVolume = None
        self.EjectionFraction = None

    def Calc_func(self):
        self.StrokeVolume = LeftHeartPumping_Diastole.EDV - LeftHeartPumping_Systole.ESV
        self.BloodFlow = Heart_Ventricles.Rate * self.StrokeVolume
        self.EjectionFraction = self.StrokeVolume / LeftHeartPumping_Diastole.EDV

class LeftHeartPumping:

    def Dervs_func(self):
        LeftHeartPumping_Diastole.Calc_func()
        LeftHeartPumping_Systole.Calc_func()
        LeftHeartPumping_Pumping.Calc_func()

class Bone_Lactate:
    def __init__(self):
        self.conc_Lac_ = None
        self.conc_Lac__mEqperL = None
        self.conc_Lac__mGperdL = None
        self.DC = 180.0
        self.Made = None
        self.Made_mGperMin = None
        self.Used = None
        self.Used_mGperMin = None
        self.Outflux = None
        self.Outflux_0 = None
        self.K = None
        self.Alpha = None
        self.MEQ_ML_TO_MG_DL = 9008.0
        self.GLUCOSE_TO_LACTATE = 0.99
        self.MG_TO_MEQ = 0.0112
        self.Mass = 3.51

    def CalcConc_func(self):
        self.conc_Lac_ = self.Mass / Bone_Size.LiquidVol
        self.conc_Lac__mEqperL = 1000.0 * self.conc_Lac_
        self.conc_Lac__mGperdL = self.MEQ_ML_TO_MG_DL * self.conc_Lac_

    def CalcDervs_func(self):
        self.Made_mGperMin = self.GLUCOSE_TO_LACTATE * Bone_Fuel.AnaerobicGlucoseUsed_mGperMin
        self.Made = self.MG_TO_MEQ * self.Made_mGperMin
        self.Used_mGperMin = Bone_Fuel.LacUsed_mGperMin
        self.Used = self.MG_TO_MEQ * self.Used_mGperMin
        self.K = self.DC / Bone_Size.LiquidVol
        if System.Dx >=0:
            self.Alpha = 0.0
        elif ( self.K * System.Dx ) >= 100.0:
            self.Alpha = 4E-44
        elif True:
            self.Alpha = ( math.e ** ( - self.K * System.Dx ) )
        self.Outflux_0 = self.DC * ( self.conc_Lac_ - LacPool.conc_Lac_ )
        self.Outflux = ( self.Alpha * self.Outflux_0 ) + ( ( 1 - self.Alpha ) * ( self.Made + self.Used ) )
        self.Change = self.Made - self.Used - self.Outflux
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.035)


class Bone_Size:
    def __init__(self):
        self.Vol = None
        self.Mass = None
        self.InitialMass = None
        self.Density = None
        self.LiquidMass = None
        self.LiquidDensity = 1.00
        self.LiquidVol = None
        self.InitialLiquidVol = None
        self.SolidMass = None
        self.InitialSolidMass = None
        self.MineralMass = None
        self.InitialMineralMass = None
        self.MineralDensity = 2.30
        self.OtherMass = None
        self.InitialOtherMass = None
        self.OtherDensity = 1.05
        self.MineralVol = None
        self.OtherVol = None
        self.SolidVol = None
        self.FractTotal = None
        self.IFV = None
        self.InitialIFV = None
        self.CellH2O = None
        self.InitialCellH2O = None
        self.MassFractBase = 0.389
        self.H2OFractMass = 0.32
        self.SolidsFractMass = None
        self.OtherFractSolids = 0.24
        self.MineralsFractSolids = None

    def Initialize_func(self):
        self.InitialMass = self.MassFractBase * Weight.InitialOtherMass
        self.InitialLiquidVol = self.H2OFractMass * self.InitialMass / self.LiquidDensity
        self.SolidsFractMass = 1.0 - self.H2OFractMass
        self.InitialSolidMass = self.SolidsFractMass * self.InitialMass
        self.InitialOtherMass = self.OtherFractSolids * self.InitialSolidMass
        self.MineralsFractSolids = 1.0 - self.OtherFractSolids
        self.InitialMineralMass = self.MineralsFractSolids * self.InitialSolidMass

    def ScaleH2O_func(self):
        self.FractTotal = self.InitialLiquidVol / TissueH2O.InitialVol
        self.InitialIFV = self.FractTotal * InterstitialWater.InitialVol
        self.InitialCellH2O = self.FractTotal * CellH2O.InitialVol

    def Calc_func(self):
        self.IFV = self.FractTotal * InterstitialWater.Vol
        self.CellH2O = self.FractTotal * CellH2O.Vol
        self.LiquidVol = self.IFV + self.CellH2O
        self.LiquidMass = self.LiquidVol * self.LiquidDensity
        self.MineralMass = Bone_Mineral.Mass
        self.OtherMass = self.InitialOtherMass
        self.SolidMass = self.MineralMass + self.OtherMass
        self.MineralVol = self.MineralMass / self.MineralDensity
        self.OtherVol = self.OtherMass / self.OtherDensity
        self.SolidVol = self.MineralVol + self.OtherVol
        self.Mass = self.LiquidMass + self.SolidMass
        self.Vol = self.LiquidVol + self.SolidVol
        self.Density = self.Mass / self.Vol

class Bone_Metabolism:
    def __init__(self):
        self.TotalCalsUsed = None
        self.NormalCalsUsed = None
        self.InitialNormalCalsUsed = None
        self.NormalCalsUsed__CalperMinperG = 0.0081
        self.CalMultiplier = 1.0
        self.AerobicCals = None
        self.AnaerobicCals = None
        self.O2Need = None
        self.O2Lack = None

    def ScaleCals_func(self):
        self.InitialNormalCalsUsed = self.CalMultiplier * self.NormalCalsUsed__CalperMinperG * Bone_Size.InitialMass

    def CalcCals_func(self):
        self.NormalCalsUsed = self.CalMultiplier * self.NormalCalsUsed__CalperMinperG * Bone_Size.Mass
        self.TotalCalsUsed = self.NormalCalsUsed * Thyroid.Effect * HeatMetabolism.Core * Bone_Structure.Effect
        self.O2Need = Metabolism_Tools.CalToO2 * self.TotalCalsUsed

    def SplitCals_func(self):
        self.O2Lack = self.O2Need - Bone_Flow.O2Use
        self.AerobicCals = Metabolism_Tools.O2ToCal * Bone_Flow.O2Use
        self.AnaerobicCals = Metabolism_Tools.O2ToCal * self.O2Lack

class Bone_CO2:
    def __init__(self):
        self.conc_HCO3 = None
        self.conc_HCO3_mEqperL = None
        self.PCO2 = None
        self.InflowGas = None
        self.InflowBase = None
        self.OutflowBase = None
        self.conc_BloodHCO3 = None
        self.Outflow_0 = None
        self.K = None
        self.Alpha = None
        self.Mass = 56.2

    def CalcConc_func(self):
        self.conc_HCO3 = self.Mass / Bone_Size.LiquidVol
        self.conc_HCO3_mEqperL = 1000.0 * self.conc_HCO3
        Tissue_BaseToGas.conc_HCO3 = self.conc_HCO3
        Tissue_BaseToGas.conc_SID = Bone_Ph.conc_SID
        Tissue_BaseToGas.Calc_func()
        self.PCO2 = Tissue_BaseToGas.pCO2

    def CalcDervs_func(self):
        self.K = Bone_Flow.BloodFlow / Bone_Size.LiquidVol
        if System.Dx >=0:
            self.Alpha = 0.0
        elif ( self.K * System.Dx ) >= 100.0:
            self.Alpha = 4E-44
        elif True:
            self.Alpha = ( math.e ** ( - self.K * System.Dx ) )
        self.InflowGas = Metabolism_RespiratoryQuotient.RQ * Bone_Flow.O2Use
        self.InflowBase = CO2Tools.LitersToMols * self.InflowGas
        Blood_GasToBase.pCO2 = self.PCO2
        Blood_GasToBase.conc_SID = BloodIons.conc_SID
        Blood_GasToBase.Calc_func()
        self.conc_BloodHCO3 = Blood_GasToBase.conc_HCO3
        self.Outflow_0 = Bone_Flow.BloodFlow * ( self.conc_BloodHCO3 - CO2Artys.conc_HCO3 )
        self.OutflowBase = ( self.Alpha * self.Outflow_0 ) + ( ( 1 - self.Alpha ) * self.InflowBase )
        self.Change = self.InflowBase - self.OutflowBase
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.56)


class Bone_Fuel:
    def __init__(self):
        self.FADelivered = None
        self.GlucoseDelivered = None
        self.KR = 0.026
        self.Ratio = None
        self.FAFraction = None
        self.GlucoseFraction = None
        self.FA_GlucoseFraction = None
        self.LacFraction = None
        self.FAUsed_CalperMin = None
        self.AerobicGlucoseUsed_CalperMin = None
        self.AnaerobicGlucoseUsed_CalperMin = None
        self.LacUsed_CalperMin = None
        self.FAUsed_mGperMin = None
        self.AerobicGlucoseUsed_mGperMin = None
        self.AnaerobicGlucoseUsed_mGperMin = None
        self.LacUsed_mGperMin = None
        self.TotalGlucoseUsed_mGperMin = None
        self.AnaerobicGlucoseDelivered = None
        self.FAFractionalDelivery = None
        self.AerobicGlucoseFractionalDelivery = None
        self.AnaerobicGlucoseFractionalDelivery = None
        self.MinimumFractionalDelivery = None
        self.FractUseDelay = 1.0

    def LacFraction_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 100.0], [0.0, 0.3], [0.0, 0.0])

    def Dervs_func(self):
        self.FADelivered = ( max( ( FAPool.conc_FA * Bone_Flow.PlasmaFlow ), 0.0) )
        self.GlucoseDelivered = ( max( ( GlucosePool.conc_Glucose * Bone_Flow.PlasmaFlow ), 0.0) )
        self.LacFraction = self.LacFraction_curve( Bone_Lactate.conc_Lac__mGperdL )
        self.FA_GlucoseFraction = 1.0 - self.LacFraction
        self.Ratio = FAPool.conc_FA_mGperdL / GlucosePool.conc_Glucose_mGperdL
        self.FAFraction = self.FA_GlucoseFraction * ( self.Ratio / ( self.Ratio + self.KR ) )
        self.GlucoseFraction = self.FA_GlucoseFraction - self.FAFraction
        self.FAUsed_CalperMin = self.FAFraction * Bone_Metabolism.AerobicCals
        self.FAUsed_mGperMin = self.FAUsed_CalperMin * Metabolism_Tools.Fat_mGperCal
        self.AerobicGlucoseUsed_CalperMin = self.GlucoseFraction * Bone_Metabolism.AerobicCals
        self.AerobicGlucoseUsed_mGperMin = self.AerobicGlucoseUsed_CalperMin * Metabolism_Tools.CarboAerobic_mGperCal
        self.LacUsed_CalperMin = self.LacFraction * Bone_Metabolism.AerobicCals
        self.LacUsed_mGperMin = self.LacUsed_CalperMin * Metabolism_Tools.Lac__mGperCal
        self.AnaerobicGlucoseDelivered = self.GlucoseDelivered - self.AerobicGlucoseUsed_mGperMin
        self.AnaerobicGlucoseUsed_CalperMin = ( min( Bone_Metabolism.AnaerobicCals, self.AnaerobicGlucoseDelivered) )
        self.AnaerobicGlucoseUsed_mGperMin = self.AnaerobicGlucoseUsed_CalperMin * Metabolism_Tools.CarboAnaerobic_mGperCal
        self.TotalGlucoseUsed_mGperMin = self.AerobicGlucoseUsed_mGperMin + self.AnaerobicGlucoseUsed_mGperMin
        if self.FAUsed_mGperMin > 0.0:
            self.FAFractionalDelivery = ( min( ( self.FADelivered / self.FAUsed_mGperMin ), 1.0) )
        else:
            self.FAFractionalDelivery = 1.0

        if self.AerobicGlucoseUsed_mGperMin > 0.0:
            self.AerobicGlucoseFractionalDelivery = ( min( ( self.GlucoseDelivered / self.AerobicGlucoseUsed_mGperMin ), 1.0) )
        else:
            self.AerobicGlucoseFractionalDelivery = 1.0

        if self.AnaerobicGlucoseUsed_mGperMin > 0.0:
            self.AnaerobicGlucoseFractionalDelivery = ( min( ( self.AnaerobicGlucoseDelivered / self.AnaerobicGlucoseUsed_mGperMin ), 1.0) )
        else:
            self.AnaerobicGlucoseFractionalDelivery = 1.0

        self.MinimumFractionalDelivery = ( min( ( min( self.FAFractionalDelivery, self.AerobicGlucoseFractionalDelivery) ), self.AnaerobicGlucoseFractionalDelivery) )
        self.K = 0.5
        self.DxMax = 1.0
        self.FractUse = self.MinimumFractionalDelivery
        self.FractUseDelay = delay( self.K, self.FractUse, self.FractUseDelay, System.Dx, 0.01)


class Bone_Vasculature:
    def __init__(self):
        self.Tau = 30.0
        self.Effect = 1.0

    def PO2OnStimulus_curve(self, x):
        return cubic_hermite_spline(x, [41.0, 51.0, 61.0], [1.2, 1.0, 0.8], [0.0, -0.03, 0.0])

    def Parms_func(self):
        self.K = 1.0 / ( self.Tau * 1440.0 )

    def Calc_func(self):
        if Bone_Function.Failed:
            self.Stimulus = 0.0
        else:
            self.Stimulus = self.PO2OnStimulus_curve( Bone_Flow.PO2 )

        self.Effect = delay( self.K, self.Stimulus, self.Effect, System.Dx, None)


class Bone_Structure:
    def __init__(self):
        self.PhEffect = None
        self.FuelEffect = None
        self.TemperatureEffect = None
        self.Effect = 1.0

    def PhOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [6.5, 6.6], [0.1, 0.0], [0.0, 0.0])

    def FuelOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [0.5, 0.8], [0.05, 0.0], [0.0, 0.0])

    def TemperatureOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [44.0, 46.0], [0.0, 0.05], [0.0, 0.0])

    def Calc_func(self):
        self.PhEffect = self.PhOnStructure_curve( Bone_Ph.Ph )
        self.FuelEffect = self.FuelOnStructure_curve( Bone_Fuel.FractUseDelay )
        self.TemperatureEffect = self.TemperatureOnStructure_curve( HeatCore.Temp_C )
        self.F1 = 0.0
        self.F2 = self.PhEffect + self.TemperatureEffect + self.FuelEffect
        self.Effect = backwardeuler( self.F1, self.F2, System.Dx, self.Effect, None)


class Bone:
    def __init__(self):
        pass
    
class Bone_Function:
    def __init__(self):
        self.Failed = False
        self.Effect = None
        self.PhEffect = None
        self.ProteinEffect = None
        self.FuelEffect = None
        self.TemperatureEffect = None

    def PhOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [6.6, 6.7], [0.0, 1.0], [0.0, 0.0])

    def ProteinOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [3000.0, 5200.0], [0.0, 1.0], [0.0, 0.0])

    def FuelOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.9], [0.0, 1.0], [0.0, 0.0])

    def TemperatureOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 37.0, 40.0, 46.0], [0.0, 1.0, 1.5, 0.0], [0.0, 0.12, 0.0, 0.0])

    def Calc_func(self):
        self.PhEffect = self.PhOnFunction_curve( Bone_Ph.Ph )
        self.ProteinEffect = self.ProteinOnFunction_curve( CellProtein.Mass_G )
        self.FuelEffect = self.FuelOnFunction_curve( Bone_Fuel.FractUseDelay )
        self.TemperatureEffect = self.TemperatureOnFunction_curve( HeatCore.Temp_C )
        self.Effect = self.PhEffect * self.ProteinEffect * self.FuelEffect * self.TemperatureEffect * Bone_Structure.Effect

    def Wrapup_func(self):
        if not self.Failed and ( self.Effect < 0.2 ):
            self.Failed = True
        elif self.Failed and ( self.Effect > 0.4 ):
            self.Failed = False

class Bone_Mineral:

    def Initialize_func(self):
        self.Mass = Bone_Size.InitialMineralMass

    def Dervs_func(self):
        self.Change = 0.0
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 57.5)


class Bone_Flow:
    def __init__(self):
        self.Conductance = None
        self.BasicConductance = None
        self.Multiplier = 1.0
        self.InitialConductance = None
        self.Conductance_perG = 0.000424
        self.A2Effect = None
        self.SympsEffect = None
        self.ADHEffect = None
        self.PO2Effect = None
        self.AerobicFraction = None
        self.O2Use = None
        self.conc_O2 = None
        self.BloodFlow = None
        self.PlasmaFlow = None
        self.PO2 = 40.0
    def A2OnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.3, 3.5], [1.05, 1.0, 0.5], [0.0, -0.08, 0.0])

    def SympsOnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.0, 5.0], [1.3, 1.0, 0.1], [0.0, -0.3, 0.0])

    def PO2OnConductance_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 30.0], [2.0, 1.0], [0.0, 0.0])

    def ADHOnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.8, 3.0], [1.0, 0.1], [0.0, 0.0])

    def PO2OnAerobicFraction_curve(self, x):
        return cubic_hermite_spline(x, [2.0, 10.0], [0.0, 1.0], [0.0, 0.0])

    def Initialize_func(self):
        self.InitialConductance = self.Conductance_perG * Bone_Size.InitialMass

    def Calc_func(self):
        self.BasicConductance = self.InitialConductance * self.Multiplier
        self.A2Effect = self.A2OnConductance_curve( A2Pool.Log10Conc )
        self.SympsEffect = self.SympsOnConductance_curve( OtherTissue_AlphaReceptors.Activity )
        self.ADHEffect = self.ADHOnConductance_curve( ADHPool.Log10Conc )
        self.SearchMax = PO2Artys.Pressure

        def PO2implicitfunc(PO2):
            self.PO2Effect = self.PO2OnConductance_curve( PO2 )
            self.Conductance = self.BasicConductance * self.A2Effect * self.SympsEffect * self.PO2Effect * self.ADHEffect * Viscosity.ConductanceEffect * Anesthesia.VascularConductance * Bone_Vasculature.Effect
            self.BloodFlow = ( max( ( Bone_Pressure.PressureGradient * self.Conductance ), 0.0) )
            self.AerobicFraction = self.PO2OnAerobicFraction_curve( PO2 )
            self.O2Use = Bone_Metabolism.O2Need * self.AerobicFraction
            if self.BloodFlow > 0.0:
                self.conc_O2 = O2Artys.conc_O2 - ( self.O2Use / self.BloodFlow )
            else:
                self.conc_O2 = 0.0

            HgbTissue.conc_O2 = self.conc_O2
            HgbTissue.O2ToPO2_func()
            PO2End = HgbTissue.pO2

            return PO2End
        self.PO2 = impliciteq( PO2implicitfunc, self.PO2, 0.40)
        self.PlasmaFlow = self.BloodFlow * BloodVol.PVCrit

class Bone_Ph:
    def __init__(self):
        self.Ph = None
        self.conc_SID = None
        self.conc_SID_mEqperL = None

    def CalcSID_func(self):
        self.conc_SID = KCell.conc_K_ + CellSID.OtherCations - CellSID.StrongAnions - Bone_Lactate.conc_Lac_
        self.conc_SID_mEqperL = 1000.0 * self.conc_SID

    def CalcPh_func(self):
        PhCells.pCO2 = Bone_CO2.PCO2
        PhCells.SID = self.conc_SID_mEqperL
        PhCells.Calc_func()
        self.Ph = PhCells.pH

class Bone_Pressure:
    def __init__(self):
        self.ArtyPressure = None
        self.VeinPressure = None
        self.PressureGradient = None
        self.PumpSwitch = False
        self.PumpSetting = 0.0

    def Calc_func(self):
        if self.PumpSwitch:
            self.ArtyPressure = self.PumpSetting
        else:
            self.ArtyPressure = SystemicArtys.Pressure

        self.VeinPressure = SystemicVeins.Pressure
        self.PressureGradient = ( max( ( self.ArtyPressure - self.VeinPressure ), 0.0) )

class Bone_AlphaReceptors:
    def __init__(self):
        self.Activity = None
        self.TotalAgonism = None
        self.NeuralAgonism = None
        self.HumoralAgonism = None
        self.Switch = False
        self.Setting = 0.0
        self.NEURALK = 0.333
        self.HUMORALK = 0.5

    def Calc_func(self):
        self.NeuralAgonism = GangliaGeneral.NA_Hz
        self.HumoralAgonism = AlphaPool.Effect
        self.TotalAgonism = ( self.NEURALK * self.NeuralAgonism ) + ( self.HUMORALK * self.HumoralAgonism )
        if self.Switch:
            self.Activity = self.Setting
        else:
            self.Activity = self.TotalAgonism * AlphaBlockade.Effect


class TissueH2O:
    def __init__(self):
        self.Vol = None
        self.InitialVol = None
        self.Vol_L = None
        self.Change = None
        self.Gain = None
        self.Loss = None
        self.LT_SizeFract = 0.30
        self.MT_SizeFract = 0.50
        self.UT_SizeFract = 0.20
        self.LT_CalsFract = 0.20
        self.MT_CalsFract = 0.50
        self.UT_CalsFract = 0.30
        self.LT_SweatFract = 0.33
        self.MT_SweatFract = 0.34
        self.UT_SweatFract = 0.33
        self.LT_SkinFract = 0.33
        self.MT_SkinFract = 0.34
        self.UT_SkinFract = 0.33
        self.LT_LungFract = 0.0
        self.MT_LungFract = 1.0
        self.UT_LungFract = 0.0

    def Initialize_func(self):
        self.InitialVol = Bone_Size.InitialLiquidVol + Brain_Size.InitialLiquidVol + Fat_Size.InitialLiquidVol + GITract_Size.InitialLiquidVol + Kidney_Size.InitialLiquidVol + LeftHeart_Size.InitialLiquidVol + Liver_Size.InitialLiquidVol + OtherTissue_Size.InitialLiquidVol + RespiratoryMuscle_Size.InitialLiquidVol + RightHeart_Size.InitialLiquidVol + SkeletalMuscle_Size.InitialLiquidVol + Skin_Size.InitialLiquidVol
        UT_H2O.Initialize_func()
        MT_H2O.Initialize_func()
        LT_H2O.Initialize_func()

    def CalcVol_func(self):
        UT_H2O.Calc_func()
        MT_H2O.Calc_func()
        LT_H2O.Calc_func()
        self.Vol = UT_H2O.Vol + MT_H2O.Vol + LT_H2O.Vol
        self.Vol_L = self.Vol / 1000.0

    def Calc_func(self):
        CellH2O.Calc_func()
        InterstitialWater.Calc_func()
        InterstitialProtein.Calc_func()

    def Dervs_func(self):
        CapillaryProtein.Dervs_func()
        CapillaryWater.Dervs_func()
        LymphWater.Dervs_func()
        LymphProtein.Dervs_func()
        InterstitialProtein.Dervs_func()
        UT_H2O.Dervs_func()
        MT_H2O.Dervs_func()
        LT_H2O.Dervs_func()
        self.Gain = UT_H2O.Gain + MT_H2O.Gain + LT_H2O.Gain
        self.Loss = UT_H2O.Loss + MT_H2O.Loss + LT_H2O.Loss
        self.Change = self.Gain - self.Loss

class UT_H2O:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.InitialVol = None
        self.Vol_L = None
        self.MetabolicH2O = None
        self.SweatH2O = None
        self.InsensibleSkinH2O = None
        self.InsensibleLungH2O = None

    def Initialize_func(self):
        self.InitialVol = TissueH2O.UT_SizeFract * TissueH2O.InitialVol
        self.Vol = self.InitialVol

    def Calc_func(self):
        self.Vol_L = self.Vol / 1000.0

    def Dervs_func(self):
        self.MetabolicH2O = TissueH2O.UT_CalsFract * MetabolicH2O.Rate
        self.SweatH2O = TissueH2O.UT_SweatFract * SweatDuct.H2OOutflow
        self.InsensibleSkinH2O = TissueH2O.UT_SkinFract * HeatInsensibleSkin.H2O
        self.InsensibleLungH2O = TissueH2O.UT_LungFract * HeatInsensibleLung.H2O
        self.Gain = UT_CapillaryWater.Rate + self.MetabolicH2O
        self.Loss = UT_LymphWater.Rate + self.SweatH2O + self.InsensibleSkinH2O + self.InsensibleLungH2O
        self.Change = self.Gain - self.Loss
        self.Vol = diffeq( self.Change, System.Dx, self.Vol, 98.0)


class MT_H2O:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.InitialVol = None
        self.Vol_L = None
        self.MetabolicH2O = None
        self.SweatH2O = None
        self.InsensibleSkinH2O = None
        self.InsensibleLungH2O = None

    def Initialize_func(self):
        self.InitialVol = TissueH2O.MT_SizeFract * TissueH2O.InitialVol
        self.Vol = self.InitialVol

    def Calc_func(self):
        self.Vol_L = self.Vol / 1000.0

    def Dervs_func(self):
        self.MetabolicH2O = TissueH2O.MT_CalsFract * MetabolicH2O.Rate
        self.SweatH2O = TissueH2O.MT_SweatFract * SweatDuct.H2OOutflow
        self.InsensibleSkinH2O = TissueH2O.MT_SkinFract * HeatInsensibleSkin.H2O
        self.InsensibleLungH2O = TissueH2O.MT_LungFract * HeatInsensibleLung.H2O
        self.Gain = MT_CapillaryWater.Rate + self.MetabolicH2O
        self.Loss = MT_LymphWater.Rate + self.SweatH2O + self.InsensibleSkinH2O + self.InsensibleLungH2O
        self.Change = self.Gain - self.Loss
        self.Vol = diffeq( self.Change, System.Dx, self.Vol, 190.0)


class LT_H2O:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.InitialVol = None
        self.Vol_L = None
        self.MetabolicH2O = None
        self.SweatH2O = None
        self.InsensibleSkinH2O = None
        self.InsensibleLungH2O = None

    def Initialize_func(self):
        self.InitialVol = TissueH2O.LT_SizeFract * TissueH2O.InitialVol
        self.Vol = self.InitialVol

    def Calc_func(self):
        self.Vol_L = self.Vol / 1000.0

    def Dervs_func(self):
        self.MetabolicH2O = TissueH2O.LT_CalsFract * MetabolicH2O.Rate
        self.SweatH2O = TissueH2O.LT_SweatFract * SweatDuct.H2OOutflow
        self.InsensibleSkinH2O = TissueH2O.LT_SkinFract * HeatInsensibleSkin.H2O
        self.InsensibleLungH2O = TissueH2O.LT_LungFract * HeatInsensibleLung.H2O
        self.Gain = LT_CapillaryWater.Rate + self.MetabolicH2O
        self.Loss = LT_LymphWater.Rate + self.SweatH2O + self.InsensibleSkinH2O + self.InsensibleLungH2O
        self.Change = self.Gain - self.Loss
        self.Vol = diffeq( self.Change, System.Dx, self.Vol, 98.0)


class MT_CapillaryProtein:
    def __init__(self):
        self.Rate = None
        self.Gradient = None
        self.Perm = 0.44

    def Dervs_func(self):
        self.Gradient = PlasmaProtein.conc_Protein - MT_InterstitialProtein.conc_Protein
        self.Rate = self.Perm * self.Gradient

class CapillaryProtein:
    def __init__(self):
        self.Rate = None

    def Dervs_func(self):
        UT_CapillaryProtein.Dervs_func()
        MT_CapillaryProtein.Dervs_func()
        LT_CapillaryProtein.Dervs_func()
        self.Rate = UT_CapillaryProtein.Rate + MT_CapillaryProtein.Rate + LT_CapillaryProtein.Rate

class LT_CapillaryProtein:
    def __init__(self):
        self.Rate = None
        self.Gradient = None
        self.Perm = 0.71

    def Dervs_func(self):
        self.Gradient = PlasmaProtein.conc_Protein - LT_InterstitialProtein.conc_Protein
        self.Rate = self.Perm * self.Gradient

class UT_CapillaryProtein:
    def __init__(self):
        self.Rate = None
        self.Gradient = None
        self.Perm = 0.22

    def Dervs_func(self):
        self.Gradient = PlasmaProtein.conc_Protein - UT_InterstitialProtein.conc_Protein
        self.Rate = self.Perm * self.Gradient

class LT_LymphWater:
    def __init__(self):
        self.Rate = None
        self.PressureEffect = None
        self.NormalRate = 1.3

    def PressureFlow_curve(self, x):
        return cubic_hermite_spline(x, [-14.0, -4.0, 2.0, 6.0], [0.0, 1.0, 8.0, 25.0], [0.0, 0.1, 4.0, 0.0])

    def Dervs_func(self):
        self.PressureEffect = self.PressureFlow_curve( LT_InterstitialWater.Pressure )
        self.Rate = self.PressureEffect * self.NormalRate

class MT_LymphWater:
    def __init__(self):
        self.Rate = None
        self.PressureEffect = None
        self.NormalRate = 0.8

    def PressureFlow_curve(self, x):
        return cubic_hermite_spline(x, [-14.0, -4.0, 2.0, 6.0], [0.0, 1.0, 8.0, 25.0], [0.0, 0.1, 4.0, 0.0])

    def Dervs_func(self):
        self.PressureEffect = self.PressureFlow_curve( MT_InterstitialWater.Pressure )
        self.Rate = self.PressureEffect * self.NormalRate

class LymphWater:
    def __init__(self):
        self.Rate = None

    def Dervs_func(self):
        UT_LymphWater.Dervs_func()
        MT_LymphWater.Dervs_func()
        LT_LymphWater.Dervs_func()
        self.Rate = UT_LymphWater.Rate + MT_LymphWater.Rate + LT_LymphWater.Rate

class UT_LymphWater:
    def __init__(self):
        self.Rate = None
        self.PressureEffect = None
        self.NormalRate = 0.4

    def PressureFlow_curve(self, x):
        return cubic_hermite_spline(x, [-14.0, -4.0, 2.0, 6.0], [0.0, 1.0, 8.0, 25.0], [0.0, 0.1, 4.0, 0.0])

    def Dervs_func(self):
        self.PressureEffect = self.PressureFlow_curve( UT_InterstitialWater.Pressure )
        self.Rate = self.PressureEffect * self.NormalRate

class CellH2O:
    def __init__(self):
        self.Vol = None
        self.InitialVol = None
        self.Vol_L = None
        self.UT_Vol = None
        self.MT_Vol = None
        self.LT_Vol = None

    def Initialize_func(self):
        self.InitialVol = ICFV.InitialVol - RBCH2O.InitialVol

    def Calc_func(self):
        self.Vol = ICFV.Vol - RBCH2O.Vol
        self.Vol_L = self.Vol / 1000.0
        self.UT_Vol = TissueH2O.UT_SizeFract * self.Vol
        self.MT_Vol = TissueH2O.MT_SizeFract * self.Vol
        self.LT_Vol = TissueH2O.LT_SizeFract * self.Vol

class UT_LymphProtein:
    def __init__(self):
        self.Rate = None

    def Dervs_func(self):
        self.Rate = UT_InterstitialProtein.conc_Protein * UT_LymphWater.Rate

class MT_LymphProtein:
    def __init__(self):
        self.Rate = None

    def Dervs_func(self):
        self.Rate = MT_InterstitialProtein.conc_Protein * MT_LymphWater.Rate

class LT_LymphProtein:
    def __init__(self):
        self.Rate = None

    def Dervs_func(self):
        self.Rate = LT_InterstitialProtein.conc_Protein * LT_LymphWater.Rate

class LymphProtein:
    def __init__(self):
        self.Rate = None

    def Dervs_func(self):
        UT_LymphProtein.Dervs_func()
        MT_LymphProtein.Dervs_func()
        LT_LymphProtein.Dervs_func()
        self.Rate = UT_LymphProtein.Rate + MT_LymphProtein.Rate + LT_LymphProtein.Rate

class LT_InterstitialWater:
    def __init__(self):
        self.Vol = None
        self.Vol_L = None
        self.Pressure = None

    def PressureVolume_curve(self, x):
        return cubic_hermite_spline(x, [600.0, 3000.0, 4000.0, 6000.0], [-30.0, -4.8, -4.0, 50.0], [0.02, 0.0004, 0.0004, 0.03])

    def Calc_func(self):
        self.Vol = LT_H2O.Vol - CellH2O.LT_Vol
        self.Vol_L = self.Vol / 1000.0
        self.Pressure = self.PressureVolume_curve( self.Vol )

class MT_InterstitialWater:
    def __init__(self):
        self.Vol = None
        self.Vol_L = None
        self.Pressure = None

    def PressureVolume_curve(self, x):
        return cubic_hermite_spline(x, [1200.0, 4800.0, 12000.0, 24000.0], [-30.0, -4.8, 0.0, 50.0], [0.01, 0.0004, 0.0004, 0.01])

    def Calc_func(self):
        self.Vol = MT_H2O.Vol - CellH2O.MT_Vol
        self.Vol_L = self.Vol / 1000.0
        self.Pressure = self.PressureVolume_curve( self.Vol )

class UT_InterstitialWater:
    def __init__(self):
        self.Vol = None
        self.Vol_L = None
        self.Pressure = None

    def PressureVolume_curve(self, x):
        return cubic_hermite_spline(x, [600.0, 2000.0, 5000.0, 12000.0], [-30.0, -4.8, 0.0, 50.0], [0.01, 0.0004, 0.0004, 0.01])

    def Calc_func(self):
        self.Vol = UT_H2O.Vol - CellH2O.UT_Vol
        self.Vol_L = self.Vol / 1000.0
        self.Pressure = self.PressureVolume_curve( self.Vol )

class InterstitialWater:
    def __init__(self):
        self.Vol = None
        self.InitialVol = None
        self.Vol_L = None

    def Initialize_func(self):
        self.InitialVol = ECFV.InitialVol - PlasmaVol.InitialVol - ExternalH2O.InitialCore

    def Calc_func(self):
        UT_InterstitialWater.Calc_func()
        MT_InterstitialWater.Calc_func()
        LT_InterstitialWater.Calc_func()
        self.Vol = UT_InterstitialWater.Vol + MT_InterstitialWater.Vol + LT_InterstitialWater.Vol
        self.Vol_L = self.Vol / 1000.0

class MT_InterstitialProtein:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.conc_Protein = None
        self.conc_Protein_GperdL = None
        self.COP = None
        self.Mass = 150.0

    def Calc_func(self):
        self.conc_Protein = self.Mass / MT_InterstitialWater.Vol
        self.conc_Protein_GperdL = 100.0 * self.conc_Protein
        Colloids.conc_Prot = self.conc_Protein
        Colloids.GetPres_func()
        self.COP = Colloids.Pres

    def Dervs_func(self):
        self.Gain = MT_CapillaryProtein.Rate
        self.Loss = MT_LymphProtein.Rate
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.75)


class UT_InterstitialProtein:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.conc_Protein = None
        self.conc_Protein_GperdL = None
        self.COP = None
        self.Mass = 75.0

    def Calc_func(self):
        self.conc_Protein = self.Mass / UT_InterstitialWater.Vol
        self.conc_Protein_GperdL = 100.0 * self.conc_Protein
        Colloids.conc_Prot = self.conc_Protein
        Colloids.GetPres_func()
        self.COP = Colloids.Pres

    def Dervs_func(self):
        self.Gain = UT_CapillaryProtein.Rate
        self.Loss = UT_LymphProtein.Rate
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.75)


class LT_InterstitialProtein:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.conc_Protein = None
        self.conc_Protein_GperdL = None
        self.COP = None
        self.Mass = 75.0

    def Calc_func(self):
        self.conc_Protein = self.Mass / LT_InterstitialWater.Vol
        self.conc_Protein_GperdL = 100.0 * self.conc_Protein
        Colloids.conc_Prot = self.conc_Protein
        Colloids.GetPres_func()
        self.COP = Colloids.Pres

    def Dervs_func(self):
        self.Gain = LT_CapillaryProtein.Rate
        self.Loss = LT_LymphProtein.Rate
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.75)


class InterstitialProtein:
    def __init__(self):
        self.Mass = None
        self.Change = None
        self.Gain = None
        self.Loss = None

    def Calc_func(self):
        UT_InterstitialProtein.Calc_func()
        MT_InterstitialProtein.Calc_func()
        LT_InterstitialProtein.Calc_func()
        self.Mass = UT_InterstitialProtein.Mass + MT_InterstitialProtein.Mass + LT_InterstitialProtein.Mass

    def Dervs_func(self):
        UT_InterstitialProtein.Dervs_func()
        MT_InterstitialProtein.Dervs_func()
        LT_InterstitialProtein.Dervs_func()
        self.Gain = UT_InterstitialProtein.Gain + MT_InterstitialProtein.Gain + LT_InterstitialProtein.Gain
        self.Loss = UT_InterstitialProtein.Loss + MT_InterstitialProtein.Loss + LT_InterstitialProtein.Loss
        self.Change = self.Gain - self.Loss

class UT_CapillaryWater:
    def __init__(self):
        self.Rate = None
        self.Gradient = None
        self.Perm = 1.0

    def Dervs_func(self):
        self.Gradient = RegionalPressure.UpperCapy - UT_InterstitialWater.Pressure + UT_InterstitialProtein.COP - PlasmaProtein.COP
        self.Rate = self.Perm * self.Gradient

class CapillaryWater:
    def __init__(self):
        self.Rate = None

    def Dervs_func(self):
        UT_CapillaryWater.Dervs_func()
        MT_CapillaryWater.Dervs_func()
        LT_CapillaryWater.Dervs_func()
        self.Rate = UT_CapillaryWater.Rate + MT_CapillaryWater.Rate + LT_CapillaryWater.Rate

class LT_CapillaryWater:
    def __init__(self):
        self.Rate = None
        self.Gradient = None
        self.Perm = 0.27

    def Dervs_func(self):
        self.Gradient = RegionalPressure.UpperCapy - LT_InterstitialWater.Pressure + LT_InterstitialProtein.COP - PlasmaProtein.COP
        self.Rate = self.Perm * self.Gradient

class MT_CapillaryWater:
    def __init__(self):
        self.Rate = None
        self.Gradient = None
        self.Perm = 0.44

    def Dervs_func(self):
        self.Gradient = RegionalPressure.UpperCapy - MT_InterstitialWater.Pressure + MT_InterstitialProtein.COP - PlasmaProtein.COP
        self.Rate = self.Perm * self.Gradient

class PeritoneumSpace:
    def __init__(self):
        self.InitialVolume = None
        self.Volume_L = None
        self.Gain = None
        self.Loss = None
        self.InflowPerm = 0.9
        self.OutflowPerm = 1.5
        self.InflowGrad = None
        self.OutflowGrad = None
        self.Pressure = None
        self.Compliance = 760.0
        self.ExternalPressure = 9.0
        self.Volume = 0.0

    def Initialize_func(self):
        self.InitialVolume = 0.0
        self.Volume = self.InitialVolume

    def Dervs_func(self):
        self.Volume_L = self.Volume / 1000.0
        self.Pressure = ( self.Volume / self.Compliance ) + self.ExternalPressure
        self.InflowGrad = SplanchnicVeins.Pressure - self.Pressure
        self.Gain = ( max( ( self.InflowGrad * self.InflowPerm ), 0.0) )
        self.OutflowGrad = self.Pressure - self.ExternalPressure
        self.Loss = ( max( ( self.OutflowGrad * self.OutflowPerm ), 0.0) )
        self.Change = self.Gain - self.Loss
        self.Volume = diffeq( self.Change, System.Dx, self.Volume, 10.0)


class Peritoneum:

    def Dervs_func(self):
        PeritoneumSpace.Dervs_func()
        PeritoneumProtein.Dervs_func()

class PeritoneumProtein:
    def __init__(self):
        self.conc_Protein = None
        self.Gain = None
        self.Loss = None
        self.Mass = 0.0

    def Dervs_func(self):
        if PeritoneumSpace.Volume > 0.0:
            self.conc_Protein = self.Mass / PeritoneumSpace.Volume
        else:
            self.conc_Protein = 0.0

        self.Gain = PeritoneumSpace.Gain * PlasmaProtein.conc_Protein
        self.Loss = PeritoneumSpace.Loss * self.conc_Protein
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 10.0)


class GlycerolPool:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.conc_Glycerol = None
        self.conc_Glycerol_mGperdL = None
        self.conc_Glycerol_mMolperL = None
        self.PER_ML_TO_PER_DL = 100.0
        self.MG_TO_MMOL = 10.86
        self.FFA_TO_GLY = 0.13
        self.Synthesis = None
        self.conc_GlycerolEffect = None
        self.BasicSynthesis = 1.5
        self.AdiposeFFAUptake = None
        self.Degradation = None
        self.K = 0.001
        self.GutFAAbsorption = None
        self.LiverFARelease = None
        self.TriglycerideHydrolysis = None
        self.Mass = 1500.0

    def conc_GlycerolEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.1, 0.2], [2.0, 1.0, 0.0], [0.0, -20.0, 0.0])

    def CalcConc_func(self):
        self.conc_Glycerol = self.Mass / ECFV.Vol
        self.conc_Glycerol_mGperdL = self.PER_ML_TO_PER_DL * self.conc_Glycerol
        self.conc_Glycerol_mMolperL = self.MG_TO_MMOL * self.conc_Glycerol

    def Dervs_func(self):
        self.conc_GlycerolEffect = self.conc_GlycerolEffect_curve( self.conc_Glycerol )
        self.Synthesis = self.BasicSynthesis * self.conc_GlycerolEffect
        self.Degradation = self.K * self.Mass
        self.GutFAAbsorption = self.FFA_TO_GLY * GILumenFat.Absorption
        self.LiverFARelease = self.FFA_TO_GLY * LM_FattyAcids.Release
        self.TriglycerideHydrolysis = TriglycerideHydrolysis.GlycerolRate
        self.Gain = self.Synthesis + self.TriglycerideHydrolysis
        self.Loss = self.Degradation + self.GutFAAbsorption + self.LiverFARelease
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 15.0)


class Glycerol:
    def __init__(self):
        pass
    
class Metabolism_RespiratoryQuotient:
    def __init__(self):
        self.RQ = 0.8
    
class Metabolism_MetabolicRate:
    def __init__(self):
        self.Total_CalperMin = None
        self.Total_CalperDay = None
        self.Total_kCalperMin = None
        self.Total_kCalperDay = None
        self.BMRUnits = None
        self.BMRNormal = 36.9
        self.BMR_percent = None
        self.Net_CalperMin = None
        self.Net_kCalperDay = None
        self.Watts = None

    def Calc_func(self):
        self.Total_CalperMin = Metabolism_CaloriesUsed.Total
        self.Total_kCalperMin = 0.001 * self.Total_CalperMin
        self.Total_CalperDay = 1440.0 * self.Total_CalperMin
        self.Total_kCalperDay = 1440.0 * self.Total_kCalperMin
        self.BMRUnits = 60.0 * self.Total_kCalperMin / SurfaceArea.Area
        self.BMR_percent = 100.0 * ( ( self.BMRUnits / self.BMRNormal ) - 1.0 )
        self.Watts = Metabolism_Tools.KCAL_MIN_TO_WATT * self.Total_kCalperMin
        self.Net_CalperMin = DietIntakeNutrition.Total_CalperMin - self.Total_CalperMin
        self.Net_kCalperDay = DietIntakeNutrition.Total_kCalperDay - self.Total_kCalperDay

class Metabolism_Tools:
    def __init__(self):
        self.CalToO2 = 0.2093
        self.O2ToCal = 4.778
        self.FatCalToCO2 = 0.1465
        self.CarboCalToCO2 = 0.2093
        self.WattToKPM = 6.12
        self.CAL_MIN_TO_KCAL_DAY = 1.44
        self.CAL_MIN_TO_WATT = 0.0697
        self.KCAL_MIN_TO_WATT = 69.7
        self.WATT_TO_CAL_MIN = 14.34
        self.WATT_TO_KCAL_MIN = 0.0143
        self.CAL_TO_JOULE = 4.19
        self.CarboAerobic_kCalperG = 4.10
        self.CarboAerobic_kCalpermG = 0.00410
        self.CarboAerobic_mGperkCal = 243.90
        self.CarboAerobic_mGperCal = 0.2439
        self.CarboAnaerobic_kCalperG = 0.1577
        self.CarboAnaerobic_kCalpermG = 0.0001577
        self.CarboAnaerobic_mGperkCal = 6341.1
        self.CarboAnaerobic_mGperCal = 6.3411
        self.Fat_kCalperG = 9.3
        self.Fat_kCalpermG = 0.0093
        self.Fat_mGperkCal = 107.5
        self.Fat_mGperCal = 0.1075
        self.Protein_kCalperG = 4.35
        self.Lac__kCalperG = 3.94
        self.Lac__mGperCal = 0.2538
        self.Carbo_CalpermG = 4.10
        self.Fat_CalpermG = 9.3
        self.Protein_CalpermG = 4.35
    
class Thyroid:
    def __init__(self):
        self.Effect = None

    def Effect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 8.0, 40.0], [0.7, 1.0, 1.5], [0.0, 0.4, 0.0])

    def CalcEffect_func(self):
        self.Effect = self.Effect_curve( ThyroidPool.conc_Total_T4_T3 )

class Metabolism:
    def __init__(self):
        pass
    
class Metabolism_FattyAcid:
    def __init__(self):
        self.TotalBurn = None

    def Calc_func(self):
        self.TotalBurn = Bone_Fuel.FAUsed_mGperMin + Fat_Fuel.FAUsed_mGperMin + GITract_Fuel.FAUsed_mGperMin + Kidney_Fuel.FAUsed_mGperMin + LeftHeart_Fuel.FAUsed_mGperMin + Liver_Fuel.FAUsed_mGperMin + OtherTissue_Fuel.FAUsed_mGperMin + RespiratoryMuscle_Fuel.FAUsed_mGperMin + RightHeart_Fuel.FAUsed_mGperMin + SkeletalMuscle_Fuel.FAUsed_mGperMin + Skin_Fuel.FAUsed_mGperMin

class Metabolism_Glucose:
    def __init__(self):
        self.TotalBurn = None
        self.GlucoseBurn = None
        self.GlycogenBurn = None
        self.TotalUptake = None
        self.GlucoseUptake = None
        self.GlycogenUptake = None

    def Calc_func(self):
        self.GlucoseBurn = Bone_Fuel.TotalGlucoseUsed_mGperMin + Brain_Fuel.TotalGlucoseUsed_mGperMin + Fat_Fuel.TotalGlucoseUsed_mGperMin + GITract_Fuel.TotalGlucoseUsed_mGperMin + Kidney_Fuel.TotalGlucoseUsed_mGperMin + LeftHeart_Fuel.TotalGlucoseUsed_mGperMin + Liver_Fuel.TotalGlucoseUsed_mGperMin + OtherTissue_Fuel.TotalGlucoseUsed_mGperMin + RespiratoryMuscle_Fuel.AerobicGlucoseUsed_mGperMin + RightHeart_Fuel.TotalGlucoseUsed_mGperMin + SkeletalMuscle_Fuel.AerobicGlucoseUsed_mGperMin + Skin_Fuel.TotalGlucoseUsed_mGperMin
        self.GlycogenBurn = RespiratoryMuscle_Glycogen.Metabolism + SkeletalMuscle_Glycogen.Metabolism
        self.TotalBurn = self.GlucoseBurn + self.GlycogenBurn
        self.GlucoseUptake = self.GlucoseBurn
        self.GlycogenUptake = RespiratoryMuscle_Glycogen.Synthesis + SkeletalMuscle_Glycogen.Synthesis
        self.TotalUptake = self.GlucoseUptake + self.GlycogenUptake

class Metabolism_FuelUse:
    def __init__(self):
        self.GlycerolTotal = None
        self.GlycerolUptake = None
        self.GlycerolStored = None

    def Calc_func(self):
        self.GlycerolUptake = 0.0
        self.GlycerolStored = 0.0
        self.GlycerolTotal = self.GlycerolUptake + self.GlycerolStored

class Metabolism_CaloriesUsed:
    def __init__(self):
        self.Total = None
        self.Total_kCalperMin = None
        self.TotalHeat = None
        self.TotalHeat_kCalperMin = None
        self.TotalMotion = None
        self.TotalMotion_kCalperMin = None
        self.CoreHeat = None
        self.CoreHeat_kCalperMin = None
        self.CoreMotion = None
        self.CoreMotion_kCalperMin = None
        self.SkeletalMuscleHeat = None
        self.SkeletalMuscleHeat_kCalperMin = None
        self.SkeletalMuscleMotion = None
        self.SkeletalMuscleMotion_kCalperMin = None
        self.SkinHeat = None
        self.SkinHeat_kCalperMin = None
        self.SkinMotion = None
        self.SkinMotion_kCalperMin = None

    def Calc_func(self):
        self.CoreMotion = RespiratoryMuscle_Work.MotionCals + RightHeart_Work.MotionCals + LeftHeart_Work.MotionCals
        self.CoreMotion_kCalperMin = self.CoreMotion / 1000.0
        self.CoreHeat = Brain_Metabolism.TotalCalsUsed + Bone_Metabolism.TotalCalsUsed + Fat_Metabolism.TotalCalsUsed + GITract_Metabolism.TotalCalsUsed + Kidney_Metabolism.TotalCalsUsed + LeftHeart_Metabolism.TotalCalsUsed + Liver_Metabolism.TotalCalsUsed + OtherTissue_Metabolism.TotalCalsUsed + RespiratoryMuscle_Metabolism.TotalCalsUsed + RightHeart_Metabolism.TotalCalsUsed - self.CoreMotion
        self.CoreHeat_kCalperMin = self.CoreHeat / 1000.0
        self.SkeletalMuscleMotion = SkeletalMuscle_Work.MotionCals
        self.SkeletalMuscleMotion_kCalperMin = self.SkeletalMuscleMotion / 1000.0
        self.SkeletalMuscleHeat = SkeletalMuscle_Metabolism.TotalCalsUsed - self.SkeletalMuscleMotion
        self.SkeletalMuscleHeat_kCalperMin = self.SkeletalMuscleHeat / 1000.0
        self.SkinMotion = 0.0
        self.SkinMotion_kCalperMin = self.SkinMotion / 1000.0
        self.SkinHeat = Skin_Metabolism.TotalCalsUsed
        self.SkinHeat_kCalperMin = self.SkinHeat / 1000.0
        self.TotalHeat = self.CoreHeat + self.SkeletalMuscleHeat + self.SkinHeat
        self.TotalHeat_kCalperMin = self.TotalHeat / 1000.0
        self.TotalMotion = self.CoreMotion + self.SkeletalMuscleMotion + self.SkinMotion
        self.TotalMotion_kCalperMin = self.TotalMotion / 1000.0
        self.Total = self.TotalHeat + self.TotalMotion
        self.Total_kCalperMin = self.Total / 1000.0

class OsmCell:
    def __init__(self):
        self.Total = None
        self.Electrolytes = None
        self.Anions = None
        self.Cations = None
        self.OtherCations = 692.0
        self.Non_Electrolytes = None
        self.UnknownOsmoles = 354.0

    def Calc_func(self):
        self.Cations = KCell.Mass + self.OtherCations
        self.Anions = self.Cations - 1000.0
        self.Non_Electrolytes = UreaCell.Osmoles + self.UnknownOsmoles
        self.Electrolytes = self.Cations + self.Anions
        self.Total = self.Electrolytes + self.Non_Electrolytes

class Osmoles:
    def __init__(self):
        pass
    
class OsmBody:
    def __init__(self):
        self.Total = None
        self.Electrolytes = None
        self.Non_Electrolytes = None
        self.conc_Osm_CellWall = None
        self.conc_Osm_mOsmperL_CellWall = None
        self.conc_Osm_Osmoreceptors = None
        self.conc_Osm_mOsmperL_Osmoreceptors = None
        self.Dissociation = 0.890
        self.ECFVActiveElectrolytes = None
        self.ICFVActiveElectrolytes = None
        self.ActiveElectrolytes = None
        self.ECFVActiveOsmoles = None
        self.ICFVActiveOsmoles = None
        self.ActiveOsmoles = None
        self.ECFV = None
        self.ECFV_L = None
        self.ICFV = None
        self.ICFV_L = None

    def Calc_func(self):
        self.Electrolytes = OsmECFV.Electrolytes + OsmCell.Electrolytes
        self.Non_Electrolytes = OsmECFV.Non_Electrolytes + OsmCell.Non_Electrolytes
        self.Total = self.Electrolytes + self.Non_Electrolytes
        self.ECFVActiveElectrolytes = self.Dissociation * OsmECFV.Electrolytes
        self.ICFVActiveElectrolytes = self.Dissociation * OsmCell.Electrolytes
        self.ActiveElectrolytes = self.ECFVActiveElectrolytes + self.ICFVActiveElectrolytes
        self.ECFVActiveOsmoles = self.ECFVActiveElectrolytes + OsmECFV.Non_Electrolytes
        self.ICFVActiveOsmoles = self.ICFVActiveElectrolytes + OsmCell.Non_Electrolytes
        self.ActiveOsmoles = self.ECFVActiveOsmoles + self.ICFVActiveOsmoles
        self.conc_Osm_CellWall = self.ActiveOsmoles / BodyH2O.Vol
        self.conc_Osm_mOsmperL_CellWall = 1000.0 * self.conc_Osm_CellWall
        self.conc_Osm_Osmoreceptors = self.ActiveElectrolytes / BodyH2O.Vol
        self.conc_Osm_mOsmperL_Osmoreceptors = 1000.0 * self.conc_Osm_Osmoreceptors
        self.ICFV = ( self.ICFVActiveOsmoles / self.ActiveOsmoles ) * BodyH2O.Vol
        self.ICFV_L = self.ICFV / 1000.0
        self.ECFV = BodyH2O.Vol - self.ICFV
        self.ECFV_L = self.ECFV / 1000.0

class OsmECFV:
    def __init__(self):
        self.Total = None
        self.Electrolytes = None
        self.Anions = None
        self.OtherAnions = 373.0
        self.Cations = None
        self.Non_Electrolytes = None
        self.UnknownOsmoles = 340.0

    def Calc_func(self):
        self.Cations = NaPool.Mass + KPool.Mass
        self.Anions = ClPool.Mass + LacPool.Mass + KAPool.Osmoles + SO4Pool.Osmoles + PO4Pool.Osmoles + self.OtherAnions
        self.Non_Electrolytes = GlucosePool.Osmoles + UreaPool.Osmoles + self.UnknownOsmoles
        self.Electrolytes = self.Cations + self.Anions
        self.Total = self.Electrolytes + self.Non_Electrolytes

class conc_EPODelay:
    def __init__(self):
        self.Tau = 3.0
        self.Effect = 1.0

    def SteadyState_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.3, 4.0], [0.0, 1.0, 4.0], [0.0, 1.0, 0.0])

    def Parms_func(self):
        self.K = ( 1 / ( 1440.0 * self.Tau ) )

    def Dervs_func(self):
        self.SteadyState = self.SteadyState_curve( EPOPool.Log10Conc )
        self.Effect = delay( self.K, self.SteadyState, self.Effect, System.Dx, 0.01)


class RBCSecretion:
    def __init__(self):
        self.Rate = None
        self.Base = 0.014

    def Dervs_func(self):
        if not Bone_Function.Failed:
            self.Rate = self.Base * conc_EPODelay.Effect
        else:
            self.Rate = 0.0


class PlasmaVol:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.InitialVol = None
        self.Vol_L = None

    def Initialize_func(self):
        self.InitialVol = BloodVol.InitialPVCrit * BloodVol.InitialVol
        self.Vol = self.InitialVol

    def CalcVol_func(self):
        self.Vol_L = self.Vol / 1000.0

    def Dervs_func(self):
        self.Gain = GILumenVolume.Absorption + LymphWater.Rate + IVDrip.H2ORate + ExcessLungWater.Flux + PeritoneumSpace.Loss + Transfusion.PlasmaRate
        self.Loss = CD_H2O.Outflow + CapillaryWater.Rate + ExcessLungWater.Flux + PeritoneumSpace.Gain + Hemorrhage.PlasmaRate + Pericardium_Hemorrhage.PlasmaFlow
        self.Change = self.Gain - self.Loss
        self.Vol = diffeq( self.Change, System.Dx, self.Vol, 30.0)


class BloodVol:
    def __init__(self):
        self.Vol = None
        self.InitialVol = None
        self.Vol_L = None
        self.Change = None
        self.Gain = None
        self.Loss = None
        self.Hct = None
        self.InitialHct = None
        self.Hct_percent = None
        self.InitialHct_Male = 0.44
        self.InitialHct_Female = 0.40
        self.PVCrit = None
        self.InitialPVCrit = None
        self.StressedVol = None
        self.V0 = None
        self.Collapsed = None
        self.CollapsedEffect = None
        self.TextbookVolume = 5400.0

    def Initialize_func(self):
        self.InitialVol = Start_General.X_Textbook * self.TextbookVolume
        if Gender.IsMale:
            self.InitialHct = self.InitialHct_Male
        else:
            self.InitialHct = self.InitialHct_Female

        self.InitialPVCrit = 1.0 - self.InitialHct

    def CalcVol_func(self):
        self.Vol = RBCVol.Vol + PlasmaVol.Vol
        self.Vol_L = self.Vol / 1000.0
        self.Hct = RBCVol.Vol / self.Vol
        self.Hct_percent = self.Hct * 100.0
        self.PVCrit = 1.0 - self.Hct

    def CalcV0_func(self):
        self.V0 = PulmArty.V0 + PulmCapys.V0 + PulmVeins.V0 + SystemicArtys.V0 + SystemicVeins.V0 + SplanchnicVeins.V0
        self.StressedVol = self.Vol - self.V0
        if self.Vol <= self.V0:
            self.Collapsed = True
            self.CollapsedEffect = self.Vol / self.V0
        else:
            self.Collapsed = False
            self.CollapsedEffect = 1.0

    def Dervs_func(self):
        self.Gain = RBCVol.Gain + PlasmaVol.Gain
        self.Loss = RBCVol.Loss + PlasmaVol.Loss
        self.Change = self.Gain - self.Loss

class BloodVolume:

    def Parms_func(self):
        RBCClearance.Parms_func()
        conc_EPODelay.Parms_func()

    def CalcVol_func(self):
        RBCVol.CalcVol_func()
        RBCSolids.CalcVol_func()
        RBCH2O.CalcVol_func()
        PlasmaVol.CalcVol_func()
        BloodVol.CalcVol_func()

    def CalcV0_func(self):
        BloodVol.CalcV0_func()

    def Dervs_func(self):
        RBCSecretion.Dervs_func()
        RBCClearance.Dervs_func()
        conc_EPODelay.Dervs_func()
        RBCVol.Dervs_func()
        RBCH2O.Dervs_func()
        PlasmaVol.Dervs_func()
        BloodVol.Dervs_func()

class RBCVol:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.InitialVol = None
        self.Vol_L = None

    def Initialize_func(self):
        self.InitialVol = BloodVol.InitialHct * BloodVol.InitialVol
        self.Vol = self.InitialVol

    def CalcVol_func(self):
        self.Vol_L = self.Vol / 1000.0

    def Dervs_func(self):
        self.Gain = RBCSecretion.Rate + Transfusion.RBCRate
        self.Loss = RBCClearance.Rate + Hemorrhage.RBCRate + Pericardium_Hemorrhage.RBCFlow
        self.Change = self.Gain - self.Loss
        self.Vol = diffeq( self.Change, System.Dx, self.Vol, 24.0)


class RBCH2O:
    def __init__(self):
        self.Vol = None
        self.InitialVol = None
        self.Vol_L = None
        self.FractH2O = None
        self.Gain = None
        self.Loss = None
        self.Change = None

    def Initialize_func(self):
        self.FractH2O = 1.0 - RBCSolids.FractSolids
        self.InitialVol = self.FractH2O * RBCVol.InitialVol

    def CalcVol_func(self):
        self.FractH2O = 1.0 - RBCSolids.FractSolids
        self.Vol = self.FractH2O * RBCVol.Vol
        self.Vol_L = self.Vol / 1000.0

    def Dervs_func(self):
        self.Gain = self.FractH2O * RBCVol.Gain
        self.Loss = self.FractH2O * RBCVol.Loss
        self.Change = self.Gain - self.Loss

class RBCClearance:
    def __init__(self):
        self.Rate = None
        self.K = None
        self.Tau = 120.0

    def Parms_func(self):
        self.K = ( 1 / ( 1440.0 * self.Tau ) )

    def Dervs_func(self):
        self.Rate = self.K * RBCVol.Vol

class RBCSolids:
    def __init__(self):
        self.Mass = None
        self.InitialMass = None
        self.FractSolids = 0.34

    def Initialize_func(self):
        self.InitialMass = self.FractSolids * RBCVol.InitialVol

    def CalcVol_func(self):
        self.Mass = self.FractSolids * RBCVol.Vol

class TriglycerideHydrolysis:
    def __init__(self):
        self.Rate = None
        self.TriglycerideEffect = None
        self.Basic = 100.0
        self.TRIG_TO_FFA = 0.89
        self.TRIG_TO_GLY = 0.11
        self.FattyAcidRate = None
        self.GlycerolRate = None

    def TriglycerideEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 100.0, 200.0], [0.0, 1.0, 3.0], [0.0, 0.03, 0.0])

    def Rate_func(self):
        self.TriglycerideEffect = self.TriglycerideEffect_curve( TriglyceridePool.conc_Triglyceride_mGperdL )
        self.Rate = self.Basic * self.TriglycerideEffect
        self.FattyAcidRate = self.TRIG_TO_FFA * self.Rate
        self.GlycerolRate = self.TRIG_TO_GLY * self.Rate

class TriglyceridePool:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.conc_Triglyceride = None
        self.conc_Triglyceride_mGperdL = None
        self.conc_Triglyceride_mMolperL = None
        self.PER_ML_TO_PER_DL = 100.0
        self.MG_TO_MMOL = 1.24
        self.TRIG_TO_FFA = 0.89
        self.FFA_TO_TRIG = 1.12
        self.GutAbsorption = None
        self.LiverRelease = None
        self.Targetconc_Triglyceride = 1.0
        self.InitialMass = None

    def Init_func(self):
        self.InitialMass = self.Targetconc_Triglyceride * ECFV.Vol
        self.Mass = self.InitialMass

    def Conc_func(self):
        self.conc_Triglyceride = self.Mass / ECFV.Vol
        self.conc_Triglyceride_mGperdL = self.PER_ML_TO_PER_DL * self.conc_Triglyceride
        self.conc_Triglyceride_mMolperL = self.MG_TO_MMOL * self.conc_Triglyceride

    def Dervs_func(self):
        self.GutAbsorption = self.FFA_TO_TRIG * GILumenFat.Absorption
        self.LiverRelease = self.FFA_TO_TRIG * LM_FattyAcids.Release
        self.Gain = self.GutAbsorption + self.LiverRelease
        self.Loss = TriglycerideHydrolysis.Rate + TriglycerideDecomposition.Rate
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 125.0)


class Triglyceride:

    def Init_func(self):
        TriglyceridePool.Init_func()

    def Conc_func(self):
        TriglyceridePool.Conc_func()

    def Rate_func(self):
        TriglycerideHydrolysis.Rate_func()
        TriglycerideDecomposition.Rate_func()

    def Dervs_func(self):
        TriglyceridePool.Dervs_func()

class TriglycerideDecomposition:
    def __init__(self):
        self.Rate = None
        self.K = 0.0007

    def Rate_func(self):
        self.Rate = self.K * TriglyceridePool.Mass

class Organs_AlphaReceptors:

    def Calc_func(self):
        Bone_AlphaReceptors.Calc_func()
        Fat_AlphaReceptors.Calc_func()
        GITract_AlphaReceptors.Calc_func()
        Kidney_AlphaReceptors.Calc_func()
        LeftHeart_AlphaReceptors.Calc_func()
        Liver_AlphaReceptors.Calc_func()
        OtherTissue_AlphaReceptors.Calc_func()
        RespiratoryMuscle_AlphaReceptors.Calc_func()
        RightHeart_AlphaReceptors.Calc_func()
        SkeletalMuscle_AlphaReceptors.Calc_func()
        Skin_AlphaReceptors.Calc_func()

class Organs_Ph:

    def CalcSID_func(self):
        Bone_Ph.CalcSID_func()
        Brain_Ph.CalcSID_func()
        Fat_Ph.CalcSID_func()
        GITract_Ph.CalcSID_func()
        Kidney_Ph.CalcSID_func()
        LeftHeart_Ph.CalcSID_func()
        Liver_Ph.CalcSID_func()
        OtherTissue_Ph.CalcSID_func()
        RespiratoryMuscle_Ph.CalcSID_func()
        RightHeart_Ph.CalcSID_func()
        SkeletalMuscle_Ph.CalcSID_func()
        Skin_Ph.CalcSID_func()

    def CalcPh_func(self):
        Bone_Ph.CalcPh_func()
        Brain_Ph.CalcPh_func()
        Fat_Ph.CalcPh_func()
        GITract_Ph.CalcPh_func()
        Kidney_Ph.CalcPh_func()
        LeftHeart_Ph.CalcPh_func()
        Liver_Ph.CalcPh_func()
        OtherTissue_Ph.CalcPh_func()
        RespiratoryMuscle_Ph.CalcPh_func()
        RightHeart_Ph.CalcPh_func()
        SkeletalMuscle_Ph.CalcPh_func()
        Skin_Ph.CalcPh_func()

class Organs_Flow:

    def Calc_func(self):
        A_VFistula_Flow.Calc_func()
        Bone_Flow.Calc_func()
        Brain_Flow.Calc_func()
        Fat_Flow.Calc_func()
        GITract_Flow.Calc_func()
        LeftHeart_Flow.Calc_func()
        OtherTissue_Flow.Calc_func()
        RespiratoryMuscle_Flow.Calc_func()
        RightHeart_Flow.Calc_func()
        SkeletalMuscle_Flow.Calc_func()
        Skin_Flow.Calc_func()

class Organs_ScaleH2O:

    def ScaleH2O_func(self):
        Bone_Size.ScaleH2O_func()
        Brain_Size.ScaleH2O_func()
        Fat_Size.ScaleH2O_func()
        GITract_Size.ScaleH2O_func()
        Kidney_Size.ScaleH2O_func()
        LeftHeart_Size.ScaleH2O_func()
        Liver_Size.ScaleH2O_func()
        OtherTissue_Size.ScaleH2O_func()
        RespiratoryMuscle_Size.ScaleH2O_func()
        RightHeart_Size.ScaleH2O_func()
        SkeletalMuscle_Size.ScaleH2O_func()
        Skin_Size.ScaleH2O_func()

class Organs_ScaleConductance:

    def Calc_func(self):
        Bone_Flow.Initialize_func()

class Organs_Fuel:

    def Dervs_func(self):
        Bone_Fuel.Dervs_func()
        Brain_Fuel.Dervs_func()
        Fat_Fuel.Dervs_func()
        GITract_Fuel.Dervs_func()
        Kidney_Fuel.Dervs_func()
        LeftHeart_Fuel.Dervs_func()
        OtherTissue_Fuel.Dervs_func()
        RespiratoryMuscle_Fuel.Dervs_func()
        RightHeart_Fuel.Dervs_func()
        SkeletalMuscle_Fuel.Dervs_func()
        Skin_Fuel.Dervs_func()

class Organs_Pressure:

    def Calc_func(self):
        A_VFistula_Pressure.Calc_func()
        Bone_Pressure.Calc_func()
        Brain_Pressure.Calc_func()
        Fat_Pressure.Calc_func()
        GITract_Pressure.Calc_func()
        Kidney_Pressure.Calc_func()
        LeftHeart_Pressure.Calc_func()
        OtherTissue_Pressure.Calc_func()
        RespiratoryMuscle_Pressure.Calc_func()
        RightHeart_Pressure.Calc_func()
        SkeletalMuscle_Pressure.Calc_func()
        Skin_Pressure.Calc_func()

class Organs:
    def __init__(self):
        pass
    
class Organs_Lactate:

    def CalcConc_func(self):
        Bone_Lactate.CalcConc_func()
        Brain_Lactate.CalcConc_func()
        Fat_Lactate.CalcConc_func()
        GITract_Lactate.CalcConc_func()
        Kidney_Lactate.CalcConc_func()
        LeftHeart_Lactate.CalcConc_func()
        Liver_Lactate.CalcConc_func()
        OtherTissue_Lactate.CalcConc_func()
        RespiratoryMuscle_Lactate.CalcConc_func()
        RightHeart_Lactate.CalcConc_func()
        SkeletalMuscle_Lactate.CalcConc_func()
        Skin_Lactate.CalcConc_func()

    def CalcDervs_func(self):
        Bone_Lactate.CalcDervs_func()
        Brain_Lactate.CalcDervs_func()
        Fat_Lactate.CalcDervs_func()
        GITract_Lactate.CalcDervs_func()
        Kidney_Lactate.CalcDervs_func()
        LeftHeart_Lactate.CalcDervs_func()
        Liver_Lactate.CalcDervs_func()
        OtherTissue_Lactate.CalcDervs_func()
        RespiratoryMuscle_Lactate.CalcDervs_func()
        RightHeart_Lactate.CalcDervs_func()
        SkeletalMuscle_Lactate.CalcDervs_func()
        Skin_Lactate.CalcDervs_func()

class Organs_Vasculature:

    def Parms_func(self):
        Bone_Vasculature.Parms_func()
        Brain_Vasculature.Parms_func()
        Fat_Vasculature.Parms_func()
        GITract_Vasculature.Parms_func()
        LeftHeart_Vasculature.Parms_func()
        OtherTissue_Vasculature.Parms_func()
        RespiratoryMuscle_Vasculature.Parms_func()
        RightHeart_Vasculature.Parms_func()
        SkeletalMuscle_Vasculature.Parms_func()
        Skin_Vasculature.Parms_func()

    def Calc_func(self):
        Bone_Vasculature.Calc_func()
        Brain_Vasculature.Calc_func()
        Fat_Vasculature.Calc_func()
        GITract_Vasculature.Calc_func()
        LeftHeart_Vasculature.Calc_func()
        OtherTissue_Vasculature.Calc_func()
        RespiratoryMuscle_Vasculature.Calc_func()
        RightHeart_Vasculature.Calc_func()
        SkeletalMuscle_Vasculature.Calc_func()
        Skin_Vasculature.Calc_func()

class Organs_Function:

    def Calc_func(self):
        Bone_Function.Calc_func()
        Fat_Function.Calc_func()
        GITract_Function.Calc_func()
        Kidney_Function.Calc_func()
        LeftHeart_Function.Calc_func()
        Liver_Function.Calc_func()
        OtherTissue_Function.Calc_func()
        RespiratoryMuscle_Function.Calc_func()
        RightHeart_Function.Calc_func()
        SkeletalMuscle_Function.Calc_func()
        Skin_Function.Calc_func()

    def Wrapup_func(self):
        Bone_Function.Wrapup_func()
        Brain_Function.Wrapup_func()
        Fat_Function.Wrapup_func()
        GITract_Function.Wrapup_func()
        Kidney_Function.Wrapup_func()
        LeftHeart_Function.Wrapup_func()
        Liver_Function.Wrapup_func()
        OtherTissue_Function.Wrapup_func()
        RespiratoryMuscle_Function.Wrapup_func()
        RightHeart_Function.Wrapup_func()
        SkeletalMuscle_Function.Wrapup_func()
        Skin_Function.Wrapup_func()

class Organs_Structure:

    def Calc_func(self):
        Bone_Structure.Calc_func()
        Brain_Structure.Calc_func()
        Fat_Structure.Calc_func()
        GITract_Structure.Calc_func()
        Kidney_Structure.Calc_func()
        LeftHeart_Structure.Calc_func()
        Liver_Structure.Calc_func()
        OtherTissue_Structure.Calc_func()
        RespiratoryMuscle_Structure.Calc_func()
        RightHeart_Structure.Calc_func()
        SkeletalMuscle_Structure.Calc_func()
        Skin_Structure.Calc_func()

class Organs_ScaleCals:

    def Calc_func(self):
        Bone_Metabolism.ScaleCals_func()
        Brain_Metabolism.ScaleCals_func()
        Fat_Metabolism.ScaleCals_func()
        GITract_Metabolism.ScaleCals_func()
        Kidney_Metabolism.ScaleCals_func()
        LeftHeart_Metabolism.ScaleCals_func()
        Liver_Metabolism.ScaleCals_func()
        OtherTissue_Metabolism.ScaleCals_func()
        RespiratoryMuscle_Metabolism.ScaleCals_func()
        RightHeart_Metabolism.ScaleCals_func()
        SkeletalMuscle_Metabolism.ScaleCals_func()
        Skin_Metabolism.ScaleCals_func()

class Organs_Metabolism:

    def CalcCals_func(self):
        Bone_Metabolism.CalcCals_func()
        Brain_Metabolism.CalcCals_func()
        Fat_Metabolism.CalcCals_func()
        GITract_Metabolism.CalcCals_func()
        Kidney_Metabolism.CalcCals_func()
        LeftHeart_Metabolism.CalcCals_func()
        Liver_Metabolism.CalcCals_func()
        OtherTissue_Metabolism.CalcCals_func()
        RespiratoryMuscle_Metabolism.CalcCals_func()
        RightHeart_Metabolism.CalcCals_func()
        SkeletalMuscle_Metabolism.CalcCals_func()
        Skin_Metabolism.CalcCals_func()

    def SplitCals_func(self):
        Bone_Metabolism.SplitCals_func()
        Brain_Metabolism.SplitCals_func()
        Fat_Metabolism.SplitCals_func()
        GITract_Metabolism.SplitCals_func()
        Kidney_Metabolism.SplitCals_func()
        LeftHeart_Metabolism.SplitCals_func()
        Liver_Metabolism.SplitCals_func()
        OtherTissue_Metabolism.SplitCals_func()
        RespiratoryMuscle_Metabolism.SplitCals_func()
        RightHeart_Metabolism.SplitCals_func()
        SkeletalMuscle_Metabolism.SplitCals_func()
        Skin_Metabolism.SplitCals_func()

class Organs_CO2:

    def CalcConc_func(self):
        Bone_CO2.CalcConc_func()
        Brain_CO2.CalcConc_func()
        Fat_CO2.CalcConc_func()
        GITract_CO2.CalcConc_func()
        Kidney_CO2.CalcConc_func()
        LeftHeart_CO2.CalcConc_func()
        Liver_CO2.CalcConc_func()
        OtherTissue_CO2.CalcConc_func()
        RespiratoryMuscle_CO2.CalcConc_func()
        RightHeart_CO2.CalcConc_func()
        SkeletalMuscle_CO2.CalcConc_func()
        Skin_CO2.CalcConc_func()

    def CalcDervs_func(self):
        Bone_CO2.CalcDervs_func()
        Brain_CO2.CalcDervs_func()
        Fat_CO2.CalcDervs_func()
        GITract_CO2.CalcDervs_func()
        Kidney_CO2.CalcDervs_func()
        LeftHeart_CO2.CalcDervs_func()
        Liver_CO2.CalcDervs_func()
        OtherTissue_CO2.CalcDervs_func()
        RespiratoryMuscle_CO2.CalcDervs_func()
        RightHeart_CO2.CalcDervs_func()
        SkeletalMuscle_CO2.CalcDervs_func()
        Skin_CO2.CalcDervs_func()

class Organs_Size:

    def Calc_func(self):
        Bone_Size.Calc_func()
        Brain_Size.Calc_func()
        Fat_Size.Calc_func()
        GITract_Size.Calc_func()
        Kidney_Size.Calc_func()
        LeftHeart_Size.Calc_func()
        Liver_Size.Calc_func()
        OtherTissue_Size.Calc_func()
        RespiratoryMuscle_Size.Calc_func()
        RightHeart_Size.Calc_func()
        SkeletalMuscle_Size.Calc_func()
        Skin_Size.Calc_func()

class Organs_BetaReceptors:

    def Calc_func(self):
        Kidney_BetaReceptors.Calc_func()
        LeftHeart_BetaReceptors.Calc_func()
        RightHeart_BetaReceptors.Calc_func()
        SANode_BetaReceptors.Calc_func()

class DietGoalElectrolytes:
    def __init__(self):
        self.Na__mEqperDay = 180.0
        self.Cl__mEqperDay = 200.0
        self.K__mEqperDay = 70.0
        self.PO4__mEqperDay = 30.0
        self.SO4__mEqperDay = 50.0
    
class DietIntakeElectrolytes:
    def __init__(self):
        self.Na__mEqperMin = None
        self.Cl__mEqperMin = None
        self.K__mEqperMin = None
        self.PO4__mEqperMin = None
        self.SO4__mEqperMin = None
        self.Intake_xGoal = None

    def Dervs_func(self):
        if Brain_Function.IsReallyDead:
            self.Na__mEqperMin = 0.0
            self.Cl__mEqperMin = 0.0
            self.K__mEqperMin = 0.0
            self.PO4__mEqperMin = 0.0
            self.SO4__mEqperMin = 0.0
        else:
            self.Intake_xGoal = DietIntakeNutrition.Intake_xGoal
            self.Na__mEqperMin = DietFeeding.Fraction * DietGoalElectrolytes.Na__mEqperDay * self.Intake_xGoal
            self.Cl__mEqperMin = DietFeeding.Fraction * DietGoalElectrolytes.Cl__mEqperDay * self.Intake_xGoal
            self.K__mEqperMin = DietFeeding.Fraction * DietGoalElectrolytes.K__mEqperDay * self.Intake_xGoal
            self.PO4__mEqperMin = DietFeeding.Fraction * DietGoalElectrolytes.PO4__mEqperDay * self.Intake_xGoal
            self.SO4__mEqperMin = DietFeeding.Fraction * DietGoalElectrolytes.SO4__mEqperDay * self.Intake_xGoal

class DietThirst:
    def __init__(self):
        self.Rate_LperDay = None

    def Rate_LperDay_curve(self, x):
        return cubic_hermite_spline(x, [233.0, 253.0, 313.0], [0.0, 2.0, 30.0], [0.0, 0.2, 0.0])

    def Dervs_func(self):
        self.Rate_LperDay = self.Rate_LperDay_curve( OsmBody.conc_Osm_mOsmperL_Osmoreceptors )

class DietFeeding:
    def __init__(self):
        self.Time = None
        self.Fraction = None

    def Dervs_func(self):
        if Status.Nutrition == 2:
            self.Time = 1440.0
            self.Fraction = ( 1 / self.Time )
        elif Status.Nutrition == 0:
            self.Time = DailyPlannerSchedule.MealCount * DailyPlannerControl.MealsDuration
            if self.Time == 0.0:
                self.Fraction = 0.0
            else:
                self.Fraction = ( 1 / self.Time )

        elif Status.Nutrition == 1:
            self.Time = DailyPlannerSchedule.MealCount * DailyPlannerControl.MealsDuration
            self.Fraction = 0.0
        elif Status.Nutrition == 3:
            self.Time = 0.0
            self.Fraction = 0.0

class DietGoalH2O:
    def __init__(self):
        self.Rate_LperDay = 2.0
        self.DegF = 70.0
        self.DegC = None
        self.DegK = None

    def Parms_func(self):
        self.DegC = ( 5 / 9 ) * ( self.DegF - 32 )
        self.DegK = self.DegC + 273.15

class DietIntakeNutrition:
    def __init__(self):
        self.Carbo_mGperMin = None
        self.Fat_mGperMin = None
        self.Protein_mGperMin = None
        self.Total_mGperMin = None
        self.query_Fixed = False
        self.FixedIntake_xGoal = 1.0
        self.Intake_xGoal = None
        self.Carbo_CalperMin = None
        self.Fat_CalperMin = None
        self.Protein_CalperMin = None
        self.Total_CalperMin = None
        self.Total_kCalperDay = None

    def Dervs_func(self):
        if Brain_Function.IsReallyDead:
            self.Carbo_mGperMin = 0.0
            self.Fat_mGperMin = 0.0
            self.Protein_mGperMin = 0.0
            self.DailyCalories_func()
        else:
            if self.query_Fixed:
                self.Intake_xGoal = self.FixedIntake_xGoal
            else:
                self.Intake_xGoal = DietAppetite.LeptinEffect

            self.Carbo_mGperMin = 1000.0 * DietFeeding.Fraction * DietGoalNutrition.Carbo_GperDay * self.Intake_xGoal
            self.Fat_mGperMin = 1000.0 * DietFeeding.Fraction * DietGoalNutrition.Fat_GperDay * self.Intake_xGoal
            self.Protein_mGperMin = 1000.0 * DietFeeding.Fraction * DietGoalNutrition.Protein_GperDay * self.Intake_xGoal
            self.DailyCalories_func()

    def DailyCalories_func(self):
        self.Total_mGperMin = self.Carbo_mGperMin + self.Fat_mGperMin + self.Protein_mGperMin
        self.Carbo_CalperMin = self.Carbo_mGperMin * Metabolism_Tools.Carbo_CalpermG
        self.Fat_CalperMin = self.Fat_mGperMin * Metabolism_Tools.Fat_CalpermG
        self.Protein_CalperMin = self.Protein_mGperMin * Metabolism_Tools.Protein_CalpermG
        self.Total_CalperMin = self.Carbo_CalperMin + self.Fat_CalperMin + self.Protein_CalperMin
        self.Total_kCalperDay = self.Total_CalperMin * Metabolism_Tools.CAL_MIN_TO_KCAL_DAY

class DietGoalNutrition:
    def __init__(self):
        self.CARBO_KCALperG = 4.10
        self.FAT_KCALperG = 9.30
        self.PROTEIN_KCALperG = 4.35
        self.Carbo_kCalperDay = 900.0
        self.Fat_kCalperDay = 800.0
        self.Protein_kCalperDay = 500.0
        self.Total_kCalperDay = None
        self.Carbo_GperDay = None
        self.Fat_GperDay = None
        self.Protein_GperDay = None

    def Parms_func(self):
        self.Total_kCalperDay = self.Carbo_kCalperDay + self.Fat_kCalperDay + self.Protein_kCalperDay
        self.Carbo_GperDay = self.Carbo_kCalperDay / self.CARBO_KCALperG
        self.Fat_GperDay = self.Fat_kCalperDay / self.FAT_KCALperG
        self.Protein_GperDay = self.Protein_kCalperDay / self.PROTEIN_KCALperG

class Diet:

    def Parms_func(self):
        DietGoalNutrition.Parms_func()
        DietGoalH2O.Parms_func()

    def Dervs_func(self):
        DietThirst.Dervs_func()
        DietFeeding.Dervs_func()
        DietAppetite.Dervs_func()
        DietIntakeNutrition.Dervs_func()
        DietIntakeElectrolytes.Dervs_func()
        DietIntakeH2O.Dervs_func()

class DietAppetite:
    def __init__(self):
        self.LeptinEffect = None
        self.conc_Leptin_Receptor = None
        self.Block_percent = 0.0
        self.K = None

    def LeptinEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 8.0, 50.0], [3.0, 1.0, 0.0], [0.0, -0.04, 0.0])

    def Dervs_func(self):
        self.K = 1.0 - ( self.Block_percent / 100.0 )
        self.conc_Leptin_Receptor = self.K * LeptinPool.conc_Leptin_nGpermL
        self.LeptinEffect = self.LeptinEffect_curve( self.conc_Leptin_Receptor )

class DietIntakeH2O:
    def __init__(self):
        self.Rate_LperDay = None
        self.Rate_mLperMin = None
        self.query_Fixed = False

    def Dervs_func(self):
        if Brain_Function.IsReallyDead:
            self.Rate_LperDay = 0.0
            self.Rate_mLperMin = 0.0
        else:
            if self.query_Fixed:
                self.Rate_LperDay = DietGoalH2O.Rate_LperDay
            else:
                self.Rate_LperDay = DietThirst.Rate_LperDay

            self.Rate_mLperMin = 1000.0 * self.Rate_LperDay * DietFeeding.Fraction

class RightHeart_Pressure:
    def __init__(self):
        self.ArtyPressure = None
        self.VeinPressure = None
        self.PressureGradient = None
        self.PumpSwitch = False
        self.PumpSetting = 0.0

    def Calc_func(self):
        if self.PumpSwitch:
            self.ArtyPressure = self.PumpSetting
        else:
            self.ArtyPressure = SystemicArtys.Pressure

        self.VeinPressure = SystemicVeins.Pressure
        self.PressureGradient = ( max( ( self.ArtyPressure - self.VeinPressure ), 0.0) )

class RightHeart_Vasculature:
    def __init__(self):
        self.Tau = 30.0
        self.Effect = 1.0

    def PO2OnStimulus_curve(self, x):
        return cubic_hermite_spline(x, [41.0, 51.0, 61.0], [1.2, 1.0, 0.8], [0.0, -0.03, 0.0])

    def Parms_func(self):
        self.K = 1.0 / ( self.Tau * 1440.0 )

    def Calc_func(self):
        if RightHeart_Function.Failed:
            self.Stimulus = 0.0
        else:
            self.Stimulus = self.PO2OnStimulus_curve( RightHeart_Flow.PO2 )

        self.Effect = delay( self.K, self.Stimulus, self.Effect, System.Dx, None)


class RightHeart_Work:
    def __init__(self):
        self.TotalCals = None
        self.MotionCals = None
        self.HeatCals = None

    def Calc_func(self):
        self.MotionCals = 5.0
        self.HeatCals = 17.0
        self.TotalCals = self.MotionCals + self.HeatCals

class RightHeart_Size:
    def __init__(self):
        self.Vol = None
        self.Mass = None
        self.InitialMass = None
        self.Density = None
        self.LiquidMass = None
        self.LiquidDensity = 1.00
        self.LiquidVol = None
        self.InitialLiquidVol = None
        self.SolidMass = None
        self.InitialSolidMass = None
        self.ContractileProteinMass = None
        self.InitialProteinMass = None
        self.ContractileProteinDensity = 1.17
        self.OtherMass = None
        self.InitialOtherMass = None
        self.OtherDensity = 1.17
        self.ContractileProteinVol = None
        self.OtherVol = None
        self.SolidVol = None
        self.FractTotal = None
        self.IFV = None
        self.InitialIFV = None
        self.CellH2O = None
        self.InitialCellH2O = None
        self.MassFractBase = 0.00175
        self.H2OFractMass = 0.67
        self.SolidsFractMass = None
        self.OtherFractSolids = 0.30
        self.ProteinFractSolids = None

    def Initialize_func(self):
        self.InitialMass = self.MassFractBase * Weight.InitialOtherMass
        self.InitialLiquidVol = self.H2OFractMass * self.InitialMass / self.LiquidDensity
        self.SolidsFractMass = 1.0 - self.H2OFractMass
        self.InitialSolidMass = self.SolidsFractMass * self.InitialMass
        self.InitialOtherMass = self.OtherFractSolids * self.InitialSolidMass
        self.ProteinFractSolids = 1.0 - self.OtherFractSolids
        self.InitialProteinMass = self.ProteinFractSolids * self.InitialSolidMass

    def ScaleH2O_func(self):
        self.FractTotal = self.InitialLiquidVol / TissueH2O.InitialVol
        self.InitialIFV = self.FractTotal * InterstitialWater.InitialVol
        self.InitialCellH2O = self.FractTotal * CellH2O.InitialVol

    def Calc_func(self):
        self.IFV = self.FractTotal * InterstitialWater.Vol
        self.CellH2O = self.FractTotal * CellH2O.Vol
        self.LiquidVol = self.IFV + self.CellH2O
        self.LiquidMass = self.LiquidVol * self.LiquidDensity
        self.ContractileProteinMass = RightHeart_ContractileProtein.Mass
        self.OtherMass = self.InitialOtherMass
        self.SolidMass = self.ContractileProteinMass + self.OtherMass
        self.ContractileProteinVol = self.ContractileProteinMass / self.ContractileProteinDensity
        self.OtherVol = self.OtherMass / self.OtherDensity
        self.SolidVol = self.ContractileProteinVol + self.OtherVol
        self.Mass = self.LiquidMass + self.SolidMass
        self.Vol = self.LiquidVol + self.SolidVol
        self.Density = self.Mass / self.Vol

class RightHeart_Function:
    def __init__(self):
        self.Failed = False
        self.Effect = None
        self.PhEffect = None
        self.ProteinEffect = None
        self.FuelEffect = None
        self.TemperatureEffect = None

    def PhOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [6.6, 6.7], [0.0, 1.0], [0.0, 0.0])

    def ProteinOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [3000.0, 5200.0], [0.0, 1.0], [0.0, 0.0])

    def FuelOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.9], [0.0, 1.0], [0.0, 0.0])

    def TemperatureOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 37.0, 40.0, 46.0], [0.0, 1.0, 1.5, 0.0], [0.0, 0.12, 0.0, 0.0])

    def Calc_func(self):
        self.PhEffect = self.PhOnFunction_curve( RightHeart_Ph.Ph )
        self.ProteinEffect = self.ProteinOnFunction_curve( CellProtein.Mass_G )
        self.FuelEffect = self.FuelOnFunction_curve( RightHeart_Fuel.FractUseDelay )
        self.TemperatureEffect = self.TemperatureOnFunction_curve( HeatCore.Temp_C )
        self.Effect = self.PhEffect * self.ProteinEffect * self.FuelEffect * self.TemperatureEffect * RightHeart_Structure.Effect

    def Wrapup_func(self):
        if not self.Failed and ( self.Effect < 0.2 ):
            self.Failed = True
        elif self.Failed and ( self.Effect > 0.4 ):
            self.Failed = False

class RightHeart_Fuel:
    def __init__(self):
        self.FADelivered = None
        self.GlucoseDelivered = None
        self.KR = 0.026
        self.Ratio = None
        self.FAFraction = None
        self.GlucoseFraction = None
        self.FA_GlucoseFraction = None
        self.LacFraction = None
        self.FAUsed_CalperMin = None
        self.AerobicGlucoseUsed_CalperMin = None
        self.AnaerobicGlucoseUsed_CalperMin = None
        self.LacUsed_CalperMin = None
        self.FAUsed_mGperMin = None
        self.AerobicGlucoseUsed_mGperMin = None
        self.AnaerobicGlucoseUsed_mGperMin = None
        self.LacUsed_mGperMin = None
        self.TotalGlucoseUsed_mGperMin = None
        self.AnaerobicGlucoseDelivered = None
        self.FAFractionalDelivery = None
        self.AerobicGlucoseFractionalDelivery = None
        self.AnaerobicGlucoseFractionalDelivery = None
        self.MinimumFractionalDelivery = None
        self.FractUseDelay = 1.0

    def LacFraction_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 100.0], [0.0, 0.3], [0.0, 0.0])

    def Dervs_func(self):
        self.FADelivered = ( max( ( FAPool.conc_FA * RightHeart_Flow.PlasmaFlow ), 0.0) )
        self.GlucoseDelivered = ( max( ( GlucosePool.conc_Glucose * RightHeart_Flow.PlasmaFlow ), 0.0) )
        self.LacFraction = self.LacFraction_curve( RightHeart_Lactate.conc_Lac__mGperdL )
        self.FA_GlucoseFraction = 1.0 - self.LacFraction
        self.Ratio = FAPool.conc_FA_mGperdL / GlucosePool.conc_Glucose_mGperdL
        self.FAFraction = self.FA_GlucoseFraction * ( self.Ratio / ( self.Ratio + self.KR ) )
        self.GlucoseFraction = self.FA_GlucoseFraction - self.FAFraction
        self.FAUsed_CalperMin = self.FAFraction * RightHeart_Metabolism.AerobicCals
        self.FAUsed_mGperMin = self.FAUsed_CalperMin * Metabolism_Tools.Fat_mGperCal
        self.AerobicGlucoseUsed_CalperMin = self.GlucoseFraction * RightHeart_Metabolism.AerobicCals
        self.AerobicGlucoseUsed_mGperMin = self.AerobicGlucoseUsed_CalperMin * Metabolism_Tools.CarboAerobic_mGperCal
        self.LacUsed_CalperMin = self.LacFraction * RightHeart_Metabolism.AerobicCals
        self.LacUsed_mGperMin = self.LacUsed_CalperMin * Metabolism_Tools.Lac__mGperCal
        self.AnaerobicGlucoseDelivered = self.GlucoseDelivered - self.AerobicGlucoseUsed_mGperMin
        self.AnaerobicGlucoseUsed_CalperMin = ( min( RightHeart_Metabolism.AnaerobicCals, self.AnaerobicGlucoseDelivered) )
        self.AnaerobicGlucoseUsed_mGperMin = self.AnaerobicGlucoseUsed_CalperMin * Metabolism_Tools.CarboAnaerobic_mGperCal
        self.TotalGlucoseUsed_mGperMin = self.AerobicGlucoseUsed_mGperMin + self.AnaerobicGlucoseUsed_mGperMin
        if self.FAUsed_mGperMin > 0.0:
            self.FAFractionalDelivery = ( min( ( self.FADelivered / self.FAUsed_mGperMin ), 1.0) )
        else:
            self.FAFractionalDelivery = 1.0

        if self.AerobicGlucoseUsed_mGperMin > 0.0:
            self.AerobicGlucoseFractionalDelivery = ( min( ( self.GlucoseDelivered / self.AerobicGlucoseUsed_mGperMin ), 1.0) )
        else:
            self.AerobicGlucoseFractionalDelivery = 1.0

        if self.AnaerobicGlucoseUsed_mGperMin > 0.0:
            self.AnaerobicGlucoseFractionalDelivery = ( min( ( self.AnaerobicGlucoseDelivered / self.AnaerobicGlucoseUsed_mGperMin ), 1.0) )
        else:
            self.AnaerobicGlucoseFractionalDelivery = 1.0

        self.MinimumFractionalDelivery = ( min( ( min( self.FAFractionalDelivery, self.AerobicGlucoseFractionalDelivery) ), self.AnaerobicGlucoseFractionalDelivery) )
        self.K = 0.5
        self.DxMax = 1.0
        self.FractUse = self.MinimumFractionalDelivery
        self.FractUseDelay = delay( self.K, self.FractUse, self.FractUseDelay, System.Dx, 0.01)


class RightHeart_CO2:
    def __init__(self):
        self.conc_HCO3 = None
        self.conc_HCO3_mEqperL = None
        self.PCO2 = None
        self.InflowGas = None
        self.InflowBase = None
        self.OutflowBase = None
        self.conc_BloodHCO3 = None
        self.Outflow_0 = None
        self.K = None
        self.Alpha = None
        self.Mass = 0.6

    def CalcConc_func(self):
        self.conc_HCO3 = self.Mass / RightHeart_Size.LiquidVol
        self.conc_HCO3_mEqperL = 1000.0 * self.conc_HCO3
        Tissue_BaseToGas.conc_HCO3 = self.conc_HCO3
        Tissue_BaseToGas.conc_SID = RightHeart_Ph.conc_SID
        Tissue_BaseToGas.Calc_func()
        self.PCO2 = Tissue_BaseToGas.pCO2

    def CalcDervs_func(self):
        self.K = RightHeart_Flow.BloodFlow / RightHeart_Size.LiquidVol
        if System.Dx >=0:
            self.Alpha = 0.0
        elif ( self.K * System.Dx ) >= 100.0:
            self.Alpha = 4E-44
        elif True:
            self.Alpha = ( math.e ** ( - self.K * System.Dx ) )
        self.InflowGas = Metabolism_RespiratoryQuotient.RQ * RightHeart_Flow.O2Use
        self.InflowBase = CO2Tools.LitersToMols * self.InflowGas
        Blood_GasToBase.pCO2 = self.PCO2
        Blood_GasToBase.conc_SID = BloodIons.conc_SID
        Blood_GasToBase.Calc_func()
        self.conc_BloodHCO3 = Blood_GasToBase.conc_HCO3
        self.Outflow_0 = RightHeart_Flow.BloodFlow * ( self.conc_BloodHCO3 - CO2Artys.conc_HCO3 )
        self.OutflowBase = ( self.Alpha * self.Outflow_0 ) + ( ( 1 - self.Alpha ) * self.InflowBase )
        self.Change = self.InflowBase - self.OutflowBase
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.01)


class RightHeart_AlphaReceptors:
    def __init__(self):
        self.Activity = None
        self.TotalAgonism = None
        self.NeuralAgonism = None
        self.HumoralAgonism = None
        self.Switch = False
        self.Setting = 0.0
        self.NEURALK = 0.333
        self.HUMORALK = 0.5

    def Calc_func(self):
        self.NeuralAgonism = GangliaGeneral.NA_Hz
        self.HumoralAgonism = AlphaPool.Effect
        self.TotalAgonism = ( self.NEURALK * self.NeuralAgonism ) + ( self.HUMORALK * self.HumoralAgonism )
        if self.Switch:
            self.Activity = self.Setting
        else:
            self.Activity = self.TotalAgonism * AlphaBlockade.Effect


class RightHeart_ContractileProtein:

    def Initialize_func(self):
        self.Mass = RightHeart_Size.InitialProteinMass

    def Dervs_func(self):
        self.Change = 0.0
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.12)


class RightHeart_Ph:
    def __init__(self):
        self.Ph = None
        self.conc_SID = None
        self.conc_SID_mEqperL = None

    def CalcSID_func(self):
        self.conc_SID = KCell.conc_K_ + CellSID.OtherCations - CellSID.StrongAnions - RightHeart_Lactate.conc_Lac_
        self.conc_SID_mEqperL = 1000.0 * self.conc_SID

    def CalcPh_func(self):
        PhCells.pCO2 = RightHeart_CO2.PCO2
        PhCells.SID = self.conc_SID_mEqperL
        PhCells.Calc_func()
        self.Ph = PhCells.pH

class RightHeart_Structure:
    def __init__(self):
        self.PhEffect = None
        self.FuelEffect = None
        self.TemperatureEffect = None
        self.Effect = 1.0

    def PhOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [6.5, 6.6], [0.1, 0.0], [0.0, 0.0])

    def FuelOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.3], [0.05, 0.0], [0.0, 0.0])

    def TemperatureOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [44.0, 46.0], [0.0, 0.05], [0.0, 0.0])

    def Calc_func(self):
        self.PhEffect = self.PhOnStructure_curve( RightHeart_Ph.Ph )
        self.FuelEffect = self.FuelOnStructure_curve( RightHeart_Fuel.FractUseDelay )
        self.TemperatureEffect = self.TemperatureOnStructure_curve( HeatCore.Temp_C )
        self.F1 = 0.0
        self.F2 = self.PhEffect + self.TemperatureEffect + self.FuelEffect
        self.Effect = backwardeuler( self.F1, self.F2, System.Dx, self.Effect, None)


class RightHeart_Metabolism:
    def __init__(self):
        self.TotalCalsUsed = None
        self.BasalCalsUsed = None
        self.InitialBasalCalsUsed = None
        self.BasalCalsUsed__CalperMinperG = 0.0600
        self.CalMultiplier = 1.0
        self.AerobicCals = None
        self.AnaerobicCals = None
        self.O2Need = None
        self.O2Lack = None

    def ScaleCals_func(self):
        self.InitialBasalCalsUsed = self.CalMultiplier * self.BasalCalsUsed__CalperMinperG * RightHeart_Size.InitialMass

    def CalcCals_func(self):
        self.BasalCalsUsed = self.CalMultiplier * self.BasalCalsUsed__CalperMinperG * RightHeart_Size.Mass
        self.TotalCalsUsed = ( self.BasalCalsUsed * Thyroid.Effect * HeatMetabolism.Core * RightHeart_Structure.Effect ) + RightHeart_Work.TotalCals
        self.O2Need = Metabolism_Tools.CalToO2 * self.TotalCalsUsed

    def SplitCals_func(self):
        self.O2Lack = self.O2Need - RightHeart_Flow.O2Use
        self.AerobicCals = Metabolism_Tools.O2ToCal * RightHeart_Flow.O2Use
        self.AnaerobicCals = Metabolism_Tools.O2ToCal * self.O2Lack

class RightHeart:
    def __init__(self):
        pass
    
class RightHeart_BetaReceptors:
    def __init__(self):
        self.Activity = None
        self.TotalAgonism = None
        self.NeuralAgonism = None
        self.HumoralAgonism = None
        self.Switch = False
        self.Setting = 0.0
        self.NEURALK = 0.333
        self.HUMORALK = 0.5

    def Calc_func(self):
        self.NeuralAgonism = GangliaGeneral.NA_Hz
        self.HumoralAgonism = BetaPool.Effect
        self.TotalAgonism = ( self.NEURALK * self.NeuralAgonism ) + ( self.HUMORALK * self.HumoralAgonism )
        if self.Switch:
            self.Activity = self.Setting
        else:
            self.Activity = self.TotalAgonism * BetaBlockade.Effect


class RightHeart_Infarction:
    def __init__(self):
        self.Areapercent = 0.0
        self.Effect = None
        self.IschemicTissueFraction = None
        self.IsIschemic = False
        self.DeadTissueFraction = 0.0

    def Parms_func(self):
        self.DeadTissueK = 0.004
        self.DamagedTissueFraction = self.Areapercent / 100.0
        self.Effect = 1.0 - self.DamagedTissueFraction
        self.DeadTissueFraction = delay( self.DeadTissueK, self.DamagedTissueFraction, self.DeadTissueFraction, System.Dx, 0.01)


    def Dervs_func(self):
        self.IschemicTissueFraction = self.DamagedTissueFraction - self.DeadTissueFraction
        if ( self.IsIschemic ) and ( self.IschemicTissueFraction < 0.03 ):
            self.IsIschemic = False
        else:
            pass
        if ( not self.IsIschemic ) and ( self.IschemicTissueFraction > 0.05 ):
            self.IsIschemic = True
        else:
            pass
        self.DeadTissueFraction = delay( self.DeadTissueK, self.DamagedTissueFraction, self.DeadTissueFraction, System.Dx, 0.01)


class RightHeart_Flow:
    def __init__(self):
        self.Conductance = None
        self.SmallVesselConductance = None
        self.SmallVesselBasicConductance = 0.4
        self.LargeVesselConductance = None
        self.LargeVesselBasicConductance = 10.0
        self.A2Effect = None
        self.SympsEffect = None
        self.ADHEffect = None
        self.PO2Effect = None
        self.MetabolismEffect = None
        self.AerobicFraction = None
        self.O2Use = None
        self.conc_O2 = None
        self.BloodFlow = None
        self.PlasmaFlow = None
        self.PO2 = 17.1
    def SympsOnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.0, 4.0], [1.3, 1.0, 0.8], [0.0, -0.16, 0.0])

    def PO2OnConductance_curve(self, x):
        return cubic_hermite_spline(x, [12.0, 17.0, 30.0], [2.0, 1.0, 0.8], [0.0, -0.04, 0.0])

    def ADHOnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.8, 3.0], [1.0, 0.1], [0.0, 0.0])

    def PO2OnAerobicFraction_curve(self, x):
        return cubic_hermite_spline(x, [2.0, 10.0], [0.0, 1.0], [0.0, 0.0])

    def MetabolismOnConductance_curve(self, x):
        return cubic_hermite_spline(x, [30.0, 100.0], [1.0, 3.0], [0.0, 0.0])

    def Calc_func(self):
        self.LargeVesselConductance = self.LargeVesselBasicConductance * Viscosity.ConductanceEffect
        self.SympsEffect = self.SympsOnConductance_curve( RightHeart_AlphaReceptors.Activity )
        self.ADHEffect = self.ADHOnConductance_curve( ADHPool.Log10Conc )
        self.MetabolismEffect = self.MetabolismOnConductance_curve( RightHeart_Metabolism.O2Need )
        self.SearchMax = PO2Artys.Pressure

        def PO2implicitfunc(PO2):
            self.PO2Effect = self.PO2OnConductance_curve( PO2 )
            self.SmallVesselConductance = self.SmallVesselBasicConductance * self.SympsEffect * self.PO2Effect * self.ADHEffect * self.MetabolismEffect * Viscosity.ConductanceEffect * Anesthesia.VascularConductance * RightHeart_Vasculature.Effect * RightHeart_Infarction.Effect
            self.Conductance = ( self.SmallVesselConductance * self.LargeVesselConductance ) / ( self.SmallVesselConductance + self.LargeVesselConductance )
            self.BloodFlow = ( max( ( RightHeart_Pressure.PressureGradient * self.Conductance ), 0.0) )
            self.AerobicFraction = self.PO2OnAerobicFraction_curve( PO2 )
            self.O2Use = RightHeart_Metabolism.O2Need * self.AerobicFraction
            if self.BloodFlow > 0.0:
                self.conc_O2 = O2Artys.conc_O2 - ( self.O2Use / self.BloodFlow )
            else:
                self.conc_O2 = 0.0

            HgbTissue.conc_O2 = self.conc_O2
            HgbTissue.O2ToPO2_func()
            PO2End = HgbTissue.pO2

            return PO2End
        self.PO2 = impliciteq( PO2implicitfunc, self.PO2, 0.17)
        self.PlasmaFlow = self.BloodFlow * BloodVol.PVCrit

class RightHeart_Lactate:
    def __init__(self):
        self.conc_Lac_ = None
        self.conc_Lac__mEqperL = None
        self.conc_Lac__mGperdL = None
        self.DC = 3.0
        self.Made = None
        self.Made_mGperMin = None
        self.Used = None
        self.Used_mGperMin = None
        self.Outflux = None
        self.Outflux_0 = None
        self.K = None
        self.Alpha = None
        self.MEQ_ML_TO_MG_DL = 9008.0
        self.GLUCOSE_TO_LACTATE = 0.99
        self.MG_TO_MEQ = 0.0112
        self.Mass = 0.030

    def CalcConc_func(self):
        self.conc_Lac_ = self.Mass / RightHeart_Size.LiquidVol
        self.conc_Lac__mEqperL = 1000.0 * self.conc_Lac_
        self.conc_Lac__mGperdL = self.MEQ_ML_TO_MG_DL * self.conc_Lac_

    def CalcDervs_func(self):
        self.Made_mGperMin = self.GLUCOSE_TO_LACTATE * RightHeart_Fuel.AnaerobicGlucoseUsed_mGperMin
        self.Made = self.MG_TO_MEQ * self.Made_mGperMin
        self.Used_mGperMin = RightHeart_Fuel.LacUsed_mGperMin
        self.Used = self.MG_TO_MEQ * self.Used_mGperMin
        self.K = self.DC / RightHeart_Size.LiquidVol
        if System.Dx >=0:
            self.Alpha = 0.0
        elif ( self.K * System.Dx ) >= 100.0:
            self.Alpha = 4E-44
        elif True:
            self.Alpha = ( math.e ** ( - self.K * System.Dx ) )
        self.Outflux_0 = self.DC * ( self.conc_Lac_ - LacPool.conc_Lac_ )
        self.Outflux = ( self.Alpha * self.Outflux_0 ) + ( ( 1 - self.Alpha ) * ( self.Made + self.Used ) )
        self.Change = self.Made - self.Used - self.Outflux
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.0003)


class AminoAcid:
    def __init__(self):
        pass
    
class AAPool:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.conc_AA = None
        self.conc_AA_mGperdL = None
        self.conc_AA_mMolperL = None
        self.PER_ML_TO_PER_DL = 100.0
        self.MG_TO_MMOL = 10.0
        self.Targetconc_AA = 0.50
        self.InitialMass = None

    def Init_func(self):
        self.InitialMass = self.Targetconc_AA * ECFV.Vol
        self.Mass = self.InitialMass

    def CalcConc_func(self):
        self.conc_AA = self.Mass / ECFV.Vol
        self.conc_AA_mGperdL = self.PER_ML_TO_PER_DL * self.conc_AA
        self.conc_AA_mMolperL = self.MG_TO_MMOL * self.conc_AA

    def CalcDervs_func(self):
        self.Gain = GILumenProtein.Absorption + CellProtein.Outflow
        self.Loss = CellProtein.Inflow + LM_AminoAcids.Uptake
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 75.0)


class GnRH:
    def __init__(self):
        self.BasicPeriod_Min = 80.0
        self.Pulses_perDay = None
        self.Period_Min = None
        self.Period_Hr = None
        self.TestosteroneEffect = None
        self.EstradiolEffect = None

    def TestosteroneEffect_curve(self, x):
        return cubic_hermite_spline(x, [5.0, 20.0], [1.0, 2.0], [0.0, 0.0])

    def EstradiolEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.0, 2.0], [1.0, 1.5, 0.5], [0.0, 0.0, 0.0])

    def Dervs_func(self):
        self.TestosteroneEffect = self.TestosteroneEffect_curve( Testosterone.conc_Conc_nMolperL )
        self.EstradiolEffect = self.EstradiolEffect_curve( Estradiol.conc_Conc_nMolperL )
        self.Period_Min = self.BasicPeriod_Min * self.TestosteroneEffect * self.EstradiolEffect
        self.Period_Hr = self.Period_Min / 60.0
        self.Pulses_perDay = 24.0 / self.Period_Hr

class Status:
    def __init__(self):
        self.Activity = 3
        self.Exertion = 0
        self.Posture = 1
        self.Nutrition = 2
        self.Sleeping = None
        self.Awake = None
        self.Unconscious = None
        self.NotDefined = None
        self.Resting = None
        self.Working = None
        self.Aerobics = None
        self.ExerciseBike = None
        self.Treadmill = None
        self.Lying = None
        self.Sitting = None
        self.Standing = None
        self.Tilting = None
        self.Eating = None
        self.BetweenMeals = None
        self.Continuous = None
        self.CantEat = None
        self.Conscious = True

    def CheckConscious_func(self):
        if Brain_Function.Comatose:
            if self.Conscious:
                self.Conscious = False
                self.JustLostConscious_func()
            else:
                pass
        else:
            if not self.Conscious:
                self.Conscious = True
            else:
                pass

    def Wrapup_func(self):
        self.Activity_func()
        self.Exertion_func()
        self.Posture_func()
        self.Nutrition_func()

    def Activity_func(self):
        if self.Activity == 3:
            self.Sleeping = 0
            self.Awake = 0
            self.Unconscious = 0
            self.NotDefined = 1
        elif self.Activity == 1:
            self.Sleeping = 0
            self.Awake = 1
            self.Unconscious = 0
            self.NotDefined = 0
        elif self.Activity == 0:
            self.Sleeping = 1
            self.Awake = 0
            self.Unconscious = 0
            self.NotDefined = 0
        elif self.Activity == 2:
            self.Sleeping = 0
            self.Awake = 0
            self.Unconscious = 1
            self.NotDefined = 0

    def Exertion_func(self):
        if self.Exertion == 0:
            self.Resting = 1
            self.Working = 0
            self.Aerobics = 0
            self.ExerciseBike = 0
            self.Treadmill = 0
        elif self.Exertion == 1:
            self.Resting = 0
            self.Working = 1
            self.Aerobics = 0
            self.ExerciseBike = 0
            self.Treadmill = 0
        elif self.Exertion == 2:
            self.Resting = 0
            self.Working = 0
            self.Aerobics = 1
            self.ExerciseBike = 0
            self.Treadmill = 0
        elif self.Exertion == 3:
            self.Resting = 0
            self.Working = 0
            self.Aerobics = 0
            self.ExerciseBike = 1
            self.Treadmill = 0
        elif self.Exertion == 4:
            self.Resting = 0
            self.Working = 0
            self.Aerobics = 0
            self.ExerciseBike = 0
            self.Treadmill = 1

    def Posture_func(self):
        if self.Posture == PostureControl.LYING:
            self.Lying = True
            self.Sitting = False
            self.Standing = False
            self.Tilting = False
        elif self.Posture == PostureControl.SITTING:
            self.Lying = False
            self.Sitting = True
            self.Standing = False
            self.Tilting = False
        elif self.Posture == PostureControl.STANDING:
            self.Lying = False
            self.Sitting = False
            self.Standing = True
            self.Tilting = False
        elif self.Posture == PostureControl.TILTED:
            self.Lying = False
            self.Sitting = False
            self.Standing = False
            self.Tilting = True

    def Nutrition_func(self):
        if self.Nutrition == 2:
            self.Eating = 0
            self.BetweenMeals = 0
            self.Continuous = 1
            self.CantEat = 0
        elif self.Nutrition == 0:
            self.Eating = 1
            self.BetweenMeals = 0
            self.Continuous = 0
            self.CantEat = 0
        elif self.Nutrition == 1:
            self.Eating = 0
            self.BetweenMeals = 1
            self.Continuous = 0
            self.CantEat = 0
        elif self.Nutrition == 3:
            self.Eating = 0
            self.BetweenMeals = 0
            self.Continuous = 0
            self.CantEat = 1

    def JustLostConscious_func(self):
        if DailyPlannerControl.Switch:
            DailyPlannerControl.Switch = False
            DailyPlannerControl.Stop_func()
        else:
            pass
        PostureControl.Request = 0
        Status.Activity = 2
        Status.Exertion = 0
        Status.Posture = 0
        Status.Nutrition = 3

class LipidDeposits:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.Change_mGperMin = None

    def Initialize_func(self):
        self.Mass = Fat_Size.InitialLipidMass

    def Dervs_func(self):
        LipidDeposits_Uptake.Dervs_func()
        LipidDeposits_Release.Dervs_func()
        self.Gain = LipidDeposits_Uptake.Rate
        self.Loss = LipidDeposits_Release.Rate
        self.Change_mGperMin = self.Gain - self.Loss
        self.Change = 0.001 * self.Change_mGperMin
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 130.0)


class LipidDeposits_Uptake:
    def __init__(self):
        self.Rate = None
        self.Basic = 100.0
        self.InsulinEffect = None
        self.FattyAcidEffect = None

    def InsulinEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 20.0, 100.0], [0.5, 1.0, 2.0], [0.0, 0.03, 0.0])

    def FattyAcidEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 15.0, 50.0], [0.0, 1.0, 3.0], [0.0, 0.1, 0.0])

    def Dervs_func(self):
        self.InsulinEffect = self.InsulinEffect_curve( InsulinPool.conc_Insulin )
        self.FattyAcidEffect = self.FattyAcidEffect_curve( FAPool.conc_FA_mGperdL )
        self.Rate = self.Basic * self.InsulinEffect * self.FattyAcidEffect

class LipidDeposits_Release:
    def __init__(self):
        self.Rate = None
        self.Fraction = 0.0075
        self.BasicRate = None
        self.InsulinEffect = None
        self.GlucagonEffect = None
        self.EpinephrineEffect = None
        self.FattyAcidEffect = None

    def InsulinEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 20.0, 100.0], [2.0, 1.0, 0.0], [0.0, -0.04, 0.0])

    def GlucagonEffect_curve(self, x):
        return cubic_hermite_spline(x, [120.0, 200.0], [1.0, 2.0], [0.0, 0.0])

    def EpinephrineEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 40.0, 400.0], [0.5, 1.0, 4.0], [0.0, 0.013, 0.0])

    def FattyAcidEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 15.0, 100.0], [3.0, 1.0, 0.0], [0.0, -0.04, 0.0])

    def Dervs_func(self):
        self.BasicRate = self.Fraction * LipidDeposits.Mass
        self.InsulinEffect = self.InsulinEffect_curve( InsulinPool.conc_Insulin )
        self.GlucagonEffect = self.GlucagonEffect_curve( GlucagonPool.conc_Glucagon )
        self.EpinephrineEffect = self.EpinephrineEffect_curve( EpiPool.conc_Epi_pGpermL )
        self.FattyAcidEffect = self.FattyAcidEffect_curve( FAPool.conc_FA_mGperdL )
        self.Rate = self.BasicRate * self.InsulinEffect * self.GlucagonEffect * self.EpinephrineEffect * self.FattyAcidEffect

class OralH2OGlucoseLoad:
    def __init__(self):
        self.Switch = False
        self.H2ORate = 0.0
        self.Glucose_percent = 5.0
        self.GlucoseRate = None
        self.TotalH2O = 0.0
        self.TotalGlucose = 0.0

    def Parms_func(self):
        self.GlucoseRate = 0.01 * self.Glucose_percent * self.H2ORate

    def Dervs_func(self):
        self.H2OChange = self.H2ORate
        self.GlucoseChange = self.GlucoseRate
        self.TotalH2O = diffeq( self.H2OChange, System.Dx, self.TotalH2O, None)

        self.TotalGlucose = diffeq( self.GlucoseChange, System.Dx, self.TotalGlucose, None)


class BVSeq:
    def __init__(self):
        self.Vol = None

    def Calc_func(self):
        self.Vol = BVSeqArtys.Vol + BVSeqVeins.Vol

class SequesteredBlood:
    def __init__(self):
        pass
    
class BVSeqVeins:
    def __init__(self):
        self.Pressure = None
        self.TMP = None
        self.Conductance = 10.0
        self.Vol = 150.0

    def VolOnPressure_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 150.0, 600.0], [-100.0, 11.0, 50.0], [2.0, 0.11, 0.15])

    def CalcPressure_func(self):
        self.TMP = self.VolOnPressure_curve( self.Vol )
        self.Pressure = self.TMP + LowerExternalPressure.Pressure

    def Dervs_func(self):
        self.DxMax = 0.8
        self.Change = self.Conductance * ( RegionalPressure.LowerVein - self.Pressure )

class BVSeqArtys:
    def __init__(self):
        self.Pressure = None
        self.TMP = None
        self.Conductance = 4.0
        self.Vol = 50.0

    def VolOnPressure_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 50.0, 200.0], [0.0, 97.0, 150.0], [0.0, 1.0, 0.5])

    def CalcPressure_func(self):
        self.TMP = self.VolOnPressure_curve( self.Vol )
        self.Pressure = self.TMP + LowerExternalPressure.Pressure

    def Dervs_func(self):
        self.DxMax = 0.2
        self.Change = self.Conductance * ( RegionalPressure.LowerArty - self.Pressure )

class CardiacCycle:
    def __init__(self):
        pass
    
class DiastolicPressure:
    def __init__(self):
        self.Pres = None
        self.Vol = None
        self.Stiffness = None

    def Calc_func(self):
        if self.Vol > 0.0:
            self.Pres = ( math.e ** ( self.Stiffness * self.Vol ) ) - 1.0
        else:
            self.Pres = 0.0


class HypothalamusSweatingAcclimation:
    def __init__(self):
        self.Tau = 7.0
        self.Offset = 0.0

    def SteadyState_curve(self, x):
        return cubic_hermite_spline(x, [20.0, 28.0, 39.0], [0.3, 0.0, -0.3], [0.0, -0.04, 0.0])

    def Parms_func(self):
        self.K = ( 1 / ( 1440.0 * self.Tau ) )

    def Dervs_func(self):
        self.SteadyState = self.SteadyState_curve( HeatSkin.Temp_C )
        self.Offset = delay( self.K, self.SteadyState, self.Offset, System.Dx, 0.003)


class HypothalamusShivering:
    def __init__(self):
        self.NerveActivity = None
        self.TemperatureDifference = None
        self.SetPoint = None
        self.SkinTempOffset = None
        self.Base = 37.0

    def SkinTempOffset_curve(self, x):
        return cubic_hermite_spline(x, [24.0, 32.0], [0.0, -1.0], [0.0, 0.0])

    def NerveActivity_curve(self, x):
        return cubic_hermite_spline(x, [-2.0, 0.0], [4.0, 0.0], [0.0, 0.0])

    def CalcEffect_func(self):
        self.SkinTempOffset = self.SkinTempOffset_curve( HeatSkin.Temp_C )
        self.SetPoint = self.Base + self.SkinTempOffset + HypothalamusSweatingAcclimation.Offset
        self.TemperatureDifference = HeatCore.Temp_C - self.SetPoint
        self.NerveActivity = self.NerveActivity_curve( self.TemperatureDifference )

class Hypothalamus:

    def Parms_func(self):
        HypothalamusShiveringAcclimation.Parms_func()
        HypothalamusSweatingAcclimation.Parms_func()

    def CalcEffect_func(self):
        HypothalamusSweating.CalcEffect_func()
        HypothalamusShivering.CalcEffect_func()
        HypothalamusSkinFlow.CalcEffect_func()
        HypothalamusTSH.CalcEffect_func()

    def Dervs_func(self):
        HypothalamusShiveringAcclimation.Dervs_func()
        HypothalamusSweatingAcclimation.Dervs_func()

class HypothalamusTSH:
    def __init__(self):
        self.TemperatureEffect = None
        self.TemperatureDifference = None
        self.SetPoint = 37.0

    def TemperatureEffect_curve(self, x):
        return cubic_hermite_spline(x, [-2.0, 0.0, 2.0], [4.0, 1.0, 0.2], [0.0, -1.0, 0.0])

    def CalcEffect_func(self):
        self.TemperatureDifference = HeatCore.Temp_C - self.SetPoint
        self.TemperatureEffect = Brain_Function.Effect * self.TemperatureEffect_curve( self.TemperatureDifference )

class HypothalamusSkinFlow:
    def __init__(self):
        self.NerveActivity = None
        self.TemperatureDifference = None
        self.SetPoint = 37.0

    def TemperatureEffect_curve(self, x):
        return cubic_hermite_spline(x, [-2.0, 0.0, 2.0], [0.0, 1.0, 4.0], [0.0, 1.8, 0.0])

    def CalcEffect_func(self):
        self.TemperatureDifference = HeatCore.Temp_C - self.SetPoint
        self.NerveActivity = self.TemperatureEffect_curve( self.TemperatureDifference ) * Brain_Function.Effect

class HypothalamusSweating:
    def __init__(self):
        self.NerveActivity = None
        self.TemperatureDifference = None
        self.SetPoint = None
        self.SkinTempOffset = None
        self.Base = 37.0

    def SkinTempOffset_curve(self, x):
        return cubic_hermite_spline(x, [25.0, 35.0], [1.0, 0.0], [0.0, 0.0])

    def NerveActivity_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 2.0], [0.0, 4.0], [0.0, 0.0])

    def CalcEffect_func(self):
        self.SkinTempOffset = self.SkinTempOffset_curve( HeatSkin.Temp_C )
        self.SetPoint = self.Base + self.SkinTempOffset + HypothalamusSweatingAcclimation.Offset
        self.TemperatureDifference = HeatCore.Temp_C - self.SetPoint
        self.NerveActivity = self.NerveActivity_curve( self.TemperatureDifference )

class HypothalamusShiveringAcclimation:
    def __init__(self):
        self.Tau = 7.0
        self.Offset = 0.0

    def SteadyState_curve(self, x):
        return cubic_hermite_spline(x, [20.0, 28.0, 39.0], [0.3, 0.0, -0.3], [0.0, -0.04, 0.0])

    def Parms_func(self):
        self.K = ( 1 / ( 1440.0 * self.Tau ) )

    def Dervs_func(self):
        self.SteadyState = self.SteadyState_curve( HeatSkin.Temp_C )
        self.Offset = delay( self.K, self.SteadyState, self.Offset, System.Dx, 0.003)


class RespiratoryCenter_Exercise:
    def __init__(self):
        self.TotalDrive = None

    def Calc_func(self):
        self.TotalDrive = RespiratoryCenter_Radiation.TotalDrive + RespiratoryCenter_Metaboreflex.Drive

class RespiratoryCenter_Metaboreflex:
    def __init__(self):
        self.Drive = None

    def Calc_func(self):
        self.Drive = SkeletalMuscle_Metaboreflex.NerveActivity

class RespiratoryCenter:

    def Calc_func(self):
        RespiratoryCenter_Chemical.Calc_func()
        RespiratoryCenter_Radiation.Calc_func()
        RespiratoryCenter_Metaboreflex.Calc_func()
        RespiratoryCenter_Exercise.Calc_func()
        RespiratoryCenter_Integration.Calc_func()
        RespiratoryCenter_Output.Calc_func()

class RespiratoryCenter_Chemical:
    def __init__(self):
        self.TotalDrive = None
        self.CentralDrive = None
        self.PhEffect = None
        self.PeripheralDrive = None
        self.ChemoreceptorEffect = None
        self.CentralBase = 0.6
        self.PeripheralBase = 0.4

    def PhOnCentralDrive_curve(self, x):
        return cubic_hermite_spline(x, [6.6, 6.87, 7.12, 7.5], [0.0, 10.0, 1.0, 0.0], [0.0, 0.0, -8.0, 0.0])

    def Calc_func(self):
        self.PhEffect = self.PhOnCentralDrive_curve( Brain_Ph.Ph )
        self.CentralDrive = self.PhEffect * self.CentralBase
        self.ChemoreceptorEffect = Chemoreceptors.FiringRate
        self.PeripheralDrive = self.ChemoreceptorEffect * self.PeripheralBase
        self.TotalDrive = self.CentralDrive + self.PeripheralDrive

class RespiratoryCenter_Radiation:
    def __init__(self):
        self.TotalDrive = None

    def TotalDrive_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 500.0, 1000.0], [0.0, 3.5, 4.0], [0.0, 0.003, 0.0])

    def Calc_func(self):
        self.TotalDrive = self.TotalDrive_curve( Exercise_Metabolism.TotalWatts )

class RespiratoryCenter_Output:
    def __init__(self):
        self.Rate = None
        self.MotorNerveActivity = None

    def Rate_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.0, 10.0], [0.0, 12.0, 40.0], [12.0, 4.0, 0.0])

    def Calc_func(self):
        self.Rate = Brain_Function.Effect * self.Rate_curve( RespiratoryCenter_Integration.TotalDrive )
        self.MotorNerveActivity = Brain_Function.Effect * Anesthesia.TidalVolume * RespiratoryCenter_Integration.TotalDrive

class RespiratoryCenter_Integration:
    def __init__(self):
        self.TotalDrive = None
        self.Clamp = False
        self.Level = 0.0

    def Calc_func(self):
        if Brain_Function.NotBreathing:
            self.TotalDrive = 0.0
        elif self.Clamp:
            self.TotalDrive = self.Level
        elif True:
            self.TotalDrive = RespiratoryCenter_Chemical.TotalDrive + RespiratoryCenter_Exercise.TotalDrive

class GlucagonSecretion:
    def __init__(self):
        self.Rate = None
        self.InsulinEffect = None
        self.GlucoseEffect = None
        self.Base = 50.0

    def InsulinEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 7.0, 20.0, 100.0], [6.0, 1.3, 1.0, 0.6], [0.0, -0.02, -0.006, 0.0])

    def GlucoseEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 70.0, 110.0, 400.0], [2.5, 1.1, 1.0, 0.6], [0.0, -0.005, -0.001, 0.0])

    def Dervs_func(self):
        self.InsulinEffect = self.InsulinEffect_curve( InsulinPool.conc_Insulin )
        self.GlucoseEffect = self.GlucoseEffect_curve( GlucosePool.conc_Glucose_mGperdL )
        self.Rate = self.Base * self.InsulinEffect * self.GlucoseEffect * GITract_Function.Effect

class Glucagon:

    def CalcConc_func(self):
        GlucagonPool.CalcConc_func()

    def Dervs_func(self):
        GlucagonSecretion.Dervs_func()
        GlucagonClearance.Dervs_func()
        GlucagonPool.Dervs_func()

class GlucagonPool:
    def __init__(self):
        self.conc_Glucagon = None
        self.Gain = None
        self.Loss = None
        self.Targetconc_Glucagon = 70.0
        self.InitialMass = None

    def Init_func(self):
        self.InitialMass = self.Targetconc_Glucagon * ECFV.InitialVol_L
        self.Mass = self.InitialMass

    def CalcConc_func(self):
        self.conc_Glucagon = self.Mass / ECFV.Vol_L

    def Dervs_func(self):
        self.Gain = GlucagonSecretion.Rate
        self.Loss = GlucagonClearance.Rate
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 15.0)


class GlucagonClearance:
    def __init__(self):
        self.Rate = None
        self.K = 0.05

    def Dervs_func(self):
        self.Rate = self.K * GlucagonPool.Mass

class FractReab:
    def __init__(self):
        self.Normal = None
        self.Effects = None
        self.Fract = None

    def GetFract_func(self):
        if self.Normal <= 0.0:
            self.Fract = 0.0
        elif self.Normal >= 1.0:
            self.Fract = 1.0
        elif self.Effects <= 0.0:
            self.Fract = 0.0
        elif True:
            self.Fract = self.Normal ** ( ( 1 / self.Effects ) )

class Nephrons:
    def __init__(self):
        pass
    
class NephronANP:
    def __init__(self):
        self.conc_ANP = None
        self.Tau = 20.0
        self.Clamp = False
        self.Level = 0.0
        self.Log10Conc = None
        self.conc_ANPDelayed = 20.0

    def Parms_func(self):
        self.K = ( 1 / self.Tau )

    def Calc_func(self):
        if self.Clamp:
            self.conc_ANP = self.Level
        else:
            self.conc_ANP = self.conc_ANPDelayed

        if self.conc_ANP > 1.0:
            self.Log10Conc = ( math.log10( self.conc_ANP ) )
        else:
            self.Log10Conc = 0.0

        self.conc_ANPPool = ANPPool.conc_ANP
        self.conc_ANPDelayed = delay( self.K, self.conc_ANPPool, self.conc_ANPDelayed, System.Dx, None)


class NephronIFP:
    def __init__(self):
        self.Pressure = None
        self.Clamp = False
        self.Level = 0.0
        self.K = 0.042

    def Calc_func(self):
        if self.Clamp:
            self.Pressure = self.Level
        else:
            self.Pressure = self.K * Kidney_ArcuateArtery.Pressure


class NephronGlucose:
    def __init__(self):
        self.TubularMax = 250.0
        self.Reab = None
        self.Spillover = None
        self.Spillover_mMolperMin = None
        self.MG_TO_MMOL = 0.00555

    def CalcSpillover_func(self):
        if GlomerulusGlucose.Rate > self.TubularMax:
            self.Reab = self.TubularMax
        else:
            self.Reab = GlomerulusGlucose.Rate

        self.Spillover = GlomerulusGlucose.Rate - self.Reab
        self.Spillover_mMolperMin = self.MG_TO_MMOL * self.Spillover

class NephronAldo:
    def __init__(self):
        self.conc_Aldo_nGperdL = None
        self.Tau = 3.0
        self.Clamp = False
        self.Level = 0.0
        self.conc_AldoDelayed = 11.0

    def Parms_func(self):
        self.K = ( 1 / ( self.Tau * 60.0 ) )

    def Calc_func(self):
        if self.Clamp:
            self.conc_Aldo_nGperdL = self.Level
        else:
            self.conc_Aldo_nGperdL = self.conc_AldoDelayed

        self.conc_AldoPool = AldoPool.conc_Aldo_nGperdL
        self.conc_AldoDelayed = delay( self.K, self.conc_AldoPool, self.conc_AldoDelayed, System.Dx, None)


class VasaRecta:
    def __init__(self):
        self.Inflow = None
        self.Outflow = None
        self.Conductance = None
        self.ADHEffect = None
        self.OsmEffect = None
        self.A2Effect = None
        self.SympsEffect = None
        self.BasicConductance = 0.27

    def ADHOnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.3, 1.0], [1.4, 1.0, 0.9], [0.0, -0.4, 0.0])

    def OsmOnConductance_curve(self, x):
        return cubic_hermite_spline(x, [600.0, 1100.0, 2000.0], [1.4, 1.0, 0.8], [0.0, -0.0006, 0.0])

    def A2OnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.3, 2.0], [1.3, 1.0, 0.5], [0.0, -0.6, 0.0])

    def SympsOnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.0, 1.4], [1.1, 1.0, 0.6], [0.0, -0.13, 0.0])

    def Calc_func(self):
        self.ADHEffect = self.ADHOnConductance_curve( NephronADH.conc_ADH )
        self.OsmEffect = self.OsmOnConductance_curve( Medulla.conc_Osm )
        self.A2Effect = self.A2OnConductance_curve( A2Pool.Log10Conc )
        self.SympsEffect = self.SympsOnConductance_curve( Kidney_Alpha.NA )
        self.Conductance = self.BasicConductance * self.ADHEffect * self.OsmEffect * self.A2Effect * self.SympsEffect
        self.Inflow = self.Conductance * ( Kidney_ArcuateArtery.Pressure - Kidney_Pressure.VeinPressure )
        self.Outflow = self.Inflow + CD_H2O.Reab

class NephronADH:
    def __init__(self):
        self.conc_ADH = None
        self.Tau = 20.0
        self.Clamp = False
        self.Level = 0.0
        self.Log10Conc = None
        self.conc_ADHDelayed = 2.0

    def Parms_func(self):
        self.K = ( 1 / self.Tau )

    def Calc_func(self):
        if self.Clamp:
            self.conc_ADH = self.Level
        else:
            self.conc_ADH = self.conc_ADHDelayed

        if self.conc_ADH > 1.0:
            self.Log10Conc = ( math.log10( self.conc_ADH ) )
        else:
            self.Log10Conc = 0.0

        self.conc_ADHPool = ADHPool.conc_ADH
        self.conc_ADHDelayed = delay( self.K, self.conc_ADHPool, self.conc_ADHDelayed, System.Dx, None)


class NephronKetoacids:
    def __init__(self):
        self.Excretion = None
        self.Excretion_mMolperMin = None
        self.Reab = None
        self.Reab_mMolperMin = None
        self.ReabMax = 30.0
        self.PhEffect = None
        self.MG_TO_MMOL = 0.0098

    def PhOnExcretion_curve(self, x):
        return cubic_hermite_spline(x, [7.0, 7.4], [0.0, 1.0], [0.0, 0.0])

    def CalcExcretion_func(self):
        self.PhEffect = self.PhOnExcretion_curve( BloodPh.ArtysPh )
        self.Reab = ( min( ( GlomerulusKetoacid.Rate * self.PhEffect ), self.ReabMax) )
        self.Reab_mMolperMin = self.MG_TO_MMOL * self.Reab
        self.Excretion = GlomerulusKetoacid.Rate - self.Reab
        self.Excretion_mMolperMin = self.MG_TO_MMOL * self.Excretion

class GlomerulusKetoacid:
    def __init__(self):
        self.Rate = None
        self.conc_KA_ = None
        self.Rate_mMolperMin = None
        self.MG_TO_MMOL = 0.0098

    def Calc_func(self):
        self.conc_KA_ = KAPool.conc_KA * GlomerulusFiltrate.AnionAdjustment
        self.Rate = self.conc_KA_ * GlomerulusFiltrate.GFR
        self.Rate_mMolperMin = self.MG_TO_MMOL * self.Rate

    def Failed_func(self):
        self.conc_KA_ = 0.0
        self.Rate = 0.0
        self.Rate_mMolperMin = 0.0

class GlomerulusBicarbonate:
    def __init__(self):
        self.Rate = None
        self.conc_HCO3_ = None

    def Calc_func(self):
        self.conc_HCO3_ = CO2Veins.conc_HCO3 * GlomerulusFiltrate.AnionAdjustment
        self.Rate = self.conc_HCO3_ * GlomerulusFiltrate.GFR

    def Failed_func(self):
        self.conc_HCO3_ = 0.0
        self.Rate = 0.0

class GlomerulusUrea:
    def __init__(self):
        self.Rate = None
        self.conc_Urea = None

    def Calc_func(self):
        self.conc_Urea = UreaPool.conc_Urea
        self.Rate = self.conc_Urea * GlomerulusFiltrate.GFR

    def Failed_func(self):
        self.conc_Urea = 0.0
        self.Rate = 0.0

class GlomerulusChloride:
    def __init__(self):
        self.Rate = None
        self.conc_Cl_ = None

    def Calc_func(self):
        self.conc_Cl_ = ClPool.conc_Cl_ * GlomerulusFiltrate.AnionAdjustment
        self.Rate = self.conc_Cl_ * GlomerulusFiltrate.GFR

    def Failed_func(self):
        self.conc_Cl_ = 0.0
        self.Rate = 0.0

class GlomerulusSulphate:
    def __init__(self):
        self.Rate = None
        self.conc_SO4__ = None

    def Calc_func(self):
        self.conc_SO4__ = SO4Pool.conc_SO4__ * GlomerulusFiltrate.AnionAdjustment
        self.Rate = self.conc_SO4__ * GlomerulusFiltrate.GFR

    def Failed_func(self):
        self.conc_SO4__ = 0.0
        self.Rate = 0.0

class GlomerulusSodium:
    def __init__(self):
        self.Rate = None
        self.conc_Na_ = None

    def Calc_func(self):
        self.conc_Na_ = NaPool.conc_Na_ * GlomerulusFiltrate.CationAdjustment
        self.Rate = self.conc_Na_ * GlomerulusFiltrate.GFR

    def Failed_func(self):
        self.conc_Na_ = 0.0
        self.Rate = 0.0

class Glomerulus:
    def __init__(self):
        pass
    
class GlomerulusCreatinine:
    def __init__(self):
        self.Rate = None
        self.conc_Creatinine = None

    def Calc_func(self):
        self.conc_Creatinine = CreatininePool.conc_Creatinine
        self.Rate = self.conc_Creatinine * GlomerulusFiltrate.GFR

    def Failed_func(self):
        self.conc_Creatinine = 0.0
        self.Rate = 0.0

class GlomerulusGlucose:
    def __init__(self):
        self.Rate = None
        self.conc_Glucose = None

    def Calc_func(self):
        self.conc_Glucose = GlucosePool.conc_Glucose
        self.Rate = self.conc_Glucose * GlomerulusFiltrate.GFR

    def Failed_func(self):
        self.conc_Glucose = 0.0
        self.Rate = 0.0

class GlomerulusPhosphate:
    def __init__(self):
        self.Rate = None
        self.conc_PO4__ = None

    def Calc_func(self):
        self.conc_PO4__ = PO4Pool.conc_PO4__ * GlomerulusFiltrate.AnionAdjustment
        self.Rate = self.conc_PO4__ * GlomerulusFiltrate.GFR

    def Failed_func(self):
        self.conc_PO4__ = 0.0
        self.Rate = 0.0

class GlomerulusProtein:
    def __init__(self):
        self.Rate = None
        self.conc_Protein = None
        self.Perm = 0.0

    def Calc_func(self):
        self.conc_Protein = PlasmaProtein.conc_Protein
        self.Rate = self.conc_Protein * self.Perm

    def Failed_func(self):
        self.conc_Protein = 0.0
        self.Rate = 0.0

class GlomerulusFiltrate:
    def __init__(self):
        self.GFRxNormal = None
        self.GFRNORMAL = 125.0
        self.AnionAdjustment = None
        self.CationAdjustment = None
        self.KAdjustment = None
        self.Pressure = None
        self.FiltrationFraction = None
        self.EffCOP = None
        self.conc_EffProtein = None
        self.PressureGradient = None
        self.Perm = 20.0
        self.Kf = None
        self.PT_Pressure = None
        self.PT_Conductance = 7.0
        self.PelvisPressure = 0.0
        self.GFR = 125.0
    def AdjustIons_func(self):
        self.KAdjustment = ( BloodIons.Cations - BloodIons.AnionsLessProtein ) / ( BloodIons.Cations + BloodIons.AnionsLessProtein )
        self.AnionAdjustment = 1.0 + self.KAdjustment
        self.CationAdjustment = 1.0 - self.KAdjustment

    def Calc_func(self):
        if Kidney_Flow.BloodFlow <= 0.0:
            self.Pressure = ( Kidney_Pressure.ArtyPressure + Kidney_Pressure.VeinPressure ) / 2.0
            self.Failed_func()
        else:
            self.AdjustIons_func()
            self.Pressure = Kidney_Pressure.VeinPressure + ( Kidney_Flow.BloodFlow / Kidney_EfferentArtery.Conductance )
            self.Kf = Kidney_NephronCount.Filtering_xNormal * self.Perm
            self.SearchMax = ( min( ( self.Kf * ( self.Pressure - PlasmaProtein.COP - self.PelvisPressure ) ), ( 0.8 * Kidney_Flow.PlasmaFlow )) )
            if self.SearchMax <= 0.0:
                self.Failed_func()
            else:

                def GFRimplicitfunc(GFR):
                    self.FiltrationFraction = GFR / Kidney_Flow.PlasmaFlow
                    self.conc_EffProtein = PlasmaProtein.conc_Protein / ( 1.0 - self.FiltrationFraction )
                    Colloids.conc_Prot = self.conc_EffProtein
                    Colloids.GetPres_func()
                    self.EffCOP = Colloids.Pres
                    self.PT_Pressure = self.PelvisPressure + ( GFR / self.PT_Conductance )
                    self.PressureGradient = self.Pressure - self.EffCOP - self.PT_Pressure
                    EndGFR = self.Kf * self.PressureGradient

                    return EndGFR
                self.GFR = impliciteq( GFRimplicitfunc, self.GFR, 1.25)
                self.GFRxNormal = self.GFR / self.GFRNORMAL
                GlomerulusBicarbonate.Calc_func()
                GlomerulusChloride.Calc_func()
                GlomerulusCreatinine.Calc_func()
                GlomerulusGlucose.Calc_func()
                GlomerulusKetoacid.Calc_func()
                GlomerulusPhosphate.Calc_func()
                GlomerulusProtein.Calc_func()
                GlomerulusSodium.Calc_func()
                GlomerulusSulphate.Calc_func()
                GlomerulusUrea.Calc_func()

    def Failed_func(self):
        self.GFR = 0.0
        self.EndGFR = 0.0
        self.GFRxNormal = 0.0
        self.FiltrationFraction = 0
        self.EffCOP = self.Pressure
        Colloids.Pres = self.EffCOP
        Colloids.Getconc_Prot_func()
        self.conc_EffProtein = Colloids.conc_Prot
        self.PT_Pressure = 0.0
        self.PressureGradient = 0.0
        GlomerulusBicarbonate.Failed_func()
        GlomerulusChloride.Failed_func()
        GlomerulusCreatinine.Failed_func()
        GlomerulusGlucose.Failed_func()
        GlomerulusKetoacid.Failed_func()
        GlomerulusPhosphate.Failed_func()
        GlomerulusProtein.Failed_func()
        GlomerulusSodium.Failed_func()
        GlomerulusSulphate.Failed_func()
        GlomerulusUrea.Failed_func()

class TGF_Renin:
    def __init__(self):
        self.BasicSignal = 1.0
        self.Signal = None
        self.NaEffect = None
        self.A2Effect = None
        self.ANPEffect = None
        self.FurosemideEffect = None
        self.Clamp = False
        self.Level = 0.0

    def NaEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 48.0, 100.0], [0.0, 1.0, 2.0], [0.0, 0.03, 0.0])

    def A2Effect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.3, 2.5, 3.5], [0.9, 1.0, 2.0, 5.0], [0.0, 0.1, 2.0, 0.0])

    def ANPEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.3, 2.7], [1.2, 1.0, 0.8], [0.0, -0.3, 0.0])

    def FurosemideEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.3], [1.0, 0.2], [0.0, 0.0])

    def Dervs_func(self):
        self.NaEffect = self.NaEffect_curve( MD_Na.conc_Na__mEqperL )
        self.A2Effect = self.A2Effect_curve( A2Pool.Log10Conc )
        self.ANPEffect = self.ANPEffect_curve( ANPPool.Log10Conc )
        self.FurosemideEffect = self.FurosemideEffect_curve( FurosemidePool.Loss )
        if self.Clamp:
            self.Signal = self.Level
        else:
            self.Signal = self.BasicSignal * self.NaEffect * self.A2Effect * self.ANPEffect * self.FurosemideEffect


class MD_Na:
    def __init__(self):
        self.conc_Na__mEqperL = None
        self.Na_Flow = None

    def Calc_func(self):
        if LH_Na.conc_Na_ ==0:
            self.conc_Na__mEqperL = 0.0
        else:
            self.conc_Na__mEqperL = LH_Na.conc_Na_

        self.Na_Flow = LH_Na.Outflow

class MaculaDensa:
    def __init__(self):
        pass
    
class TGF_Vascular:
    def __init__(self):
        self.BasicSignal = 1.0
        self.NaEffect = None
        self.A2Effect = None
        self.ANPEffect = None
        self.FurosemideEffect = None
        self.Clamp = False
        self.Level = 0.0
        self.Signal = 1.0

    def NaEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 48.0, 100.0], [0.0, 1.0, 3.0], [0.0, 0.03, 0.0])

    def A2Effect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.2, 1.3, 3.0], [0.0, 0.6, 1.0, 8.0], [0.0, 0.05, 0.1, 0.0])

    def ANPEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.3, 2.7], [1.2, 1.0, 0.8], [0.0, -0.3, 0.0])

    def FurosemideEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.3], [1.0, 0.2], [0.0, 0.0])

    def Dervs_func(self):
        self.K = 1.0
        self.DxMax = 0.2
        self.NaEffect = self.NaEffect_curve( MD_Na.conc_Na__mEqperL )
        self.A2Effect = self.A2Effect_curve( A2Pool.Log10Conc )
        self.ANPEffect = self.ANPEffect_curve( ANPPool.Log10Conc )
        self.FurosemideEffect = self.FurosemideEffect_curve( FurosemidePool.Loss )
        if self.Clamp:
            self.Steady_State = self.Level
        else:
            self.Steady_State = self.BasicSignal * self.NaEffect * self.A2Effect * self.ANPEffect * self.FurosemideEffect

        self.Signal = delay( self.K, self.Steady_State, self.Signal, System.Dx, 0.01)


class MedullaUrea:
    def __init__(self):
        self.conc_Urea = None
        self.conc_Urea_mGperdL = None
        self.Osmolarity = None
        self.MG_TO_MOSM = 16.67
        self.Washup = None
        self.CCEfficiency = 98.0
        self.CCK = None
        self.Mass = 590.0

    def Parms_func(self):
        self.CCK = 1.0 - ( self.CCEfficiency / 100.0 )

    def CalcConc_func(self):
        self.conc_Urea = self.Mass / Medulla.Volume
        self.conc_Urea_mGperdL = 100.0 * self.conc_Urea
        self.Osmolarity = self.MG_TO_MOSM * self.conc_Urea

    def Dervs_func(self):
        self.Washup = self.CCK * self.conc_Urea * VasaRecta.Outflow
        self.Change = CD_Urea.Reab - self.Washup
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 5.9)


class MedullaNa:
    def __init__(self):
        self.conc_Na_ = None
        self.conc_Na__mEqperL = None
        self.Osmolarity = None
        self.Washup = None
        self.CCEfficiency = 97.0
        self.CCK = None
        self.Mass = 13.0

    def Parms_func(self):
        self.CCK = 1.0 - ( self.CCEfficiency / 100.0 )

    def CalcConc_func(self):
        self.conc_Na_ = self.Mass / Medulla.Volume
        self.conc_Na__mEqperL = 1000.0 * self.conc_Na_
        self.Osmolarity = 2.0 * self.conc_Na__mEqperL

    def Dervs_func(self):
        self.Washup = self.CCK * self.conc_Na_ * VasaRecta.Outflow
        self.Change = CD_Na.Reab - self.Washup
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.13)


class Medulla:
    def __init__(self):
        self.Volume = 31
        self.conc_Osm = None

    def CalcOsm_func(self):
        self.conc_Osm = MedullaNa.Osmolarity + MedullaUrea.Osmolarity

class PT_Na:
    def __init__(self):
        self.Inflow = None
        self.Outflow = None
        self.FractReab = None
        self.Reab = None
        self.BasicFract = 0.58
        self.TotalEffect = None
        self.A2Effect = None
        self.SympsEffect = None
        self.ANPEffect = None
        self.IFPEffect = None
        self.conc_Na_ = None
        self.MaxReab = 14.0
        self.ANPClamp = False
        self.ANPLevel = 0.0

    def A2OnFract_curve(self, x):
        return cubic_hermite_spline(x, [0.7, 1.3, 1.6], [0.8, 1.0, 1.2], [0.0, 0.8, 0.0])

    def SympsOnFract_curve(self, x):
        return cubic_hermite_spline(x, [0.6, 1.0, 4.0], [0.6, 1.0, 1.5], [0.0, 0.5, 0.0])

    def ANPOnFract_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.3, 2.7], [1.2, 1.0, 0.6], [0.0, -0.2, 0.0])

    def IFPOnFract_curve(self, x):
        return cubic_hermite_spline(x, [1.0, 4.0, 7.0], [1.4, 1.0, 0.3], [0.0, -0.2, 0.0])

    def Calc_func(self):
        self.Inflow = GlomerulusSodium.Rate
        self.A2Effect = self.A2OnFract_curve( A2Pool.Log10Conc )
        self.SympsEffect = self.SympsOnFract_curve( Kidney_Alpha.PT_NA )
        if self.ANPClamp:
            self.ANPEffect = self.ANPLevel
        else:
            self.ANPEffect = self.ANPOnFract_curve( NephronANP.Log10Conc )

        self.IFPEffect = self.IFPOnFract_curve( NephronIFP.Pressure )
        self.TotalEffect = self.A2Effect * self.SympsEffect * self.ANPEffect * self.IFPEffect * Kidney_Function.Effect
        FractReab.Normal = self.BasicFract
        FractReab.Effects = self.TotalEffect
        FractReab.GetFract_func()
        self.FractReab = FractReab.Fract
        self.Reab = ( min( ( self.FractReab * self.Inflow ), self.MaxReab) )
        self.Outflow = self.Inflow - self.Reab

    def CalcConc_func(self):
        if PT_H2O.Outflow > 0.0:
            self.conc_Na_ = 1000.0 * self.Outflow / PT_H2O.Outflow
        else:
            self.conc_Na_ = 0


class PT_H2O:
    def __init__(self):
        self.Inflow = None
        self.Outflow = None
        self.FractReab = None
        self.Reab = None

    def Calc_func(self):
        self.Inflow = GlomerulusFiltrate.GFR
        self.FractReab = PT_Na.FractReab
        self.Reab = self.Inflow * self.FractReab
        self.Outflow = self.Inflow - self.Reab

class PT_NH3:
    def __init__(self):
        self.SecretionRate = None
        self.BasicRate = 0.04
        self.Tau = 3.0
        self.AcutePhEffect = None
        self.ChronicDelay = 1.0

    def PhOnAcute_curve(self, x):
        return cubic_hermite_spline(x, [7.0, 7.45, 7.8], [2.0, 1.0, 0.0], [0.0, -3.0, 0.0])

    def PhOnChronic_curve(self, x):
        return cubic_hermite_spline(x, [7.0, 7.45, 7.8], [3.0, 1.0, 0.0], [0.0, -4.0, 0.0])

    def Parms_func(self):
        self.K = ( 1 / ( self.Tau * 1440.0 ) )

    def Calc_func(self):
        self.AcutePhEffect = self.PhOnAcute_curve( BloodPh.ArtysPh )
        self.ChronicPhEffect = self.PhOnChronic_curve( BloodPh.ArtysPh )
        self.SecretionRate = self.BasicRate * self.AcutePhEffect * self.ChronicDelay
        self.ChronicDelay = delay( self.K, self.ChronicPhEffect, self.ChronicDelay, System.Dx, None)


class ProximalTubule:
    def __init__(self):
        pass
    
class CD_Urea:
    def __init__(self):
        self.Inflow = None
        self.Reab = None
        self.Outflow = None
        self.conc_Urea = None
        self.conc_Urea_mGperdL = None
        self.MG_TO_MOSM = 16.67
        self.Osmolarity = None

    def CalcFlux_func(self):
        self.Inflow = 0.60 * GlomerulusUrea.Rate
        self.Osmolarity = MedullaUrea.Osmolarity
        self.conc_Urea = self.Osmolarity / self.MG_TO_MOSM
        self.Outflow = self.conc_Urea * CD_H2O.Outflow
        self.Reab = self.Inflow - self.Outflow

    def CalcConc_func(self):
        self.conc_Urea_mGperdL = 100.0 * self.conc_Urea

    def NoFlow_func(self):
        self.Inflow = 0.0
        self.Reab = 0.0
        self.Outflow = 0.0
        self.conc_Urea = 0
        self.conc_Urea_mGperdL = 0
        self.Osmolarity = 0.0

class CD_K:
    def __init__(self):
        self.Inflow = None
        self.Outflow = None
        self.conc_K_ = None
        self.conc_K__mEqperL = None
        self.Osmolarity = None

    def CalcFlux_func(self):
        self.Inflow = DT_K.Outflow
        self.Outflow = self.Inflow

    def CalcConc_func(self):
        self.conc_K_ = self.Outflow / CD_H2O.Outflow
        self.conc_K__mEqperL = 1000.0 * self.conc_K_
        self.Osmolarity = self.conc_K__mEqperL

    def NoFlow_func(self):
        self.Inflow = 0.0
        self.Outflow = 0.0
        self.conc_K_ = 0
        self.conc_K__mEqperL = 0
        self.Osmolarity = 0.0

class CD_NH4:
    def __init__(self):
        self.Inflow = None
        self.Outflow = None
        self.conc_NH4 = None
        self.conc_NH4_mEqperL = None
        self.Osmolarity = None
        self.Flux = None
        self.PhEffect = None

    def PhOnFlux_curve(self, x):
        return cubic_hermite_spline(x, [7.0, 7.45, 7.8], [1.0, 0.6, 0.0], [0.0, -2.0, 0.0])

    def CalcFlux_func(self):
        self.Inflow = 0.0
        self.PhEffect = self.PhOnFlux_curve( BloodPh.ArtysPh )
        self.Flux = self.PhEffect * PT_NH3.SecretionRate
        self.Outflow = self.Inflow + self.Flux

    def CalcConc_func(self):
        self.conc_NH4 = self.Outflow / CD_H2O.Outflow
        self.conc_NH4_mEqperL = 1000.0 * self.conc_NH4
        self.Osmolarity = self.conc_NH4_mEqperL

    def NoFlow_func(self):
        self.Inflow = 0.0
        self.Outflow = 0.0
        self.conc_NH4 = 0
        self.conc_NH4_mEqperL = 0
        self.Osmolarity = 0.0

class CD_PO4:
    def __init__(self):
        self.Inflow = None
        self.Outflow = None
        self.conc_PO4__ = None
        self.conc_PO4___mEqperL = None
        self.Osmolarity = None

    def CalcFlux_func(self):
        self.Inflow = GlomerulusPhosphate.Rate
        self.Outflow = self.Inflow

    def CalcConc_func(self):
        self.conc_PO4__ = self.Outflow / CD_H2O.Outflow
        self.conc_PO4___mEqperL = 1000.0 * self.conc_PO4__
        self.Osmolarity = self.conc_PO4___mEqperL / 2.0

    def NoFlow_func(self):
        self.Inflow = 0.0
        self.Outflow = 0.0
        self.conc_PO4__ = 0
        self.conc_PO4___mEqperL = 0
        self.Osmolarity = 0.0

class CD_Glucose:
    def __init__(self):
        self.Outflow = None
        self.conc_Glucose = None
        self.conc_Glucose_mMolperL = None
        self.Osmolarity = None

    def CalcFlux_func(self):
        self.Outflow = NephronGlucose.Spillover_mMolperMin

    def CalcConc_func(self):
        self.conc_Glucose = self.Outflow / CD_H2O.Outflow
        self.conc_Glucose_mMolperL = 1000.0 * self.conc_Glucose
        self.Osmolarity = self.conc_Glucose_mMolperL

    def NoFlow_func(self):
        self.Outflow = 0.0
        self.conc_Glucose = 0
        self.conc_Glucose_mMolperL = 0
        self.Osmolarity = 0.0

class CD_Cl:
    def __init__(self):
        self.Outflow = None
        self.conc_Cl_ = None
        self.conc_Cl__mEqperL = None
        self.Osmolarity = None

    def CalcFlux_func(self):
        self.Outflow = CollectingDuct.ClFract * CollectingDuct.ClAndHCO3

    def CalcConc_func(self):
        self.conc_Cl_ = self.Outflow / CD_H2O.Outflow
        self.conc_Cl__mEqperL = 1000.0 * self.conc_Cl_
        self.Osmolarity = self.conc_Cl__mEqperL

    def NoFlow_func(self):
        self.Outflow = 0.0
        self.conc_Cl_ = 0
        self.conc_Cl__mEqperL = 0
        self.Osmolarity = 0.0

class CD_KA:
    def __init__(self):
        self.Outflow = None
        self.conc_KA = None
        self.conc_KA_mMolperL = None
        self.Osmolarity = None

    def CalcFlux_func(self):
        self.Outflow = NephronKetoacids.Excretion_mMolperMin

    def CalcConc_func(self):
        self.conc_KA = self.Outflow / CD_H2O.Outflow
        self.conc_KA_mMolperL = 1000.0 * self.conc_KA
        self.Osmolarity = self.conc_KA_mMolperL

    def NoFlow_func(self):
        self.Outflow = 0.0
        self.conc_KA = 0
        self.conc_KA_mMolperL = 0
        self.Osmolarity = 0.0

class CD_HCO3:
    def __init__(self):
        self.Outflow = None
        self.conc_HCO3 = None
        self.conc_HCO3_mEqperL = None
        self.Osmolarity = None

    def CalcFlux_func(self):
        self.Outflow = ( 1.0 - CollectingDuct.ClFract ) * CollectingDuct.ClAndHCO3

    def CalcConc_func(self):
        self.conc_HCO3 = self.Outflow / CD_H2O.Outflow
        self.conc_HCO3_mEqperL = 1000.0 * self.conc_HCO3
        self.Osmolarity = self.conc_HCO3_mEqperL

    def NoFlow_func(self):
        self.Outflow = 0.0
        self.conc_HCO3 = 0
        self.conc_HCO3_mEqperL = 0
        self.Osmolarity = 0.0

class CD_SO4:
    def __init__(self):
        self.Inflow = None
        self.Outflow = None
        self.conc_SO4 = None
        self.conc_SO4_mEqperL = None
        self.Osmolarity = None

    def CalcFlux_func(self):
        self.Inflow = GlomerulusSulphate.Rate
        self.Outflow = self.Inflow

    def CalcConc_func(self):
        self.conc_SO4 = self.Outflow / CD_H2O.Outflow
        self.conc_SO4_mEqperL = 1000.0 * self.conc_SO4
        self.Osmolarity = self.conc_SO4_mEqperL / 2.0

    def NoFlow_func(self):
        self.Inflow = 0.0
        self.Outflow = 0.0
        self.conc_SO4 = 0
        self.conc_SO4_mEqperL = 0
        self.Osmolarity = 0.0

class CD_Protein:
    def __init__(self):
        self.Outflow = None
        self.conc_Protein_GpermL = None

    def CalcFlux_func(self):
        self.Outflow = GlomerulusProtein.Rate

    def CalcConc_func(self):
        self.conc_Protein_GpermL = self.Outflow / CD_H2O.Outflow

    def NoFlow_func(self):
        self.Outflow = 0.0
        self.conc_Protein_GpermL = 0

class CD_Creatinine:
    def __init__(self):
        self.Outflow = None
        self.conc_Creatinine = None
        self.conc_Creatinine_mGperdL = None
        self.Secretion = None
        self.K = 22.0
        self.Block = 0.0
        self.Osmolarity = None

    def CalcFlux_func(self):
        self.Secretion = ( 1.0 - ( self.Block / 100.0 ) ) * self.K * CreatininePool.conc_Creatinine
        self.Outflow = GlomerulusCreatinine.Rate + self.Secretion

    def CalcConc_func(self):
        self.conc_Creatinine = self.Outflow / CD_H2O.Outflow
        self.conc_Creatinine_mGperdL = 100.0 * self.conc_Creatinine
        self.Osmolarity = 8.84 * self.conc_Creatinine

    def NoFlow_func(self):
        self.Outflow = 0.0
        self.conc_Creatinine = 0
        self.conc_Creatinine_mGperdL = 0
        self.Osmolarity = 0.0

class CD_H2OChannels:
    def __init__(self):
        self.Active = None
        self.InactivateK = 0.000125
        self.ReactivateK = 0.0004
        self.Inactive = 1.0

    def CalcActive_func(self):
        self.Active = 2.0 - self.Inactive

    def CalcDervs_func(self):
        self.Change = ( self.InactivateK * CD_H2O.Reab ) - ( self.ReactivateK * self.Inactive )
        self.Inactive = diffeq( self.Change, System.Dx, self.Inactive, 0.01)


class CD_Na:
    def __init__(self):
        self.Inflow = None
        self.FractReab = None
        self.BasicFract = 0.75
        self.Reab = None
        self.Outflow = None
        self.conc_Na_ = None
        self.conc_Na__mEqperL = None
        self.Osmolarity = None
        self.TotalEffect = None
        self.LoadEffect = None
        self.ANPEffect = None
        self.MaxReab = 0.7
        self.ANPClamp = False
        self.ANPLevel = 0.0

    def LoadOnFract_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.4], [2.0, 1.0], [0.0, 0.0])

    def ANPOnFract_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.3, 2.7], [1.2, 1.0, 0.2], [0.0, -0.4, 0.0])

    def CalcFlux_func(self):
        self.Inflow = DT_Na.Outflow
        self.LoadEffect = self.LoadOnFract_curve( self.Inflow )
        if self.ANPClamp:
            self.ANPEffect = self.ANPLevel
        else:
            self.ANPEffect = self.ANPOnFract_curve( NephronANP.Log10Conc )

        self.TotalEffect = self.LoadEffect * self.ANPEffect * Kidney_Function.Effect
        FractReab.Normal = self.BasicFract
        FractReab.Effects = self.TotalEffect
        FractReab.GetFract_func()
        self.FractReab = FractReab.Fract
        self.Reab = ( min( ( self.FractReab * self.Inflow ), self.MaxReab) )
        self.Outflow = self.Inflow - self.Reab

    def CalcConc_func(self):
        self.conc_Na_ = self.Outflow / CD_H2O.Outflow
        self.conc_Na__mEqperL = 1000.0 * self.conc_Na_
        self.Osmolarity = self.conc_Na__mEqperL

    def NoFlow_func(self):
        self.Inflow = 0.0
        self.Reab = 0.0
        self.Outflow = 0.0
        self.conc_Na_ = 0
        self.conc_Na__mEqperL = 0
        self.Osmolarity = 0.0

class CollectingDuct:
    def __init__(self):
        self.Osmolarity = None
        self.ClAndHCO3 = None
        self.ClFract = None
        self.NetSumCats = None

    def PhOnClFract_curve(self, x):
        return cubic_hermite_spline(x, [7.0, 7.45, 7.8], [1.0, 0.93, 0.0], [0.0, -0.5, 0.0])

    def Calc_func(self):
        CD_H2O.CalcInflow_func()
        if CD_H2O.Inflow < 0.1:
            CD_Cl.NoFlow_func()
            CD_Glucose.NoFlow_func()
            CD_H2O.NoFlow_func()
            CD_HCO3.NoFlow_func()
            CD_K.NoFlow_func()
            CD_KA.NoFlow_func()
            CD_Na.NoFlow_func()
            CD_NH4.NoFlow_func()
            CD_PO4.NoFlow_func()
            CD_SO4.NoFlow_func()
            CD_Urea.NoFlow_func()
            CD_Creatinine.NoFlow_func()
            CD_Protein.NoFlow_func()
            self.Osmolarity = 0.0
        else:
            CD_Glucose.CalcFlux_func()
            CD_KA.CalcFlux_func()
            CD_NH4.CalcFlux_func()
            CD_PO4.CalcFlux_func()
            CD_K.CalcFlux_func()
            CD_SO4.CalcFlux_func()
            CD_Na.CalcFlux_func()
            CD_Creatinine.CalcFlux_func()
            CD_Protein.CalcFlux_func()
            CD_H2OChannels.CalcActive_func()
            self.NetSumCats = CD_Na.Outflow + CD_K.Outflow + CD_NH4.Outflow - CD_KA.Outflow - CD_PO4.Outflow - CD_SO4.Outflow
            if self.NetSumCats > 0.0:
                self.ClAndHCO3 = self.NetSumCats
            else:
                self.ClAndHCO3 = 0.0
                CD_NH4.Flux = CD_NH4.Flux - self.NetSumCats
                CD_NH4.Outflow = CD_NH4.Inflow + CD_NH4.Flux
            self.ClFract = self.PhOnClFract_curve( BloodPh.ArtysPh )
            CD_Cl.CalcFlux_func()
            CD_HCO3.CalcFlux_func()
            CD_H2O.CalcFlux_func()
            CD_Cl.CalcConc_func()
            CD_Glucose.CalcConc_func()
            CD_HCO3.CalcConc_func()
            CD_KA.CalcConc_func()
            CD_NH4.CalcConc_func()
            CD_PO4.CalcConc_func()
            CD_K.CalcConc_func()
            CD_SO4.CalcConc_func()
            CD_Na.CalcConc_func()
            CD_Creatinine.CalcConc_func()
            CD_Protein.CalcConc_func()
            CD_Urea.CalcFlux_func()
            CD_Urea.CalcConc_func()
            self.Osmolarity = CD_Cl.Osmolarity + CD_Glucose.Osmolarity + CD_HCO3.Osmolarity + CD_KA.Osmolarity + CD_NH4.Osmolarity + CD_PO4.Osmolarity + CD_K.Osmolarity + CD_SO4.Osmolarity + CD_Na.Osmolarity + CD_Urea.Osmolarity
            CD_H2OChannels.CalcDervs_func()

class CD_H2O:
    def __init__(self):
        self.Inflow = None
        self.Outflow = None
        self.FractReab = None
        self.Reab = None
        self.OutflowMin = None
        self.ADHEffect = None
        self.Perm = None
        self.BasicPerm = 1.0
        self.PermSwitch = False
        self.PermLevel = 0.0
        self.PermEffect = None

    def ADHOnPerm_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 2.0, 10.0], [0.3, 1.0, 3.0], [0.0, 0.5, 0.0])

    def PermOnOutflow_curve(self, x):
        return cubic_hermite_spline(x, [0.3, 1.0, 3.0], [0.0, 0.93, 1.0], [0.0, 0.1, 0.0])

    def CalcInflow_func(self):
        self.Inflow = DT_H2O.Outflow

    def CalcFlux_func(self):
        self.OutflowMin = ( CD_Na.Outflow + CD_K.Outflow + CD_NH4.Outflow + ( 0.5 * CD_Glucose.Outflow ) ) / MedullaNa.conc_Na_
        self.ADHEffect = self.ADHOnPerm_curve( NephronADH.conc_ADH )
        if self.PermSwitch:
            self.Perm = self.PermLevel
        else:
            self.Perm = self.BasicPerm * self.ADHEffect * CD_H2OChannels.Active

        self.PermEffect = self.PermOnOutflow_curve( self.Perm )
        self.Outflow = ( self.PermEffect * self.OutflowMin ) + ( ( 1.0 - self.PermEffect ) * self.Inflow )
        self.Reab = self.Inflow - self.Outflow
        if self.Inflow > 0.0:
            self.FractReab = ( min( ( self.Reab / self.Inflow ), 1.0) )
        else:
            self.FractReab = 0.0


    def NoFlow_func(self):
        self.Outflow = 0.0
        self.Reab = 0.0

class DT_Na:
    def __init__(self):
        self.Inflow = None
        self.Outflow = None
        self.FractReab = None
        self.Reab = None
        self.BasicFract = 0.75
        self.TotalEffect = None
        self.LoadEffect = None
        self.AldoEffect = None
        self.ThiazideEffect = None
        self.AldoSwitch = False
        self.AldoLevel = 0.0
        self.conc_Na_ = None
        self.NormMaxReab = 2.0

    def LoadOnFract_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.6], [2.0, 1.0], [0.0, 0.0])

    def AldoOnFract_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 12.0, 50.0], [0.5, 1.0, 3.0], [0.0, 0.08, 0.0])

    def ThiazideOnFract_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.6], [1.0, 0.2], [-2.0, 0.0])

    def Calc_func(self):
        self.Inflow = LH_Na.Outflow
        self.LoadEffect = self.LoadOnFract_curve( self.Inflow )
        self.AldoEffect = self.AldoOnFract_curve( NephronAldo.conc_Aldo_nGperdL )
        self.ThiazideEffect = self.ThiazideOnFract_curve( ThiazidePool.conc_Thiazide )
        self.TotalEffect = self.LoadEffect * self.AldoEffect * self.ThiazideEffect * Kidney_Function.Effect
        FractReab.Normal = self.BasicFract
        FractReab.Effects = self.TotalEffect
        FractReab.GetFract_func()
        self.FractReab = FractReab.Fract
        self.Reab = ( min( ( self.FractReab * self.Inflow ), ( self.NormMaxReab * self.AldoEffect )) )
        self.Outflow = self.Inflow - self.Reab

    def CalcConc_func(self):
        self.conc_Na_ = 1000.0 * DT_H2O.ADHEffect

class DT_K:
    def __init__(self):
        self.Outflow = None
        self.BasicOutflow = 0.05
        self.AldoEffect = None
        self.KEffect = None
        self.NaEffect = None
        self.ThiazideEffect = None
        self.AldoSwitch = False
        self.AldoLevel = 0.0

    def AldoOnOutflow_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 12.0, 50.0], [0.3, 1.0, 3.0], [0.0, 0.06, 0.0])

    def KOnOutflow_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 4.4, 5.5], [0.0, 1.0, 3.0], [0.0, 0.5, 0.0])

    def NaOnOutflow_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.4, 4.0], [0.3, 1.0, 3.0], [0.0, 1.5, 0.0])

    def ThiazideOnOutflow_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.6], [1.0, 2.0], [2.0, 0.0])

    def Calc_func(self):
        if self.AldoSwitch:
            self.AldoEffect = self.AldoLevel
        else:
            self.AldoEffect = self.AldoOnOutflow_curve( NephronAldo.conc_Aldo_nGperdL )

        self.KEffect = self.KOnOutflow_curve( KPool.conc_K__mEqperL )
        self.NaEffect = self.NaOnOutflow_curve( DT_Na.Outflow )
        self.ThiazideEffect = self.ThiazideOnOutflow_curve( ThiazidePool.conc_Thiazide )
        self.Outflow = self.BasicOutflow * self.AldoEffect * self.KEffect * self.NaEffect * self.ThiazideEffect * Kidney_Function.Effect

class DT_H2O:
    def __init__(self):
        self.Inflow = None
        self.Outflow = None
        self.FractReab = None
        self.Reab = None
        self.ADHEffect = None

    def ADHOnOutflow_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 2.0, 10.0], [0.06, 0.11, 0.16], [0.0, 0.02, 0.0])

    def Calc_func(self):
        self.Inflow = LH_H2O.Outflow
        self.ADHEffect = self.ADHOnOutflow_curve( NephronADH.conc_ADH )
        self.Outflow = DT_Na.Outflow / self.ADHEffect
        self.Reab = self.Inflow - self.Outflow
        if self.Inflow > 0.0:
            self.FractReab = ( min( ( self.Reab / self.Inflow ), 1.0) )
        else:
            self.FractReab = 0.0


class DistalTubule:
    def __init__(self):
        pass
    
class LoopOfHenle:
    def __init__(self):
        pass
    
class LH_:

    def Calc_func(self):
        pass

class LH_Na:
    def __init__(self):
        self.Inflow = None
        self.Outflow = None
        self.FractReab = None
        self.Reab = None
        self.BasicFract = 0.75
        self.TotalEffect = None
        self.LoadEffect = None
        self.AldoEffect = None
        self.FurosemideEffect = None
        self.conc_Na_ = None
        self.MaxReab = 7.0

    def LoadOnFract_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 7.2, 20.0], [3.0, 1.0, 0.5], [0.0, -0.2, 0.0])

    def AldoOnFract_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 10.0], [0.7, 1.0], [0.0, 0.0])

    def FurosemideOnFract_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.1], [1.0, 0.0], [-1.0, 0.0])

    def Calc_func(self):
        self.Inflow = PT_Na.Outflow
        self.LoadEffect = self.LoadOnFract_curve( self.Inflow )
        self.AldoEffect = self.AldoOnFract_curve( NephronAldo.conc_Aldo_nGperdL )
        self.FurosemideEffect = Kidney_Function.Effect * Kidney_NephronCount.Filtering_xNormal * self.FurosemideOnFract_curve( FurosemidePool.conc_Furosemide )
        self.TotalEffect = self.LoadEffect * self.AldoEffect * self.FurosemideEffect * Kidney_Function.Effect
        FractReab.Normal = self.BasicFract
        FractReab.Effects = self.TotalEffect
        FractReab.GetFract_func()
        self.FractReab = FractReab.Fract
        self.Reab = ( min( ( self.FractReab * self.Inflow ), self.MaxReab) )
        self.Outflow = self.Inflow - self.Reab

    def CalcConc_func(self):
        if LH_H2O.Outflow > 0.0:
            self.conc_Na_ = 1000.0 * self.Outflow / LH_H2O.Outflow
        else:
            self.conc_Na_ = 0


class LH_H2O:
    def __init__(self):
        self.Inflow = None
        self.Outflow = None
        self.FractReab = None
        self.Reab = None
        self.LoopPerm_percent = 37.0

    def Calc_func(self):
        self.Inflow = PT_H2O.Outflow
        self.FractReab = 0.01 * self.LoopPerm_percent * LH_Na.FractReab
        self.Reab = self.FractReab * self.Inflow
        self.Outflow = self.Inflow - self.Reab

class Testosterone:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.Secretion = None
        self.Degradation = None
        self.TargetConcFemale = 0.60
        self.TargetConcMale = 18.5
        self.TargetConc = None
        self.InitialMass = None
        self.conc_Conc_nMolperL = None
        self.conc_Conc_nGpermL = None
        self.NMOLperL_TO_NGperML = 0.2884
        self.PumpSwitch = False
        self.PumpSetting = 0.0
        self.K = 0.043

    def Init_func(self):
        if Gender.IsFemale:
            self.TargetConc = self.TargetConcFemale
        else:
            self.TargetConc = self.TargetConcMale

        self.InitialMass = self.TargetConc * ECFV.InitialVol_L
        self.Mass = self.InitialMass

    def Conc_func(self):
        self.conc_Conc_nMolperL = self.Mass / ECFV.Vol_L
        self.conc_Conc_nGpermL = self.conc_Conc_nMolperL * self.NMOLperL_TO_NGperML

    def Dervs_func(self):
        if Gender.IsFemale:
            self.Secretion = Ovaries_Testosterone.Secretion
        else:
            self.Secretion = Testes_Testosterone.Secretion

        self.Degradation = self.K * self.Mass
        self.Gain = self.Secretion + ( self.PumpSetting * self.PumpSwitch )
        self.Loss = self.Degradation
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 2.0)


class HeartValves:

    def Parms_func(self):
        AorticValve.Parms_func()
        MitralValve.Parms_func()
        PulmonicValve.Parms_func()
        TricuspidValve.Parms_func()

class TricuspidValve_Regurgitation:
    def __init__(self):
        self.Area = 0.0
        self.Effect = None

    def Effect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 7.4], [1.0, 0.0], [0.0, 0.0])

    def Parms_func(self):
        self.Effect = self.Effect_curve( self.Area )

class TricuspidValve:

    def Parms_func(self):
        TricuspidValve_Stenosis.Parms_func()
        TricuspidValve_Regurgitation.Parms_func()

class TricuspidValve_Stenosis:
    def __init__(self):
        self.Area = 7.4
        self.Effect = None

    def Effect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 7.4], [0.0, 1.0], [0.0, 0.0])

    def Parms_func(self):
        self.Effect = self.Effect_curve( self.Area )

class MitralValve:

    def Parms_func(self):
        MitralValve_Stenosis.Parms_func()
        MitralValve_Regurgitation.Parms_func()

class MitralValve_Regurgitation:
    def __init__(self):
        self.Area = 0.0
        self.Effect = None

    def Effect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 5.0], [1.0, 0.0], [0.0, 0.0])

    def Parms_func(self):
        self.Effect = self.Effect_curve( self.Area )

class MitralValve_Stenosis:
    def __init__(self):
        self.Area = 5.0
        self.Effect = None

    def Effect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 5.0], [0.0, 1.0], [0.0, 0.0])

    def Parms_func(self):
        self.Effect = self.Effect_curve( self.Area )

class AorticValve:

    def Parms_func(self):
        AorticValve_Stenosis.Parms_func()
        AorticValve_Regurgitation.Parms_func()

class AorticValve_Regurgitation:
    def __init__(self):
        self.Area = 0.0
        self.Effect = None

    def Effect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 3.3], [1.0, 0.0], [0.0, 0.0])

    def Parms_func(self):
        self.Effect = self.Effect_curve( self.Area )

class AorticValve_Stenosis:
    def __init__(self):
        self.Area = 3.3
        self.Effect = None

    def Effect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 3.3], [0.0, 1.0], [0.0, 0.0])

    def Parms_func(self):
        self.Effect = self.Effect_curve( self.Area )

class PulmonicValve_Stenosis:
    def __init__(self):
        self.Area = 3.3
        self.Effect = None

    def Effect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 3.3], [0.0, 1.0], [0.0, 0.0])

    def Parms_func(self):
        self.Effect = self.Effect_curve( self.Area )

class PulmonicValve_Regurgitation:
    def __init__(self):
        self.Area = 0.0
        self.Effect = None

    def Effect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 3.3], [1.0, 0.0], [0.0, 0.0])

    def Parms_func(self):
        self.Effect = self.Effect_curve( self.Area )

class PulmonicValve:

    def Parms_func(self):
        PulmonicValve_Stenosis.Parms_func()
        PulmonicValve_Regurgitation.Parms_func()

class DialyzerActivity:
    def __init__(self):
        self.query_Scheduled = 0.0
        self.query_Active = 0.0
        self.BloodFlow = None
        self.DialysateFlow = None
        self.UltrafiltrationRate = None
        self.Alpha = None
        self.Na_Flux = None
        self.K_Flux = None
        self.Cl_Flux = None
        self.UreaFlux = None
        self.IntervalTimer = Timer(0, "None", System.Dx)
        timervars.append(self.IntervalTimer)
        self.DurationTimer = Timer(0, "None", System.Dx)
        timervars.append(self.DurationTimer)
        self.TotalDialysateUsed = 0.0
        self.TotalUltrafiltration = 0.0

    def Dervs_func(self):
        if self.query_Active:
            self.BloodFlow = 0.01 * DialyzerControl.BloodFlow_percent * DialysisShunt.BloodFlow
            self.DialysateFlow = DialyzerControl.DialysateFlow
            self.UltrafiltrationRate = DialyzerControl.Ultrafiltration
            self.Alpha = ( self.BloodFlow * self.DialysateFlow ) / ( self.BloodFlow + self.DialysateFlow )
            self.Na_Flux = 0.001 * self.Alpha * ( NaPool.conc_Na__mEqperL - DialysateComposition.conc_Na_ )
            self.K_Flux = 0.001 * self.Alpha * ( KPool.conc_K__mEqperL - DialysateComposition.conc_K_ )
            self.Cl_Flux = 0.001 * self.Alpha * ( ClPool.conc_Cl__mEqperL - DialysateComposition.conc_Cl_ )
            self.UreaFlux = 0.001 * self.Alpha * ( UreaPool.conc_Urea_mGperdL - DialysateComposition.conc_Urea )
        else:
            self.BloodFlow = 0.0
            self.DialysateFlow = 0.0
            self.UltrafiltrationRate = 0.0
            self.Alpha = 0.0
            self.Na_Flux = 0.0
            self.K_Flux = 0.0
            self.Cl_Flux = 0.0
            self.UreaFlux = 0.0
        self.DialysateChange = self.DialysateFlow
        self.UltrafiltrationChange = self.UltrafiltrationRate
        self.TotalDialysateUsed = diffeq( self.DialysateChange, System.Dx, self.TotalDialysateUsed, None)

        self.TotalUltrafiltration = diffeq( self.UltrafiltrationChange, System.Dx, self.TotalUltrafiltration, None)


    def Wrapup_func(self):
        if self.query_Scheduled:
            if self.IntervalTimer == 0:
                self.Start_func()
            if self.query_Active:
                if self.DurationTimer == 0:
                    self.StopDuration_func()
            else:
                pass
        else:
            pass

    def Start_func(self):
        self.StartSchedule_func()
        self.StartDuration_func()

    def Stop_func(self):
        self.StopSchedule_func()
        self.StopDuration_func()

    def StartSchedule_func(self):
        self.query_Scheduled = True
        self.IntervalTimer.val = 1440.0 * DialyzerControl.Interval_Days
        self.IntervalTimer.state = "DOWN"

    def StopSchedule_func(self):
        self.query_Scheduled = False
        self.IntervalTimer.state = "OFF"

    def StartDuration_func(self):
        self.query_Active = True
        self.DurationTimer.val = 60.0 * DialyzerControl.Duration_Hrs
        self.DurationTimer.state = "DOWN"

    def StopDuration_func(self):
        self.query_Active = False
        self.DurationTimer.state = "OFF"

class DialysateComposition:
    def __init__(self):
        self.conc_Na_ = 140.0
        self.conc_K_ = 3.0
        self.conc_Cl_ = 100.0
        self.conc_Urea = 0.0
    
class DialysisShunt:
    def __init__(self):
        self.BasicConductance = 0.0
        self.Conductance = None
        self.PressureGradient = None
        self.BloodFlow = None

    def Dervs_func(self):
        self.Conductance = Viscosity.ConductanceEffect * self.BasicConductance
        self.PressureGradient = SystemicArtys.Pressure - SystemicVeins.Pressure
        self.BloodFlow = self.Conductance * self.PressureGradient

class DialyzerControl:
    def __init__(self):
        self.Switch = False
        self.Interval_Days = 3.0
        self.Duration_Hrs = 5.0
        self.BloodFlow_percent = 20.0
        self.DialysateFlow = 500.0
        self.Ultrafiltration = 10.0

    def Parms_func(self):
        if self.Switch:
            self.TurnOn_func()
        else:
            DialyzerActivity.Stop_func()

    def TurnOn_func(self):
        if DialysisShunt.BloodFlow > 0.0:
            DialyzerActivity.Start_func()
        else:
            self.Switch = False

class Hemodialysis:

    def Parms_func(self):
        DialyzerControl.Parms_func()

    def Dervs_func(self):
        DialysisShunt.Dervs_func()
        DialyzerActivity.Dervs_func()

    def Wrapup_func(self):
        DialyzerActivity.Wrapup_func()

class ANP:

    def Parms_func(self):
        ANPSecretion.Parms_func()
        ANPPump.Parms_func()

    def CalcConc_func(self):
        ANPPool.CalcConc_func()

    def Dervs_func(self):
        ANPSecretion.Dervs_func()
        ANPClearance.Dervs_func()
        ANPPool.Dervs_func()

class ANPSecretion:
    def __init__(self):
        self.Rate = None
        self.Tau = 20.0
        self.RightRate = None
        self.RightBase = 41
        self.RAPEffect = None
        self.LeftRate = None
        self.LeftBase = 26
        self.LAPEffect = None
        self.Clamp = False
        self.Level = 0.0
        self.NaturalRate = 67.0

    def RAPEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 4.0, 20.0], [0.0, 1.0, 10.0], [0.0, 0.4, 0.0])

    def LAPEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 8.0, 20.0], [0.0, 1.0, 10.0], [0.0, 0.4, 0.0])

    def Parms_func(self):
        self.K = ( 1 / self.Tau )

    def Dervs_func(self):
        self.RAPEffect = self.RAPEffect_curve( RightAtrium.TMP )
        self.LAPEffect = self.LAPEffect_curve( LeftAtrium.TMP )
        self.RightRate = self.RightBase * self.RAPEffect
        self.LeftRate = self.LeftBase * self.LAPEffect
        self.SteadyState = self.RightRate + self.LeftRate
        if self.Clamp:
            self.Rate = self.Level
        else:
            self.Rate = self.NaturalRate

        self.NaturalRate = delay( self.K, self.SteadyState, self.NaturalRate, System.Dx, 0.67)


class ANPPool:
    def __init__(self):
        self.conc_ANP = None
        self.conc_ANP_pGpermL = None
        self.Log10Conc = None
        self.PMOLTOPG = 3.060
        self.Gain = None
        self.Loss = None
        self.Change = None
        self.Targetconc_ANP = 20.0
        self.InitialMass = None

    def Init_func(self):
        self.InitialMass = self.Targetconc_ANP * ECFV.InitialVol_L
        self.Mass = self.InitialMass

    def Initialize_func(self):
        self.Mass = self.InitialConc * ECFV.Vol_L

    def CalcConc_func(self):
        self.conc_ANP = self.Mass / ECFV.Vol_L
        self.conc_ANP_pGpermL = self.PMOLTOPG * self.conc_ANP
        if self.conc_ANP > 1.0:
            self.Log10Conc = ( math.log10( self.conc_ANP ) )
        else:
            self.Log10Conc = 0.0


    def Dervs_func(self):
        self.Gain = ANPSecretion.Rate + ANPPump.Rate
        self.Loss = ANPClearance.Rate
        self.Change = self.Gain - self.Loss
        self.F1 = self.Gain
        self.F2 = ANPClearance.K
        self.Mass = backwardeuler( self.F1, self.F2, System.Dx, self.Mass, 3.0)


class ANPClearance:
    def __init__(self):
        self.Rate = None
        self.K = 0.223

    def Dervs_func(self):
        self.Rate = self.K * ANPPool.Mass

class ANPPump:
    def __init__(self):
        self.Rate = None
        self.Switch = False
        self.Setting = 0.0

    def Parms_func(self):
        if self.Switch:
            self.Rate = self.Setting
        else:
            self.Rate = 0.0


class BloodIons:
    def __init__(self):
        self.Cations = None
        self.Anions = None
        self.StrongAnions = None
        self.WeakAnions = None
        self.Protein = None
        self.AnionsLessProtein = None
        self.conc_SID = None
        self.conc_SID_mEqperL = None

    def CalcSID_func(self):
        self.Cations = NaPool.conc_Na__mEqperL + KPool.conc_K__mEqperL
        self.Anions = self.Cations
        self.StrongAnions = ClPool.conc_Cl__mEqperL + LacPool.conc_Lac__mEqperL + KAPool.conc_KA_mMolperL + SO4Pool.conc_SO4___mEqperL + PO4Pool.conc_PO4___mEqperL
        self.conc_SID_mEqperL = self.Cations - self.StrongAnions
        self.conc_SID = 0.001 * self.conc_SID_mEqperL

    def FinishSums_func(self):
        self.WeakAnions = self.Anions - self.StrongAnions
        self.Protein = self.WeakAnions - CO2Veins.conc_HCO3_mEqperL
        self.AnionsLessProtein = self.Anions - self.Protein

class CreatininePool:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.RenalLoss = None
        self.ExtrarenalLoss = None
        self.conc_Creatinine = None
        self.conc_Creatinine_mGperdL = None
        self.conc_Creatinine_uMolperL = None
        self.VolDist = None
        self.VolDistFract = 0.87
        self.PER_ML_TO_PER_DL = 100.0
        self.MG_TO_UMOL = 8840.0
        self.Targetconc_Creatinine = 0.0082
        self.InitialMass = None
        self.InitialVolDist = None

    def Init_func(self):
        self.InitialVolDist = self.VolDistFract * BodyH2O.InitialTotalVol
        self.InitialMass = self.Targetconc_Creatinine * self.InitialVolDist
        self.Mass = self.InitialMass

    def Conc_func(self):
        self.VolDist = self.VolDistFract * BodyH2O.TotalVol
        self.conc_Creatinine = self.Mass / self.VolDist
        self.conc_Creatinine_mGperdL = self.PER_ML_TO_PER_DL * self.conc_Creatinine
        self.conc_Creatinine_uMolperL = self.MG_TO_UMOL * self.conc_Creatinine

    def Dervs_func(self):
        self.RenalLoss = CD_Creatinine.Outflow
        self.ExtrarenalLoss = 0.02 * self.conc_Creatinine_mGperdL
        self.Gain = CreatineCells.CreatineToCreatinine
        self.Loss = self.RenalLoss + self.ExtrarenalLoss
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 3.1)


class Creatinine:

    def Conc_func(self):
        CreatininePool.Conc_func()

    def Dervs_func(self):
        CreatininePool.Dervs_func()

class Anesthesia:
    def __init__(self):
        self.BrainFunction = None
        self.TidalVolume = None
        self.HeartContractility = None
        self.VascularConductance = None

    def Parms_func(self):
        AnesthesiaGas.Parms_func()
        AnesthesiaIV.Parms_func()

    def Calc_func(self):
        AnesthesiaGas.CalcConc_func()
        AnesthesiaIV.CalcConc_func()
        self.BrainFunction = AnesthesiaGasBrain.BrainFunc * AnesthesiaIVBrain.BrainFunc
        self.TidalVolume = AnesthesiaGasBrain.TidalVol * AnesthesiaIVBrain.TidalVol
        self.HeartContractility = AnesthesiaGasLeftHeart.HrtCont * AnesthesiaIVLeftHeart.HrtCont
        self.VascularConductance = AnesthesiaGasOtherTissue.VascCond * AnesthesiaIVOtherTissue.VascCond

    def Dervs_func(self):
        AnesthesiaGas.Dervs_func()
        AnesthesiaIV.Dervs_func()

class NoAnesthesia:
    def __init__(self):
        self.BrainFunction = None
        self.TidalVolume = None
        self.HeartContractility = None
        self.VascularConductance = None

    def Parms_func(self):
        pass

    def Calc_func(self):
        self.BrainFunction = 1.0
        self.TidalVolume = 1.0
        self.HeartContractility = 1.0
        self.VascularConductance = 1.0

    def Dervs_func(self):
        pass

class Transfusion:
    def __init__(self):
        self.Switch = False
        self.Setting = 0.0
        self.Hct_percent = 44.0
        self.Hct = None
        self.PlasmaRate = None
        self.ProteinRate = None
        self.RBCRate = None
        self.NaRate = None
        self.KRate = None
        self.ClRate = None
        self.Units = None
        self.Volume = 0.0

    def Parms_func(self):
        if self.Switch:
            self.Rate = self.Setting
        else:
            self.Rate = 0.0

        self.Hct = self.Hct_percent / 100.0
        self.PlasmaRate = ( 1.0 - self.Hct ) * self.Rate
        self.ProteinRate = 0.07 * self.PlasmaRate
        self.RBCRate = self.Hct * self.Rate
        self.NaRate = 0.140 * self.Rate
        self.KRate = 0.0044 * self.Rate
        self.ClRate = 0.105 * self.Rate
        self.Volume = diffeq( self.Rate, System.Dx, self.Volume, 10.0)


    def CalcVol_func(self):
        self.Units = 0.0025 * self.Volume

    def ResetVolume_func(self):
        self.Volume = 0.0

class Bladder:
    def __init__(self):
        self.TimeLastVoid = 0.0

    def Dervs_func(self):
        BladderVolume.Dervs_func()
        BladderSodium.Dervs_func()
        BladderChloride.Dervs_func()
        BladderCreatinine.Dervs_func()
        BladderGlucose.Dervs_func()
        BladderBicarbonate.Dervs_func()
        BladderPotassium.Dervs_func()
        BladderKetoacid.Dervs_func()
        BladderAmmonia.Dervs_func()
        BladderPhosphate.Dervs_func()
        BladderProtein.Dervs_func()
        BladderSulphate.Dervs_func()
        BladderUrea.Dervs_func()

    def Wrapup_func(self):
        BladderSodium.Conc_func()
        BladderChloride.Conc_func()
        BladderCreatinine.Conc_func()
        BladderGlucose.Conc_func()
        BladderBicarbonate.Conc_func()
        BladderPotassium.Conc_func()
        BladderKetoacid.Conc_func()
        BladderAmmonia.Conc_func()
        BladderPhosphate.Conc_func()
        BladderProtein.Conc_func()
        BladderSulphate.Conc_func()
        BladderUrea.Conc_func()
        if BladderVolume.Mass >= 1000.0:
            self.TimeLastVoid = System.X
            BladderVolume.Void_func()
            BladderSodium.Void_func()
            BladderChloride.Void_func()
            BladderCreatinine.Void_func()
            BladderGlucose.Void_func()
            BladderBicarbonate.Void_func()
            BladderPotassium.Void_func()
            BladderKetoacid.Void_func()
            BladderAmmonia.Void_func()
            BladderPhosphate.Void_func()
            BladderProtein.Void_func()
            BladderSulphate.Void_func()
            BladderUrea.Void_func()
        else:
            pass

class BladderChloride:
    def __init__(self):
        self.conc_Cl_ = None
        self.conc_Cl__mEqperL = None
        self.Mass = 0.0

    def Dervs_func(self):
        self.Change = CD_Cl.Outflow
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, None)


    def Conc_func(self):
        self.conc_Cl_ = self.Mass / BladderVolume.Mass
        self.conc_Cl__mEqperL = 1000.0 * self.conc_Cl_

    def Void_func(self):
        self.Mass = self.Mass - ( BladderVolume.VolumeVoid * self.conc_Cl_ )

class BladderSulphate:
    def __init__(self):
        self.conc_SO4__ = None
        self.conc_SO4___mEqperL = None
        self.Mass = 0.0

    def Dervs_func(self):
        self.Change = CD_SO4.Outflow
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, None)


    def Conc_func(self):
        self.conc_SO4__ = self.Mass / BladderVolume.Mass
        self.conc_SO4___mEqperL = 1000.0 * self.conc_SO4__

    def Void_func(self):
        self.Mass = self.Mass - ( BladderVolume.VolumeVoid * self.conc_SO4__ )

class BladderKetoacid:
    def __init__(self):
        self.conc_KA_ = None
        self.conc_KA__mMolperL = None
        self.Mass = 0.0

    def Dervs_func(self):
        self.Change = CD_KA.Outflow
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, None)


    def Conc_func(self):
        self.conc_KA_ = self.Mass / BladderVolume.Mass
        self.conc_KA__mMolperL = 100.0 * self.conc_KA_

    def Void_func(self):
        self.Mass = self.Mass - ( BladderVolume.VolumeVoid * self.conc_KA_ )

class BladderCreatinine:
    def __init__(self):
        self.conc_Creatinine = None
        self.conc_Creatinine_mGperdL = None
        self.Mass = 0.0

    def Dervs_func(self):
        self.Change = CD_Creatinine.Outflow
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, None)


    def Conc_func(self):
        self.conc_Creatinine = self.Mass / BladderVolume.Mass
        self.conc_Creatinine_mGperdL = 100.0 * self.conc_Creatinine

    def Void_func(self):
        self.Mass = self.Mass - ( BladderVolume.VolumeVoid * self.conc_Creatinine )

class BladderGlucose:
    def __init__(self):
        self.conc_Glucose = None
        self.conc_Glucose_mMolperL = None
        self.Mass = 0.0

    def Dervs_func(self):
        self.Change = CD_Glucose.Outflow
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, None)


    def Conc_func(self):
        self.conc_Glucose = self.Mass / BladderVolume.Mass
        self.conc_Glucose_mMolperL = 100.0 * self.conc_Glucose

    def Void_func(self):
        self.Mass = self.Mass - ( BladderVolume.VolumeVoid * self.conc_Glucose )

class BladderUrea:
    def __init__(self):
        self.conc_Urea = None
        self.conc_Urea_mGperdL = None
        self.Mass = 0.0

    def Dervs_func(self):
        self.Change = CD_Urea.Outflow
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, None)


    def Conc_func(self):
        self.conc_Urea = self.Mass / BladderVolume.Mass
        self.conc_Urea_mGperdL = 100.0 * self.conc_Urea

    def Void_func(self):
        self.Mass = self.Mass - ( BladderVolume.VolumeVoid * self.conc_Urea )

class BladderPotassium:
    def __init__(self):
        self.conc_K_ = None
        self.conc_K__mEqperL = None
        self.Mass = 0.0

    def Dervs_func(self):
        self.Change = CD_K.Outflow
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, None)


    def Conc_func(self):
        self.conc_K_ = self.Mass / BladderVolume.Mass
        self.conc_K__mEqperL = 1000.0 * self.conc_K_

    def Void_func(self):
        self.Mass = self.Mass - ( BladderVolume.VolumeVoid * self.conc_K_ )

class BladderPhosphate:
    def __init__(self):
        self.conc_PO4__ = None
        self.conc_PO4___mEqperL = None
        self.Mass = 0.0

    def Dervs_func(self):
        self.Change = CD_PO4.Outflow
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, None)


    def Conc_func(self):
        self.conc_PO4__ = self.Mass / BladderVolume.Mass
        self.conc_PO4___mEqperL = 1000.0 * self.conc_PO4__

    def Void_func(self):
        self.Mass = self.Mass - ( BladderVolume.VolumeVoid * self.conc_PO4__ )

class BladderSodium:
    def __init__(self):
        self.conc_Na_ = None
        self.conc_Na__mEqperL = None
        self.Mass = 0.0

    def Dervs_func(self):
        self.Change = CD_Na.Outflow
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, None)


    def Conc_func(self):
        self.conc_Na_ = self.Mass / BladderVolume.Mass
        self.conc_Na__mEqperL = 1000.0 * self.conc_Na_

    def Void_func(self):
        self.Mass = self.Mass - ( BladderVolume.VolumeVoid * self.conc_Na_ )

class BladderProtein:
    def __init__(self):
        self.conc_Protein = None
        self.conc_Protein_GpermL = None
        self.Mass = 0.0

    def Dervs_func(self):
        self.Change = CD_Protein.Outflow
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, None)


    def Conc_func(self):
        self.conc_Protein = self.Mass / BladderVolume.Mass
        self.conc_Protein_GpermL = self.conc_Protein

    def Void_func(self):
        self.Mass = self.Mass - ( BladderVolume.VolumeVoid * self.conc_Protein )

class BladderBicarbonate:
    def __init__(self):
        self.conc_HCO3_ = None
        self.conc_HCO3__mEqperL = None
        self.Mass = 0.0

    def Dervs_func(self):
        self.Change = CD_HCO3.Outflow
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, None)


    def Conc_func(self):
        self.conc_HCO3_ = self.Mass / BladderVolume.Mass
        self.conc_HCO3__mEqperL = 1000.0 * self.conc_HCO3_

    def Void_func(self):
        self.Mass = self.Mass - ( BladderVolume.VolumeVoid * self.conc_HCO3_ )

class BladderAmmonia:
    def __init__(self):
        self.conc_NH4_ = None
        self.conc_NH4__mEqperL = None
        self.Mass = 0.0

    def Dervs_func(self):
        self.Change = CD_NH4.Outflow
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, None)


    def Conc_func(self):
        self.conc_NH4_ = self.Mass / BladderVolume.Mass
        self.conc_NH4__mEqperL = 1000.0 * self.conc_NH4_

    def Void_func(self):
        self.Mass = self.Mass - ( BladderVolume.VolumeVoid * self.conc_NH4_ )

class BladderVolume:
    def __init__(self):
        self.VolumeVoid = 0.0
        self.Mass = 200.0

    def Dervs_func(self):
        self.Change = CD_H2O.Outflow
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 10.0)


    def Void_func(self):
        self.VolumeVoid = self.Mass - 300.0
        self.Mass = 300.0

class Hemorrhage:
    def __init__(self):
        self.Switch = False
        self.TargetRate = 0.0
        self.PlasmaRate = None
        self.ProteinRate = None
        self.RBCRate = None
        self.NaRate = None
        self.KRate = None
        self.ClRate = None
        self.Volume = 0.0

    def Parms_func(self):
        if self.Switch:
            self.Rate = self.TargetRate
        else:
            self.Rate = 0.0

        self.Volume = diffeq( self.Rate, System.Dx, self.Volume, 10.0)


    def Dervs_func(self):
        self.PlasmaRate = BloodVol.PVCrit * self.Rate
        self.ProteinRate = PlasmaProtein.conc_Protein * self.PlasmaRate
        self.RBCRate = BloodVol.Hct * self.Rate
        self.NaRate = NaPool.conc_Na_ * self.Rate
        self.KRate = KPool.conc_K_ * self.Rate
        self.ClRate = ClPool.conc_Cl_ * self.Rate

    def ResetVolume_func(self):
        self.Volume = 0.0

class LeftHeart_Lactate:
    def __init__(self):
        self.conc_Lac_ = None
        self.conc_Lac__mEqperL = None
        self.conc_Lac__mGperdL = None
        self.DC = 18.0
        self.Made = None
        self.Made_mGperMin = None
        self.Used = None
        self.Used_mGperMin = None
        self.Outflux = None
        self.Outflux_0 = None
        self.K = None
        self.Alpha = None
        self.MEQ_ML_TO_MG_DL = 9008.0
        self.GLUCOSE_TO_LACTATE = 0.99
        self.MG_TO_MEQ = 0.0112
        self.Mass = 0.17

    def CalcConc_func(self):
        self.conc_Lac_ = self.Mass / LeftHeart_Size.LiquidVol
        self.conc_Lac__mEqperL = 1000.0 * self.conc_Lac_
        self.conc_Lac__mGperdL = self.MEQ_ML_TO_MG_DL * self.conc_Lac_

    def CalcDervs_func(self):
        self.Made_mGperMin = self.GLUCOSE_TO_LACTATE * LeftHeart_Fuel.AnaerobicGlucoseUsed_mGperMin
        self.Made = self.MG_TO_MEQ * self.Made_mGperMin
        self.Used_mGperMin = LeftHeart_Fuel.LacUsed_mGperMin
        self.Used = self.MG_TO_MEQ * self.Used_mGperMin
        self.K = self.DC / LeftHeart_Size.LiquidVol
        if System.Dx >=0:
            self.Alpha = 0.0
        elif ( self.K * System.Dx ) >= 100.0:
            self.Alpha = 4E-44
        elif True:
            self.Alpha = ( math.e ** ( - self.K * System.Dx ) )
        self.Outflux_0 = self.DC * ( self.conc_Lac_ - LacPool.conc_Lac_ )
        self.Outflux = ( self.Alpha * self.Outflux_0 ) + ( ( 1 - self.Alpha ) * ( self.Made + self.Used ) )
        self.Change = self.Made - self.Used - self.Outflux
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.002)


class LeftHeart_Metabolism:
    def __init__(self):
        self.TotalCalsUsed = None
        self.BasalCalsUsed = None
        self.InitialBasalCalsUsed = None
        self.BasalCalsUsed__CalperMinperG = 0.0669
        self.CalMultiplier = 1.0
        self.AerobicCals = None
        self.AnaerobicCals = None
        self.O2Need = None
        self.O2Lack = None

    def ScaleCals_func(self):
        self.InitialBasalCalsUsed = self.CalMultiplier * self.BasalCalsUsed__CalperMinperG * LeftHeart_Size.InitialMass

    def CalcCals_func(self):
        self.BasalCalsUsed = self.CalMultiplier * self.BasalCalsUsed__CalperMinperG * LeftHeart_Size.Mass
        self.TotalCalsUsed = ( self.BasalCalsUsed * Thyroid.Effect * HeatMetabolism.Core * LeftHeart_Structure.Effect ) + LeftHeart_Work.TotalCals
        self.O2Need = Metabolism_Tools.CalToO2 * self.TotalCalsUsed

    def SplitCals_func(self):
        self.O2Lack = self.O2Need - LeftHeart_Flow.O2Use
        self.AerobicCals = Metabolism_Tools.O2ToCal * LeftHeart_Flow.O2Use
        self.AnaerobicCals = Metabolism_Tools.O2ToCal * self.O2Lack

class LeftHeart_Infarction:
    def __init__(self):
        self.Areapercent = 0.0
        self.Effect = None
        self.IschemicTissueFraction = None
        self.IsIschemic = False
        self.DeadTissueFraction = 0.0

    def Parms_func(self):
        self.DeadTissueK = 0.004
        self.DamagedTissueFraction = self.Areapercent / 100.0
        self.Effect = 1.0 - self.DamagedTissueFraction
        self.DeadTissueFraction = delay( self.DeadTissueK, self.DamagedTissueFraction, self.DeadTissueFraction, System.Dx, 0.01)


    def Dervs_func(self):
        self.IschemicTissueFraction = self.DamagedTissueFraction - self.DeadTissueFraction
        if ( self.IsIschemic ) and ( self.IschemicTissueFraction < 0.03 ):
            self.IsIschemic = False
        else:
            pass
        if ( not self.IsIschemic ) and ( self.IschemicTissueFraction > 0.05 ):
            self.IsIschemic = True
        else:
            pass
        self.DeadTissueFraction = delay( self.DeadTissueK, self.DamagedTissueFraction, self.DeadTissueFraction, System.Dx, 0.01)


class LeftHeart_Flow:
    def __init__(self):
        self.Conductance = None
        self.SmallVesselConductance = None
        self.SmallVesselBasicConductance = 2.2
        self.LargeVesselConductance = None
        self.LargeVesselBasicConductance = 50.0
        self.A2Effect = None
        self.SympsEffect = None
        self.ADHEffect = None
        self.PO2Effect = None
        self.MetabolismEffect = None
        self.AerobicFraction = None
        self.O2Use = None
        self.conc_O2 = None
        self.BloodFlow = None
        self.PlasmaFlow = None
        self.PO2 = 16.8
    def SympsOnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.0, 4.0], [1.3, 1.0, 0.8], [0.0, -0.16, 0.0])

    def PO2OnConductance_curve(self, x):
        return cubic_hermite_spline(x, [12.0, 17.0, 30.0], [2.0, 1.0, 0.8], [0.0, -0.04, 0.0])

    def ADHOnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.8, 3.0], [1.0, 0.1], [0.0, 0.0])

    def PO2OnAerobicFraction_curve(self, x):
        return cubic_hermite_spline(x, [2.0, 10.0], [0.0, 1.0], [0.0, 0.0])

    def MetabolismOnConductance_curve(self, x):
        return cubic_hermite_spline(x, [30.0, 100.0], [1.0, 3.0], [0.0, 0.0])

    def Calc_func(self):
        self.LargeVesselConductance = self.LargeVesselBasicConductance * Viscosity.ConductanceEffect
        self.SympsEffect = self.SympsOnConductance_curve( LeftHeart_AlphaReceptors.Activity )
        self.ADHEffect = self.ADHOnConductance_curve( ADHPool.Log10Conc )
        self.MetabolismEffect = self.MetabolismOnConductance_curve( LeftHeart_Metabolism.O2Need )
        self.SearchMax = PO2Artys.Pressure

        def PO2implicitfunc(PO2):
            self.PO2Effect = self.PO2OnConductance_curve( PO2 )
            self.SmallVesselConductance = self.SmallVesselBasicConductance * self.SympsEffect * self.PO2Effect * self.ADHEffect * self.MetabolismEffect * Viscosity.ConductanceEffect * Anesthesia.VascularConductance * LeftHeart_Vasculature.Effect * LeftHeart_Infarction.Effect
            self.Conductance = ( self.SmallVesselConductance * self.LargeVesselConductance ) / ( self.SmallVesselConductance + self.LargeVesselConductance )
            self.BloodFlow = ( max( ( LeftHeart_Pressure.PressureGradient * self.Conductance ), 0.0) )
            self.AerobicFraction = self.PO2OnAerobicFraction_curve( PO2 )
            self.O2Use = LeftHeart_Metabolism.O2Need * self.AerobicFraction
            if self.BloodFlow > 0.0:
                self.conc_O2 = O2Artys.conc_O2 - ( self.O2Use / self.BloodFlow )
            else:
                self.conc_O2 = 0.0

            HgbTissue.conc_O2 = self.conc_O2
            HgbTissue.O2ToPO2_func()
            PO2End = HgbTissue.pO2

            return PO2End
        self.PO2 = impliciteq( PO2implicitfunc, self.PO2, 0.17)
        self.PlasmaFlow = self.BloodFlow * BloodVol.PVCrit

class LeftHeart_Function:
    def __init__(self):
        self.Failed = False
        self.Effect = None
        self.PhEffect = None
        self.ProteinEffect = None
        self.FuelEffect = None
        self.TemperatureEffect = None

    def PhOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [6.6, 6.7], [0.0, 1.0], [0.0, 0.0])

    def ProteinOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [3000.0, 5200.0], [0.0, 1.0], [0.0, 0.0])

    def FuelOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.9], [0.0, 1.0], [0.0, 0.0])

    def TemperatureOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 37.0, 40.0, 46.0], [0.0, 1.0, 1.5, 0.0], [0.0, 0.12, 0.0, 0.0])

    def Calc_func(self):
        self.PhEffect = self.PhOnFunction_curve( LeftHeart_Ph.Ph )
        self.ProteinEffect = self.ProteinOnFunction_curve( CellProtein.Mass_G )
        self.FuelEffect = self.FuelOnFunction_curve( LeftHeart_Fuel.FractUseDelay )
        self.TemperatureEffect = self.TemperatureOnFunction_curve( HeatCore.Temp_C )
        self.Effect = self.PhEffect * self.ProteinEffect * self.FuelEffect * self.TemperatureEffect * LeftHeart_Structure.Effect

    def Wrapup_func(self):
        if not self.Failed and ( self.Effect < 0.2 ):
            self.Failed = True
        elif self.Failed and ( self.Effect > 0.4 ):
            self.Failed = False

class LeftHeart_Size:
    def __init__(self):
        self.Vol = None
        self.Mass = None
        self.InitialMass = None
        self.Density = None
        self.LiquidMass = None
        self.LiquidDensity = 1.00
        self.LiquidVol = None
        self.InitialLiquidVol = None
        self.SolidMass = None
        self.InitialSolidMass = None
        self.ContractileProteinMass = None
        self.InitialProteinMass = None
        self.ContractileProteinDensity = 1.17
        self.OtherMass = None
        self.InitialOtherMass = None
        self.OtherDensity = 1.17
        self.ContractileProteinVol = None
        self.OtherVol = None
        self.SolidVol = None
        self.FractTotal = None
        self.IFV = None
        self.InitialIFV = None
        self.CellH2O = None
        self.InitialCellH2O = None
        self.MassFractBase = 0.0105
        self.H2OFractMass = 0.67
        self.SolidsFractMass = None
        self.OtherFractSolids = 0.30
        self.ProteinFractSolids = None

    def Initialize_func(self):
        self.InitialMass = self.MassFractBase * Weight.InitialOtherMass
        self.InitialLiquidVol = self.H2OFractMass * self.InitialMass / self.LiquidDensity
        self.SolidsFractMass = 1.0 - self.H2OFractMass
        self.InitialSolidMass = self.SolidsFractMass * self.InitialMass
        self.InitialOtherMass = self.OtherFractSolids * self.InitialSolidMass
        self.ProteinFractSolids = 1.0 - self.OtherFractSolids
        self.InitialProteinMass = self.ProteinFractSolids * self.InitialSolidMass

    def ScaleH2O_func(self):
        self.FractTotal = self.InitialLiquidVol / TissueH2O.InitialVol
        self.InitialIFV = self.FractTotal * InterstitialWater.InitialVol
        self.InitialCellH2O = self.FractTotal * CellH2O.InitialVol

    def Calc_func(self):
        self.IFV = self.FractTotal * InterstitialWater.Vol
        self.CellH2O = self.FractTotal * CellH2O.Vol
        self.LiquidVol = self.IFV + self.CellH2O
        self.LiquidMass = self.LiquidVol * self.LiquidDensity
        self.ContractileProteinMass = LeftHeart_ContractileProtein.Mass
        self.OtherMass = self.InitialOtherMass
        self.SolidMass = self.ContractileProteinMass + self.OtherMass
        self.ContractileProteinVol = self.ContractileProteinMass / self.ContractileProteinDensity
        self.OtherVol = self.OtherMass / self.OtherDensity
        self.SolidVol = self.ContractileProteinVol + self.OtherVol
        self.Mass = self.LiquidMass + self.SolidMass
        self.Vol = self.LiquidVol + self.SolidVol
        self.Density = self.Mass / self.Vol

class LeftHeart_Work:
    def __init__(self):
        self.TotalCals = None
        self.MotionCals = None
        self.HeatCals = None

    def Calc_func(self):
        self.MotionCals = 24.0
        self.HeatCals = 87.0
        self.TotalCals = self.MotionCals + self.HeatCals

class LeftHeart_AlphaReceptors:
    def __init__(self):
        self.Activity = None
        self.TotalAgonism = None
        self.NeuralAgonism = None
        self.HumoralAgonism = None
        self.Switch = False
        self.Setting = 0.0
        self.NEURALK = 0.333
        self.HUMORALK = 0.5

    def Calc_func(self):
        self.NeuralAgonism = GangliaGeneral.NA_Hz
        self.HumoralAgonism = AlphaPool.Effect
        self.TotalAgonism = ( self.NEURALK * self.NeuralAgonism ) + ( self.HUMORALK * self.HumoralAgonism )
        if self.Switch:
            self.Activity = self.Setting
        else:
            self.Activity = self.TotalAgonism * AlphaBlockade.Effect


class LeftHeart_Vasculature:
    def __init__(self):
        self.Tau = 30.0
        self.Effect = 1.0

    def PO2OnStimulus_curve(self, x):
        return cubic_hermite_spline(x, [41.0, 51.0, 61.0], [1.2, 1.0, 0.8], [0.0, -0.03, 0.0])

    def Parms_func(self):
        self.K = 1.0 / ( self.Tau * 1440.0 )

    def Calc_func(self):
        if LeftHeart_Function.Failed:
            self.Stimulus = 0.0
        else:
            self.Stimulus = self.PO2OnStimulus_curve( LeftHeart_Flow.PO2 )

        self.Effect = delay( self.K, self.Stimulus, self.Effect, System.Dx, None)


class LeftHeart_Ph:
    def __init__(self):
        self.Ph = None
        self.conc_SID = None
        self.conc_SID_mEqperL = None

    def CalcSID_func(self):
        self.conc_SID = KCell.conc_K_ + CellSID.OtherCations - CellSID.StrongAnions - LeftHeart_Lactate.conc_Lac_
        self.conc_SID_mEqperL = 1000.0 * self.conc_SID

    def CalcPh_func(self):
        PhCells.pCO2 = LeftHeart_CO2.PCO2
        PhCells.SID = self.conc_SID_mEqperL
        PhCells.Calc_func()
        self.Ph = PhCells.pH

class LeftHeart:
    def __init__(self):
        pass
    
class LeftHeart_Pressure:
    def __init__(self):
        self.ArtyPressure = None
        self.VeinPressure = None
        self.PressureGradient = None
        self.PumpSwitch = False
        self.PumpSetting = 0.0

    def Calc_func(self):
        if self.PumpSwitch:
            self.ArtyPressure = self.PumpSetting
        else:
            self.ArtyPressure = SystemicArtys.Pressure

        self.VeinPressure = SystemicVeins.Pressure
        self.PressureGradient = ( max( ( self.ArtyPressure - self.VeinPressure ), 0.0) )

class LeftHeart_BetaReceptors:
    def __init__(self):
        self.Activity = None
        self.TotalAgonism = None
        self.NeuralAgonism = None
        self.HumoralAgonism = None
        self.Switch = False
        self.Setting = 0.0
        self.NEURALK = 0.333
        self.HUMORALK = 0.5

    def Calc_func(self):
        self.NeuralAgonism = GangliaGeneral.NA_Hz
        self.HumoralAgonism = BetaPool.Effect
        self.TotalAgonism = ( self.NEURALK * self.NeuralAgonism ) + ( self.HUMORALK * self.HumoralAgonism )
        if self.Switch:
            self.Activity = self.Setting
        else:
            self.Activity = self.TotalAgonism * BetaBlockade.Effect


class LeftHeart_CO2:
    def __init__(self):
        self.conc_HCO3 = None
        self.conc_HCO3_mEqperL = None
        self.PCO2 = None
        self.InflowGas = None
        self.InflowBase = None
        self.OutflowBase = None
        self.conc_BloodHCO3 = None
        self.Outflow_0 = None
        self.K = None
        self.Alpha = None
        self.Mass = 3.5

    def CalcConc_func(self):
        self.conc_HCO3 = self.Mass / LeftHeart_Size.LiquidVol
        self.conc_HCO3_mEqperL = 1000.0 * self.conc_HCO3
        Tissue_BaseToGas.conc_HCO3 = self.conc_HCO3
        Tissue_BaseToGas.conc_SID = LeftHeart_Ph.conc_SID
        Tissue_BaseToGas.Calc_func()
        self.PCO2 = Tissue_BaseToGas.pCO2

    def CalcDervs_func(self):
        self.K = LeftHeart_Flow.BloodFlow / LeftHeart_Size.LiquidVol
        if System.Dx >=0:
            self.Alpha = 0.0
        elif ( self.K * System.Dx ) >= 100.0:
            self.Alpha = 4E-44
        elif True:
            self.Alpha = ( math.e ** ( - self.K * System.Dx ) )
        self.InflowGas = Metabolism_RespiratoryQuotient.RQ * LeftHeart_Flow.O2Use
        self.InflowBase = CO2Tools.LitersToMols * self.InflowGas
        Blood_GasToBase.pCO2 = self.PCO2
        Blood_GasToBase.conc_SID = BloodIons.conc_SID
        Blood_GasToBase.Calc_func()
        self.conc_BloodHCO3 = Blood_GasToBase.conc_HCO3
        self.Outflow_0 = LeftHeart_Flow.BloodFlow * ( self.conc_BloodHCO3 - CO2Artys.conc_HCO3 )
        self.OutflowBase = ( self.Alpha * self.Outflow_0 ) + ( ( 1 - self.Alpha ) * self.InflowBase )
        self.Change = self.InflowBase - self.OutflowBase
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.04)


class LeftHeart_Structure:
    def __init__(self):
        self.PhEffect = None
        self.FuelEffect = None
        self.TemperatureEffect = None
        self.Effect = 1.0

    def PhOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [6.5, 6.6], [0.1, 0.0], [0.0, 0.0])

    def FuelOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.3], [0.05, 0.0], [0.0, 0.0])

    def TemperatureOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [44.0, 46.0], [0.0, 0.05], [0.0, 0.0])

    def Calc_func(self):
        self.PhEffect = self.PhOnStructure_curve( LeftHeart_Ph.Ph )
        self.FuelEffect = self.FuelOnStructure_curve( LeftHeart_Fuel.FractUseDelay )
        self.TemperatureEffect = self.TemperatureOnStructure_curve( HeatCore.Temp_C )
        self.F1 = 0.0
        self.F2 = self.PhEffect + self.TemperatureEffect + self.FuelEffect
        self.Effect = backwardeuler( self.F1, self.F2, System.Dx, self.Effect, None)


class LeftHeart_Fuel:
    def __init__(self):
        self.FADelivered = None
        self.GlucoseDelivered = None
        self.KR = 0.026
        self.Ratio = None
        self.FAFraction = None
        self.GlucoseFraction = None
        self.FA_GlucoseFraction = None
        self.LacFraction = None
        self.FAUsed_CalperMin = None
        self.AerobicGlucoseUsed_CalperMin = None
        self.AnaerobicGlucoseUsed_CalperMin = None
        self.LacUsed_CalperMin = None
        self.FAUsed_mGperMin = None
        self.AerobicGlucoseUsed_mGperMin = None
        self.AnaerobicGlucoseUsed_mGperMin = None
        self.LacUsed_mGperMin = None
        self.TotalGlucoseUsed_mGperMin = None
        self.AnaerobicGlucoseDelivered = None
        self.FAFractionalDelivery = None
        self.AerobicGlucoseFractionalDelivery = None
        self.AnaerobicGlucoseFractionalDelivery = None
        self.MinimumFractionalDelivery = None
        self.FractUseDelay = 1.0

    def LacFraction_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 100.0], [0.0, 0.3], [0.0, 0.0])

    def Dervs_func(self):
        self.FADelivered = ( max( ( FAPool.conc_FA * LeftHeart_Flow.PlasmaFlow ), 0.0) )
        self.GlucoseDelivered = ( max( ( GlucosePool.conc_Glucose * LeftHeart_Flow.PlasmaFlow ), 0.0) )
        self.LacFraction = self.LacFraction_curve( LeftHeart_Lactate.conc_Lac__mGperdL )
        self.FA_GlucoseFraction = 1.0 - self.LacFraction
        self.Ratio = FAPool.conc_FA_mGperdL / GlucosePool.conc_Glucose_mGperdL
        self.FAFraction = self.FA_GlucoseFraction * ( self.Ratio / ( self.Ratio + self.KR ) )
        self.GlucoseFraction = self.FA_GlucoseFraction - self.FAFraction
        self.FAUsed_CalperMin = self.FAFraction * LeftHeart_Metabolism.AerobicCals
        self.FAUsed_mGperMin = self.FAUsed_CalperMin * Metabolism_Tools.Fat_mGperCal
        self.AerobicGlucoseUsed_CalperMin = self.GlucoseFraction * LeftHeart_Metabolism.AerobicCals
        self.AerobicGlucoseUsed_mGperMin = self.AerobicGlucoseUsed_CalperMin * Metabolism_Tools.CarboAerobic_mGperCal
        self.LacUsed_CalperMin = self.LacFraction * LeftHeart_Metabolism.AerobicCals
        self.LacUsed_mGperMin = self.LacUsed_CalperMin * Metabolism_Tools.Lac__mGperCal
        self.AnaerobicGlucoseDelivered = self.GlucoseDelivered - self.AerobicGlucoseUsed_mGperMin
        self.AnaerobicGlucoseUsed_CalperMin = ( min( LeftHeart_Metabolism.AnaerobicCals, self.AnaerobicGlucoseDelivered) )
        self.AnaerobicGlucoseUsed_mGperMin = self.AnaerobicGlucoseUsed_CalperMin * Metabolism_Tools.CarboAnaerobic_mGperCal
        self.TotalGlucoseUsed_mGperMin = self.AerobicGlucoseUsed_mGperMin + self.AnaerobicGlucoseUsed_mGperMin
        if self.FAUsed_mGperMin > 0.0:
            self.FAFractionalDelivery = ( min( ( self.FADelivered / self.FAUsed_mGperMin ), 1.0) )
        else:
            self.FAFractionalDelivery = 1.0

        if self.AerobicGlucoseUsed_mGperMin > 0.0:
            self.AerobicGlucoseFractionalDelivery = ( min( ( self.GlucoseDelivered / self.AerobicGlucoseUsed_mGperMin ), 1.0) )
        else:
            self.AerobicGlucoseFractionalDelivery = 1.0

        if self.AnaerobicGlucoseUsed_mGperMin > 0.0:
            self.AnaerobicGlucoseFractionalDelivery = ( min( ( self.AnaerobicGlucoseDelivered / self.AnaerobicGlucoseUsed_mGperMin ), 1.0) )
        else:
            self.AnaerobicGlucoseFractionalDelivery = 1.0

        self.MinimumFractionalDelivery = ( min( ( min( self.FAFractionalDelivery, self.AerobicGlucoseFractionalDelivery) ), self.AnaerobicGlucoseFractionalDelivery) )
        self.K = 0.5
        self.DxMax = 1.0
        self.FractUse = self.MinimumFractionalDelivery
        self.FractUseDelay = delay( self.K, self.FractUse, self.FractUseDelay, System.Dx, 0.01)


class LeftHeart_ContractileProtein:

    def Initialize_func(self):
        self.Mass = LeftHeart_Size.InitialProteinMass

    def Dervs_func(self):
        self.Change = 0.0
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.38)


class Exercise_Treadmill:
    def __init__(self):
        self.Speed_MPH = 0.0
        self.Grade_percent = 0.0
        self.Efficiency_percent = 30.0
        self.RunOrWalk = 0.0
        self.Power_W = None
        self.Power_kPMperMin = None
        self.ElapsedTime = Timer(0.0, "None", System.Dx)
        timervars.append(self.ElapsedTime)
        self.Efficiency = None
        self.TotalWatts = None
        self.Speed_FPM = None
        self.Speed_KPH = None
        self.StepsPerMinute = None
        self.Distance_Miles = None
        self.Distance_kM = None
        self.DistanceTraveled_Feet = 0.0

    def GradeX_curve(self, x):
        return cubic_hermite_spline(x, [-10.0, 0.0, 10.0], [0.6, 1.0, 2.0], [0.0, 0.08, 0.0])

    def WalkingBonus_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 5.0], [0.6, 1.0], [0.0, 0.0])

    def Parms_func(self):
        if self.RunOrWalk:
            self.Speed_MPH = ( min( self.Speed_MPH, 5.0) )
        else:
            pass
        self.Speed_FPM = 88.0 * self.Speed_MPH
        self.Speed_KPH = 1.609 * self.Speed_MPH
        self.StepsPerMinute = 39.0 * self.Speed_MPH
        self.Efficiency = 0.01 * self.Efficiency_percent

    def Calc_func(self):
        self.Power_W = 0.412 * Weight.Weight_kG * self.Speed_MPH * self.GradeX_curve( self.Grade_percent )
        if self.RunOrWalk:
            self.Power_W = self.Power_W * self.WalkingBonus_curve( self.Speed_MPH )
        else:
            pass
        self.Power_kPMperMin = 6.12 * self.Power_W
        self.TotalWatts = self.Power_W / self.Efficiency

    def Dervs_func(self):
        if Status.Exertion == 4:
            self.ElapsedTime.state = "UP"
            self.Velocity = self.Speed_FPM
        else:
            self.ElapsedTime.state = "OFF"
            self.Velocity = 0.0
        self.Distance_Miles = self.DistanceTraveled_Feet / 5280.0
        self.Distance_kM = 1.609 * self.Distance_Miles
        self.DistanceTraveled_Feet = diffeq( self.Velocity, System.Dx, self.DistanceTraveled_Feet, None)


    def ResetTime_and_Distance_func(self):
        self.ElapsedTime.val = 0.0
        self.DistanceTraveled_Feet = 0.0

class Exercise_MusclePump:
    def __init__(self):
        self.Effect = None

    def Effect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1600.0], [1.0, 5.0], [0.005, 0.0])

    def Calc_func(self):
        self.Effect = self.Effect_curve( Exercise_Metabolism.TotalWatts )

class Exercise_Bike:
    def __init__(self):
        self.Power_W = 0.0
        self.Power_kPMperMin = None
        self.RPM = 50.0
        self.ElapsedTime = Timer(0.0, "None", System.Dx)
        timervars.append(self.ElapsedTime)
        self.WattToKPMM = 6.12
        self.Efficiency_percent = 30.0
        self.Efficiency = None
        self.TotalWatts = None

    def Calc_func(self):
        self.Power_kPMperMin = self.WattToKPMM * self.Power_W
        self.Efficiency = 0.01 * self.Efficiency_percent
        self.TotalWatts = self.Power_W / self.Efficiency
        if Status.Exertion == 3:
            self.ElapsedTime.state = "UP"
        else:
            self.ElapsedTime.state = "OFF"

    def ResetElapsedTime_func(self):
        self.ElapsedTime.val = 0.0

class Exercise_Motivation:
    def __init__(self):
        self.Motivation = 0.03
    
class Exercise_Metabolism:
    def __init__(self):
        self.HeatWatts = None
        self.WattsToCals = 14.34
        self.TotalCals = None
        self.MotionCals = None
        self.HeatCals = None
        self.Tau = 0.2
        self.K = None
        self.TotalWatts = 0.0
        self.MotionWatts = 0.0
        self.ContractionRate = 0.0

    def Parms_func(self):
        if self.Tau > 0.0:
            self.K = ( 1 / self.Tau )
        else:
            self.K = self.float("inf")

        self.TotalWattsK = self.K
        self.MotionWattsK = self.K
        self.ContractionRateK = self.K

    def Dervs_func(self):
        if Status.Exertion == 0:
            self.TargetTotalWatts = 0.0
            self.TargetMotionWatts = 0.0
            self.TargetContractionRate = 0.0
        elif Status.Exertion == 1:
            self.TargetMotionWatts = DailyPlannerControl.WorkLevel
            self.TargetTotalWatts = self.MotionWatts / 0.22
            self.TargetContractionRate = 10.0
        elif Status.Exertion == 2:
            self.TargetMotionWatts = DailyPlannerControl.AerobicsLevel
            self.TargetTotalWatts = self.MotionWatts / 0.22
            self.TargetContractionRate = 50.0
        elif Status.Exertion == 3:
            self.TargetTotalWatts = Exercise_Bike.TotalWatts
            self.TargetMotionWatts = Exercise_Bike.Power_W
            self.TargetContractionRate = Exercise_Bike.RPM
        elif Status.Exertion == 4:
            self.TargetTotalWatts = Exercise_Treadmill.TotalWatts
            self.TargetMotionWatts = Exercise_Treadmill.Power_W
            self.TargetContractionRate = Exercise_Treadmill.StepsPerMinute
        self.HeatWatts = self.TotalWatts - self.MotionWatts
        self.TotalCals = self.WattsToCals * self.TotalWatts
        self.MotionCals = self.WattsToCals * self.MotionWatts
        self.HeatCals = self.WattsToCals * self.HeatWatts
        self.TotalWatts = delay( self.TotalWattsK, self.TargetTotalWatts, self.TotalWatts, System.Dx, 3.0)

        self.MotionWatts = delay( self.MotionWattsK, self.TargetMotionWatts, self.MotionWatts, System.Dx, 0.6)

        self.ContractionRate = delay( self.ContractionRateK, self.TargetContractionRate, self.ContractionRate, System.Dx, 0.5)


class Exercise:
    def __init__(self):
        pass
    
class Exercise_Control:
    def __init__(self):
        self.Request = 0.0
        self.LastValidRequest = 0
        self.Motivation = 0.04
        self.NO_EXERCISE = 0

    def Parms_func(self):
        if DailyPlannerControl.Switch:
            self.Request = self.LastValidRequest
        else:
            if Brain_Function.Comatose:
                self.Request = self.LastValidRequest
            else:
                Status.Exertion = self.Request
                self.LastValidRequest = self.Request

    def Wrapup_func(self):
        if self.Request == self.NO_EXERCISE:
            pass
        else:
            if SkeletalMuscle_Lactate.conc_Lac_ > Exercise_Motivation.Motivation:
                self.StopExercising_func()
            elif SkeletalMuscle_Function.Failed:
                self.StopExercising_func()
            elif Brain_Function.Comatose:
                self.StopExercising_func()
            elif Brain_Function.Impaired:
                self.StopExercising_func()
            elif RespiratoryMuscle_Function.Failed:
                self.StopExercising_func()

    def StopExercising_func(self):
        self.Request = self.NO_EXERCISE
        self.LastValidRequest = self.NO_EXERCISE
        Status.Exertion = self.NO_EXERCISE

class EpiClearance:
    def __init__(self):
        self.Rate = None
        self.K = 9.4

    def Dervs_func(self):
        self.Rate = self.K * EpiPool.conc_Epi_pGpermL

class AlphaBlockade:
    def __init__(self):
        self.Block_percent = 0.0
        self.Effect = None

    def Parms_func(self):
        self.Effect = 1.0 - ( self.Block_percent / 100.0 )

class NESecretion:
    def __init__(self):
        self.Rate = None
        self.AdrenalNerveEffect = None
        self.Base = 220.0
        self.Spillover = None
        self.SpilloverK = 570.0

    def AdrenalNerveEffect_curve(self, x):
        return cubic_hermite_spline(x, [2.0, 8.0], [1.0, 20.0], [0.0, 0.0])

    def Dervs_func(self):
        self.AdrenalNerveEffect = self.AdrenalNerveEffect_curve( AdrenalNerve.NA_Hz )
        self.Rate = self.Base * self.AdrenalNerveEffect * OtherTissue_Function.Effect
        self.Spillover = self.SpilloverK * GangliaGeneral.NA_Hz

class NEPump:
    def __init__(self):
        self.Rate = None
        self.Switch = False
        self.Setting = 0.0

    def Parms_func(self):
        if self.Switch:
            self.Rate = self.Setting
        else:
            self.Rate = 0.0


class Pheochromocytoma:
    def __init__(self):
        self.Rate = None
        self.EpiRate = None
        self.NERate = None
        self.Epi_percent = 80.0
        self.EpiFract = None
        self.NEFract = None
        self.FractSec = 0.0
        self.FRACTSEC = 0.004
        self.Severity = 0.0
        self.Timer = Timer(0, "None", System.Dx)
        timervars.append(self.Timer)
        self.Period = 0.0
        self.Switch = False
        self.LastState = False
        self.InEpisode = False
        self.MAXEPISODE = 240.0
        self.MAXPAUSE = 480.0
        self.Mass = 0.0

    def Dervs_func(self):
        self.Rate = self.FractSec * self.Mass
        self.EpiFract = self.Epi_percent / 100.0
        self.NEFract = 1.0 - self.EpiFract
        self.EpiRate = self.EpiFract * self.Rate
        self.NERate = self.NEFract * self.Rate
        self.Change = self.Switch * self.Severity - self.Rate
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 50000.0)


    def Wrapup_func(self):
        if self.Switch:
            if Timer < self.Period:
                pass
            else:
                if self.InEpisode:
                    self.TurnOff_func()
                else:
                    self.TurnOn_func()
        else:
            pass

    def TurnOff_func(self):
        self.InEpisode = False
        self.FractSec = 0.0
        self.Period = self.Noise * self.MAXPAUSE
        self.Timer.val = 0.0
        self.Timer.state = "UP"

    def TurnOn_func(self):
        self.InEpisode = True
        self.FractSec = self.FRACTSEC
        self.Period = self.Noise * self.MAXEPISODE
        self.Timer.val = 0.0
        self.Timer.state = "UP"

class NEPool:
    def __init__(self):
        self.conc_NE = None
        self.conc_NE_pGpermL = None
        self.conc_NE_nMolperL = None
        self.Gain = None
        self.Loss = None
        self.Targetconc_NE = 0.240
        self.InitialMass = None

    def Init_func(self):
        self.InitialMass = self.Targetconc_NE * ECFV.Vol
        self.Mass = self.InitialMass

    def CalcConc_func(self):
        self.conc_NE = self.Mass / ECFV.Vol
        self.conc_NE_pGpermL = 1000.0 * self.conc_NE
        self.conc_NE_nMolperL = 0.00592 * self.conc_NE_pGpermL

    def Dervs_func(self):
        self.Gain = NESecretion.Rate + NESecretion.Spillover + NEPump.Rate
        self.Loss = NEClearance.Rate
        self.Change = self.Gain - self.Loss
        self.F1 = self.Gain
        self.F2 = 1000 * NEClearance.K / ECFV.Vol
        self.Mass = backwardeuler( self.F1, self.F2, System.Dx, self.Mass, 36.0)


class EpiPump:
    def __init__(self):
        self.Rate = None
        self.Switch = False
        self.Setting = 0.0

    def Parms_func(self):
        if self.Switch:
            self.Rate = self.Setting
        else:
            self.Rate = 0.0


class AlphaPool:
    def __init__(self):
        self.Effect = None
        self.Total = None
        self.NEPart = None
        self.EpiPart = None
        self.MidoPart = None
        self.NESCALE = 0.021
        self.EPISCALE = 0.125
        self.MIDOSCALE = 5.0

    def Calc_func(self):
        self.NEPart = NEPool.conc_NE_pGpermL * self.NESCALE
        self.EpiPart = EpiPool.conc_Epi_pGpermL * self.EPISCALE
        self.MidoPart = DesglymidodrinePool.conc_Desglymidodrine * self.MIDOSCALE
        self.Total = self.NEPart + self.EpiPart + self.MidoPart
        if self.Total > 1.0:
            self.Effect = ( math.log10( self.Total ) )
        else:
            self.Effect = 0.0


class BetaPool:
    def __init__(self):
        self.Effect = None
        self.Total = None
        self.NEPart = None
        self.EpiPart = None
        self.NESCALE = 0.021
        self.EPISCALE = 0.125

    def Calc_func(self):
        self.NEPart = NEPool.conc_NE_pGpermL * self.NESCALE
        self.EpiPart = EpiPool.conc_Epi_pGpermL * self.EPISCALE
        self.Total = self.NEPart + self.EpiPart
        if self.Total > 1.0:
            self.Effect = ( math.log10( self.Total ) )
        else:
            self.Effect = 0.0


class Catechols:

    def Parms_func(self):
        AlphaBlockade.Parms_func()
        BetaBlockade.Parms_func()
        NEPump.Parms_func()
        EpiPump.Parms_func()

    def CalcConc_func(self):
        EpiPool.CalcConc_func()
        NEPool.CalcConc_func()
        AlphaPool.Calc_func()
        BetaPool.Calc_func()

    def Dervs_func(self):
        EpiSecretion.Dervs_func()
        NESecretion.Dervs_func()
        NEClearance.Dervs_func()
        EpiClearance.Dervs_func()
        Pheochromocytoma.Dervs_func()
        EpiPool.Dervs_func()
        NEPool.Dervs_func()

    def Wrapup_func(self):
        Pheochromocytoma.Wrapup_func()

class EpiPool:
    def __init__(self):
        self.conc_Epi = None
        self.conc_Epi_pGpermL = None
        self.conc_Epi_nMolperL = None
        self.Gain = None
        self.Loss = None
        self.Targetconc_Epi = 0.040
        self.InitialMass = None

    def Init_func(self):
        self.InitialMass = self.Targetconc_Epi * ECFV.Vol
        self.Mass = self.InitialMass

    def CalcConc_func(self):
        self.conc_Epi = self.Mass / ECFV.Vol
        self.conc_Epi_pGpermL = 1000.0 * self.conc_Epi
        self.conc_Epi_nMolperL = 0.00546 * self.conc_Epi_pGpermL

    def Dervs_func(self):
        self.Gain = EpiSecretion.Rate + EpiPump.Rate + Pheochromocytoma.EpiRate
        self.Loss = EpiClearance.Rate
        self.Change = self.Gain - self.Loss
        self.F1 = self.Gain
        self.F2 = 1000.0 * EpiClearance.K / ECFV.Vol
        self.Mass = backwardeuler( self.F1, self.F2, System.Dx, self.Mass, 6.0)


class NEClearance:
    def __init__(self):
        self.Rate = None
        self.K = 4.5

    def Dervs_func(self):
        self.Rate = self.K * NEPool.conc_NE_pGpermL

class EpiSecretion:
    def __init__(self):
        self.Rate = None
        self.AdrenalNerveEffect = None
        self.Base = 375.0

    def AdrenalNerveEffect_curve(self, x):
        return cubic_hermite_spline(x, [2.0, 8.0], [1.0, 20.0], [0.0, 0.0])

    def Dervs_func(self):
        self.AdrenalNerveEffect = self.AdrenalNerveEffect_curve( AdrenalNerve.NA_Hz )
        self.Rate = self.Base * self.AdrenalNerveEffect * OtherTissue_Function.Effect

class BetaBlockade:
    def __init__(self):
        self.Block_percent = 0.0
        self.Effect = None

    def Parms_func(self):
        self.Effect = 1.0 - ( self.Block_percent / 100.0 )

class Uterus:

    def Dervs_func(self):
        pass

class Testes_Inhibin:
    def __init__(self):
        self.Secretion = None

    def Dervs_func(self):
        self.Secretion = 1.0

class Testes_Estradiol:
    def __init__(self):
        self.Secretion = None

    def Dervs_func(self):
        self.Secretion = 0.0173

class Testes:

    def Dervs_func(self):
        Testes_Estradiol.Dervs_func()
        Testes_Progesterone.Dervs_func()
        Testes_Testosterone.Dervs_func()
        Testes_Inhibin.Dervs_func()

class Testes_Testosterone:
    def __init__(self):
        self.Secretion = None

    def Dervs_func(self):
        self.Secretion = 12.0

class Testes_Progesterone:
    def __init__(self):
        self.Secretion = None

    def Dervs_func(self):
        self.Secretion = 2.64

class Inhibin:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.Secretion = None
        self.Degradation = None
        self.InitialConcFemale = 224.0
        self.InitialConcMale = 8.0
        self.TargetConcFemale = 224.0
        self.TargetConcMale = 8.0
        self.TargetConc = None
        self.InitialMass = None
        self.IUperL_TO_PGperML = 0.0134
        self.conc_Conc_IUperL = None
        self.conc_Conc_pGpermL = None
        self.PumpSwitch = False
        self.PumpSetting = 0.0
        self.K = 0.008

    def Init_func(self):
        if Gender.IsFemale:
            self.TargetConc = self.TargetConcFemale
        else:
            self.TargetConc = self.TargetConcMale

        self.InitialMass = self.TargetConc * ECFV.InitialVol_L
        self.Mass = self.InitialMass

    def Conc_func(self):
        self.conc_Conc_IUperL = self.Mass / ECFV.Vol_L
        self.conc_Conc_pGpermL = self.IUperL_TO_PGperML * self.conc_Conc_IUperL

    def Dervs_func(self):
        if Gender.IsFemale:
            self.Secretion = Ovaries_Inhibin.Secretion
        else:
            self.Secretion = Testes_Inhibin.Secretion

        self.Degradation = self.K * self.Mass
        self.Gain = self.Secretion + ( self.PumpSetting * self.PumpSwitch )
        self.Loss = self.Degradation
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.8)


class UreaPool:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.FluxFromCells = None
        self.conc_Urea = None
        self.conc_Urea_mGperdL = None
        self.conc_Urea_mMolperL = None
        self.MG_TO_MOSM = 0.01667
        self.PER_ML_TO_PER_DL = 100.0
        self.MG_TO_MMOL = 16.67
        self.Osmoles = None
        self.conc_Osm = None
        self.conc_Osm_mOsmperL = None
        self.Targetconc_Urea = 0.40
        self.InitialMass = None
        self.UREA_TO_BUN = 0.467
        self.conc_BUN = None

    def CalcOsmoles_func(self):
        self.Osmoles = self.MG_TO_MOSM * self.Mass

    def Init_func(self):
        self.InitialMass = self.Targetconc_Urea * ECFV.Vol
        self.Mass = self.InitialMass

    def CalcConc_func(self):
        self.conc_Urea = self.Mass / ECFV.Vol
        self.conc_Urea_mGperdL = self.PER_ML_TO_PER_DL * self.conc_Urea
        self.conc_Urea_mMolperL = self.MG_TO_MMOL * self.conc_Urea
        self.conc_BUN = self.UREA_TO_BUN * self.conc_Urea_mGperdL
        self.conc_Osm = self.Osmoles / ECFV.Vol
        self.conc_Osm_mOsmperL = 1000.0 * self.conc_Osm

    def Dervs_func(self):
        self.FluxFromCells = -1.0 * UreaCell.Change
        self.Gain = LM_AminoAcids.Urea + self.FluxFromCells
        self.Loss = CD_Urea.Outflow
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 54.0)


class Urea:

    def CalcOsmoles_func(self):
        UreaCell.CalcOsmoles_func()
        UreaPool.CalcOsmoles_func()

    def CalcConc_func(self):
        UreaCell.CalcConc_func()
        UreaPool.CalcConc_func()

    def Dervs_func(self):
        UreaCell.Dervs_func()
        UreaPool.Dervs_func()

class UreaCell:
    def __init__(self):
        self.conc_Urea = None
        self.conc_Urea_mGperdL = None
        self.conc_Urea_mMolperL = None
        self.MG_TO_MOSM = 0.01667
        self.PER_ML_TO_PER_DL = 100.0
        self.MG_TO_MMOL = 16.67
        self.DC = 910.0
        self.Osmoles = None
        self.Mass = 10150.0

    def CalcOsmoles_func(self):
        self.Osmoles = self.MG_TO_MOSM * self.Mass

    def CalcConc_func(self):
        self.conc_Urea = self.Mass / ICFV.Vol
        self.conc_Urea_mGperdL = self.PER_ML_TO_PER_DL * self.conc_Urea
        self.conc_Urea_mMolperL = self.MG_TO_MMOL * self.conc_Urea

    def Dervs_func(self):
        self.Change = ( UreaPool.conc_Urea - self.conc_Urea ) * self.DC
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 101.0)


class EPOClearance:
    def __init__(self):
        self.Rate = None
        self.K = 0.00555

    def Dervs_func(self):
        self.Rate = self.K * EPOPool.Mass

class EPOPump:
    def __init__(self):
        self.Rate = None
        self.Switch = False
        self.Setting = 0.0

    def Parms_func(self):
        if self.Switch:
            self.Rate = self.Setting
        else:
            self.Rate = 0.0


class EPOPool:
    def __init__(self):
        self.conc_EPO = None
        self.Log10Conc = None
        self.VOLDIST = 0.40
        self.VolDist = None
        self.InitialVolDist = None
        self.Gain = None
        self.Loss = None
        self.Targetconc_EPO = 20.0
        self.InitialMass = None

    def Init_func(self):
        self.InitialVolDist = self.VOLDIST * ECFV.InitialVol_L
        self.InitialMass = self.Targetconc_EPO * self.InitialVolDist
        self.Mass = self.InitialMass

    def CalcConc_func(self):
        self.VolDist = self.VOLDIST * ECFV.Vol_L
        self.conc_EPO = self.Mass / self.VolDist
        if self.conc_EPO > 1.0:
            self.Log10Conc = ( math.log10( self.conc_EPO ) )
        else:
            self.Log10Conc = 0.0


    def Dervs_func(self):
        self.Gain = EPOSecretion.Rate + EPOPump.Rate
        self.Loss = EPOClearance.Rate
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 1.2)


class EPO:

    def Parms_func(self):
        EPOPump.Parms_func()

    def CalcConc_func(self):
        EPOPool.CalcConc_func()

    def Dervs_func(self):
        EPOSecretion.Dervs_func()
        EPOClearance.Dervs_func()
        EPOPool.Dervs_func()

class EPOSecretion:
    def __init__(self):
        self.Rate = None
        self.PO2Effect = None
        self.Base = 0.67

    def PO2Effect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 35.0, 60.0], [4.0, 0.0, -1.0], [0.0, -0.14, 0.0])

    def Dervs_func(self):
        self.PO2Effect = 10.0 ** self.PO2Effect_curve( Kidney_O2.TubulePO2 )
        self.Rate = self.Base * self.PO2Effect * Kidney_NephronCount.Total_xNormal * Kidney_Function.Effect

class Lactate:
    def __init__(self):
        pass
    
class LacPool:
    def __init__(self):
        self.conc_Lac_ = None
        self.conc_Lac__mEqperL = None
        self.conc_Lac__mGperdL = None
        self.PumpSwitch = False
        self.PumpSetting = 0.0
        self.PumpRate = None
        self.Mass = 15.0

    def Parms_func(self):
        if self.PumpSwitch:
            self.PumpRate = self.PumpSetting
        else:
            self.PumpRate = 0.0


    def CalcConc_func(self):
        self.conc_Lac_ = self.Mass / ECFV.Vol
        self.conc_Lac__mEqperL = 1000.0 * self.conc_Lac_
        self.conc_Lac__mGperdL = 9008.0 * self.conc_Lac_

    def CalcDervs_func(self):
        self.Change = Bone_Lactate.Outflux + Brain_Lactate.Outflux + Fat_Lactate.Outflux + GITract_Lactate.Outflux + Kidney_Lactate.Outflux + LeftHeart_Lactate.Outflux + Liver_Lactate.Outflux + OtherTissue_Lactate.Outflux + RespiratoryMuscle_Lactate.Outflux + RightHeart_Lactate.Outflux + SkeletalMuscle_Lactate.Outflux + Skin_Lactate.Outflux + self.PumpRate
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.15)


class Infusions:
    def __init__(self):
        pass
    
class LowerExternalPressure:
    def __init__(self):
        self.Pressure = 0.0
    
class SplanchnicCirculation:

    def Calc_func(self):
        PortalVein.Calc_func()
        HepaticArtery.Calc_func()
        HepaticVein.Calc_func()

class HepaticVein:
    def __init__(self):
        self.BloodFlow = None
        self.PlasmaFlow = None

    def Calc_func(self):
        self.BloodFlow = SplanchnicVeins.Outflow
        self.PlasmaFlow = BloodVol.PVCrit * self.BloodFlow

class HepaticArtery:
    def __init__(self):
        self.BloodFlow = None
        self.PlasmaFlow = None

    def Calc_func(self):
        self.BloodFlow = HepaticArty.Flow
        self.PlasmaFlow = BloodVol.PVCrit * self.BloodFlow

class PortalVein_Glucose:
    def __init__(self):
        self.conc_Glucose = None
        self.conc_Glucose_mGperdL = None
        self.conc_Increment = None
        self.conc_Increment_mGperdL = None
        self.conc_Decrement = None
        self.conc_Decrement_mGperdL = None

    def Calc_func(self):
        if PortalVein.PlasmaFlow > 0.0:
            self.conc_Increment = GILumenCarbohydrates.Absorption / PortalVein.PlasmaFlow
        else:
            self.conc_Increment = 0.0

        if PortalVein.PlasmaFlow > 0.0:
            self.conc_Decrement = GITract_Fuel.TotalGlucoseUsed_mGperMin / PortalVein.PlasmaFlow
        else:
            self.conc_Decrement = 0.0

        self.conc_Glucose = GlucosePool.conc_Glucose + self.conc_Increment - self.conc_Decrement
        self.conc_Increment_mGperdL = 100.0 * self.conc_Increment
        self.conc_Decrement_mGperdL = 100.0 * self.conc_Decrement
        self.conc_Glucose_mGperdL = GlucosePool.conc_Glucose_mGperdL + self.conc_Increment_mGperdL - self.conc_Decrement_mGperdL

class PortalVein:
    def __init__(self):
        self.BloodFlow = None
        self.PlasmaFlow = None

    def Calc_func(self):
        self.BloodFlow = GITract_Flow.BloodFlow
        self.PlasmaFlow = BloodVol.PVCrit * self.BloodFlow
        PortalVein_Insulin.Calc_func()
        PortalVein_Glucagon.Calc_func()
        PortalVein_Glucose.Calc_func()
        PortalVein_FattyAcid.Calc_func()

class PortalVein_Insulin:
    def __init__(self):
        self.conc_Insulin = None
        self.conc_Increment = None

    def Calc_func(self):
        if PortalVein.PlasmaFlow > 0.0:
            self.conc_Increment = 1000.0 * ( InsulinSecretion.Rate / PortalVein.PlasmaFlow )
        else:
            self.conc_Increment = 0.0

        self.conc_Insulin = InsulinPool.conc_Insulin + self.conc_Increment

class PortalVein_FattyAcid:
    def __init__(self):
        self.conc_FattyAcid = None
        self.conc_FattyAcid_mGperdL = None
        self.conc_Increment = None
        self.conc_Increment_mGperdL = None
        self.conc_Decrement = None
        self.conc_Decrement_mGperdL = None

    def Calc_func(self):
        if PortalVein.PlasmaFlow > 0.0:
            self.conc_Increment = GILumenFat.Absorption / PortalVein.PlasmaFlow
        else:
            self.conc_Increment = 0.0

        if PortalVein.PlasmaFlow > 0.0:
            self.conc_Decrement = GITract_Fuel.FAUsed_mGperMin / PortalVein.PlasmaFlow
        else:
            self.conc_Decrement = 0.0

        self.conc_FattyAcid = FAPool.conc_FA + self.conc_Increment - self.conc_Decrement
        self.conc_Increment_mGperdL = 100.0 * self.conc_Increment
        self.conc_Decrement_mGperdL = 100.0 * self.conc_Decrement
        self.conc_FattyAcid_mGperdL = FAPool.conc_FA_mGperdL + self.conc_Increment_mGperdL - self.conc_Decrement_mGperdL

class PortalVein_Glucagon:
    def __init__(self):
        self.conc_Glucagon = None
        self.conc_Increment = None

    def Calc_func(self):
        if PortalVein.PlasmaFlow > 0.0:
            self.conc_Increment = 1000.0 * ( GlucagonSecretion.Rate / PortalVein.PlasmaFlow )
        else:
            self.conc_Increment = 0.0

        self.conc_Glucagon = GlucagonPool.conc_Glucagon + self.conc_Increment

class Wind:
    def __init__(self):
        self.MPH = 0.0
    
class Clothes:
    def __init__(self):
        self.Weight = 2
    
class Altitude:
    def __init__(self):
        self.Feet = 0.0
        self.Meters = None

    def Parms_func(self):
        self.Meters = 0.3048 * self.Feet

class RelativeHumidity:
    def __init__(self):
        self.Percent = 30.0
        self.VaporPressure = None
        self.conc_H2O = None
        self.SaturationPressure = None
        self.DewPoint = None
        self.A = 18.6686
        self.B = 4030.183
        self.C = 235.0

    def Parms_func(self):
        if AmbientTemperature.Temp_C > 100.0:
            self.SaturationPressure = 760.0
        elif AmbientTemperature.Temp_C < -273.15:
            self.SaturationPressure = 0.0
        elif True:
            self.SaturationPressure = ( math.e ** ( self.A - ( self.B / ( AmbientTemperature.Temp_C + self.C ) ) ) )
        self.VaporPressure = 0.01 * self.Percent * self.SaturationPressure
        self.conc_H2O = self.VaporPressure / Barometer.Pressure
        if self.VaporPressure > 760.0:
            self.DewPoint = 100.0
        elif self.VaporPressure < 0.0:
            self.DewPoint = -273.15
        elif True:
            self.DewPoint = self.B / ( self.A - ( math.log( ( self.VaporPressure ) ) ) ) - self.C

class Environment:

    def Parms_func(self):
        Altitude.Parms_func()
        Barometer.Calc_func()
        AmbientTemperature.Parms_func()
        RelativeHumidity.Parms_func()

    def FinishParms_func(self):
        EquivalentAltitude.Parms_func()

class AmbientTemperature:
    def __init__(self):
        self.Temp_F = 72.0
        self.Temp_C = None
        self.Temp_K = None

    def Parms_func(self):
        self.Temp_C = ( 5 / 9 ) * ( self.Temp_F - 32 )
        self.Temp_K = self.Temp_C + 273.15

class Barometer:
    def __init__(self):
        self.Pressure = None
        self.Pressure_Atm = None

    def Calc_func(self):
        self.Pressure = 760.0 * ( math.e ** ( -4.0e-5 * Altitude.Feet ) )
        self.Pressure_Atm = self.Pressure / 760.0

class EquivalentAltitude:
    def __init__(self):
        self.Feet = None
        self.Pressure = None
        self.K = -25000.0
        self.GeographicAltitude = None
        self.OxygenAltitude = None

    def Parms_func(self):
        self.Pressure = ( AirSupply_InspiredAir.O2_percent / 21.0 ) * Barometer.Pressure
        self.Feet = ( max( ( self.K * ( math.log( ( self.Pressure / 760.0 ) ) ) ), 0.0) )
        self.GeographicAltitude = Altitude.Feet
        self.OxygenAltitude = self.Feet - self.GeographicAltitude

class Symptoms:
    def __init__(self):
        self.Number = None

    def Calc_func(self):
        if Brain_Function.NotResponding:
            self.Number = 1
        elif Heart_Pain.HasPain:
            self.Number = 2
        elif False:
            self.Number = 3
        elif BloodVol.Hct < 0.34:
            self.Number = 4
        elif Brain_Function.Confused:
            self.Number = 5
        elif Brain_Function.Impaired:
            self.Number = 6
        elif False:
            self.Number = 7
        elif False:
            self.Number = 8
        elif False:
            self.Number = 9
        elif Kidney_NephronCount.Total_xNormal < 0.40:
            self.Number = 10
        elif Status.Working:
            self.Number = 11
        elif Status.Aerobics:
            self.Number = 12
        elif Status.ExerciseBike:
            self.Number = 13
        elif Status.Treadmill:
            self.Number = 14
        elif True:
            self.Number = 0

class Brain:
    def __init__(self):
        pass
    
class Brain_Ph:
    def __init__(self):
        self.Ph = None
        self.conc_SID = None
        self.conc_SID_mEqperL = None

    def CalcSID_func(self):
        self.conc_SID = KCell.conc_K_ + CellSID.OtherCations - CellSID.StrongAnions - Brain_Lactate.conc_Lac_
        self.conc_SID_mEqperL = 1000.0 * self.conc_SID

    def CalcPh_func(self):
        PhCells.pCO2 = Brain_CO2.PCO2
        PhCells.SID = self.conc_SID_mEqperL
        PhCells.Calc_func()
        self.Ph = PhCells.pH

class Brain_Pressure:
    def __init__(self):
        self.ArtyPressure = None
        self.VeinPressure = None
        self.PressureGradient = None
        self.PumpSwitch = False
        self.PumpSetting = 0.0

    def Calc_func(self):
        if self.PumpSwitch:
            self.ArtyPressure = self.PumpSetting
        else:
            self.ArtyPressure = RegionalPressure.Brain

        self.VeinPressure = SystemicVeins.Pressure
        self.PressureGradient = ( max( ( self.ArtyPressure - self.VeinPressure ), 0.0) )

class Brain_Flow:
    def __init__(self):
        self.Conductance = None
        self.BasicConductance = 9.1
        self.PO2OnTension = None
        self.PCO2OnTension = None
        self.TotalTension = None
        self.TensionEffect = None
        self.AerobicFraction = None
        self.O2Use = None
        self.conc_O2 = None
        self.BloodFlow = None
        self.PlasmaFlow = None
        self.PO2 = 37.0
    def PO2OnTension_curve(self, x):
        return cubic_hermite_spline(x, [22.0, 36.0, 60.0], [0.0, 1.0, 1.2], [0.0, 0.02, 0.0])

    def PCO2OnTension_curve(self, x):
        return cubic_hermite_spline(x, [20.0, 45.0, 75.0], [1.8, 1.0, 0.0], [0.0, -0.05, 0.0])

    def TensionOnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.0, 2.0], [2.2, 1.0, 0.6], [0.0, -0.5, 0.0])

    def PO2OnAerobicFraction_curve(self, x):
        return cubic_hermite_spline(x, [2.0, 20.0], [0.0, 1.0], [0.0, 0.0])

    def Calc_func(self):
        self.PCO2OnTension = self.PCO2OnTension_curve( Brain_CO2.PCO2 )
        self.SearchMax = PO2Artys.Pressure

        def PO2implicitfunc(PO2):
            self.PO2OnTension = self.PO2OnTension_curve( PO2 )
            self.TotalTension = self.PO2OnTension * self.PCO2OnTension * Anesthesia.VascularConductance
            self.TensionEffect = self.TensionOnConductance_curve( self.TotalTension )
            self.Conductance = self.BasicConductance * self.TensionEffect * Viscosity.ConductanceEffect * Brain_Vasculature.Effect
            self.BloodFlow = ( max( ( Brain_Pressure.PressureGradient * self.Conductance ), 0.0) )
            self.AerobicFraction = self.PO2OnAerobicFraction_curve( PO2 )
            self.O2Use = Brain_Metabolism.O2Need * self.AerobicFraction
            if self.BloodFlow > 0.0:
                self.conc_O2 = O2Artys.conc_O2 - ( self.O2Use / self.BloodFlow )
            else:
                self.conc_O2 = 0.0

            HgbTissue.conc_O2 = self.conc_O2
            HgbTissue.O2ToPO2_func()
            PO2End = HgbTissue.pO2

            return PO2End
        self.PO2 = impliciteq( PO2implicitfunc, self.PO2, 0.37)
        self.PlasmaFlow = self.BloodFlow * BloodVol.PVCrit

class Seizure:
    def __init__(self):
        self.Convulsing = False

    def Calc_func(self):
        if self.Convulsing:
            if ( ( HeatCore.Temp_C < 41.5 ) or ( HeatCore.Temp_C > 44.5 ) ) and ( ( Brain_Fuel.FractUseDelay > 0.85 ) or ( Brain_Fuel.FractUseDelay < 0.40 ) ):
                self.Convulsing = False
            else:
                pass
        else:
            if ( ( HeatCore.Temp_C >= 42.0 ) and ( HeatCore.Temp_C <= 44.0 ) ) or ( ( Brain_Fuel.FractUseDelay <= 0.80 ) and ( Brain_Fuel.FractUseDelay >= 0.45 ) ):
                self.Convulsing = True
            else:
                pass

class Brain_Function:
    def __init__(self):
        self.Failed = False
        self.Effect = None
        self.Normal = True
        self.Confused = False
        self.Impaired = False
        self.Comatose = False
        self.NotBreathing = False
        self.MayBeDead = False
        self.IsReallyDead = False
        self.NotResponding = False
        self.LastState = 0

    def Calc_func(self):
        self.Effect = BrainInsult.Effect
        self.Normal = False
        self.Confused = False
        self.Impaired = False
        self.Comatose = False
        self.NotBreathing = False
        self.MayBeDead = False
        self.IsReallyDead = False
        self.NotResponding = False
        if self.Effect <= 0.40:
            self.Comatose = True
            self.NotResponding = True
        elif self.Effect <= 0.60:
            self.Impaired = True
        elif self.Effect <= 0.80:
            self.Confused = True
        elif True:
            self.Normal = True
        if self.Effect <= 0.20:
            self.NotBreathing = True
            self.NotResponding = True
        if self.Effect == 0.0:
            self.IsReallyDead = True
            self.NotResponding = True
        elif self.Effect <= 0.10:
            self.MayBeDead = True
            self.NotResponding = True

    def Page_func(self):
        if ( self.Effect == 0.0 ) and ( self.LastState < 6 ):
            self.LastState = 6
        elif ( self.Effect <= 0.1 ) and ( self.LastState < 5 ):
            self.LastState = 5
        elif ( self.Effect <= 0.2 ) and ( self.LastState < 4 ):
            self.LastState = 4
        elif ( self.Effect <= 0.4 ) and ( self.LastState < 3 ):
            self.LastState = 3
        elif ( self.Effect <= 0.6 ) and ( self.LastState < 2 ):
            self.LastState = 2
        elif ( self.Effect <= 0.8 ) and ( self.LastState < 1 ):
            self.LastState = 1
        elif ( self.Effect >= 0.95 ) and ( self.LastState > 0 ):
            self.LastState = 0
        elif ( self.Effect >= 0.60 ) and ( self.LastState > 3 ):
            self.LastState = 3
        elif ( self.Effect >= 0.40 ) and ( self.LastState > 4 ):
            self.LastState = 4
        elif ( self.Effect >= 0.20 ) and ( self.LastState >= 5 ):
            self.LastState = 5

    def Wrapup_func(self):
        if not self.Failed and ( self.Effect < 0.2 ):
            self.Failed = True
        elif self.Failed and ( self.Effect > 0.4 ):
            self.Failed = False

class Brain_CO2:
    def __init__(self):
        self.conc_HCO3 = None
        self.conc_HCO3_mEqperL = None
        self.PCO2 = None
        self.InflowGas = None
        self.InflowBase = None
        self.OutflowBase = None
        self.conc_BloodHCO3 = None
        self.Outflow_0 = None
        self.K = None
        self.Alpha = None
        self.Mass = 14.3

    def CalcConc_func(self):
        self.conc_HCO3 = self.Mass / Brain_Size.LiquidVol
        self.conc_HCO3_mEqperL = 1000.0 * self.conc_HCO3
        Tissue_BaseToGas.conc_HCO3 = self.conc_HCO3
        Tissue_BaseToGas.conc_SID = Brain_Ph.conc_SID
        Tissue_BaseToGas.Calc_func()
        self.PCO2 = Tissue_BaseToGas.pCO2

    def CalcDervs_func(self):
        self.K = Brain_Flow.BloodFlow / Brain_Size.LiquidVol
        if System.Dx >=0:
            self.Alpha = 0.0
        elif ( self.K * System.Dx ) >= 100.0:
            self.Alpha = 4E-44
        elif True:
            self.Alpha = ( math.e ** ( - self.K * System.Dx ) )
        self.InflowGas = Metabolism_RespiratoryQuotient.RQ * Brain_Flow.O2Use
        self.InflowBase = CO2Tools.LitersToMols * self.InflowGas
        Blood_GasToBase.pCO2 = self.PCO2
        Blood_GasToBase.conc_SID = BloodIons.conc_SID
        Blood_GasToBase.Calc_func()
        self.conc_BloodHCO3 = Blood_GasToBase.conc_HCO3
        self.Outflow_0 = Brain_Flow.BloodFlow * ( self.conc_BloodHCO3 - CO2Artys.conc_HCO3 )
        self.OutflowBase = ( self.Alpha * self.Outflow_0 ) + ( ( 1 - self.Alpha ) * self.InflowBase )
        self.Change = self.InflowBase - self.OutflowBase
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.14)


class Brain_Fuel:
    def __init__(self):
        self.KADelivered = None
        self.GlucoseDelivered = None
        self.KR = 0.222
        self.Ratio = None
        self.KAFraction = None
        self.GlucoseFraction = None
        self.KA_GlucoseFraction = None
        self.LacFraction = None
        self.KAUsed_CalperMin = None
        self.AerobicGlucoseUsed_CalperMin = None
        self.AnaerobicGlucoseUsed_CalperMin = None
        self.LacUsed_CalperMin = None
        self.KAUsed_mGperMin = None
        self.AerobicGlucoseUsed_mGperMin = None
        self.AnaerobicGlucoseUsed_mGperMin = None
        self.LacUsed_mGperMin = None
        self.TotalGlucoseUsed_mGperMin = None
        self.AnaerobicGlucoseDelivered = None
        self.KAFractionalDelivery = None
        self.AerobicGlucoseFractionalDelivery = None
        self.AnaerobicGlucoseFractionalDelivery = None
        self.MinimumFractionalDelivery = None
        self.FractUseDelay = 1.0

    def LacFraction_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 100.0], [0.0, 0.3], [0.0, 0.0])

    def Dervs_func(self):
        self.KADelivered = ( max( ( KAPool.conc_KA * Brain_Flow.PlasmaFlow ), 0.0) )
        self.GlucoseDelivered = ( max( ( GlucosePool.conc_Glucose * Brain_Flow.PlasmaFlow ), 0.0) )
        self.LacFraction = self.LacFraction_curve( Brain_Lactate.conc_Lac__mGperdL )
        self.KA_GlucoseFraction = 1.0 - self.LacFraction
        self.Ratio = KAPool.conc_KA_mGperdL / GlucosePool.conc_Glucose_mGperdL
        self.KAFraction = self.KA_GlucoseFraction * ( self.Ratio / ( self.Ratio + self.KR ) )
        self.GlucoseFraction = self.KA_GlucoseFraction - self.KAFraction
        self.KAUsed_CalperMin = self.KAFraction * Brain_Metabolism.AerobicCals
        self.KAUsed_mGperMin = self.KAUsed_CalperMin * Metabolism_Tools.Fat_mGperCal
        self.AerobicGlucoseUsed_CalperMin = self.GlucoseFraction * Brain_Metabolism.AerobicCals
        self.AerobicGlucoseUsed_mGperMin = self.AerobicGlucoseUsed_CalperMin * Metabolism_Tools.CarboAerobic_mGperCal
        self.LacUsed_CalperMin = self.LacFraction * Brain_Metabolism.AerobicCals
        self.LacUsed_mGperMin = self.LacUsed_CalperMin * Metabolism_Tools.Lac__mGperCal
        self.AnaerobicGlucoseDelivered = self.GlucoseDelivered - self.AerobicGlucoseUsed_mGperMin
        self.AnaerobicGlucoseUsed_CalperMin = ( min( Brain_Metabolism.AnaerobicCals, self.AnaerobicGlucoseDelivered) )
        self.AnaerobicGlucoseUsed_mGperMin = self.AnaerobicGlucoseUsed_CalperMin * Metabolism_Tools.CarboAnaerobic_mGperCal
        self.TotalGlucoseUsed_mGperMin = self.AerobicGlucoseUsed_mGperMin + self.AnaerobicGlucoseUsed_mGperMin
        if self.KAUsed_mGperMin > 0.0:
            self.KAFractionalDelivery = ( min( ( self.KADelivered / self.KAUsed_mGperMin ), 1.0) )
        else:
            self.KAFractionalDelivery = 1.0

        if self.AerobicGlucoseUsed_mGperMin > 0.0:
            self.AerobicGlucoseFractionalDelivery = ( min( ( self.GlucoseDelivered / self.AerobicGlucoseUsed_mGperMin ), 1.0) )
        else:
            self.AerobicGlucoseFractionalDelivery = 1.0

        if self.AnaerobicGlucoseUsed_mGperMin > 0.0:
            self.AnaerobicGlucoseFractionalDelivery = ( min( ( self.AnaerobicGlucoseDelivered / self.AnaerobicGlucoseUsed_mGperMin ), 1.0) )
        else:
            self.AnaerobicGlucoseFractionalDelivery = 1.0

        self.MinimumFractionalDelivery = ( min( ( min( self.KAFractionalDelivery, self.AerobicGlucoseFractionalDelivery) ), self.AnaerobicGlucoseFractionalDelivery) )
        self.K = 0.5
        self.DxMax = 1.0
        self.FractUse = self.MinimumFractionalDelivery
        self.FractUseDelay = delay( self.K, self.FractUse, self.FractUseDelay, System.Dx, 0.01)


class Brain_Lactate:
    def __init__(self):
        self.conc_Lac_ = None
        self.conc_Lac__mEqperL = None
        self.conc_Lac__mGperdL = None
        self.DC = 100.0
        self.Made = None
        self.Made_mGperMin = None
        self.Used = None
        self.Used_mGperMin = None
        self.Outflux = None
        self.Outflux_0 = None
        self.K = None
        self.Alpha = None
        self.MEQ_ML_TO_MG_DL = 9008.0
        self.GLUCOSE_TO_LACTATE = 0.99
        self.MG_TO_MEQ = 0.0112
        self.Mass = 0.82

    def CalcConc_func(self):
        self.conc_Lac_ = self.Mass / Brain_Size.LiquidVol
        self.conc_Lac__mEqperL = 1000.0 * self.conc_Lac_
        self.conc_Lac__mGperdL = self.MEQ_ML_TO_MG_DL * self.conc_Lac_

    def CalcDervs_func(self):
        self.Made_mGperMin = self.GLUCOSE_TO_LACTATE * Brain_Fuel.AnaerobicGlucoseUsed_mGperMin
        self.Made = self.MG_TO_MEQ * self.Made_mGperMin
        self.Used_mGperMin = Brain_Fuel.LacUsed_mGperMin
        self.Used = self.MG_TO_MEQ * self.Used_mGperMin
        self.K = self.DC / Brain_Size.LiquidVol
        if System.Dx >=0:
            self.Alpha = 0.0
        elif ( self.K * System.Dx ) >= 100.0:
            self.Alpha = 4E-44
        elif True:
            self.Alpha = ( math.e ** ( - self.K * System.Dx ) )
        self.Outflux_0 = self.DC * ( self.conc_Lac_ - LacPool.conc_Lac_ )
        self.Outflux = ( self.Alpha * self.Outflux_0 ) + ( ( 1 - self.Alpha ) * ( self.Made + self.Used ) )
        self.Change = self.Made - self.Used - self.Outflux
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.008)


class Brain_Metabolism:
    def __init__(self):
        self.TotalCalsUsed = None
        self.NormalCalsUsed = None
        self.InitialNormalCalsUsed = None
        self.NormalCalsUsed__CalperMinperG = 0.1647
        self.CalMultiplier = 1.0
        self.AerobicCals = None
        self.AnaerobicCals = None
        self.O2Need = None
        self.O2Lack = None

    def ScaleCals_func(self):
        self.InitialNormalCalsUsed = self.CalMultiplier * self.NormalCalsUsed__CalperMinperG * Brain_Size.InitialMass

    def CalcCals_func(self):
        self.NormalCalsUsed = self.CalMultiplier * self.NormalCalsUsed__CalperMinperG * Brain_Size.Mass
        self.TotalCalsUsed = self.NormalCalsUsed * Thyroid.Effect * HeatMetabolism.Core * Brain_Structure.Effect
        self.O2Need = Metabolism_Tools.CalToO2 * self.TotalCalsUsed

    def SplitCals_func(self):
        self.O2Lack = self.O2Need - Brain_Flow.O2Use
        self.AerobicCals = Metabolism_Tools.O2ToCal * Brain_Flow.O2Use
        self.AnaerobicCals = Metabolism_Tools.O2ToCal * self.O2Lack

class Brain_Structure:
    def __init__(self):
        self.PhEffect = None
        self.FuelEffect = None
        self.TemperatureEffect = None
        self.Effect = 1.0

    def PhOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [6.5, 6.6], [0.1, 0.0], [0.0, 0.0])

    def FuelOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [0.5, 0.8], [0.05, 0.0], [0.0, 0.0])

    def TemperatureOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [44.0, 46.0], [0.0, 0.05], [0.0, 0.0])

    def Calc_func(self):
        self.PhEffect = self.PhOnStructure_curve( Brain_Ph.Ph )
        self.FuelEffect = self.FuelOnStructure_curve( Brain_Fuel.FractUseDelay )
        self.TemperatureEffect = self.TemperatureOnStructure_curve( HeatCore.Temp_C )
        self.F1 = 0.0
        self.F2 = self.PhEffect + self.TemperatureEffect + self.FuelEffect
        self.Effect = backwardeuler( self.F1, self.F2, System.Dx, self.Effect, None)


class GlasgowComaScale:
    def __init__(self):
        self.Value = None

    def Calc_func(self):
        if Brain_Function.IsReallyDead:
            self.Value = 3.0
        elif Brain_Function.MayBeDead:
            self.Value = 4.0
        elif Brain_Function.NotBreathing:
            self.Value = 5.0
        elif Seizure.Convulsing:
            self.Value = 6.0
        elif Brain_Function.Comatose:
            self.Value = 7.0
        elif Brain_Function.Impaired:
            self.Value = 13.0
        elif Brain_Function.Confused:
            self.Value = 14.0
        elif Brain_Function.Normal:
            self.Value = 15.0

class Brain_Vasculature:
    def __init__(self):
        self.Tau = 30.0
        self.Effect = 1.0

    def PO2OnStimulus_curve(self, x):
        return cubic_hermite_spline(x, [27.0, 37.0, 47.0], [1.2, 1.0, 0.8], [0.0, -0.03, 0.0])

    def Parms_func(self):
        self.K = 1.0 / ( self.Tau * 1440.0 )

    def Calc_func(self):
        if Brain_Function.Failed:
            self.Stimulus = 0.0
        else:
            self.Stimulus = self.PO2OnStimulus_curve( Brain_Flow.PO2 )

        self.Effect = delay( self.K, self.Stimulus, self.Effect, System.Dx, None)


class Brain_Size:
    def __init__(self):
        self.Vol = None
        self.Mass = None
        self.InitialMass = None
        self.Density = None
        self.LiquidMass = None
        self.LiquidDensity = 1.00
        self.LiquidVol = None
        self.InitialLiquidVol = None
        self.SolidMass = None
        self.InitialSolidMass = None
        self.SolidDensity = 1.17
        self.SolidVol = None
        self.FractTotal = None
        self.IFV = None
        self.InitialIFV = None
        self.CellH2O = None
        self.InitialCellH2O = None
        self.MassFractBase = 0.0526
        self.H2OFractMass = 0.67
        self.SolidsFractMass = None

    def Initialize_func(self):
        self.InitialMass = self.MassFractBase * Weight.InitialOtherMass
        self.InitialLiquidVol = self.H2OFractMass * self.InitialMass / self.LiquidDensity
        self.SolidsFractMass = 1.0 - self.H2OFractMass
        self.InitialSolidMass = self.SolidsFractMass * self.InitialMass

    def ScaleH2O_func(self):
        self.FractTotal = self.InitialLiquidVol / TissueH2O.InitialVol
        self.InitialIFV = self.FractTotal * InterstitialWater.InitialVol
        self.InitialCellH2O = self.FractTotal * CellH2O.InitialVol

    def Calc_func(self):
        self.IFV = self.FractTotal * InterstitialWater.Vol
        self.CellH2O = self.FractTotal * CellH2O.Vol
        self.LiquidVol = self.IFV + self.CellH2O
        self.LiquidMass = self.LiquidVol * self.LiquidDensity
        self.SolidMass = self.InitialSolidMass
        self.SolidVol = self.SolidMass / self.SolidDensity
        self.Mass = self.LiquidMass + self.SolidMass
        self.Vol = self.LiquidVol + self.SolidVol
        self.Density = self.Mass / self.Vol

class BrainInsult:
    def __init__(self):
        self.Effect = None

    def Calc_func(self):
        BrainInsult_Ph.Calc_func()
        BrainInsult_Fuel.Calc_func()
        BrainInsult_Temperature.Calc_func()
        BrainInsult_Lowconc_Osm.Calc_func()
        BrainInsult_Highconc_Osm.Calc_func()
        BrainInsult_PO2.Calc_func()
        BrainInsult_Structure.Calc_func()
        self.Effect = ( min( ( min( ( min( ( min( ( min( ( min( ( min( BrainInsult_Ph.Effect, BrainInsult_Fuel.Effect) ), BrainInsult_Temperature.Effect) ), Anesthesia.BrainFunction) ), BrainInsult_Lowconc_Osm.Effect) ), BrainInsult_Highconc_Osm.Effect) ), BrainInsult_PO2.Effect) ), BrainInsult_Structure.Effect) )

class BrainInsult_PO2:
    def __init__(self):
        self.Effect = None
        self.PO2Delay = 37.0

    def PO2_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 30.0], [0.0, 1.0], [0.0, 0.0])

    def Calc_func(self):
        self.Effect = self.PO2_curve( self.PO2Delay )

    def Dervs_func(self):
        self.K = 4.0
        self.DxMax = 1.0
        self.PO2 = Brain_Flow.PO2
        self.PO2Delay = delay( self.K, self.PO2, self.PO2Delay, System.Dx, 0.37)


class BrainInsult_Temperature:
    def __init__(self):
        self.Effect = None

    def Temperature_curve(self, x):
        return cubic_hermite_spline(x, [41.0, 41.5, 45.0], [1.0, 0.4, 0.0], [0.0, -0.4, 0.0])

    def Calc_func(self):
        self.Effect = self.Temperature_curve( HeatCore.Temp_C )

class BrainInsult_Ph:
    def __init__(self):
        self.Effect = None

    def Ph_curve(self, x):
        return cubic_hermite_spline(x, [6.6, 6.7], [0.0, 1.0], [0.0, 0.0])

    def Calc_func(self):
        self.Effect = self.Ph_curve( Brain_Ph.Ph )

class BrainInsult_Structure:
    def __init__(self):
        self.Effect = None

    def Structure_curve(self, x):
        return cubic_hermite_spline(x, [0.5, 0.8], [0.0, 1.0], [0.0, 0.0])

    def Calc_func(self):
        self.Effect = self.Structure_curve( Brain_Structure.Effect )

class BrainInsult_Fuel:
    def __init__(self):
        self.Effect = None

    def Fuel_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.9], [0.0, 1.0], [0.0, 0.0])

    def Calc_func(self):
        self.Effect = self.Fuel_curve( Brain_Fuel.FractUseDelay )

class BrainInsult_Highconc_Osm:
    def __init__(self):
        self.Effect = None

    def Highconc_Osm_curve(self, x):
        return cubic_hermite_spline(x, [310.0, 370.0], [1.0, 0.0], [0.0, 0.0])

    def Calc_func(self):
        self.Effect = self.Highconc_Osm_curve( OsmBody.conc_Osm_mOsmperL_CellWall )

class BrainInsult_Lowconc_Osm:
    def __init__(self):
        self.Effect = None

    def Lowconc_Osm_curve(self, x):
        return cubic_hermite_spline(x, [170.0, 230.0], [0.0, 1.0], [0.0, 0.0])

    def Calc_func(self):
        self.Effect = self.Lowconc_Osm_curve( OsmBody.conc_Osm_mOsmperL_CellWall )

class AirSupply_PressureChamber:
    def __init__(self):
        self.Switch = False
        self.Pressure_Atm = 1.0
        self.Pressure = None

    def Calc_func(self):
        self.Pressure = 760.0 * self.Pressure_Atm

class AirSupply:
    def __init__(self):
        pass
    
class AirSupply_GasTanks:
    def __init__(self):
        self.Switch = False
        self.O2Valve_percent = 21.0
        self.O2_percent = None
        self.N2Valve_percent = 79.0
        self.N2_percent = None
        self.CO2Valve_percent = 0.0
        self.CO2_percent = None
        self.COValve_PPM = 0.0
        self.COValve_percent = None
        self.CO_percent = None
        self.AnestheticValve_percent = 0.0
        self.Anesthetic_percent = None
        self.SumValves = None

    def Calc_func(self):
        self.COValve_percent = self.COValve_PPM / 1e4
        self.SumValves = self.O2Valve_percent + self.N2Valve_percent + self.CO2Valve_percent + self.COValve_percent + self.AnestheticValve_percent
        self.O2_percent = ( 100.0 * self.O2Valve_percent ) / self.SumValves
        self.N2_percent = ( 100.0 * self.N2Valve_percent ) / self.SumValves
        self.CO2_percent = ( 100.0 * self.CO2Valve_percent ) / self.SumValves
        self.CO_percent = ( 100.0 * self.COValve_percent ) / self.SumValves
        self.Anesthetic_percent = ( 100.0 * self.AnestheticValve_percent ) / self.SumValves

class AirSupply_InspiredAir:
    def __init__(self):
        self.Pressure = None
        self.O2_percent = None
        self.N2_percent = None
        self.CO2_percent = None
        self.CO_percent = None
        self.Anesthetic_percent = None
        self.conc_O2 = None
        self.PO2 = None
        self.conc_N2 = None
        self.PN2 = None
        self.conc_CO2 = None
        self.PCO2 = None
        self.conc_CO = None
        self.PCO = None
        self.conc_Anesthetic = None
        self.PAnesthetic = None

    def Calc_func(self):
        if AirSupply_PressureChamber.Switch:
            self.Pressure = AirSupply_PressureChamber.Pressure
        else:
            self.Pressure = Barometer.Pressure

        if AirSupply_GasTanks.Switch:
            self.O2_percent = AirSupply_GasTanks.O2_percent
            self.N2_percent = AirSupply_GasTanks.N2_percent
            self.CO2_percent = AirSupply_GasTanks.CO2_percent
            self.CO_percent = AirSupply_GasTanks.CO_percent
            self.Anesthetic_percent = AirSupply_GasTanks.Anesthetic_percent
        else:
            self.O2_percent = 21.0
            self.N2_percent = 79.0
            self.CO2_percent = 0.0
            self.CO_percent = 0.0
            self.Anesthetic_percent = 0.0
        self.conc_O2 = 0.01 * self.O2_percent
        self.PO2 = self.conc_O2 * self.Pressure
        self.conc_N2 = 0.01 * self.N2_percent
        self.PN2 = self.conc_N2 * self.Pressure
        self.conc_CO2 = 0.01 * self.CO2_percent
        self.PCO2 = self.conc_CO2 * self.Pressure
        self.conc_CO = 0.01 * self.CO_percent
        self.PCO = self.conc_CO * self.Pressure
        self.conc_Anesthetic = 0.01 * self.Anesthetic_percent
        self.PAnesthetic = self.conc_Anesthetic * self.Pressure

class LeftAtrium:
    def __init__(self):
        self.Inflow = None
        self.Outflow = None
        self.V0 = 0.0
        self.StressedVol = None
        self.Pressure = None
        self.TMP = None
        self.ExternalPressure = None
        self.Compliance = 6.25
        self.Vol = 51.0

    def CalcPressure_func(self):
        self.StressedVol = self.Vol - self.V0
        self.TMP = self.StressedVol / self.Compliance
        self.ExternalPressure = Pericardium_Cavity.Pressure
        self.Pressure = self.TMP + self.ExternalPressure

    def Dervs_func(self):
        self.DxMax = 0.00005 * self.Compliance
        self.Inflow = PulmVeins.Outflow
        self.Outflow = LeftVentricle.Outflow
        self.Change = self.Inflow - self.Outflow

class SplanchnicVeins:
    def __init__(self):
        self.Inflow = None
        self.Outflow = None
        self.V0 = 500.0
        self.StressedVol = None
        self.Pressure = None
        self.ExternalPressure = None
        self.Compliance = 62.5
        self.Conductance = 178
        self.Vol = 1007.0

    def CalcPressure_func(self):
        self.StressedVol = ( max( ( self.Vol - self.V0 ), 0.0) )
        self.ExternalPressure = 0.0
        self.Pressure = ( self.StressedVol / self.Compliance ) + self.ExternalPressure

    def Dervs_func(self):
        if self.Conductance > 0.0:
            self.DxMax = 0.5 * self.Compliance / self.Conductance
        else:
            self.DxMax = self.INFINITY

        self.Inflow = OrganFlow.HepaticVeinFlow
        self.Outflow = self.Conductance * ( self.Pressure - RightAtrium.Pressure )
        self.Change = self.Inflow - self.Outflow

class PulmVeins:
    def __init__(self):
        self.Inflow = None
        self.Outflow = None
        self.V0 = 150.0
        self.StressedVol = None
        self.Pressure = None
        self.ExternalPressure = None
        self.Compliance = 6.0
        self.Conductance = 5400
        self.Vol = 211.0

    def CalcPressure_func(self):
        self.StressedVol = ( max( ( self.Vol - self.V0 ), 0.0) )
        self.ExternalPressure = Thorax.AvePressure
        self.Pressure = ( self.StressedVol / self.Compliance ) + self.ExternalPressure

    def Dervs_func(self):
        if self.Conductance > 0.0:
            self.DxMax = 0.5 * self.Compliance / self.Conductance
        else:
            self.DxMax = self.INFINITY

        self.Inflow = PulmCapys.Outflow
        self.Outflow = self.Conductance * ( self.Pressure - LeftAtrium.Pressure )
        self.Change = self.Inflow - self.Outflow

class PulmArty:
    def __init__(self):
        self.Inflow = None
        self.Outflow = None
        self.V0 = 110.0
        self.StressedVol = None
        self.Pressure = None
        self.ExternalPressure = None
        self.Compliance = 5.3
        self.Conductance = 1350
        self.KS = 0.475
        self.KD = 0.351
        self.SBP = None
        self.DBP = None
        self.Vol = 201.0

    def CalcPressure_func(self):
        self.StressedVol = ( max( ( self.Vol - self.V0 ), 0.0) )
        self.ExternalPressure = Thorax.AvePressure
        self.Pressure = ( self.StressedVol / self.Compliance ) + self.ExternalPressure

    def CalcOutflow_func(self):
        self.Outflow = self.Conductance * ( self.Pressure - PulmCapys.Pressure )

    def Dervs_func(self):
        if self.Conductance > 0.0:
            self.DxMax = 0.5 * self.Compliance / self.Conductance
        else:
            self.DxMax = self.INFINITY

        self.Inflow = RightVentricle.Outflow
        self.Change = self.Inflow - self.Outflow

    def PulsatilePressure_func(self):
        self.SBP = self.Pressure + ( self.KS * ( CardiacOutput.StrokeVolume / self.Compliance ) )
        self.DBP = self.Pressure - ( self.KD * ( CardiacOutput.StrokeVolume / self.Compliance ) )

class RightVentricle:
    def __init__(self):
        self.Inflow = None
        self.Outflow = None
        self.Vol = 87.5

    def Dervs_func(self):
        self.Inflow = RightHeartPumping_Pumping.BloodFlow
        self.Outflow = RightHeartPumping_Pumping.BloodFlow
        self.Vol_SteadyState = ( RightHeartPumping_Diastole.EDV + RightHeartPumping_Systole.ESV ) / 2.0
        self.K = 1.0
        self.DxMax = 1.0
        self.Vol = delay( self.K, self.Vol_SteadyState, self.Vol, System.Dx, 0.9)


class RightAtrium:
    def __init__(self):
        self.Inflow = None
        self.Outflow = None
        self.V0 = 0.0
        self.StressedVol = None
        self.Pressure = None
        self.TMP = None
        self.ExternalPressure = None
        self.Compliance = 12.5
        self.Vol = 51.0

    def CalcPressure_func(self):
        self.StressedVol = self.Vol - self.V0
        self.TMP = self.StressedVol / self.Compliance
        self.ExternalPressure = Pericardium_Cavity.Pressure
        self.Pressure = self.TMP + self.ExternalPressure

    def Dervs_func(self):
        self.DxMax = 0.0001 * self.Compliance
        self.Inflow = SystemicVeins.Outflow + SplanchnicVeins.Outflow
        self.Outflow = RightVentricle.Outflow
        self.Change = self.Inflow - self.Outflow

class LeftVentricle:
    def __init__(self):
        self.Inflow = None
        self.Outflow = None
        self.Vol = 87.5

    def Dervs_func(self):
        self.Inflow = LeftHeartPumping_Pumping.BloodFlow
        self.Outflow = LeftHeartPumping_Pumping.BloodFlow
        self.Vol_SteadyState = ( LeftHeartPumping_Diastole.EDV + LeftHeartPumping_Systole.ESV ) / 2.0
        self.K = 1.0
        self.DxMax = 1.0
        self.Vol = delay( self.K, self.Vol_SteadyState, self.Vol, System.Dx, 0.9)


class VascularCompartments:

    def CalcPressure_1_func(self):
        RightAtrium.CalcPressure_func()
        LeftAtrium.CalcPressure_func()
        SystemicArtys.CalcPressure_func()

    def CalcPressure_2_func(self):
        SystemicVeins.CalcPressure_func()
        SplanchnicVeins.CalcPressure_func()
        PulmArty.CalcPressure_func()
        PulmCapys.CalcPressure_func()
        PulmVeins.CalcPressure_func()

    def Dervs_func(self):
        RightVentricle.Dervs_func()
        LeftVentricle.Dervs_func()
        SystemicVeins.Dervs_func()
        SplanchnicVeins.Dervs_func()
        RightAtrium.Dervs_func()
        PulmArty.Dervs_func()
        PulmCapys.Dervs_func()
        PulmVeins.Dervs_func()
        LeftAtrium.Dervs_func()
        SystemicArtys.Dervs_func()

class SystemicArtys:
    def __init__(self):
        self.Inflow = None
        self.Outflow = None
        self.V0 = 850.0
        self.StressedVol = None
        self.Pressure = None
        self.ExternalPressure = None
        self.Compliance = 1.55
        self.Conductance = 60
        self.MMHG_TO_KPA = 0.133
        self.KS = 0.475
        self.KD = 0.351
        self.SBP = None
        self.DBP = None
        self.SBP_kPa = None
        self.MeanBP_kPa = None
        self.DBP_kPa = None
        self.Vol = 999.0

    def CalcPressure_func(self):
        self.StressedVol = ( max( ( self.Vol - self.V0 ), 0.0) )
        self.ExternalPressure = 0.0
        self.Pressure = ( self.StressedVol / self.Compliance ) + self.ExternalPressure

    def Dervs_func(self):
        if self.Conductance > 0.0:
            self.DxMax = 0.4 * self.Compliance / self.Conductance
        else:
            self.DxMax = self.INFINITY

        self.Inflow = LeftVentricle.Outflow
        self.Outflow = OrganFlow.HepaticVeinFlow + OrganFlow.PeripheralFlow
        self.Change = self.Inflow - self.Outflow

    def PulsatilePressure_func(self):
        self.SBP = self.Pressure + ( self.KS * ( CardiacOutput.StrokeVolume / self.Compliance ) )
        self.DBP = self.Pressure - ( self.KD * ( CardiacOutput.StrokeVolume / self.Compliance ) )

    def Wrapup_func(self):
        self.SBP_kPa = self.MMHG_TO_KPA * self.SBP
        self.MeanBP_kPa = self.MMHG_TO_KPA * self.Pressure
        self.DBP_kPa = self.MMHG_TO_KPA * self.DBP

class PulmCapys:
    def __init__(self):
        self.Inflow = None
        self.Outflow = None
        self.V0 = 140.0
        self.StressedVol = None
        self.Pressure = None
        self.ExternalPressure = None
        self.Compliance = 4.6
        self.Conductance = 1800
        self.Vol = 200.0

    def CalcPressure_func(self):
        self.StressedVol = ( max( ( self.Vol - self.V0 ), 0.0) )
        self.ExternalPressure = Thorax.AvePressure
        self.Pressure = ( self.StressedVol / self.Compliance ) + self.ExternalPressure

    def CalcOutflow_func(self):
        self.Outflow = self.Conductance * ( self.Pressure - PulmVeins.Pressure )

    def Dervs_func(self):
        if self.Conductance > 0.0:
            self.DxMax = 0.5 * self.Compliance / self.Conductance
        else:
            self.DxMax = self.INFINITY

        self.Inflow = PulmArty.Outflow
        self.Change = self.Inflow - self.Outflow

class SystemicVeins:
    def __init__(self):
        self.Inflow = None
        self.Outflow = None
        self.V0Basic = 1700.0
        self.V0 = None
        self.V0_Alpha_Effect = None
        self.V0_A2_Effect = None
        self.StressedVol = None
        self.Pressure = None
        self.ExternalPressure = None
        self.Compliance = 88.6
        self.ConductanceBasic = 692.0
        self.Conductance = None
        self.Vol = None
        self.Change = None

    def V0_Alpha_Effect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.0, 3.0], [1.2, 1.0, 0.6], [0.0, -0.3, 0.0])

    def V0_A2_Effect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.3, 3.0], [1.05, 1.0, 0.85], [0.0, -0.1, 0.0])

    def CalcVol_func(self):
        self.Vol = BloodVol.Vol - SystemicArtys.Vol - PulmArty.Vol - PulmCapys.Vol - PulmVeins.Vol - RightAtrium.Vol - RightVentricle.Vol - LeftAtrium.Vol - LeftVentricle.Vol - SplanchnicVeins.Vol - BVSeq.Vol

    def CalcPressure_func(self):
        self.V0_Alpha_Effect = self.V0_Alpha_Effect_curve( SystemicVeins_AlphaReceptors.Activity )
        self.V0_A2_Effect = self.V0_A2_Effect_curve( A2Pool.Log10Conc )
        self.V0 = self.V0Basic * self.V0_Alpha_Effect * self.V0_A2_Effect
        self.StressedVol = ( max( ( self.Vol - self.V0 ), 0.0) )
        self.ExternalPressure = 0.0
        self.Pressure = ( self.StressedVol / self.Compliance ) + self.ExternalPressure

    def Dervs_func(self):
        self.Inflow = OrganFlow.PeripheralFlow
        self.Conductance = self.ConductanceBasic * BloodVol.CollapsedEffect * Exercise_MusclePump.Effect * Viscosity.ConductanceEffect
        self.Outflow = self.Conductance * ( self.Pressure - RightAtrium.Pressure )
        self.Change = self.Inflow - self.Outflow

class Inhibin_B:
    def __init__(self):
        self.Secretion = None
        self.Base = 0.28

    def Dervs_func(self):
        self.Secretion = self.Base * Ovaries_Follicle.Mass * ( Ovaries.Phase == Ovaries.IS_FOLLICULAR )

class Follicle_Estradiol:
    def __init__(self):
        self.Secretion = None
        self.BasicSecretion = 0.30
        self.MassEffect = None

    def MassEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 4000.0], [0.0, 10.0], [0.0, 0.0])

    def Dervs_func(self):
        self.MassEffect = self.MassEffect_curve( Ovaries_Follicle.Mass )
        self.Secretion = self.BasicSecretion * self.MassEffect * ( Ovaries.Phase == Ovaries.IS_FOLLICULAR )

class Inhibin_A:
    def __init__(self):
        self.Secretion = None
        self.Base = 0.28

    def Dervs_func(self):
        self.Secretion = self.Base * Ovaries_CorpusLuteum.Mass

class Ovaries_CorpusLuteum:
    def __init__(self):
        self.Growth = None
        self.Involution = None
        self.Radius_mM = None
        self.Mass = 0.0

    def Dervs_func(self):
        CorpusLuteum_Growth.Dervs_func()
        CorpusLuteum_Involution.Dervs_func()
        self.Growth = CorpusLuteum_Growth.Growth
        self.Involution = CorpusLuteum_Involution.Rate
        self.Change = self.Growth - self.Involution
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 1.0)


    def Wrapup_func(self):
        if ( Ovaries.query_Cycling ) and ( Ovaries.Phase == Ovaries.IS_LUTEAL ) and ( self.Mass < 100.0 ):
            Ovaries.Phase = Ovaries.IS_IDLE
        else:
            pass
        self.Radius_mM = ( 0.239 * self.Mass ) ** 0.333

class Ovaries_Follicle:
    def __init__(self):
        self.Growth = None
        self.Atresia = None
        self.Radius_mM = None
        self.Mass = 65

    def Dervs_func(self):
        Follicle_Growth.Dervs_func()
        Follicle_Atresia.Dervs_func()
        self.Growth = Follicle_Growth.Growth
        self.Atresia = Follicle_Atresia.Rate
        self.Change = self.Growth - self.Atresia
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 1.0)


    def Wrapup_func(self):
        if ( Ovaries.query_Cycling ) and ( Ovaries.Phase != Ovaries.IS_FOLLICULAR ) and ( ( self.Mass + Ovaries_CorpusLuteum.Mass ) <= 400.0 ) and ( FSH_Circulating.conc_Conc_IUperL > 3.0 ):
            Ovaries.Phase = Ovaries.IS_FOLLICULAR
            self.Mass = 65
        else:
            pass
        if ( LH_Circulating.conc_Conc_IUperL > 20.0 ) and ( self.Mass > 2800.0 ) and ( Ovaries.Phase == Ovaries.IS_FOLLICULAR ):
            Ovaries.Phase = Ovaries.IS_OVULATORY
        else:
            pass
        self.Radius_mM = ( 0.239 * self.Mass ) ** 0.333

class CorpusLuteum_Involution:
    def __init__(self):
        self.Rate = None
        self.conc_hCGEffect = None
        self.K = None
        self.BasicK = 0.0001

    def conc_hCGEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 100.0], [1.0, -0.5], [0.0, 0.0])

    def Dervs_func(self):
        self.conc_hCGEffect = self.conc_hCGEffect_curve( hCG.conc_Conc_IUperL )
        self.K = self.BasicK * self.conc_hCGEffect
        self.Rate = self.K * Ovaries_CorpusLuteum.Mass

class Follicle_Atresia:
    def __init__(self):
        self.Rate = None
        self.IsAtretic = None
        self.MassEffect = None
        self.K = 0.5

    def MassEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 200.0], [0.0, 1.0], [0.0, 0.0])

    def Dervs_func(self):
        self.IsAtretic = ( Ovaries.Phase == Ovaries.IS_OVULATORY ) or ( Ovaries.Phase == Ovaries.IS_LUTEAL )
        self.MassEffect = self.MassEffect_curve( Ovaries_Follicle.Mass )
        self.Rate = self.K * self.MassEffect * self.IsAtretic

class CorpusLuteum_Estradiol:
    def __init__(self):
        self.Secretion = None
        self.BasicSecretion = 0.3
        self.MassEffect = None

    def MassEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 4000.0], [0.0, 10.0], [0.0, 0.0])

    def Dervs_func(self):
        self.MassEffect = self.MassEffect_curve( Ovaries_CorpusLuteum.Mass )
        self.Secretion = self.BasicSecretion * self.MassEffect

class Ovaries:
    def __init__(self):
        self.query_Cycling = False
        self.BlockCycling = False
        self.Menarche_Years = 12.5
        self.Menopause_Years = 45.0
        self.Phase = 0
        self.query_Idle = False
        self.query_Follicular = False
        self.query_Ovulatory = False
        self.query_Luteal = False
        self.IS_IDLE = 0
        self.IS_FOLLICULAR = 1
        self.IS_OVULATORY = 2
        self.IS_LUTEAL = 3

    def Parms_func(self):
        pass

    def Dervs_func(self):
        Ovaries_Follicle.Dervs_func()
        Ovaries_CorpusLuteum.Dervs_func()
        Ovaries_Estradiol.Dervs_func()
        Ovaries_Progesterone.Dervs_func()
        Ovaries_Testosterone.Dervs_func()
        Ovaries_Inhibin.Dervs_func()

    def Wrapup_func(self):
        if ( Age.Age_Years < self.Menarche_Years ) or ( Age.Age_Years > self.Menopause_Years ) or ( self.BlockCycling ):
            self.query_Cycling = False
            self.Phase = self.IS_IDLE
        else:
            self.query_Cycling = True
        Ovaries_Follicle.Wrapup_func()
        Ovaries_Ovulation.Wrapup_func()
        Ovaries_CorpusLuteum.Wrapup_func()
        self.query_Idle = self.Phase == self.IS_IDLE
        self.query_Follicular = self.Phase == self.IS_FOLLICULAR
        self.query_Ovulatory = self.Phase == self.IS_OVULATORY
        self.query_Luteal = self.Phase == self.IS_LUTEAL

class Ovaries_Estradiol:
    def __init__(self):
        self.Secretion = None

    def Dervs_func(self):
        Follicle_Estradiol.Dervs_func()
        CorpusLuteum_Estradiol.Dervs_func()
        self.Secretion = Follicle_Estradiol.Secretion + CorpusLuteum_Estradiol.Secretion

class Ovaries_Inhibin:
    def __init__(self):
        self.Secretion = None

    def Dervs_func(self):
        Inhibin_A.Dervs_func()
        Inhibin_B.Dervs_func()
        self.Secretion = Inhibin_A.Secretion + Inhibin_B.Secretion

class Follicle_Growth:
    def __init__(self):
        self.Growth = None
        self.FSHEffect = None
        self.EstradiolEffect = None
        self.MassEffect = None
        self.BasicGrowth = 0.02

    def FSHEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 5.0, 15.0], [0.8, 2.0, 3.0], [0.0, 0.2, 0.0])

    def EstradiolEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 3.0], [1.0, 3.0], [0.0, 0.0])

    def MassEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 4000.0], [1.0, 10.0], [0.005, 0.0])

    def Dervs_func(self):
        self.FSHEffect = self.FSHEffect_curve( FSH_Circulating.conc_Conc_IUperL )
        self.EstradiolEffect = self.EstradiolEffect_curve( Estradiol.conc_Conc_nMolperL )
        self.MassEffect = self.MassEffect_curve( Ovaries_Follicle.Mass )
        self.Growth = self.BasicGrowth * self.FSHEffect * self.EstradiolEffect * self.MassEffect * ( Ovaries.Phase == Ovaries.IS_FOLLICULAR )

class CorpusLuteum_Growth:
    def __init__(self):
        self.Growth = None

    def Dervs_func(self):
        self.Growth = Ovaries_Follicle.Atresia

class Ovaries_Ovulation:
    def __init__(self):
        self.AnnounceOvulation = False
        self.LastOvulation = 0

    def Wrapup_func(self):
        if ( Ovaries.Phase == Ovaries.IS_OVULATORY ) and ( Progesterone.conc_Conc_nMolperL >= 8.0 ):
            self.LastOvulation = System.X
            Ovaries.Phase = Ovaries.IS_LUTEAL
            if self.AnnounceOvulation:
                pass
            else:
                pass
        else:
            pass

class Ovaries_Testosterone:
    def __init__(self):
        self.Secretion = None

    def Dervs_func(self):
        self.Secretion = 0.25

class Ovaries_Progesterone:
    def __init__(self):
        self.Secretion = None
        self.BasicSecretion = 20.0
        self.MassEffect = None

    def MassEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 4000.0], [0.0, 10.0], [0.0, 0.0])

    def Dervs_func(self):
        self.MassEffect = self.MassEffect_curve( Ovaries_CorpusLuteum.Mass )
        self.Secretion = self.BasicSecretion * self.MassEffect

class SurfaceArea:
    def __init__(self):
        self.Area = None

    def Calc_func(self):
        self.Area = 0.007184 * ( Weight.Weight_kG ** 0.425 ) * ( Height.Height ** 0.725 )

class BMI:
    def __init__(self):
        self.BMI = None

    def Calc_func(self):
        self.BMI = Weight.Weight_kG / ( Height.Height_M ** 2 )

class Age:
    def __init__(self):
        self.InitialAge_Years = 37.0
        self.Age_Years = None

    def Initialize_func(self):
        self.InitialAge_Years = Values_Age.Age_Years

    def Calc_func(self):
        self.Age_Years = self.InitialAge_Years + ( ( System.X - System.InitialX ) / 525600.0 )

class Gender:
    def __init__(self):
        self.IsMale = None
        self.IsFemale = None
        self.Value = None
    
class Morphology:

    def Parms_func(self):
        pass

class Weight:
    def __init__(self):
        self.Weight = None
        self.InitialWeight = None
        self.Weight_kG = None
        self.Weight_Lb = None
        self.OrganMass = None
        self.InitialOrganMass = None
        self.Core = None
        self.InitialCore = None
        self.Core_kG = None
        self.OtherMass = None
        self.InitialOtherMass = None
        self.FatMass = None
        self.InitialFatMass = None
        self.MuscleMass = None
        self.InitialMuscleMass = None
        self.SkinMass = None
        self.InitialSkinMass = None

    def InitializeOtherMass_func(self):
        self.InitialOtherMass = Values_OtherMass.Mass

    def Initialize_func(self):
        Weight_Fluids.Initialize_func()
        self.InitialFatMass = Fat_Size.InitialMass
        self.InitialMuscleMass = SkeletalMuscle_Size.InitialMass
        self.InitialSkinMass = Skin_Size.InitialMass
        self.InitialOrganMass = Bone_Size.InitialMass + Brain_Size.InitialMass + GITract_Size.InitialMass + Kidney_Size.InitialMass + LeftHeart_Size.InitialMass + Liver_Size.InitialMass + OtherTissue_Size.InitialMass + RespiratoryMuscle_Size.InitialMass + RightHeart_Size.InitialMass + self.InitialFatMass + self.InitialMuscleMass + self.InitialSkinMass
        self.InitialCore = self.InitialOrganMass - self.InitialMuscleMass - self.InitialSkinMass + Weight_Fluids.InitialCore
        self.InitialWeight = self.InitialOrganMass + Weight_Fluids.InitialTotal

    def Calc_func(self):
        Weight_Fluids.Calc_func()
        self.FatMass = Fat_Size.Mass
        self.MuscleMass = SkeletalMuscle_Size.Mass
        self.SkinMass = Skin_Size.Mass
        self.OrganMass = Bone_Size.Mass + Brain_Size.Mass + GITract_Size.Mass + Kidney_Size.Mass + LeftHeart_Size.Mass + Liver_Size.Mass + OtherTissue_Size.Mass + RespiratoryMuscle_Size.Mass + RightHeart_Size.Mass + self.FatMass + self.MuscleMass + self.SkinMass
        self.OtherMass = self.OrganMass - self.FatMass - self.MuscleMass
        self.Core = self.OrganMass - self.MuscleMass - self.SkinMass + Weight_Fluids.Core
        self.Core_kG = self.Core / 1000.0
        self.Weight = self.OrganMass + Weight_Fluids.Total
        self.Weight_kG = self.Weight / 1000.0
        self.Weight_Lb = 2.2 * self.Weight_kG

class Weight_Fluids:
    def __init__(self):
        self.Total = None
        self.InitialTotal = None
        self.Core = None
        self.InitialCore = None
        self.Blood = None
        self.InitialBlood = None
        self.ExternalCore = None
        self.InitialExternalCore = None
        self.ExternalOther = None
        self.InitialExternalOther = None

    def Initialize_func(self):
        self.InitialBlood = BloodVol.InitialVol
        self.InitialExternalCore = ExternalH2O.InitialCore
        self.InitialExternalOther = ExternalH2O.InitialOther
        self.InitialCore = self.InitialBlood + self.InitialExternalCore
        self.InitialTotal = self.InitialCore + self.InitialExternalOther

    def Calc_func(self):
        self.Blood = BloodVol.Vol
        self.ExternalCore = ExternalH2O.Core
        self.ExternalOther = ExternalH2O.Other
        self.Core = self.Blood + self.ExternalCore
        self.Total = self.Core + self.ExternalOther

class Height:
    def __init__(self):
        self.Height = 178.0
        self.Height_M = None
        self.Height_In = None

    def Initialize_func(self):
        Height.Height = Values_Height.Height_cM
        self.Height_In = self.Height / 2.54
        self.Height_M = self.Height / 100.0

class AnesthesiaIVRespiratoryMuscle:
    def __init__(self):
        self.conc_Tissue = None
        self.conc_Vein = None
        self.Uptake = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Tissue = self.Mass / RespiratoryMuscle_Size.Vol
        self.conc_Vein = self.conc_Tissue * AnesthesiaIVSolubility.GeneralK

    def Dervs_func(self):
        self.Uptake = ( AnesthesiaIVBlood.conc_Blood - self.conc_Vein ) * RespiratoryMuscle_Flow.BloodFlow
        self.Change = self.Uptake
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 1.6)


class AnesthesiaIVRightHeart:
    def __init__(self):
        self.conc_Tissue = None
        self.conc_Vein = None
        self.Uptake = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Tissue = self.Mass / RightHeart_Size.Vol
        self.conc_Vein = self.conc_Tissue * AnesthesiaIVSolubility.GeneralK

    def Dervs_func(self):
        self.Uptake = ( AnesthesiaIVBlood.conc_Blood - self.conc_Vein ) * RightHeart_Flow.BloodFlow
        self.Change = self.Uptake
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.02)


class AnesthesiaIVSkin:
    def __init__(self):
        self.conc_Tissue = None
        self.conc_Vein = None
        self.Uptake = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Tissue = self.Mass / Skin_Size.Vol
        self.conc_Vein = self.conc_Tissue * AnesthesiaIVSolubility.GeneralK

    def Dervs_func(self):
        self.Uptake = ( AnesthesiaIVBlood.conc_Blood - self.conc_Vein ) * Skin_Flow.BloodFlow
        self.Change = self.Uptake
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 1.61)


class AnesthesiaIVInjection:
    def __init__(self):
        self.Dose = 300.0
        self.Timespan = 30.0
        self.K = 0.0
        self.Loss = None
        self.TotalInjections = 0.0
        self.CumulativeDose = 0.0
        self.Mass = 0.0

    def Dervs_func(self):
        self.Loss = self.K * self.Mass
        self.Change = - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 3.0)


    def InjectNow_func(self):
        self.Mass = self.Mass + self.Dose
        self.K = ( 1 / ( 2.0 * ( self.Timespan / 60.0 ) ) )
        self.TotalInjections = self.TotalInjections + 1
        self.CumulativeDose = self.CumulativeDose + self.Dose

    def Reset_func(self):
        self.TotalInjections = 0.0
        self.CumulativeDose = 0.0

class AnesthesiaIVBone:
    def __init__(self):
        self.conc_Tissue = None
        self.conc_Vein = None
        self.Uptake = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Tissue = self.Mass / Bone_Size.Vol
        self.conc_Vein = self.conc_Tissue * AnesthesiaIVSolubility.GeneralK

    def Dervs_func(self):
        self.Uptake = ( AnesthesiaIVBlood.conc_Blood - self.conc_Vein ) * Bone_Flow.BloodFlow
        self.Change = self.Uptake
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 2.4)


class AnesthesiaIV:

    def Parms_func(self):
        AnesthesiaIVSolubility.Parms_func()

    def CalcConc_func(self):
        AnesthesiaIVBlood.CalcConc_func()
        AnesthesiaIVBone.CalcConc_func()
        AnesthesiaIVBrain.CalcConc_func()
        AnesthesiaIVFat.CalcConc_func()
        AnesthesiaIVGITract.CalcConc_func()
        AnesthesiaIVKidney.CalcConc_func()
        AnesthesiaIVLeftHeart.CalcConc_func()
        AnesthesiaIVLiver.CalcConc_func()
        AnesthesiaIVOtherTissue.CalcConc_func()
        AnesthesiaIVRespiratoryMuscle.CalcConc_func()
        AnesthesiaIVRightHeart.CalcConc_func()
        AnesthesiaIVSkeletalMuscle.CalcConc_func()
        AnesthesiaIVSkin.CalcConc_func()

    def Dervs_func(self):
        AnesthesiaIVBone.Dervs_func()
        AnesthesiaIVBrain.Dervs_func()
        AnesthesiaIVFat.Dervs_func()
        AnesthesiaIVGITract.Dervs_func()
        AnesthesiaIVKidney.Dervs_func()
        AnesthesiaIVLeftHeart.Dervs_func()
        AnesthesiaIVLiver.Dervs_func()
        AnesthesiaIVOtherTissue.Dervs_func()
        AnesthesiaIVRespiratoryMuscle.Dervs_func()
        AnesthesiaIVRightHeart.Dervs_func()
        AnesthesiaIVSkeletalMuscle.Dervs_func()
        AnesthesiaIVSkin.Dervs_func()
        AnesthesiaIVInjection.Dervs_func()
        AnesthesiaIVInfusion.Dervs_func()
        AnesthesiaIVBlood.Dervs_func()

class AnesthesiaIVLeftHeart:
    def __init__(self):
        self.conc_Tissue = None
        self.conc_Vein = None
        self.Uptake = None
        self.HrtCont = None
        self.Mass = 0.0

    def HrtCont_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.045], [1.0, 0.0], [0.0, 0.0])

    def CalcConc_func(self):
        self.conc_Tissue = self.Mass / LeftHeart_Size.Vol
        self.conc_Vein = self.conc_Tissue * AnesthesiaIVSolubility.GeneralK
        self.HrtCont = self.HrtCont_curve( self.conc_Tissue )

    def Dervs_func(self):
        self.Uptake = ( AnesthesiaIVBlood.conc_Blood - self.conc_Vein ) * LeftHeart_Flow.BloodFlow
        self.Change = self.Uptake
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.11)


class AnesthesiaIVInfusion:
    def __init__(self):
        self.Switch = False
        self.Setting = 0.0
        self.Rate = None

    def Dervs_func(self):
        self.Rate = self.Switch * self.Setting

class AnesthesiaIVSolubility:
    def __init__(self):
        self.General = 1.0
        self.GeneralK = None
        self.Brain = 1.3
        self.BrainK = None
        self.Adipose = 13.3
        self.AdiposeK = None

    def Parms_func(self):
        self.GeneralK = 1.0 / self.General
        self.BrainK = 1.0 / self.Brain
        self.AdiposeK = 1.0 / self.Adipose

class AnesthesiaIVGITract:
    def __init__(self):
        self.conc_Tissue = None
        self.conc_Vein = None
        self.Uptake = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Tissue = self.Mass / GITract_Size.Vol
        self.conc_Vein = self.conc_Tissue * AnesthesiaIVSolubility.GeneralK

    def Dervs_func(self):
        self.Uptake = ( AnesthesiaIVBlood.conc_Blood - self.conc_Vein ) * GITract_Flow.BloodFlow
        self.Change = self.Uptake
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 1.08)


class AnesthesiaIVSkeletalMuscle:
    def __init__(self):
        self.conc_Tissue = None
        self.conc_Vein = None
        self.Uptake = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Tissue = self.Mass / SkeletalMuscle_Size.Vol
        self.conc_Vein = self.conc_Tissue * AnesthesiaIVSolubility.GeneralK

    def Dervs_func(self):
        self.Uptake = ( AnesthesiaIVBlood.conc_Blood - self.conc_Vein ) * SkeletalMuscle_Flow.BloodFlow
        self.Change = self.Uptake
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 11.1)


class AnesthesiaIVBlood:
    def __init__(self):
        self.conc_Blood = None
        self.Gain = None
        self.Loss = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Blood = self.Mass / BloodVol.Vol

    def Dervs_func(self):
        self.Gain = AnesthesiaIVInjection.Loss + AnesthesiaIVInfusion.Rate
        self.Loss = AnesthesiaIVBone.Uptake + AnesthesiaIVBrain.Uptake + AnesthesiaIVFat.Uptake + AnesthesiaIVGITract.Uptake + AnesthesiaIVKidney.Uptake + AnesthesiaIVLeftHeart.Uptake + AnesthesiaIVLiver.Uptake + AnesthesiaIVOtherTissue.Uptake + AnesthesiaIVRespiratoryMuscle.Uptake + AnesthesiaIVRightHeart.Uptake + AnesthesiaIVSkeletalMuscle.Uptake + AnesthesiaIVSkin.Uptake
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 2.16)


class AnesthesiaIVLiver:
    def __init__(self):
        self.conc_Tissue = None
        self.conc_Vein = None
        self.conc_Arty = None
        self.Uptake = None
        self.DegradeK = 0.09
        self.Degrade = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Tissue = self.Mass / Liver_Size.Vol
        self.conc_Vein = self.conc_Tissue * AnesthesiaIVSolubility.GeneralK

    def Dervs_func(self):
        if OrganFlow.HepaticVeinFlow > 0.0:
            self.conc_Arty = ( ( AnesthesiaIVBlood.conc_Blood * HepaticArty.Flow ) + ( AnesthesiaIVGITract.conc_Vein * GITract_Flow.BloodFlow ) ) / OrganFlow.HepaticVeinFlow
        else:
            self.conc_Arty = 0.0

        self.Uptake = ( self.conc_Arty - self.conc_Vein ) * OrganFlow.HepaticVeinFlow
        self.Degrade = self.DegradeK * self.Mass
        self.Change = self.Uptake - self.Degrade
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.6)


class AnesthesiaIVBrain:
    def __init__(self):
        self.conc_Tissue = None
        self.conc_Vein = None
        self.Uptake = None
        self.BrainFunc = None
        self.TidalVol = None
        self.Mass = 0.0

    def BrainFunc_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.015, 0.045, 0.06], [1.0, 0.4, 0.2, 0.0], [0.0, -5.0, -5.0, 0.0])

    def TidalVol_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.045], [1.0, 0.0], [0.0, 0.0])

    def CalcConc_func(self):
        self.conc_Tissue = self.Mass / Brain_Size.Vol
        self.conc_Vein = self.conc_Tissue * AnesthesiaIVSolubility.BrainK
        self.BrainFunc = self.BrainFunc_curve( self.conc_Tissue )
        self.TidalVol = self.TidalVol_curve( self.conc_Tissue )

    def Dervs_func(self):
        self.Uptake = ( AnesthesiaIVBlood.conc_Blood - self.conc_Vein ) * Brain_Flow.BloodFlow
        self.Change = self.Uptake
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.6)


class AnesthesiaIVKidney:
    def __init__(self):
        self.conc_Tissue = None
        self.conc_Vein = None
        self.Uptake = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Tissue = self.Mass / Kidney_Size.Vol
        self.conc_Vein = self.conc_Tissue * AnesthesiaIVSolubility.GeneralK

    def Dervs_func(self):
        self.Uptake = ( AnesthesiaIVBlood.conc_Blood - self.conc_Vein ) * Kidney_Flow.BloodFlow
        self.Change = self.Uptake
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.13)


class AnesthesiaIVFat:
    def __init__(self):
        self.conc_Tissue = None
        self.conc_Vein = None
        self.Uptake = None
        self.Mass = 0.0

    def CalcConc_func(self):
        self.conc_Tissue = self.Mass / Fat_Size.Vol
        self.conc_Vein = self.conc_Tissue * AnesthesiaIVSolubility.AdiposeK

    def Dervs_func(self):
        self.Uptake = ( AnesthesiaIVBlood.conc_Blood - self.conc_Vein ) * Fat_Flow.BloodFlow
        self.Change = self.Uptake
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 6.4)


class AnesthesiaIVOtherTissue:
    def __init__(self):
        self.conc_Tissue = None
        self.conc_Vein = None
        self.Uptake = None
        self.VascCond = None
        self.Mass = 0.0

    def VascCond_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.045], [1.0, 1.8], [0.0, 0.0])

    def CalcConc_func(self):
        self.conc_Tissue = self.Mass / OtherTissue_Size.Vol
        self.conc_Vein = self.conc_Tissue * AnesthesiaIVSolubility.GeneralK
        self.VascCond = self.VascCond_curve( self.conc_Tissue )

    def Dervs_func(self):
        self.Uptake = ( AnesthesiaIVBlood.conc_Blood - self.conc_Vein ) * OtherTissue_Flow.BloodFlow
        self.Change = self.Uptake
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 2.4)


class Autopsy:
    def __init__(self):
        self.StillAlive = True
        self.IsDead = False
        self.LungDisease = False
        self.PulmonaryEdema = False
        self.CardiacTamponade = False
        self.NephronLoss = False
        self.RightHeartInfarction = False
        self.RightHeartHypertrophy = False
        self.LeftHeartInfarction = False
        self.LeftHeartHypertrophy = False
        self.PulmonicValveStenosis = False
        self.PulmonicValveRegurgitation = False
        self.AorticValveStenosis = False
        self.AorticValveRegurgitation = False
        self.TricuspidValveStenosis = False
        self.TricuspidValveRegurgitation = False
        self.MitralValveStenosis = False
        self.MitralValveRegurgitation = False
        self.BloodLoss = False
        self.Anemia = False
        self.Polycythemia = False
        self.Dehydration = False
        self.PeripheralEdema = False
        self.Ascites = False
        self.VascularDamage = False
        self.AorticRupture = False
        self.VenaCavaRupture = False
        self.COPoisoning = False

    def Calc_func(self):
        if not Brain_Function.IsReallyDead:
            pass
        else:
            self.StillAlive = False
            self.IsDead = True
            if ExcessLungWater.Volume > 200.0:
                self.PulmonaryEdema = True
            else:
                pass
            if Pericardium_Cavity.Vol > 100.0:
                self.CardiacTamponade = True
            else:
                pass
            if Kidney_NephronCount.Total_xNormal < 0.40:
                self.NephronLoss = True
            else:
                pass
            if RightHeart_Infarction.Areapercent > 15.0:
                self.RightHeartInfarction = True
            else:
                pass
            if LeftHeart_Infarction.Areapercent > 15.0:
                self.LeftHeartInfarction = True
            else:
                pass
            if ( BloodVol.Vol / BloodVol.InitialVol ) < 0.85:
                self.BloodLoss = True
            else:
                pass
            if BloodVol.Hct < 0.34:
                self.Anemia = True
            else:
                pass
            if BloodVol.Hct > 0.55:
                self.Polycythemia = True
            else:
                pass
            if ( ECFV.Vol / ECFV.InitialVol ) < 0.90:
                self.Dehydration = True
            else:
                pass
            if ( ECFV.Vol / ECFV.InitialVol ) > 1.20:
                self.PeripheralEdema = True
            else:
                pass
            if PeritoneumSpace.Volume > 100.0:
                self.Ascites = True
            else:
                pass
            if HgbConc.CarboxyPercent > 25.0:
                self.COPoisoning = True
            else:
                pass

class Orthostatics:
    def __init__(self):
        pass
    
class RegionalPressure:
    def __init__(self):
        self.Alpha = 0.1667
        self.Brain = None
        self.Carotid = None
        self.UpperArty = None
        self.UpperCapy = None
        self.UpperVein = None
        self.MiddleArty = None
        self.MiddleCapy = None
        self.MiddleVein = None
        self.LowerArty = None
        self.LowerCapy = None
        self.LowerVein = None

    def Calc_func(self):
        self.Brain = ( max( ( SystemicArtys.Pressure + Hydrostatics.BrainGradient ), 0.0) )
        self.Carotid = ( max( ( SystemicArtys.Pressure + Hydrostatics.CarotidGradient ), 0.0) )
        self.UpperArty = ( max( ( SystemicArtys.Pressure + Hydrostatics.UpperTorsoGradient ), 0.0) )
        self.MiddleArty = ( max( ( SystemicArtys.Pressure + Hydrostatics.MiddleTorsoGradient ), 0.0) )
        self.LowerArty = ( max( ( SystemicArtys.Pressure + Hydrostatics.LowerTorsoArtyGradient ), 0.0) )
        self.UpperVein = ( max( ( RightAtrium.Pressure + Hydrostatics.UpperTorsoGradient ), 0.0) )
        self.MiddleVein = ( max( ( RightAtrium.Pressure + Hydrostatics.MiddleTorsoGradient ), 0.0) )
        self.LowerVein = ( max( ( RightAtrium.Pressure + ( Hydrostatics.LowerTorsoVeinGradient * LegMusclePump.Effect ) ), 0.0) )
        self.UpperCapy = ( max( ( ( self.Alpha * self.UpperArty ) + ( ( 1.0 - self.Alpha ) * self.UpperVein ) ), 0.0) )
        self.MiddleCapy = ( max( ( ( self.Alpha * self.MiddleArty ) + ( ( 1.0 - self.Alpha ) * self.MiddleVein ) ), 0.0) )
        self.LowerCapy = ( max( ( ( self.Alpha * self.LowerArty ) + ( ( 1.0 - self.Alpha ) * self.LowerVein ) ), 0.0) )

class Hydrostatics:
    def __init__(self):
        self.BrainCM = -18.0
        self.CarotidCM = -15.0
        self.UpperTorsoCM = -10.0
        self.MiddleTorsoCM = 4.0
        self.LowerTorsoCM = 50.0
        self.BrainGradient = None
        self.CarotidGradient = None
        self.UpperTorsoGradient = None
        self.MiddleTorsoGradient = None
        self.LowerTorsoArtyGradient = None
        self.LowerTorsoVeinGradient = None
        self.FractGz = None
        self.LegArtyFractGz = None
        self.LegVeinFractGz = None

    def Calc_func(self):
        if Status.Posture == PostureControl.LYING:
            self.FractGz = 0.0
            self.LegArtyFractGz = 0.0
            self.LegVeinFractGz = 0.2
        elif Status.Posture == PostureControl.SITTING:
            self.FractGz = 1.0
            self.LegArtyFractGz = 0.7
            self.LegVeinFractGz = 0.7
        elif Status.Posture == PostureControl.STANDING:
            self.FractGz = 1.0
            self.LegArtyFractGz = 1.0
            self.LegVeinFractGz = 1.0
        elif Status.Posture == PostureControl.TILTED:
            self.FractGz = ( math.sin ( math.radians ( TiltTable.Degrees ) ) )
            self.LegArtyFractGz = self.FractGz
            self.LegVeinFractGz = 0.2 + self.FractGz
        self.BrainGradient = self.BrainCM * Gravity.Gz * self.FractGz
        self.CarotidGradient = self.CarotidCM * Gravity.Gz * self.FractGz
        self.UpperTorsoGradient = self.UpperTorsoCM * Gravity.Gz * self.FractGz
        self.MiddleTorsoGradient = self.MiddleTorsoCM * Gravity.Gz * self.FractGz
        self.LowerTorsoArtyGradient = self.LowerTorsoCM * Gravity.Gz * self.LegArtyFractGz
        self.LowerTorsoVeinGradient = self.LowerTorsoCM * Gravity.Gz * self.LegVeinFractGz

class A_VFistula:
    def __init__(self):
        pass
    
class A_VFistula_Flow:
    def __init__(self):
        self.Conductance = None
        self.BasicConductance = 0.0
        self.BloodFlow = None
        self.PlasmaFlow = None

    def Calc_func(self):
        self.Conductance = self.BasicConductance * Viscosity.ConductanceEffect
        self.BloodFlow = ( max( ( A_VFistula_Pressure.PressureGradient * self.Conductance ), 0.0) )
        self.PlasmaFlow = self.BloodFlow * BloodVol.PVCrit

class A_VFistula_Pressure:
    def __init__(self):
        self.ArtyPressure = None
        self.VeinPressure = None
        self.PressureGradient = None

    def Calc_func(self):
        self.ArtyPressure = SystemicArtys.Pressure
        self.VeinPressure = SystemicVeins.Pressure
        self.PressureGradient = ( max( ( self.ArtyPressure - self.VeinPressure ), 0.0) )

class LH_AnteriorPituitary:
    def __init__(self):
        self.Secretion = None
        self.BasicSecretion = 0.6
        self.GnRHEffect = None
        self.InhibinEffect = None
        self.TestosteroneEffect = None
        self.Delay_Hrs = 24.0
        self.EstradiolEffectDelayed = 1.0

    def GnRHEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 80.0, 200.0], [2.0, 1.0, 0.2], [0.0, -0.01, 0.0])

    def EstradiolEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.4, 1.5, 2.0], [1.0, 0.5, 0.5, 20.0], [0.0, 0.0, 0.0, 0.0])

    def InhibinEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 7000.0], [1.0, 0.4], [0.0, 0.0])

    def TestosteroneEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 50.0], [0.999, 0.2], [0.0, 0.0])

    def Parms_func(self):
        self.K = ( 1 / ( 60.0 * self.Delay_Hrs ) )

    def Dervs_func(self):
        self.GnRHEffect = self.GnRHEffect_curve( GnRH.Period_Min )
        self.EstradiolEffect = self.EstradiolEffect_curve( Estradiol.conc_Conc_nMolperL )
        self.InhibinEffect = self.InhibinEffect_curve( Inhibin.conc_Conc_IUperL )
        self.TestosteroneEffect = self.TestosteroneEffect_curve( Testosterone.conc_Conc_nMolperL )
        self.Secretion = self.BasicSecretion * self.GnRHEffect * self.EstradiolEffectDelayed * self.InhibinEffect * self.TestosteroneEffect
        self.EstradiolEffectDelayed = delay( self.K, self.EstradiolEffect, self.EstradiolEffectDelayed, System.Dx, 0.01)


class LH:

    def Parms_func(self):
        LH_AnteriorPituitary.Parms_func()

    def Initialize_func(self):
        LH_Circulating.Initialize_func()

    def Conc_func(self):
        LH_Circulating.Conc_func()

    def Dervs_func(self):
        LH_AnteriorPituitary.Dervs_func()
        LH_Circulating.Dervs_func()

class LH_Circulating:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.Secretion = None
        self.Degradation = None
        self.TargetConcFemale = 13.0
        self.TargetConcMale = 7.0
        self.TargetConc = None
        self.InitialMass = None
        self.conc_Conc_IUperL = None
        self.PumpSwitch = False
        self.PumpSetting = 0.0
        self.K = 0.005

    def Init_func(self):
        if Gender.IsFemale:
            self.TargetConc = self.TargetConcFemale
        else:
            self.TargetConc = self.TargetConcMale

        self.InitialMass = self.TargetConc * ECFV.InitialVol_L
        self.Mass = self.InitialMass

    def Conc_func(self):
        self.conc_Conc_IUperL = self.Mass / ECFV.Vol_L

    def Dervs_func(self):
        self.Secretion = LH_AnteriorPituitary.Secretion
        self.Degradation = self.K * self.Mass
        self.Gain = self.Secretion + ( self.PumpSetting * self.PumpSwitch )
        self.Loss = self.Degradation
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 1.0)


class Fat_Flow:
    def __init__(self):
        self.Conductance = None
        self.BasicConductance = 2.7
        self.A2Effect = None
        self.SympsEffect = None
        self.ADHEffect = None
        self.PO2Effect = None
        self.AerobicFraction = None
        self.O2Use = None
        self.conc_O2 = None
        self.BloodFlow = None
        self.PlasmaFlow = None
        self.PO2 = 52.0
    def A2OnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.3, 3.5], [1.05, 1.0, 0.5], [0.0, -0.08, 0.0])

    def SympsOnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.0, 5.0], [1.3, 1.0, 0.1], [0.0, -0.3, 0.0])

    def PO2OnConductance_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 30.0], [2.0, 1.0], [0.0, 0.0])

    def ADHOnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.8, 3.0], [1.0, 0.1], [0.0, 0.0])

    def PO2OnAerobicFraction_curve(self, x):
        return cubic_hermite_spline(x, [2.0, 10.0], [0.0, 1.0], [0.0, 0.0])

    def Calc_func(self):
        self.A2Effect = self.A2OnConductance_curve( A2Pool.Log10Conc )
        self.SympsEffect = self.SympsOnConductance_curve( Fat_AlphaReceptors.Activity )
        self.ADHEffect = self.ADHOnConductance_curve( ADHPool.Log10Conc )
        self.SearchMax = PO2Artys.Pressure

        def PO2implicitfunc(PO2):
            self.PO2Effect = self.PO2OnConductance_curve( PO2 )
            self.Conductance = self.BasicConductance * self.A2Effect * self.SympsEffect * self.PO2Effect * self.ADHEffect * Viscosity.ConductanceEffect * Anesthesia.VascularConductance * Fat_Vasculature.Effect
            self.BloodFlow = ( max( ( Fat_Pressure.PressureGradient * self.Conductance ), 0.0) )
            self.AerobicFraction = self.PO2OnAerobicFraction_curve( PO2 )
            self.O2Use = Fat_Metabolism.O2Need * self.AerobicFraction
            if self.BloodFlow > 0.0:
                self.conc_O2 = O2Artys.conc_O2 - ( self.O2Use / self.BloodFlow )
            else:
                self.conc_O2 = 0.0

            HgbTissue.conc_O2 = self.conc_O2
            HgbTissue.O2ToPO2_func()
            PO2End = HgbTissue.pO2

            return PO2End
        self.PO2 = impliciteq( PO2implicitfunc, self.PO2, 0.52)
        self.PlasmaFlow = self.BloodFlow * BloodVol.PVCrit

class Fat_Ph:
    def __init__(self):
        self.Ph = None
        self.conc_SID = None
        self.conc_SID_mEqperL = None

    def CalcSID_func(self):
        self.conc_SID = KCell.conc_K_ + CellSID.OtherCations - CellSID.StrongAnions - Fat_Lactate.conc_Lac_
        self.conc_SID_mEqperL = 1000.0 * self.conc_SID

    def CalcPh_func(self):
        PhCells.pCO2 = Fat_CO2.PCO2
        PhCells.SID = self.conc_SID_mEqperL
        PhCells.Calc_func()
        self.Ph = PhCells.pH

class Fat_Function:
    def __init__(self):
        self.Failed = False
        self.Effect = None
        self.PhEffect = None
        self.ProteinEffect = None
        self.FuelEffect = None
        self.TemperatureEffect = None

    def PhOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [6.6, 6.7], [0.0, 1.0], [0.0, 0.0])

    def ProteinOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [3000.0, 5200.0], [0.0, 1.0], [0.0, 0.0])

    def FuelOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.9], [0.0, 1.0], [0.0, 0.0])

    def TemperatureOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 37.0, 40.0, 46.0], [0.0, 1.0, 1.5, 0.0], [0.0, 0.12, 0.0, 0.0])

    def Calc_func(self):
        self.PhEffect = self.PhOnFunction_curve( Fat_Ph.Ph )
        self.ProteinEffect = self.ProteinOnFunction_curve( CellProtein.Mass_G )
        self.FuelEffect = self.FuelOnFunction_curve( Fat_Fuel.FractUseDelay )
        self.TemperatureEffect = self.TemperatureOnFunction_curve( HeatCore.Temp_C )
        self.Effect = self.PhEffect * self.ProteinEffect * self.FuelEffect * self.TemperatureEffect * Fat_Structure.Effect

    def Wrapup_func(self):
        if not self.Failed and ( self.Effect < 0.2 ):
            self.Failed = True
        elif self.Failed and ( self.Effect > 0.4 ):
            self.Failed = False

class Fat_Lactate:
    def __init__(self):
        self.conc_Lac_ = None
        self.conc_Lac__mEqperL = None
        self.conc_Lac__mGperdL = None
        self.DC = 270.0
        self.Made = None
        self.Made_mGperMin = None
        self.Used = None
        self.Used_mGperMin = None
        self.Outflux = None
        self.Outflux_0 = None
        self.K = None
        self.Alpha = None
        self.MEQ_ML_TO_MG_DL = 9008.0
        self.GLUCOSE_TO_LACTATE = 0.99
        self.MG_TO_MEQ = 0.0112
        self.Mass = 2.49

    def CalcConc_func(self):
        self.conc_Lac_ = self.Mass / Fat_Size.LiquidVol
        self.conc_Lac__mEqperL = 1000.0 * self.conc_Lac_
        self.conc_Lac__mGperdL = self.MEQ_ML_TO_MG_DL * self.conc_Lac_

    def CalcDervs_func(self):
        self.Made_mGperMin = self.GLUCOSE_TO_LACTATE * Fat_Fuel.AnaerobicGlucoseUsed_mGperMin
        self.Made = self.MG_TO_MEQ * self.Made_mGperMin
        self.Used_mGperMin = Fat_Fuel.LacUsed_mGperMin
        self.Used = self.MG_TO_MEQ * self.Used_mGperMin
        self.K = self.DC / Fat_Size.LiquidVol
        if System.Dx >=0:
            self.Alpha = 0.0
        elif ( self.K * System.Dx ) >= 100.0:
            self.Alpha = 4E-44
        elif True:
            self.Alpha = ( math.e ** ( - self.K * System.Dx ) )
        self.Outflux_0 = self.DC * ( self.conc_Lac_ - LacPool.conc_Lac_ )
        self.Outflux = ( self.Alpha * self.Outflux_0 ) + ( ( 1 - self.Alpha ) * ( self.Made + self.Used ) )
        self.Change = self.Made - self.Used - self.Outflux
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.025)


class Fat_CO2:
    def __init__(self):
        self.conc_HCO3 = None
        self.conc_HCO3_mEqperL = None
        self.PCO2 = None
        self.InflowGas = None
        self.InflowBase = None
        self.OutflowBase = None
        self.conc_BloodHCO3 = None
        self.Outflow_0 = None
        self.K = None
        self.Alpha = None
        self.Mass = 39.8

    def CalcConc_func(self):
        self.conc_HCO3 = self.Mass / Fat_Size.LiquidVol
        self.conc_HCO3_mEqperL = 1000.0 * self.conc_HCO3
        Tissue_BaseToGas.conc_HCO3 = self.conc_HCO3
        Tissue_BaseToGas.conc_SID = Fat_Ph.conc_SID
        Tissue_BaseToGas.Calc_func()
        self.PCO2 = Tissue_BaseToGas.pCO2

    def CalcDervs_func(self):
        self.K = Fat_Flow.BloodFlow / Fat_Size.LiquidVol
        if System.Dx >=0:
            self.Alpha = 0.0
        elif ( self.K * System.Dx ) >= 100.0:
            self.Alpha = 4E-44
        elif True:
            self.Alpha = ( math.e ** ( - self.K * System.Dx ) )
        self.InflowGas = Metabolism_RespiratoryQuotient.RQ * Fat_Flow.O2Use
        self.InflowBase = CO2Tools.LitersToMols * self.InflowGas
        Blood_GasToBase.pCO2 = self.PCO2
        Blood_GasToBase.conc_SID = BloodIons.conc_SID
        Blood_GasToBase.Calc_func()
        self.conc_BloodHCO3 = Blood_GasToBase.conc_HCO3
        self.Outflow_0 = Fat_Flow.BloodFlow * ( self.conc_BloodHCO3 - CO2Artys.conc_HCO3 )
        self.OutflowBase = ( self.Alpha * self.Outflow_0 ) + ( ( 1 - self.Alpha ) * self.InflowBase )
        self.Change = self.InflowBase - self.OutflowBase
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.4)


class Fat_Pressure:
    def __init__(self):
        self.ArtyPressure = None
        self.VeinPressure = None
        self.PressureGradient = None
        self.PumpSwitch = False
        self.PumpSetting = 0.0

    def Calc_func(self):
        if self.PumpSwitch:
            self.ArtyPressure = self.PumpSetting
        else:
            self.ArtyPressure = SystemicArtys.Pressure

        self.VeinPressure = SystemicVeins.Pressure
        self.PressureGradient = ( max( ( self.ArtyPressure - self.VeinPressure ), 0.0) )

class Fat_Vasculature:
    def __init__(self):
        self.Tau = 30.0
        self.Effect = 1.0

    def PO2OnStimulus_curve(self, x):
        return cubic_hermite_spline(x, [41.0, 51.0, 61.0], [1.2, 1.0, 0.8], [0.0, -0.03, 0.0])

    def Parms_func(self):
        self.K = 1.0 / ( self.Tau * 1440.0 )

    def Calc_func(self):
        if Fat_Function.Failed:
            self.Stimulus = 0.0
        else:
            self.Stimulus = self.PO2OnStimulus_curve( Fat_Flow.PO2 )

        self.Effect = delay( self.K, self.Stimulus, self.Effect, System.Dx, None)


class Fat_AlphaReceptors:
    def __init__(self):
        self.Activity = None
        self.TotalAgonism = None
        self.NeuralAgonism = None
        self.HumoralAgonism = None
        self.Switch = False
        self.Setting = 0.0
        self.NEURALK = 0.333
        self.HUMORALK = 0.5

    def Calc_func(self):
        self.NeuralAgonism = GangliaGeneral.NA_Hz
        self.HumoralAgonism = AlphaPool.Effect
        self.TotalAgonism = ( self.NEURALK * self.NeuralAgonism ) + ( self.HUMORALK * self.HumoralAgonism )
        if self.Switch:
            self.Activity = self.Setting
        else:
            self.Activity = self.TotalAgonism * AlphaBlockade.Effect


class Fat:
    def __init__(self):
        pass
    
class Fat_Fuel:
    def __init__(self):
        self.FADelivered = None
        self.GlucoseDelivered = None
        self.KR = 0.026
        self.Ratio = None
        self.FAFraction = None
        self.GlucoseFraction = None
        self.FA_GlucoseFraction = None
        self.LacFraction = None
        self.FAUsed_CalperMin = None
        self.AerobicGlucoseUsed_CalperMin = None
        self.AnaerobicGlucoseUsed_CalperMin = None
        self.LacUsed_CalperMin = None
        self.FAUsed_mGperMin = None
        self.AerobicGlucoseUsed_mGperMin = None
        self.AnaerobicGlucoseUsed_mGperMin = None
        self.LacUsed_mGperMin = None
        self.TotalGlucoseUsed_mGperMin = None
        self.AnaerobicGlucoseDelivered = None
        self.FAFractionalDelivery = None
        self.AerobicGlucoseFractionalDelivery = None
        self.AnaerobicGlucoseFractionalDelivery = None
        self.MinimumFractionalDelivery = None
        self.FractUseDelay = 1.0

    def LacFraction_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 100.0], [0.0, 0.3], [0.0, 0.0])

    def Dervs_func(self):
        self.FADelivered = ( max( ( FAPool.conc_FA * Fat_Flow.PlasmaFlow ), 0.0) )
        self.GlucoseDelivered = ( max( ( GlucosePool.conc_Glucose * Fat_Flow.PlasmaFlow ), 0.0) )
        self.LacFraction = self.LacFraction_curve( Fat_Lactate.conc_Lac__mGperdL )
        self.FA_GlucoseFraction = 1.0 - self.LacFraction
        self.Ratio = FAPool.conc_FA_mGperdL / GlucosePool.conc_Glucose_mGperdL
        self.FAFraction = self.FA_GlucoseFraction * ( self.Ratio / ( self.Ratio + self.KR ) )
        self.GlucoseFraction = self.FA_GlucoseFraction - self.FAFraction
        self.FAUsed_CalperMin = self.FAFraction * Fat_Metabolism.AerobicCals
        self.FAUsed_mGperMin = self.FAUsed_CalperMin * Metabolism_Tools.Fat_mGperCal
        self.AerobicGlucoseUsed_CalperMin = self.GlucoseFraction * Fat_Metabolism.AerobicCals
        self.AerobicGlucoseUsed_mGperMin = self.AerobicGlucoseUsed_CalperMin * Metabolism_Tools.CarboAerobic_mGperCal
        self.LacUsed_CalperMin = self.LacFraction * Fat_Metabolism.AerobicCals
        self.LacUsed_mGperMin = self.LacUsed_CalperMin * Metabolism_Tools.Lac__mGperCal
        self.AnaerobicGlucoseDelivered = self.GlucoseDelivered - self.AerobicGlucoseUsed_mGperMin
        self.AnaerobicGlucoseUsed_CalperMin = ( min( Fat_Metabolism.AnaerobicCals, self.AnaerobicGlucoseDelivered) )
        self.AnaerobicGlucoseUsed_mGperMin = self.AnaerobicGlucoseUsed_CalperMin * Metabolism_Tools.CarboAnaerobic_mGperCal
        self.TotalGlucoseUsed_mGperMin = self.AerobicGlucoseUsed_mGperMin + self.AnaerobicGlucoseUsed_mGperMin
        if self.FAUsed_mGperMin > 0.0:
            self.FAFractionalDelivery = ( min( ( self.FADelivered / self.FAUsed_mGperMin ), 1.0) )
        else:
            self.FAFractionalDelivery = 1.0

        if self.AerobicGlucoseUsed_mGperMin > 0.0:
            self.AerobicGlucoseFractionalDelivery = ( min( ( self.GlucoseDelivered / self.AerobicGlucoseUsed_mGperMin ), 1.0) )
        else:
            self.AerobicGlucoseFractionalDelivery = 1.0

        if self.AnaerobicGlucoseUsed_mGperMin > 0.0:
            self.AnaerobicGlucoseFractionalDelivery = ( min( ( self.AnaerobicGlucoseDelivered / self.AnaerobicGlucoseUsed_mGperMin ), 1.0) )
        else:
            self.AnaerobicGlucoseFractionalDelivery = 1.0

        self.MinimumFractionalDelivery = ( min( ( min( self.FAFractionalDelivery, self.AerobicGlucoseFractionalDelivery) ), self.AnaerobicGlucoseFractionalDelivery) )
        self.K = 0.5
        self.DxMax = 1.0
        self.FractUse = self.MinimumFractionalDelivery
        self.FractUseDelay = delay( self.K, self.FractUse, self.FractUseDelay, System.Dx, 0.01)


class Fat_Structure:
    def __init__(self):
        self.PhEffect = None
        self.FuelEffect = None
        self.TemperatureEffect = None
        self.Effect = 1.0

    def PhOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [6.5, 6.6], [0.1, 0.0], [0.0, 0.0])

    def FuelOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [0.5, 0.8], [0.05, 0.0], [0.0, 0.0])

    def TemperatureOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [44.0, 46.0], [0.0, 0.05], [0.0, 0.0])

    def Calc_func(self):
        self.PhEffect = self.PhOnStructure_curve( Fat_Ph.Ph )
        self.FuelEffect = self.FuelOnStructure_curve( Fat_Fuel.FractUseDelay )
        self.TemperatureEffect = self.TemperatureOnStructure_curve( HeatCore.Temp_C )
        self.F1 = 0.0
        self.F2 = self.PhEffect + self.TemperatureEffect + self.FuelEffect
        self.Effect = backwardeuler( self.F1, self.F2, System.Dx, self.Effect, None)


class Fat_Metabolism:
    def __init__(self):
        self.TotalCalsUsed = None
        self.NormalCalsUsed = None
        self.InitialNormalCalsUsed = None
        self.NormalCalsUsed__CalperMinperG = 0.0018
        self.CalMultiplier = 1.0
        self.AerobicCals = None
        self.AnaerobicCals = None
        self.O2Need = None
        self.O2Lack = None

    def ScaleCals_func(self):
        self.InitialNormalCalsUsed = self.CalMultiplier * self.NormalCalsUsed__CalperMinperG * Fat_Size.InitialMass

    def CalcCals_func(self):
        self.NormalCalsUsed = self.CalMultiplier * self.NormalCalsUsed__CalperMinperG * Fat_Size.Mass
        self.TotalCalsUsed = self.NormalCalsUsed * Thyroid.Effect * HeatMetabolism.Core * Fat_Structure.Effect
        self.O2Need = Metabolism_Tools.CalToO2 * self.TotalCalsUsed

    def SplitCals_func(self):
        self.O2Lack = self.O2Need - Fat_Flow.O2Use
        self.AerobicCals = Metabolism_Tools.O2ToCal * Fat_Flow.O2Use
        self.AnaerobicCals = Metabolism_Tools.O2ToCal * self.O2Lack

class Fat_Size:
    def __init__(self):
        self.Vol = None
        self.Mass = None
        self.Mass_kG = None
        self.InitialMass = None
        self.InitialMass_kG = None
        self.Density = None
        self.LiquidMass = None
        self.LiquidDensity = 1.00
        self.LiquidVol = None
        self.InitialLiquidVol = None
        self.SolidMass = None
        self.InitialSolidMass = None
        self.LipidMass = None
        self.InitialLipidMass = None
        self.LipidDensity = 0.905
        self.OtherMass = None
        self.InitialOtherMass = None
        self.OtherDensity = 1.38
        self.LipidVol = None
        self.OtherVol = None
        self.SolidVol = None
        self.FractTotal = None
        self.IFV = None
        self.InitialIFV = None
        self.CellH2O = None
        self.InitialCellH2O = None
        self.H2OFractMass = 0.15
        self.SolidsFractMass = None
        self.OtherFractSolids = 0.11
        self.LipidsFractSolids = None

    def InitializeFatMass_func(self):
        self.InitialMass_kG = Values_Adiposity.Mass_kG

    def Initialize_func(self):
        self.InitialMass = 1000.0 * self.InitialMass_kG
        self.InitialLiquidVol = self.H2OFractMass * self.InitialMass / self.LiquidDensity
        self.SolidsFractMass = 1.0 - self.H2OFractMass
        self.InitialSolidMass = self.SolidsFractMass * self.InitialMass
        self.InitialOtherMass = self.OtherFractSolids * self.InitialSolidMass
        self.LipidsFractSolids = 1.0 - self.OtherFractSolids
        self.InitialLipidMass = self.LipidsFractSolids * self.InitialSolidMass

    def ScaleH2O_func(self):
        self.FractTotal = self.InitialLiquidVol / TissueH2O.InitialVol
        self.InitialIFV = self.FractTotal * InterstitialWater.InitialVol
        self.InitialCellH2O = self.FractTotal * CellH2O.InitialVol

    def Calc_func(self):
        self.IFV = self.FractTotal * InterstitialWater.Vol
        self.CellH2O = self.FractTotal * CellH2O.Vol
        self.LiquidVol = self.IFV + self.CellH2O
        self.LiquidMass = self.LiquidVol * self.LiquidDensity
        self.LipidMass = LipidDeposits.Mass
        self.OtherMass = self.InitialOtherMass
        self.SolidMass = self.LipidMass + self.OtherMass
        self.LipidVol = self.LipidMass / self.LipidDensity
        self.OtherVol = self.OtherMass / self.OtherDensity
        self.SolidVol = self.LipidVol + self.OtherVol
        self.Mass = self.LiquidMass + self.SolidMass
        self.Mass_kG = self.Mass / 1000.0
        self.Vol = self.LiquidVol + self.SolidVol
        self.Density = self.Mass / self.Vol

class Liver:
    def __init__(self):
        pass
    
class Liver_Metabolism:
    def __init__(self):
        self.TotalCalsUsed = None
        self.NormalCalsUsed = None
        self.InitialNormalCalsUsed = None
        self.NormalCalsUsed__CalperMinperG = 0.0940
        self.CalMultiplier = 1.0
        self.AerobicCals = None
        self.AnaerobicCals = None
        self.O2Need = None
        self.O2Lack = None

    def ScaleCals_func(self):
        self.InitialNormalCalsUsed = self.CalMultiplier * self.NormalCalsUsed__CalperMinperG * Liver_Size.InitialMass

    def CalcCals_func(self):
        self.NormalCalsUsed = self.CalMultiplier * self.NormalCalsUsed__CalperMinperG * Liver_Size.Mass
        self.TotalCalsUsed = self.NormalCalsUsed * Thyroid.Effect * HeatMetabolism.Core * Liver_Structure.Effect
        self.O2Need = Metabolism_Tools.CalToO2 * self.TotalCalsUsed

    def SplitCals_func(self):
        self.O2Lack = self.O2Need - Liver_O2.O2Use
        self.AerobicCals = Metabolism_Tools.O2ToCal * Liver_O2.O2Use
        self.AnaerobicCals = Metabolism_Tools.O2ToCal * self.O2Lack

class Liver_Ph:
    def __init__(self):
        self.Ph = None
        self.conc_SID = None
        self.conc_SID_mEqperL = None

    def CalcSID_func(self):
        self.conc_SID = KCell.conc_K_ + CellSID.OtherCations - CellSID.StrongAnions - Liver_Lactate.conc_Lac_
        self.conc_SID_mEqperL = 1000.0 * self.conc_SID

    def CalcPh_func(self):
        PhCells.pCO2 = Liver_CO2.PCO2
        PhCells.SID = self.conc_SID_mEqperL
        PhCells.Calc_func()
        self.Ph = PhCells.pH

class Liver_CO2:
    def __init__(self):
        self.conc_HCO3 = None
        self.conc_HCO3_mEqperL = None
        self.PCO2 = None
        self.InflowGas = None
        self.InflowBase = None
        self.OutflowBase = None
        self.conc_BloodHCO3 = None
        self.Outflow_0 = None
        self.K = None
        self.Alpha = None
        self.Mass = 22.8

    def CalcConc_func(self):
        self.conc_HCO3 = self.Mass / Liver_Size.LiquidVol
        self.conc_HCO3_mEqperL = 1000.0 * self.conc_HCO3
        Tissue_BaseToGas.conc_HCO3 = self.conc_HCO3
        Tissue_BaseToGas.conc_SID = Liver_Ph.conc_SID
        Tissue_BaseToGas.Calc_func()
        self.PCO2 = Tissue_BaseToGas.pCO2

    def CalcDervs_func(self):
        self.K = OrganFlow.HepaticVeinFlow / Liver_Size.LiquidVol
        if System.Dx >=0:
            self.Alpha = 0.0
        elif ( self.K * System.Dx ) >= 100.0:
            self.Alpha = 4E-44
        elif True:
            self.Alpha = ( math.e ** ( - self.K * System.Dx ) )
        self.InflowGas = Metabolism_RespiratoryQuotient.RQ * Liver_O2.O2Use
        self.InflowBase = CO2Tools.LitersToMols * self.InflowGas
        Blood_GasToBase.pCO2 = self.PCO2
        Blood_GasToBase.conc_SID = BloodIons.conc_SID
        Blood_GasToBase.Calc_func()
        self.conc_BloodHCO3 = Blood_GasToBase.conc_HCO3
        self.Outflow_0 = ( GITract_Flow.BloodFlow * ( self.conc_BloodHCO3 - CO2Artys.conc_HCO3 ) ) + ( HepaticArty.Flow * ( self.conc_BloodHCO3 - GITract_CO2.conc_HCO3 ) )
        self.OutflowBase = ( self.Alpha * self.Outflow_0 ) + ( ( 1 - self.Alpha ) * self.InflowBase )
        self.Change = self.InflowBase - self.OutflowBase
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.23)


class Liver_AlphaReceptors:
    def __init__(self):
        self.Activity = None
        self.TotalAgonism = None
        self.NeuralAgonism = None
        self.HumoralAgonism = None
        self.Switch = False
        self.Setting = 0.0
        self.NEURALK = 0.333
        self.HUMORALK = 0.5

    def Calc_func(self):
        self.NeuralAgonism = GangliaGeneral.NA_Hz
        self.HumoralAgonism = AlphaPool.Effect
        self.TotalAgonism = ( self.NEURALK * self.NeuralAgonism ) + ( self.HUMORALK * self.HumoralAgonism )
        if self.Switch:
            self.Activity = self.Setting
        else:
            self.Activity = self.TotalAgonism * AlphaBlockade.Effect


class Liver_Structure:
    def __init__(self):
        self.PhEffect = None
        self.FuelEffect = None
        self.TemperatureEffect = None
        self.Effect = 1.0

    def PhOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [6.5, 6.6], [0.1, 0.0], [0.0, 0.0])

    def FuelOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [0.5, 0.8], [0.05, 0.0], [0.0, 0.0])

    def TemperatureOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [44.0, 46.0], [0.0, 0.05], [0.0, 0.0])

    def Calc_func(self):
        self.PhEffect = self.PhOnStructure_curve( Liver_Ph.Ph )
        self.FuelEffect = self.FuelOnStructure_curve( Liver_Fuel.FractUseDelay )
        self.TemperatureEffect = self.TemperatureOnStructure_curve( HeatCore.Temp_C )
        self.F1 = 0.0
        self.F2 = self.PhEffect + self.TemperatureEffect + self.FuelEffect
        self.Effect = backwardeuler( self.F1, self.F2, System.Dx, self.Effect, None)


class Liver_Size:
    def __init__(self):
        self.Vol = None
        self.Mass = None
        self.InitialMass = None
        self.Density = None
        self.LiquidMass = None
        self.LiquidDensity = 1.00
        self.LiquidVol = None
        self.InitialLiquidVol = None
        self.SolidMass = None
        self.InitialSolidMass = None
        self.SolidDensity = 1.17
        self.SolidVol = None
        self.FractTotal = None
        self.IFV = None
        self.InitialIFV = None
        self.CellH2O = None
        self.InitialCellH2O = None
        self.MassFractBase = 0.0701
        self.H2OFractMass = 0.67
        self.SolidsFractMass = None

    def Initialize_func(self):
        self.InitialMass = self.MassFractBase * Weight.InitialOtherMass
        self.InitialLiquidVol = self.H2OFractMass * self.InitialMass / self.LiquidDensity
        self.SolidsFractMass = 1.0 - self.H2OFractMass
        self.InitialSolidMass = self.SolidsFractMass * self.InitialMass

    def ScaleH2O_func(self):
        self.FractTotal = self.InitialLiquidVol / TissueH2O.InitialVol
        self.InitialIFV = self.FractTotal * InterstitialWater.InitialVol
        self.InitialCellH2O = self.FractTotal * CellH2O.InitialVol

    def Calc_func(self):
        self.IFV = self.FractTotal * InterstitialWater.Vol
        self.CellH2O = self.FractTotal * CellH2O.Vol
        self.LiquidVol = self.IFV + self.CellH2O
        self.LiquidMass = self.LiquidVol * self.LiquidDensity
        self.SolidMass = self.InitialSolidMass
        self.SolidVol = self.SolidMass / self.SolidDensity
        self.Mass = self.LiquidMass + self.SolidMass
        self.Vol = self.LiquidVol + self.SolidVol
        self.Density = self.Mass / self.Vol

class Liver_O2:
    def __init__(self):
        self.Inflowconc_O2 = None
        self.InflowPO2 = None
        self.AerobicFraction = None
        self.O2Use = None
        self.conc_O2 = None
        self.BloodFlow = None
        self.PO2 = 36.5
    def PO2OnAerobicFraction_curve(self, x):
        return cubic_hermite_spline(x, [2.0, 10.0], [0.0, 1.0], [0.0, 0.0])

    def Calc_func(self):
        self.BloodFlow = GITract_Flow.BloodFlow + HepaticArty.Flow
        self.Inflowconc_O2 = ( ( GITract_Flow.conc_O2 * GITract_Flow.BloodFlow ) + ( O2Artys.conc_O2 * HepaticArty.Flow ) ) / self.BloodFlow
        HgbTissue.conc_O2 = self.Inflowconc_O2
        HgbTissue.O2ToPO2_func()
        self.InflowPO2 = HgbTissue.pO2
        self.SearchMax = self.InflowPO2

        def PO2implicitfunc(PO2):
            self.AerobicFraction = self.PO2OnAerobicFraction_curve( PO2 )
            self.O2Use = Liver_Metabolism.O2Need * self.AerobicFraction
            if self.BloodFlow > 0.0:
                self.conc_O2 = self.Inflowconc_O2 - ( self.O2Use / self.BloodFlow )
            else:
                self.conc_O2 = 0.0

            HgbTissue.conc_O2 = self.conc_O2
            HgbTissue.O2ToPO2_func()
            PO2End = HgbTissue.pO2

            return PO2End
        self.PO2 = impliciteq( PO2implicitfunc, self.PO2, 0.36)

class Liver_Function:
    def __init__(self):
        self.Failed = False
        self.Effect = None
        self.PhEffect = None
        self.ProteinEffect = None
        self.FuelEffect = None
        self.TemperatureEffect = None

    def PhOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [6.6, 6.7], [0.0, 1.0], [0.0, 0.0])

    def ProteinOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [3000.0, 5200.0], [0.0, 1.0], [0.0, 0.0])

    def FuelOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.9], [0.0, 1.0], [0.0, 0.0])

    def TemperatureOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 37.0, 40.0, 46.0], [0.0, 1.0, 1.5, 0.0], [0.0, 0.12, 0.0, 0.0])

    def Calc_func(self):
        self.PhEffect = self.PhOnFunction_curve( Liver_Ph.Ph )
        self.ProteinEffect = self.ProteinOnFunction_curve( CellProtein.Mass_G )
        self.FuelEffect = self.FuelOnFunction_curve( Liver_Fuel.FractUseDelay )
        self.TemperatureEffect = self.TemperatureOnFunction_curve( HeatCore.Temp_C )
        self.Effect = self.PhEffect * self.ProteinEffect * self.FuelEffect * self.TemperatureEffect * Liver_Structure.Effect

    def Wrapup_func(self):
        if not self.Failed and ( self.Effect < 0.2 ):
            self.Failed = True
        elif self.Failed and ( self.Effect > 0.4 ):
            self.Failed = False

class Liver_Lactate:
    def __init__(self):
        self.conc_Lac_ = None
        self.conc_Lac__mEqperL = None
        self.conc_Lac__mGperdL = None
        self.DC = 100.0
        self.Made = None
        self.Made_mGperMin = None
        self.Used = None
        self.Used_mGperMin = None
        self.Outflux = None
        self.Outflux_0 = None
        self.K = None
        self.Alpha = None
        self.MEQ_ML_TO_MG_DL = 9008.0
        self.GLUCOSE_TO_LACTATE = 0.99
        self.MG_TO_MEQ = 0.0112
        self.Mass = 1.43

    def CalcConc_func(self):
        self.conc_Lac_ = self.Mass / Liver_Size.LiquidVol
        self.conc_Lac__mEqperL = 1000.0 * self.conc_Lac_
        self.conc_Lac__mGperdL = self.MEQ_ML_TO_MG_DL * self.conc_Lac_

    def CalcDervs_func(self):
        self.Made_mGperMin = self.GLUCOSE_TO_LACTATE * Liver_Fuel.AnaerobicGlucoseUsed_mGperMin
        self.Made = self.MG_TO_MEQ * self.Made_mGperMin
        self.Used_mGperMin = Liver_Fuel.LacUsed_mGperMin
        self.Used = self.MG_TO_MEQ * self.Used_mGperMin
        self.K = self.DC / Liver_Size.LiquidVol
        if System.Dx >=0:
            self.Alpha = 0.0
        elif ( self.K * System.Dx ) >= 100.0:
            self.Alpha = 4E-44
        elif True:
            self.Alpha = ( math.e ** ( - self.K * System.Dx ) )
        self.Outflux_0 = self.DC * ( self.conc_Lac_ - LacPool.conc_Lac_ )
        self.Outflux = ( self.Alpha * self.Outflux_0 ) + ( ( 1 - self.Alpha ) * ( self.Made + self.Used ) )
        self.Change = self.Made - self.Used - self.Outflux
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.014)


class Liver_Fuel:
    def __init__(self):
        self.FADelivered = None
        self.GlucoseDelivered = None
        self.KR = 0.026
        self.Ratio = None
        self.FAFraction = None
        self.GlucoseFraction = None
        self.FA_GlucoseFraction = None
        self.LacFraction = None
        self.FAUsed_CalperMin = None
        self.AerobicGlucoseUsed_CalperMin = None
        self.AnaerobicGlucoseUsed_CalperMin = None
        self.LacUsed_CalperMin = None
        self.FAUsed_mGperMin = None
        self.AerobicGlucoseUsed_mGperMin = None
        self.AnaerobicGlucoseUsed_mGperMin = None
        self.LacUsed_mGperMin = None
        self.TotalGlucoseUsed_mGperMin = None
        self.AnaerobicGlucoseDelivered = None
        self.FAFractionalDelivery = None
        self.AerobicGlucoseFractionalDelivery = None
        self.AnaerobicGlucoseFractionalDelivery = None
        self.MinimumFractionalDelivery = None
        self.FractUseDelay = 1.0

    def LacFraction_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 100.0], [0.0, 0.3], [0.0, 0.0])

    def Dervs_func(self):
        self.FADelivered = ( max( ( PortalVein_FattyAcid.conc_FattyAcid * PortalVein.PlasmaFlow ), 0.0) )
        self.GlucoseDelivered = ( max( ( PortalVein_Glucose.conc_Glucose * PortalVein.PlasmaFlow ), 0.0) )
        self.LacFraction = self.LacFraction_curve( Liver_Lactate.conc_Lac__mGperdL )
        self.FA_GlucoseFraction = 1.0 - self.LacFraction
        self.Ratio = PortalVein_FattyAcid.conc_FattyAcid / PortalVein_Glucose.conc_Glucose
        self.FAFraction = self.FA_GlucoseFraction * ( self.Ratio / ( self.Ratio + self.KR ) )
        self.GlucoseFraction = self.FA_GlucoseFraction - self.FAFraction
        self.FAUsed_CalperMin = self.FAFraction * Liver_Metabolism.AerobicCals
        self.FAUsed_mGperMin = self.FAUsed_CalperMin * Metabolism_Tools.Fat_mGperCal
        self.AerobicGlucoseUsed_CalperMin = self.GlucoseFraction * Liver_Metabolism.AerobicCals
        self.AerobicGlucoseUsed_mGperMin = self.AerobicGlucoseUsed_CalperMin * Metabolism_Tools.CarboAerobic_mGperCal
        self.LacUsed_CalperMin = self.LacFraction * Liver_Metabolism.AerobicCals
        self.LacUsed_mGperMin = self.LacUsed_CalperMin * Metabolism_Tools.Lac__mGperCal
        self.AnaerobicGlucoseDelivered = self.GlucoseDelivered - self.AerobicGlucoseUsed_mGperMin
        self.AnaerobicGlucoseUsed_CalperMin = ( min( Liver_Metabolism.AnaerobicCals, self.AnaerobicGlucoseDelivered) )
        self.AnaerobicGlucoseUsed_mGperMin = self.AnaerobicGlucoseUsed_CalperMin * Metabolism_Tools.CarboAnaerobic_mGperCal
        self.TotalGlucoseUsed_mGperMin = self.AerobicGlucoseUsed_mGperMin + self.AnaerobicGlucoseUsed_mGperMin
        if self.FAUsed_mGperMin > 0.0:
            self.FAFractionalDelivery = ( min( ( self.FADelivered / self.FAUsed_mGperMin ), 1.0) )
        else:
            self.FAFractionalDelivery = 1.0

        if self.AerobicGlucoseUsed_mGperMin > 0.0:
            self.AerobicGlucoseFractionalDelivery = ( min( ( self.GlucoseDelivered / self.AerobicGlucoseUsed_mGperMin ), 1.0) )
        else:
            self.AerobicGlucoseFractionalDelivery = 1.0

        if self.AnaerobicGlucoseUsed_mGperMin > 0.0:
            self.AnaerobicGlucoseFractionalDelivery = ( min( ( self.AnaerobicGlucoseDelivered / self.AnaerobicGlucoseUsed_mGperMin ), 1.0) )
        else:
            self.AnaerobicGlucoseFractionalDelivery = 1.0

        self.MinimumFractionalDelivery = ( min( ( min( self.FAFractionalDelivery, self.AerobicGlucoseFractionalDelivery) ), self.AnaerobicGlucoseFractionalDelivery) )
        self.K = 0.5
        self.DxMax = 1.0
        self.FractUse = self.MinimumFractionalDelivery
        self.FractUseDelay = delay( self.K, self.FractUse, self.FractUseDelay, System.Dx, 0.01)


class KAPump:
    def __init__(self):
        self.Rate = None
        self.Switch = False
        self.Setting = 0.0

    def Parms_func(self):
        if self.Switch:
            self.Rate = self.Setting
        else:
            self.Rate = 0.0


class Ketoacid:
    def __init__(self):
        pass
    
class KAPool:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.conc_KA = None
        self.conc_KA_mGperdL = None
        self.conc_KA_mMolperL = None
        self.Osmoles = None
        self.MG_TO_MOSM = 0.0098
        self.PER_ML_TO_PER_DL = 100.0
        self.MG_TO_MMOL = 9.80
        self.Targetconc_KA = 0.0050
        self.InitialMass = None

    def CalcOsmoles_func(self):
        self.Osmoles = self.MG_TO_MOSM * self.Mass

    def Init_func(self):
        self.InitialMass = self.Targetconc_KA * ECFV.Vol
        self.Mass = self.InitialMass

    def CalcConc_func(self):
        self.conc_KA = self.Mass / ECFV.Vol
        self.conc_KA_mGperdL = self.PER_ML_TO_PER_DL * self.conc_KA
        self.conc_KA_mMolperL = self.MG_TO_MMOL * self.conc_KA

    def CalcDervs_func(self):
        self.Gain = LM_Ketoacids.Rate + KAPump.Rate
        self.Loss = Brain_Fuel.KAUsed_mGperMin + NephronKetoacids.Excretion + KADecomposition.Rate
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.0075)


class KADecomposition:
    def __init__(self):
        self.Rate = None
        self.K = 0.0007

    def Dervs_func(self):
        self.Rate = self.K * KAPool.Mass

class RespiratoryMuscle_Function:
    def __init__(self):
        self.Failed = False
        self.Effect = None
        self.PhEffect = None
        self.ProteinEffect = None
        self.FuelEffect = None
        self.TemperatureEffect = None

    def PhOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [6.6, 6.7], [0.0, 1.0], [0.0, 0.0])

    def ProteinOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [3000.0, 5200.0], [0.0, 1.0], [0.0, 0.0])

    def FuelOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.9], [0.0, 1.0], [0.0, 0.0])

    def TemperatureOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 37.0, 40.0, 46.0], [0.0, 1.0, 1.5, 0.0], [0.0, 0.12, 0.0, 0.0])

    def Calc_func(self):
        self.PhEffect = self.PhOnFunction_curve( RespiratoryMuscle_Ph.Ph )
        self.ProteinEffect = self.ProteinOnFunction_curve( CellProtein.Mass_G )
        self.FuelEffect = self.FuelOnFunction_curve( RespiratoryMuscle_Fuel.FractUseDelay )
        self.TemperatureEffect = self.TemperatureOnFunction_curve( HeatCore.Temp_C )
        self.Effect = self.PhEffect * self.ProteinEffect * self.FuelEffect * self.TemperatureEffect * RespiratoryMuscle_Structure.Effect

    def Wrapup_func(self):
        if not self.Failed and ( self.Effect < 0.2 ):
            self.Failed = True
        elif self.Failed and ( self.Effect > 0.4 ):
            self.Failed = False

class RespiratoryMuscle_Size:
    def __init__(self):
        self.Vol = None
        self.Mass = None
        self.InitialMass = None
        self.Density = None
        self.LiquidMass = None
        self.LiquidDensity = 1.00
        self.LiquidVol = None
        self.InitialLiquidVol = None
        self.SolidMass = None
        self.InitialSolidMass = None
        self.ContractileProteinMass = None
        self.InitialProteinMass = None
        self.ContractileProteinDensity = 1.17
        self.OtherMass = None
        self.InitialOtherMass = None
        self.OtherDensity = 1.17
        self.ContractileProteinVol = None
        self.OtherVol = None
        self.SolidVol = None
        self.FractTotal = None
        self.IFV = None
        self.InitialIFV = None
        self.CellH2O = None
        self.InitialCellH2O = None
        self.MassFractBase = 0.140
        self.H2OFractMass = 0.79
        self.SolidsFractMass = None
        self.OtherFractSolids = 0.50
        self.ProteinFractSolids = None

    def Initialize_func(self):
        self.InitialMass = self.MassFractBase * Weight.InitialOtherMass
        self.InitialLiquidVol = self.H2OFractMass * self.InitialMass / self.LiquidDensity
        self.SolidsFractMass = 1.0 - self.H2OFractMass
        self.InitialSolidMass = self.SolidsFractMass * self.InitialMass
        self.InitialOtherMass = self.OtherFractSolids * self.InitialSolidMass
        self.ProteinFractSolids = 1.0 - self.OtherFractSolids
        self.InitialProteinMass = self.ProteinFractSolids * self.InitialSolidMass

    def ScaleH2O_func(self):
        self.FractTotal = self.InitialLiquidVol / TissueH2O.InitialVol
        self.InitialIFV = self.FractTotal * InterstitialWater.InitialVol
        self.InitialCellH2O = self.FractTotal * CellH2O.InitialVol

    def Calc_func(self):
        self.IFV = self.FractTotal * InterstitialWater.Vol
        self.CellH2O = self.FractTotal * CellH2O.Vol
        self.LiquidVol = self.IFV + self.CellH2O
        self.LiquidMass = self.LiquidVol * self.LiquidDensity
        self.ContractileProteinMass = RespiratoryMuscle_ContractileProtein.Mass
        self.OtherMass = self.InitialOtherMass
        self.SolidMass = self.ContractileProteinMass + self.OtherMass
        self.ContractileProteinVol = self.ContractileProteinMass / self.ContractileProteinDensity
        self.OtherVol = self.OtherMass / self.OtherDensity
        self.SolidVol = self.ContractileProteinVol + self.OtherVol
        self.Mass = self.LiquidMass + self.SolidMass
        self.Vol = self.LiquidVol + self.SolidVol
        self.Density = self.Mass / self.Vol

class RespiratoryMuscle_Metabolism:
    def __init__(self):
        self.TotalCalsUsed = None
        self.BasalCalsUsed = None
        self.InitialBasalCalsUsed = None
        self.BasalCalsUsed__CalperMinperG = 0.002
        self.CalMultiplier = 1.0
        self.ShiveringCals = None
        self.AerobicCals = None
        self.AnaerobicCals = None
        self.O2Need = None
        self.O2Lack = None

    def ScaleCals_func(self):
        self.InitialBasalCalsUsed = self.CalMultiplier * self.BasalCalsUsed__CalperMinperG * RespiratoryMuscle_Size.InitialMass

    def CalcCals_func(self):
        self.BasalCalsUsed = self.CalMultiplier * self.BasalCalsUsed__CalperMinperG * RespiratoryMuscle_Size.Mass
        self.ShiveringCals = 0.0
        self.TotalCalsUsed = ( self.BasalCalsUsed * Thyroid.Effect * HeatMetabolism.Core * RespiratoryMuscle_Structure.Effect ) + RespiratoryMuscle_Work.TotalCals + self.ShiveringCals
        self.O2Need = Metabolism_Tools.CalToO2 * self.TotalCalsUsed

    def SplitCals_func(self):
        self.O2Lack = self.O2Need - RespiratoryMuscle_Flow.O2Use
        self.AerobicCals = Metabolism_Tools.O2ToCal * RespiratoryMuscle_Flow.O2Use
        self.AnaerobicCals = Metabolism_Tools.O2ToCal * self.O2Lack

class RespiratoryMuscle_Work:
    def __init__(self):
        self.TotalCals = None
        self.MotionCals = None
        self.HeatCals = None

    def Calc_func(self):
        self.MotionCals = 5.0
        self.HeatCals = 16.0
        self.TotalCals = self.MotionCals + self.HeatCals

class RespiratoryMuscle_Vasculature:
    def __init__(self):
        self.Tau = 30.0
        self.Effect = 1.0

    def PO2OnStimulus_curve(self, x):
        return cubic_hermite_spline(x, [41.0, 51.0, 61.0], [1.2, 1.0, 0.8], [0.0, -0.03, 0.0])

    def Parms_func(self):
        self.K = 1.0 / ( self.Tau * 1440.0 )

    def Calc_func(self):
        if RespiratoryMuscle_Function.Failed:
            self.Stimulus = 0.0
        else:
            self.Stimulus = self.PO2OnStimulus_curve( RespiratoryMuscle_Flow.PO2 )

        self.Effect = delay( self.K, self.Stimulus, self.Effect, System.Dx, None)


class RespiratoryMuscle_CO2:
    def __init__(self):
        self.conc_HCO3 = None
        self.conc_HCO3_mEqperL = None
        self.PCO2 = None
        self.InflowGas = None
        self.InflowBase = None
        self.OutflowBase = None
        self.conc_BloodHCO3 = None
        self.Outflow_0 = None
        self.K = None
        self.Alpha = None
        self.Mass = 48.1

    def CalcConc_func(self):
        self.conc_HCO3 = self.Mass / RespiratoryMuscle_Size.LiquidVol
        self.conc_HCO3_mEqperL = 1000.0 * self.conc_HCO3
        Tissue_BaseToGas.conc_HCO3 = self.conc_HCO3
        Tissue_BaseToGas.conc_SID = RespiratoryMuscle_Ph.conc_SID
        Tissue_BaseToGas.Calc_func()
        self.PCO2 = Tissue_BaseToGas.pCO2

    def CalcDervs_func(self):
        self.K = RespiratoryMuscle_Flow.BloodFlow / RespiratoryMuscle_Size.LiquidVol
        if System.Dx >=0:
            self.Alpha = 0.0
        elif ( self.K * System.Dx ) >= 100.0:
            self.Alpha = 4E-44
        elif True:
            self.Alpha = ( math.e ** ( - self.K * System.Dx ) )
        self.InflowGas = Metabolism_RespiratoryQuotient.RQ * RespiratoryMuscle_Flow.O2Use
        self.InflowBase = CO2Tools.LitersToMols * self.InflowGas
        Blood_GasToBase.pCO2 = self.PCO2
        Blood_GasToBase.conc_SID = BloodIons.conc_SID
        Blood_GasToBase.Calc_func()
        self.conc_BloodHCO3 = Blood_GasToBase.conc_HCO3
        self.Outflow_0 = RespiratoryMuscle_Flow.BloodFlow * ( self.conc_BloodHCO3 - CO2Artys.conc_HCO3 )
        self.OutflowBase = ( self.Alpha * self.Outflow_0 ) + ( ( 1 - self.Alpha ) * self.InflowBase )
        self.Change = self.InflowBase - self.OutflowBase
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.48)


class RespiratoryMuscle_Pressure:
    def __init__(self):
        self.ArtyPressure = None
        self.VeinPressure = None
        self.PressureGradient = None
        self.PumpSwitch = False
        self.PumpSetting = 0.0

    def Calc_func(self):
        if self.PumpSwitch:
            self.ArtyPressure = self.PumpSetting
        else:
            self.ArtyPressure = SystemicArtys.Pressure

        self.VeinPressure = SystemicVeins.Pressure
        self.PressureGradient = ( max( ( self.ArtyPressure - self.VeinPressure ), 0.0) )

class RespiratoryMuscle_ContractileProtein:

    def Initialize_func(self):
        self.Mass = RespiratoryMuscle_Size.InitialProteinMass

    def Dervs_func(self):
        self.Change = 0.0
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 4.2)


class RespiratoryMuscle_Fuel:
    def __init__(self):
        self.FADelivered = None
        self.GlucoseDelivered = None
        self.KR = 0.026
        self.Ratio = None
        self.FAFraction = None
        self.GlucoseFraction = None
        self.FA_GlucoseFraction = None
        self.LacFraction = None
        self.FAUsed_CalperMin = None
        self.AerobicGlucoseUsed_CalperMin = None
        self.AnaerobicGlucoseUsed_CalperMin = None
        self.LacUsed_CalperMin = None
        self.FAUsed_mGperMin = None
        self.AerobicGlucoseUsed_mGperMin = None
        self.AnaerobicGlucoseUsed_mGperMin = None
        self.LacUsed_mGperMin = None
        self.TotalGlucoseUsed_mGperMin = None
        self.FAFractionalDelivery = None
        self.AerobicGlucoseFractionalDelivery = None
        self.AnaerobicGlucoseFractionalDelivery = None
        self.MinimumFractionalDelivery = None
        self.FractUseDelay = 1.0

    def LacFraction_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 100.0], [0.0, 0.3], [0.0, 0.0])

    def Dervs_func(self):
        self.FADelivered = FAPool.conc_FA * RespiratoryMuscle_Flow.PlasmaFlow
        self.GlucoseDelivered = GlucosePool.conc_Glucose * RespiratoryMuscle_Flow.PlasmaFlow
        self.LacFraction = self.LacFraction_curve( RespiratoryMuscle_Lactate.conc_Lac__mGperdL )
        self.FA_GlucoseFraction = 1.0 - self.LacFraction
        self.Ratio = FAPool.conc_FA_mGperdL / GlucosePool.conc_Glucose_mGperdL
        self.FAFraction = self.FA_GlucoseFraction * ( self.Ratio / ( self.Ratio + self.KR ) )
        self.GlucoseFraction = self.FA_GlucoseFraction - self.FAFraction
        self.FAUsed_CalperMin = self.FAFraction * RespiratoryMuscle_Metabolism.AerobicCals
        self.AerobicGlucoseUsed_CalperMin = self.GlucoseFraction * RespiratoryMuscle_Metabolism.AerobicCals
        self.LacUsed_CalperMin = self.LacFraction * RespiratoryMuscle_Metabolism.AerobicCals
        self.AnaerobicGlucoseUsed_CalperMin = RespiratoryMuscle_Glycogen.Metabolism_CalperMin
        self.FAUsed_mGperMin = self.FAUsed_CalperMin * Metabolism_Tools.Fat_mGperCal
        self.AerobicGlucoseUsed_mGperMin = self.AerobicGlucoseUsed_CalperMin * Metabolism_Tools.CarboAerobic_mGperCal
        self.LacUsed_mGperMin = self.LacUsed_CalperMin * Metabolism_Tools.Lac__mGperCal
        self.AnaerobicGlucoseUsed_mGperMin = RespiratoryMuscle_Glycogen.Metabolism
        self.TotalGlucoseUsed_mGperMin = self.AerobicGlucoseUsed_mGperMin + self.AnaerobicGlucoseUsed_mGperMin
        if self.FAUsed_mGperMin > 0.0:
            self.FAFractionalDelivery = ( min( ( self.FADelivered / self.FAUsed_mGperMin ), 1.0) )
        else:
            self.FAFractionalDelivery = 1.0

        if self.AerobicGlucoseUsed_mGperMin > 0.0:
            self.AerobicGlucoseFractionalDelivery = ( min( ( self.GlucoseDelivered / self.AerobicGlucoseUsed_mGperMin ), 1.0) )
        else:
            self.AerobicGlucoseFractionalDelivery = 1.0

        self.AnaerobicGlucoseFractionalDelivery = RespiratoryMuscle_Glycogen.Availability
        self.MinimumFractionalDelivery = ( min( ( ( min( self.FAFractionalDelivery, self.AerobicGlucoseFractionalDelivery) ) ), self.AnaerobicGlucoseFractionalDelivery) )
        self.K = 0.5
        self.DxMax = 1.0
        self.FractUse = self.MinimumFractionalDelivery
        self.FractUseDelay = delay( self.K, self.FractUse, self.FractUseDelay, System.Dx, 0.01)


class RespiratoryMuscle_Ph:
    def __init__(self):
        self.Ph = None
        self.conc_SID = None
        self.conc_SID_mEqperL = None

    def CalcSID_func(self):
        self.conc_SID = KCell.conc_K_ + CellSID.OtherCations - CellSID.StrongAnions - RespiratoryMuscle_Lactate.conc_Lac_
        self.conc_SID_mEqperL = 1000.0 * self.conc_SID

    def CalcPh_func(self):
        PhCells.pCO2 = RespiratoryMuscle_CO2.PCO2
        PhCells.SID = self.conc_SID_mEqperL
        PhCells.Calc_func()
        self.Ph = PhCells.pH

class RespiratoryMuscle_Lactate:
    def __init__(self):
        self.conc_Lac_ = None
        self.conc_Lac__mEqperL = None
        self.conc_Lac__mGperdL = None
        self.DC = 270.0
        self.Made = None
        self.Made_mGperMin = None
        self.Used = None
        self.Used_mGperMin = None
        self.Outflux = None
        self.Outflux_0 = None
        self.K = None
        self.Alpha = None
        self.MEQ_ML_TO_MG_DL = 9008.0
        self.GLUCOSE_TO_LACTATE = 0.99
        self.MG_TO_MEQ = 0.0112
        self.Mass = 3.01

    def CalcConc_func(self):
        self.conc_Lac_ = self.Mass / RespiratoryMuscle_Size.LiquidVol
        self.conc_Lac__mEqperL = 1000.0 * self.conc_Lac_
        self.conc_Lac__mGperdL = self.MEQ_ML_TO_MG_DL * self.conc_Lac_

    def CalcDervs_func(self):
        self.Made_mGperMin = self.GLUCOSE_TO_LACTATE * RespiratoryMuscle_Fuel.AnaerobicGlucoseUsed_mGperMin
        self.Made = self.MG_TO_MEQ * self.Made_mGperMin
        self.Used_mGperMin = RespiratoryMuscle_Fuel.LacUsed_mGperMin
        self.Used = self.MG_TO_MEQ * self.Used_mGperMin
        self.K = self.DC / RespiratoryMuscle_Size.LiquidVol
        if System.Dx >=0:
            self.Alpha = 0.0
        elif ( self.K * System.Dx ) >= 100.0:
            self.Alpha = 4E-44
        elif True:
            self.Alpha = ( math.e ** ( - self.K * System.Dx ) )
        self.Outflux_0 = self.DC * ( self.conc_Lac_ - LacPool.conc_Lac_ )
        self.Outflux = ( self.Alpha * self.Outflux_0 ) + ( ( 1 - self.Alpha ) * ( self.Made + self.Used ) )
        self.Change = self.Made - self.Used - self.Outflux
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.03)


class RespiratoryMuscle_AlphaReceptors:
    def __init__(self):
        self.Activity = None
        self.TotalAgonism = None
        self.NeuralAgonism = None
        self.HumoralAgonism = None
        self.Switch = False
        self.Setting = 0.0
        self.NEURALK = 0.333
        self.HUMORALK = 0.5

    def Calc_func(self):
        self.NeuralAgonism = GangliaGeneral.NA_Hz
        self.HumoralAgonism = AlphaPool.Effect
        self.TotalAgonism = ( self.NEURALK * self.NeuralAgonism ) + ( self.HUMORALK * self.HumoralAgonism )
        if self.Switch:
            self.Activity = self.Setting
        else:
            self.Activity = self.TotalAgonism * AlphaBlockade.Effect


class RespiratoryMuscle_Structure:
    def __init__(self):
        self.PhEffect = None
        self.FuelEffect = None
        self.TemperatureEffect = None
        self.Effect = 1.0

    def PhOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [6.5, 6.6], [0.1, 0.0], [0.0, 0.0])

    def FuelOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [0.5, 0.8], [0.05, 0.0], [0.0, 0.0])

    def TemperatureOnStructure_curve(self, x):
        return cubic_hermite_spline(x, [44.0, 46.0], [0.0, 0.05], [0.0, 0.0])

    def Calc_func(self):
        self.PhEffect = self.PhOnStructure_curve( RespiratoryMuscle_Ph.Ph )
        self.FuelEffect = self.FuelOnStructure_curve( RespiratoryMuscle_Fuel.FractUseDelay )
        self.TemperatureEffect = self.TemperatureOnStructure_curve( HeatCore.Temp_C )
        self.F1 = 0.0
        self.F2 = self.PhEffect + self.TemperatureEffect + self.FuelEffect
        self.Effect = backwardeuler( self.F1, self.F2, System.Dx, self.Effect, None)


class RespiratoryMuscle_Flow:
    def __init__(self):
        self.Conductance = None
        self.BasicConductance = 1.1
        self.A2Effect = None
        self.SympsEffect = None
        self.ADHEffect = None
        self.PO2Effect = None
        self.MetabolismEffect = None
        self.AerobicFraction = None
        self.O2Use = None
        self.conc_O2 = None
        self.BloodFlow = None
        self.PlasmaFlow = None
        self.PO2 = 33.6
    def A2OnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.3, 3.5], [1.05, 1.0, 0.5], [0.0, -0.08, 0.0])

    def SympsOnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.0, 5.0], [1.3, 1.0, 0.1], [0.0, -0.3, 0.0])

    def PO2OnConductance_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 30.0], [2.0, 1.0], [0.0, 0.0])

    def ADHOnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.8, 3.0], [1.0, 0.1], [0.0, 0.0])

    def MetabolismOnConductance_curve(self, x):
        return cubic_hermite_spline(x, [6.0, 12.0, 400.0], [1.0, 1.3, 24.0], [0.0, 0.08, 0.0])

    def PO2OnAerobicFraction_curve(self, x):
        return cubic_hermite_spline(x, [2.0, 10.0], [0.0, 1.0], [0.0, 0.0])

    def Calc_func(self):
        self.A2Effect = self.A2OnConductance_curve( A2Pool.Log10Conc )
        self.SympsEffect = self.SympsOnConductance_curve( RespiratoryMuscle_AlphaReceptors.Activity )
        self.ADHEffect = self.ADHOnConductance_curve( ADHPool.Log10Conc )
        self.MetabolismEffect = self.MetabolismOnConductance_curve( RespiratoryMuscle_Metabolism.O2Need )
        self.SearchMax = PO2Artys.Pressure

        def PO2implicitfunc(PO2):
            self.PO2Effect = self.PO2OnConductance_curve( PO2 )
            self.Conductance = self.BasicConductance * self.A2Effect * self.SympsEffect * self.PO2Effect * self.ADHEffect * self.MetabolismEffect * Viscosity.ConductanceEffect * Anesthesia.VascularConductance * RespiratoryMuscle_Vasculature.Effect
            self.BloodFlow = ( max( ( RespiratoryMuscle_Pressure.PressureGradient * self.Conductance ), 0.0) )
            self.AerobicFraction = self.PO2OnAerobicFraction_curve( PO2 )
            self.O2Use = RespiratoryMuscle_Metabolism.O2Need * self.AerobicFraction
            if self.BloodFlow > 0.0:
                self.conc_O2 = O2Artys.conc_O2 - ( self.O2Use / self.BloodFlow )
            else:
                self.conc_O2 = 0.0

            HgbTissue.conc_O2 = self.conc_O2
            HgbTissue.O2ToPO2_func()
            PO2End = HgbTissue.pO2

            return PO2End
        self.PO2 = impliciteq( PO2implicitfunc, self.PO2, 0.34)
        self.PlasmaFlow = self.BloodFlow * BloodVol.PVCrit

class RespiratoryMuscle:
    def __init__(self):
        pass
    
class RespiratoryMuscle_Glycogen:
    def __init__(self):
        self.Synthesis = None
        self.Metabolism = None
        self.BasicSynthesis = 20.0
        self.GlucoseEffect = None
        self.InsulinEffect = None
        self.Space = None
        self.Availability = None
        self.Metabolism_CalperMin = None
        self.MG_TO_G = 0.001
        self.Mass = 46.0

    def GlucoseEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 100.0, 300.0], [0.0, 1.0, 3.0], [0.0, 0.01, 0.0])

    def InsulinEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 20.0, 100.0], [0.0, 1.0, 20.0], [0.0, 0.2, 0.0])

    def Space_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 40.0, 46.0], [4.0, 1.0, 0.0], [0.0, -0.15, 0.0])

    def Availability_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 5.0], [0.0, 1.0], [0.0, 0.0])

    def Dervs_func(self):
        self.GlucoseEffect = self.GlucoseEffect_curve( GlucosePool.conc_Glucose_mGperdL )
        self.InsulinEffect = self.InsulinEffect_curve( RespiratoryMuscle_Insulin.conc_InsulinDelayed )
        self.Space = self.Space_curve( self.Mass )
        self.Availability = self.Availability_curve( self.Mass )
        self.Synthesis = self.BasicSynthesis * self.GlucoseEffect * self.InsulinEffect * self.Space
        self.Metabolism_CalperMin = RespiratoryMuscle_Metabolism.AnaerobicCals * self.Availability
        self.Metabolism = self.Metabolism_CalperMin * Metabolism_Tools.CarboAnaerobic_mGperCal
        self.Change = self.MG_TO_G * ( self.Synthesis - self.Metabolism )
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.46)


class RespiratoryMuscle_Insulin:
    def __init__(self):
        self.Tau = 40.0
        self.conc_InsulinDelayed = 20.0

    def Parms_func(self):
        self.K = ( 1 / self.Tau )

    def Dervs_func(self):
        self.conc_Insulin = InsulinPool.conc_Insulin
        self.conc_InsulinDelayed = delay( self.K, self.conc_Insulin, self.conc_InsulinDelayed, System.Dx, 0.2)


class LM_Gluconeogenesis:
    def __init__(self):
        self.Rate = None
        self.InsulinEffect = None
        self.GlucagonEffect = None
        self.GlucoseEffect = None
        self.AminoAcidEffect = None
        self.AminoAcidUptake = None
        self.BasicUptake = 30.0
        self.AA_TO_GLU = 0.60

    def InsulinEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 50.0, 500.0], [2.5, 1.0, 0.0], [0.0, -0.005, 0.0])

    def GlucagonEffect_curve(self, x):
        return cubic_hermite_spline(x, [170.0, 680.0], [1.0, 2.0], [0.0, 0.0])

    def GlucoseEffect_curve(self, x):
        return cubic_hermite_spline(x, [45.0, 125.0, 340.0], [2.0, 1.0, 0.3], [0.0, -0.008, 0.0])

    def AminoAcidEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 50.0, 200.0], [0.0, 1.0, 2.0], [0.0, 0.03, 0.0])

    def Dervs_func(self):
        self.InsulinEffect = self.InsulinEffect_curve( LM_Insulin.conc_InsulinDelayed )
        self.GlucagonEffect = self.GlucagonEffect_curve( PortalVein_Glucagon.conc_Glucagon )
        self.GlucoseEffect = self.GlucoseEffect_curve( PortalVein_Glucose.conc_Glucose_mGperdL )
        self.AminoAcidEffect = self.AminoAcidEffect_curve( AAPool.conc_AA_mGperdL )
        self.AminoAcidUptake = self.BasicUptake * self.InsulinEffect * self.GlucagonEffect * self.GlucoseEffect * self.AminoAcidEffect * Liver_Function.Effect
        self.Rate = self.AminoAcidUptake * self.AA_TO_GLU

class LM_FA_Glucose:
    def __init__(self):
        self.Rate = None
        self.InsulinEffect = None
        self.GlucoseEffect = None
        self.GlucoseUptake = None
        self.BasicUptake = 70.0
        self.GLU_TO_FA = 0.42

    def InsulinEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 50.0, 200.0], [0.0, 1.0, 3.0], [0.0, 0.06, 0.0])

    def GlucoseEffect_curve(self, x):
        return cubic_hermite_spline(x, [120.0, 130.0, 200.0], [0.0, 1.0, 2.0], [0.0, 0.05, 0.0])

    def Dervs_func(self):
        self.InsulinEffect = self.InsulinEffect_curve( LM_Insulin.conc_InsulinDelayed )
        self.GlucoseEffect = self.GlucoseEffect_curve( PortalVein_Glucose.conc_Glucose_mGperdL )
        self.GlucoseUptake = self.BasicUptake * self.InsulinEffect * self.GlucoseEffect * Liver_Function.Effect
        self.Rate = self.GlucoseUptake * self.GLU_TO_FA

class LM_Glycogenolysis:
    def __init__(self):
        self.Rate = None
        self.BasicRate = 75.0
        self.InsulinEffect = None
        self.GlucagonEffect = None
        self.MassEffect = None
        self.GlucoseEffect = None
        self.EpinephrineEffect = None

    def InsulinEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 35.0, 120.0], [2.0, 1.0, 0.0], [0.0, -0.02, 0.0])

    def GlucagonEffect_curve(self, x):
        return cubic_hermite_spline(x, [170.0, 680.0], [1.0, 2.0], [0.0, 0.0])

    def MassEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 100.0], [0.0, 1.0], [0.0, 0.0])

    def GlucoseEffect_curve(self, x):
        return cubic_hermite_spline(x, [45.0, 125.0, 350.0], [2.0, 1.0, 0.3], [0.0, -0.01, 0.0])

    def EpinephrineEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 40.0, 400.0, 1200.0], [0.8, 1.0, 10.0, 20.0], [0.0, 0.01, 0.02, 0.0])

    def Dervs_func(self):
        self.InsulinEffect = self.InsulinEffect_curve( LM_Insulin.conc_InsulinDelayed )
        self.GlucagonEffect = self.GlucagonEffect_curve( PortalVein_Glucagon.conc_Glucagon )
        self.MassEffect = self.MassEffect_curve( LM_Glycogen.Mass )
        self.GlucoseEffect = self.GlucoseEffect_curve( PortalVein_Glucose.conc_Glucose_mGperdL )
        self.EpinephrineEffect = self.EpinephrineEffect_curve( EpiPool.conc_Epi_pGpermL )
        self.Rate = self.BasicRate * self.InsulinEffect * self.GlucagonEffect * self.MassEffect * self.GlucoseEffect * self.EpinephrineEffect * Liver_Function.Effect

class LM_Insulin:
    def __init__(self):
        self.Tau = 40.0
        self.conc_InsulinDelayed = 50.0

    def Parms_func(self):
        self.K = ( 1 / self.Tau )

    def Dervs_func(self):
        self.conc_Insulin = PortalVein_Insulin.conc_Insulin
        self.conc_InsulinDelayed = delay( self.K, self.conc_Insulin, self.conc_InsulinDelayed, System.Dx, 0.5)


class LM_FattyAcids:
    def __init__(self):
        self.NetRelease = None
        self.Uptake = None
        self.Release = None

    def Dervs_func(self):
        LM_FA_AminoAcids.Dervs_func()
        LM_FA_Glucose.Dervs_func()
        self.Uptake = LM_Ketoacids.FattyAcidUptake
        self.Release = LM_FA_AminoAcids.Rate + LM_FA_Glucose.Rate
        self.NetRelease = self.Release - self.Uptake

class LM_Ketoacids:
    def __init__(self):
        self.Rate = None
        self.FattyAcidEffect = None
        self.GlucagonEffect = None
        self.FattyAcidUptake = None
        self.BasicUptake = 2.2
        self.FA_TO_KA = 1.02

    def FattyAcidEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 15.0, 75.0], [0.5, 1.0, 5.0], [0.0, 0.05, 0.0])

    def GlucagonEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 170.0, 340.0], [0.5, 1.0, 10.0], [0.0, 0.01, 0.0])

    def Dervs_func(self):
        self.FattyAcidEffect = self.FattyAcidEffect_curve( FAPool.conc_FA_mGperdL )
        self.GlucagonEffect = self.GlucagonEffect_curve( PortalVein_Glucagon.conc_Glucagon )
        self.FattyAcidUptake = self.BasicUptake * self.FattyAcidEffect * self.GlucagonEffect * Liver_Function.Effect
        self.Rate = self.FA_TO_KA * self.FattyAcidUptake

class LM_Glycerol:
    def __init__(self):
        self.Synthesis = None
        self.Metabolism = None
        self.Mass = 530.0

    def Dervs_func(self):
        self.Synthesis = 0.0
        self.Metabolism = 0.0
        self.Change = self.Synthesis - self.Metabolism
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 5.3)


class LM_FA_AminoAcids:
    def __init__(self):
        self.Rate = None
        self.InsulinEffect = None
        self.AminoAcidEffect = None
        self.AminoAcidUptake = None
        self.BasicUptake = 20.0
        self.AA_TO_FA = 0.437

    def InsulinEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 50.0, 80.0], [0.0, 1.0, 4.0], [0.0, 0.05, 0.0])

    def AminoAcidEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 50.0, 200.0], [0.0, 1.0, 2.0], [0.0, 0.02, 0.0])

    def Dervs_func(self):
        self.InsulinEffect = self.InsulinEffect_curve( LM_Insulin.conc_InsulinDelayed )
        self.AminoAcidEffect = self.AminoAcidEffect_curve( AAPool.conc_AA_mGperdL )
        self.AminoAcidUptake = self.BasicUptake * self.InsulinEffect * self.AminoAcidEffect * Liver_Function.Effect
        self.Rate = self.AminoAcidUptake * self.AA_TO_FA

class LM_AminoAcids:
    def __init__(self):
        self.NetUptake = None
        self.Uptake = None
        self.Release = None
        self.Urea = None

    def Dervs_func(self):
        self.Uptake = LM_Gluconeogenesis.AminoAcidUptake + LM_FA_AminoAcids.AminoAcidUptake
        self.Release = 0.0
        self.NetUptake = self.Uptake - self.Release
        self.Urea = 0.3 * self.Uptake

class LM_Lactate:
    def __init__(self):
        self.Synthesis = None
        self.Metabolism = None
        self.Mass = 530.0

    def Dervs_func(self):
        self.Synthesis = 0.0
        self.Metabolism = 0.0
        self.Change = self.Synthesis - self.Metabolism
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 5.3)


class LM_Glucose:
    def __init__(self):
        self.NetUptake = None
        self.Uptake = None
        self.Release = None

    def Dervs_func(self):
        self.Uptake = LM_Glycogenesis.Rate + LM_FA_Glucose.GlucoseUptake
        self.Release = LM_Glycogenolysis.Rate + LM_Gluconeogenesis.Rate
        self.NetUptake = self.Uptake - self.Release

class LM_Glycogenesis:
    def __init__(self):
        self.Rate = None
        self.BasicRate = 75.0
        self.InsulinEffect = None
        self.MassEffect = None
        self.GlucoseEffect = None

    def InsulinEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 35.0, 120.0], [0.0, 1.0, 3.0], [0.0, 0.03, 0.0])

    def MassEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 100.0, 200.0], [3.0, 1.0, 0.0], [0.0, -0.05, 0.0])

    def GlucoseEffect_curve(self, x):
        return cubic_hermite_spline(x, [120.0, 130.0, 200.0], [0.0, 1.0, 2.0], [0.0, 0.06, 0.0])

    def Dervs_func(self):
        self.InsulinEffect = self.InsulinEffect_curve( LM_Insulin.conc_InsulinDelayed )
        self.MassEffect = self.MassEffect_curve( LM_Glycogen.Mass )
        self.GlucoseEffect = self.GlucoseEffect_curve( PortalVein_Glucose.conc_Glucose_mGperdL )
        self.Rate = self.BasicRate * self.InsulinEffect * self.MassEffect * self.GlucoseEffect * Liver_Function.Effect

class LiverMetabolism:

    def Parms_func(self):
        LM_Insulin.Parms_func()

    def Dervs_func(self):
        LM_Glycogen.Dervs_func()
        LM_Gluconeogenesis.Dervs_func()
        LM_Ketoacids.Dervs_func()
        LM_FattyAcids.Dervs_func()
        LM_AminoAcids.Dervs_func()
        LM_Glucose.Dervs_func()
        LM_Insulin.Dervs_func()

class LM_Glycogen:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.Mass = 100.0

    def Dervs_func(self):
        LM_Glycogenesis.Dervs_func()
        LM_Glycogenolysis.Dervs_func()
        self.Gain = LM_Glycogenesis.Rate
        self.Loss = LM_Glycogenolysis.Rate
        self.Change = 0.001 * ( self.Gain - self.Loss )
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 1.0)


class Progesterone:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.Secretion = None
        self.Degradation = None
        self.TargetConcFemale = 0.1
        self.TargetConcMale = 1.0
        self.TargetConc = None
        self.InitialMass = None
        self.conc_Conc_nMolperL = None
        self.conc_Conc_nGpermL = None
        self.NMOLperL_TO_NGperML = 0.3145
        self.PumpSwitch = False
        self.PumpSetting = 0.0
        self.K = 0.16

    def Init_func(self):
        if Gender.IsFemale:
            self.TargetConc = self.TargetConcFemale
        else:
            self.TargetConc = self.TargetConcMale

        self.InitialMass = self.TargetConc * ECFV.InitialVol_L
        self.Mass = self.InitialMass

    def Conc_func(self):
        self.conc_Conc_nMolperL = self.Mass / ECFV.Vol_L
        self.conc_Conc_nGpermL = self.conc_Conc_nMolperL * self.NMOLperL_TO_NGperML

    def Dervs_func(self):
        if Gender.IsFemale:
            self.Secretion = Ovaries_Progesterone.Secretion
        else:
            self.Secretion = Testes_Progesterone.Secretion

        self.Degradation = self.K * self.Mass
        self.Gain = self.Secretion + ( self.PumpSetting * self.PumpSwitch )
        self.Loss = self.Degradation
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.3)


class FSH:

    def Parms_func(self):
        FSH_AnteriorPituitary.Parms_func()

    def Initialize_func(self):
        FSH_Circulating.Initialize_func()

    def Conc_func(self):
        FSH_Circulating.Conc_func()

    def Dervs_func(self):
        FSH_AnteriorPituitary.Dervs_func()
        FSH_Circulating.Dervs_func()

class FSH_Circulating:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.Secretion = None
        self.Degradation = None
        self.TargetConcFemale = 5.5
        self.TargetConcMale = 8.0
        self.TargetConc = None
        self.InitialMass = None
        self.conc_Conc_IUperL = None
        self.PumpSwitch = False
        self.PumpSetting = 0.0
        self.K = 0.0009

    def Init_func(self):
        if Gender.IsFemale:
            self.TargetConc = self.TargetConcFemale
        else:
            self.TargetConc = self.TargetConcMale

        self.InitialMass = self.TargetConc * ECFV.InitialVol_L
        self.Mass = self.InitialMass

    def Conc_func(self):
        self.conc_Conc_IUperL = self.Mass / ECFV.Vol_L

    def Dervs_func(self):
        self.Secretion = FSH_AnteriorPituitary.Secretion
        self.Degradation = self.K * self.Mass
        self.Gain = self.Secretion + ( self.PumpSetting * self.PumpSwitch )
        self.Loss = self.Degradation
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.6)


class FSH_AnteriorPituitary:
    def __init__(self):
        self.BasicSecretion = 0.050
        self.Secretion = None
        self.GnRHEffect = None
        self.InhibinEffect = None
        self.TestosteroneEffect = None
        self.Delay_Hrs = 10.0
        self.EstradiolEffectDelayed = 1.0

    def GnRHEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 80.0, 200.0], [2.0, 1.0, 0.2], [0.0, -0.01, 0.0])

    def EstradiolEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.4, 1.5, 2.0], [1.0, 0.6, 0.6, 5.0], [0.0, 0.0, 0.0, 0.0])

    def InhibinEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 7000.0], [1.0, 0.4], [0.0, 0.0])

    def TestosteroneEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 50.0], [0.999, 0.2], [0.0, 0.0])

    def Parms_func(self):
        self.K = ( 1 / ( 60.0 * self.Delay_Hrs ) )

    def Dervs_func(self):
        self.GnRHEffect = self.GnRHEffect_curve( GnRH.Period_Min )
        self.EstradiolEffect = self.EstradiolEffect_curve( Estradiol.conc_Conc_nMolperL )
        self.InhibinEffect = self.InhibinEffect_curve( Inhibin.conc_Conc_IUperL )
        self.TestosteroneEffect = self.TestosteroneEffect_curve( Testosterone.conc_Conc_nMolperL )
        self.Secretion = self.BasicSecretion * self.GnRHEffect * self.EstradiolEffectDelayed * self.InhibinEffect * self.TestosteroneEffect
        self.EstradiolEffectDelayed = delay( self.K, self.EstradiolEffect, self.EstradiolEffectDelayed, System.Dx, 0.01)


class LeptinClearance:
    def __init__(self):
        self.Rate = None
        self.K = 0.01

    def Dervs_func(self):
        self.Rate = self.K * LeptinPool.Mass

class LeptinPump:
    def __init__(self):
        self.Rate = None
        self.Switch = False
        self.Setting = 0.0

    def Parms_func(self):
        self.Rate = self.Switch * self.Setting

class Leptin:

    def Parms_func(self):
        LeptinPump.Parms_func()

    def Conc_func(self):
        LeptinPool.Conc_func()

    def Dervs_func(self):
        LeptinSecretion.Dervs_func()
        LeptinClearance.Dervs_func()
        LeptinPool.Dervs_func()

class LeptinPool:
    def __init__(self):
        self.conc_Leptin_nGpermL = None
        self.Gain = None
        self.Loss = None
        self.Targetconc_Leptin_nGpermL = 8.0
        self.InitialMass = None

    def Init_func(self):
        self.InitialMass = self.Targetconc_Leptin_nGpermL * ECFV.Vol_L
        self.Mass = self.InitialMass

    def Conc_func(self):
        self.conc_Leptin_nGpermL = self.Mass / ECFV.Vol_L

    def Dervs_func(self):
        self.Gain = LeptinSecretion.Rate + LeptinPump.Rate
        self.Loss = LeptinClearance.Rate
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 1.2)


class LeptinSecretion:
    def __init__(self):
        self.Rate = None
        self.AdiposeEffect = None
        self.Basic = 1.2

    def AdiposeEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 13300.0, 100000.0], [0.0, 1.0, 6.0], [0.0, 8e-05, 0.0])

    def Dervs_func(self):
        self.AdiposeEffect = self.AdiposeEffect_curve( LipidDeposits.Mass )
        self.Rate = self.Basic * self.AdiposeEffect * Fat_Function.Effect

class HepaticFunction:
    def __init__(self):
        pass
    
class PlasmaProtein:
    def __init__(self):
        self.Gain = None
        self.Loss = None
        self.conc_Protein = None
        self.conc_Protein_GperdL = None
        self.PER_ML_TO_PER_DL = 100.0
        self.COP = None
        self.SynthesisBasic = 0.01
        self.COPEffect = None
        self.Synthesis = None
        self.DegradationBasic = 0.01
        self.ProteinEffect = None
        self.Degradation = None
        self.Mass = 210.0

    def COPEffect_curve(self, x):
        return cubic_hermite_spline(x, [20.0, 28.0, 40.0], [3.0, 1.0, 0.0], [0.0, -0.2, 0.0])

    def ProteinEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.07, 0.09], [0.0, 1.0, 6.0], [0.0, 40.0, 0.0])

    def CalcConc_func(self):
        self.conc_Protein = self.Mass / PlasmaVol.Vol
        self.conc_Protein_GperdL = self.PER_ML_TO_PER_DL * self.conc_Protein
        Colloids.conc_Prot = self.conc_Protein
        Colloids.GetPres_func()
        self.COP = Colloids.Pres

    def CalcDervs_func(self):
        self.COPEffect = self.COPEffect_curve( self.COP )
        self.Synthesis = self.SynthesisBasic * self.COPEffect
        self.ProteinEffect = self.ProteinEffect_curve( self.conc_Protein )
        self.Degradation = self.DegradationBasic * self.ProteinEffect
        self.Gain = self.Synthesis + LymphProtein.Rate + Transfusion.ProteinRate + PeritoneumProtein.Loss + IVDrip.ProteinRate
        self.Loss = self.Degradation + CapillaryProtein.Rate + Hemorrhage.ProteinRate + PeritoneumProtein.Gain + CD_Protein.Outflow
        self.Change = self.Gain - self.Loss
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 2.1)


class CircyProtein:
    def __init__(self):
        pass
    
class Colloids:
    def __init__(self):
        self.Pres = None
        self.conc_Prot = None
        self.C1 = 320.0
        self.C2 = 1160.0
        self.K1 = 0.138
        self.K2 = 0.019

    def GetPres_func(self):
        if self.conc_Prot > 0.0:
            self.Pres = ( self.C1 * self.conc_Prot ) + ( self.C2 * self.conc_Prot * self.conc_Prot )
        else:
            self.Pres = 0.0


    def Getconc_Prot_func(self):
        if self.Pres > 0.0:
            self.conc_Prot = ( math.sqrt( ( self.K2 + ( self.Pres / self.C2 ) ) ) ) - self.K1
        else:
            self.conc_Prot = 0.0


class CO2Veins:
    def __init__(self):
        self.conc_HCO3_mEqperL = None
        self.Pressure = None
        self.Mass = None
        self.conc_HCO3 = 0.0256

    def CalcConc_func(self):
        self.conc_HCO3_mEqperL = 1000.0 * self.conc_HCO3
        Blood_BaseToGas.conc_HCO3 = self.conc_HCO3
        Blood_BaseToGas.conc_SID = BloodIons.conc_SID
        Blood_BaseToGas.Calc_func()
        self.Pressure = Blood_BaseToGas.pCO2
        self.Mass = self.conc_HCO3 * VeinsVol.Vol

    def Dervs_func(self):
        self.K = 5.0
        self.DxMax = ( 1 / self.K )
        if CardiacOutput.Flow > 0.0:
            self.conc_HCO3_SteadyState = CO2Artys.conc_HCO3 + ( CO2Total.Inflow / CardiacOutput.Flow )
        else:
            self.conc_HCO3_SteadyState = 0.0

        self.conc_HCO3 = delay( self.K, self.conc_HCO3_SteadyState, self.conc_HCO3, System.Dx, 0.000256)


class Blood_BaseToGas:
    def __init__(self):
        self.pCO2 = None
        self.conc_SID = None
        self.conc_HCO3 = None
        self.C = -645.8
        self.D = 2777.8

    def Calc_func(self):
        if ( self.conc_HCO3 > 0.0 ) and ( self.conc_SID > 0.0 ):
            self.pCO2 = ( max( ( ( self.C * self.conc_SID ) + ( self.D * self.conc_HCO3 ) ), 0.0001) )
        else:
            self.pCO2 = 0.0001


class CO2Total:
    def __init__(self):
        self.Inflow = None
        self.Outflow = None

    def Dervs_func(self):
        self.Inflow = Bone_CO2.OutflowBase + Brain_CO2.OutflowBase + Fat_CO2.OutflowBase + GITract_CO2.OutflowBase + Kidney_CO2.OutflowBase + LeftHeart_CO2.OutflowBase + Liver_CO2.OutflowBase + OtherTissue_CO2.OutflowBase + RespiratoryMuscle_CO2.OutflowBase + RightHeart_CO2.OutflowBase + SkeletalMuscle_CO2.OutflowBase + Skin_CO2.OutflowBase
        self.Outflow = LungCO2.Expired * CO2Tools.LitersToMols

class CO2Artys:
    def __init__(self):
        self.conc_HCO3_mEqperL = None
        self.Pressure = None
        self.Mass = None
        self.conc_HCO3 = 0.0240

    def CalcConc_func(self):
        self.conc_HCO3_mEqperL = 1000.0 * self.conc_HCO3
        Blood_BaseToGas.conc_HCO3 = self.conc_HCO3
        Blood_BaseToGas.conc_SID = BloodIons.conc_SID
        Blood_BaseToGas.Calc_func()
        self.Pressure = Blood_BaseToGas.pCO2
        self.Mass = self.conc_HCO3 * ArtysVol.Vol

    def Dervs_func(self):
        self.K = 5.0
        self.DxMax = ( 1 / self.K )
        if CardiacOutput.Flow > 0.0:
            self.conc_HCO3_SteadyState = CO2Veins.conc_HCO3 - ( CO2Total.Outflow / CardiacOutput.Flow )
        else:
            self.conc_HCO3_SteadyState = 0.0

        self.conc_HCO3 = delay( self.K, self.conc_HCO3_SteadyState, self.conc_HCO3, System.Dx, 0.00024)


class CO2:

    def CalcConc_func(self):
        CO2Artys.CalcConc_func()
        CO2Veins.CalcConc_func()

    def Dervs_func(self):
        CO2Total.Dervs_func()
        CO2Artys.Dervs_func()
        CO2Veins.Dervs_func()

class Tissue_BaseToGas:
    def __init__(self):
        self.pCO2 = None
        self.conc_SID = None
        self.conc_HCO3 = None
        self.C = -1411.4
        self.D = 5988.0

    def Calc_func(self):
        if ( self.conc_HCO3 > 0.0 ) and ( self.conc_SID > 0.0 ):
            self.pCO2 = ( max( ( ( self.C * self.conc_SID ) + ( self.D * self.conc_HCO3 ) ), 0.0001) )
        else:
            self.pCO2 = 0.0001


class Muscle_BaseToGas:
    def __init__(self):
        self.pCO2 = None
        self.conc_SID = None
        self.conc_HCO3 = None
        self.C = -413.34
        self.D = 5988.0

    def Calc_func(self):
        if ( self.conc_HCO3 > 0.0 ) and ( self.conc_SID > 0.0 ):
            self.pCO2 = ( max( ( ( self.C * self.conc_SID ) + ( self.D * self.conc_HCO3 ) ), 0.0001) )
        else:
            self.pCO2 = 0.0001


class Blood_GasToBase:
    def __init__(self):
        self.pCO2 = None
        self.conc_SID = None
        self.conc_HCO3 = None
        self.A = 0.2325
        self.B = 0.00036

    def Calc_func(self):
        if ( self.pCO2 > 0.0 ) and ( self.conc_SID > 0.0 ):
            self.conc_HCO3 = ( self.A * self.conc_SID ) + ( self.B * self.pCO2 )
        else:
            self.conc_HCO3 = 0.0001


class Muscle_GasToBase:
    def __init__(self):
        self.pCO2 = None
        self.conc_SID = None
        self.conc_HCO3 = None
        self.A = 0.0690
        self.B = 0.000167

    def Calc_func(self):
        if ( self.pCO2 > 0.0 ) and ( self.conc_SID > 0.0 ):
            self.conc_HCO3 = ( self.A * self.conc_SID ) + ( self.B * self.pCO2 )
        else:
            self.conc_HCO3 = 0.0001


class CO2Tools:
    def __init__(self):
        self.MolsToLiters = 22.4
        self.LitersToMols = 0.0446
    
class Tissue_GasToBase:
    def __init__(self):
        self.pCO2 = None
        self.conc_SID = None
        self.conc_HCO3 = None
        self.A = 0.2357
        self.B = 0.000167

    def Calc_func(self):
        if ( self.pCO2 > 0.0 ) and ( self.conc_SID > 0.0 ):
            self.conc_HCO3 = ( self.A * self.conc_SID ) + ( self.B * self.pCO2 )
        else:
            self.conc_HCO3 = 0.0001


class CreatineSkeletalMuscle:
    def __init__(self):
        self.Mass = 111.0
        self.conc_Creatine = None

    def Calc_func(self):
        self.conc_Creatine = 1000.0 * ( self.Mass / SkeletalMuscle_Size.Mass )

class Creatine:

    def Calc_func(self):
        CreatineSkeletalMuscle.Calc_func()
        CreatineCells.Calc_func()

class CreatineCells:
    def __init__(self):
        self.TotalMass = None
        self.OtherMass = 17.0
        self.CreatineToCreatinine = None
        self.K = 0.010

    def Calc_func(self):
        self.TotalMass = CreatineSkeletalMuscle.Mass + self.OtherMass
        self.CreatineToCreatinine = self.K * self.TotalMass

class SympsKidy:
    def __init__(self):
        self.NA = None
        self.NA_Hz = None
        self.LowPressureEffect = None
        self.FuelEffect = None
        self.ReflexNA = None
        self.ClampSwitch = False
        self.ClampLevel = 0.0

    def LowPressureEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.0, 4.0], [1.5, 1.0, 0.2], [0.0, -0.4, 0.0])

    def FuelEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.3, 0.6, 0.8], [0.0, 3.0, 0.0], [0.0, 0.0, 0.0])

    def Calc_func(self):
        self.FuelEffect = self.FuelEffect_curve( Brain_Fuel.FractUseDelay )
        if Brain_Function.Effect > 0.1:
            self.LowPressureEffect = self.LowPressureEffect_curve( LowPressureReceptors.NA )
            self.ReflexNA = SympsCNS.BaroEffect * self.LowPressureEffect * SympsCNS.MechanoEffect * SympsChemo.Effect
            self.NA = ( self.ReflexNA + ExerciseSymps.TotalEffect + CushingResponse.Effect + self.FuelEffect ) * SympsCNS.A2Effect * CNSTrophicFactor.Effect
        else:
            self.LowPressureEffect = 0.0
            self.ReflexNA = 0.0
            self.NA = ( 1.0 + CushingResponse.Effect + self.FuelEffect ) * CNSTrophicFactor.Effect
        if self.ClampSwitch:
            self.NA_Hz = self.ClampLevel
        else:
            self.NA_Hz = 1.5 * self.NA


class GangliaKidney:
    def __init__(self):
        self.NA_Hz = None
        self.NA = None
        self.Switch = False
        self.Setting = 0.0
        self.Block_percent = 0.0

    def Calc_func(self):
        if self.Switch:
            self.NA_Hz = self.Setting
        else:
            self.NA_Hz = SympsKidy.NA_Hz * ( 1.0 - ( self.Block_percent / 100.0 ) )

        self.NA = 0.667 * self.NA_Hz

class CNSTrophicFactor:
    def __init__(self):
        self.Effect = 1.0

    def Dervs_func(self):
        self.EffectChange = 0.0
        self.Effect = diffeq( self.EffectChange, System.Dx, self.Effect, 0.01)


class Chemoreceptors:
    def __init__(self):
        self.FiringRate = None
        self.BasicFiringRate = None
        self.Clamp = False
        self.Level = 0.0
        self.PO2Effect = None
        self.PhEffect = None
        self.SympsEffect = None
        self.AlphaAgonism = None

    def PO2Effect_curve(self, x):
        return cubic_hermite_spline(x, [30.0, 60.0, 94.0, 400.0], [10.0, 2.0, 0.5, 0.2], [0.0, -0.05, -0.005, 0.0])

    def PhEffect_curve(self, x):
        return cubic_hermite_spline(x, [7.1, 7.44, 7.7], [2.0, 0.4, 0.0], [0.0, -3.0, 0.0])

    def SympsEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.0, 4.0], [0.0, 0.1, 0.6], [0.0, 0.2, 0.0])

    def Calc_func(self):
        self.PO2Effect = self.PO2Effect_curve( PO2Artys.Pressure )
        self.PhEffect = self.PhEffect_curve( BloodPh.ArtysPh )
        self.AlphaAgonism = AlphaBlockade.Effect * ( ( 0.5 * GangliaGeneral.NA ) + ( 0.5 * AlphaPool.Effect ) )
        self.SympsEffect = self.SympsEffect_curve( self.AlphaAgonism )
        self.BasicFiringRate = self.PO2Effect + self.PhEffect + self.SympsEffect
        if self.Clamp:
            self.FiringRate = self.Level
        elif OtherTissue_Function.Failed:
            self.FiringRate = 0.0
        elif True:
            self.FiringRate = self.BasicFiringRate * ChemoreceptorAcclimation.Effect

class GangliaGeneral:
    def __init__(self):
        self.NA_Hz = None
        self.NA = None
        self.Switch = False
        self.Setting = 0.0
        self.Block_percent = 0.0

    def Calc_func(self):
        if self.Switch:
            self.NA_Hz = self.Setting
        else:
            self.NA_Hz = SympsCNS.NA_Hz * ( 1.0 - ( self.Block_percent / 100.0 ) )

        self.NA = 0.667 * self.NA_Hz

class SympsCNS:
    def __init__(self):
        self.NA = None
        self.NA_Hz = None
        self.A2Effect = None
        self.BaroEffect = None
        self.BaroSensitivity = 1.0
        self.LowPressureEffect = None
        self.LowPressureSensitivity = 1.0
        self.MechanoEffect = None
        self.FuelEffect = None
        self.ReflexNA = None
        self.ClampSwitch = False
        self.ClampLevel = 0.0
        self.PituitaryNA = None

    def A2Effect_curve(self, x):
        return cubic_hermite_spline(x, [1.7, 2.3], [1.0, 1.4], [0.0, 0.0])

    def BaroEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.0, 2.0], [1.5, 1.0, 0.5], [0.0, -0.5, 0.0])

    def LowPressureEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.0, 4.0], [1.1, 1.0, 0.9], [0.0, -0.1, 0.0])

    def MechanoEffect_curve(self, x):
        return cubic_hermite_spline(x, [5.0, 20.0], [1.0, 0.5], [0.0, 0.0])

    def FuelEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.3, 0.6, 0.8], [0.0, 3.0, 0.0], [0.0, 0.0, 0.0])

    def Calc_func(self):
        self.FuelEffect = self.FuelEffect_curve( Brain_Fuel.FractUseDelay )
        if Brain_Function.Effect > 0.1:
            self.A2Effect = self.A2Effect_curve( A2Pool.Log10Conc )
            self.BaroEffect = 1.0 + ( self.BaroSensitivity * ( self.BaroEffect_curve( Baroreflex.NA ) - 1.0 ) )
            self.LowPressureEffect = 1.0 + ( self.LowPressureSensitivity * ( self.LowPressureEffect_curve( LowPressureReceptors.NA ) - 1.0 ) )
            self.MechanoEffect = self.MechanoEffect_curve( Mechanoreceptors.FiringRate )
            self.ReflexNA = self.BaroEffect * self.LowPressureEffect * self.MechanoEffect * SympsChemo.Effect
            self.NA = ( self.ReflexNA + ExerciseSymps.TotalEffect + CushingResponse.Effect + self.FuelEffect ) * self.A2Effect * CNSTrophicFactor.Effect
        else:
            self.A2Effect = 0.0
            self.BaroEffect = 0.0
            self.LowPressureEffect = 0.0
            self.MechanoEffect = 0.0
            self.ReflexNA = 0.0
            self.NA = ( 1.0 + CushingResponse.Effect + self.FuelEffect ) * CNSTrophicFactor.Effect
        if self.ClampSwitch:
            self.NA_Hz = self.ClampLevel
        else:
            self.NA_Hz = 1.5 * self.NA

        self.PituitaryNA = self.BaroEffect

class Mechanoreceptors:
    def __init__(self):
        self.FiringRate = None

    def Calc_func(self):
        self.FiringRate = 0.0

class ExerciseSymps:
    def __init__(self):
        self.TotalEffect = None
        self.RadiationEffect = None
        self.MetaboreflexEffect = None

    def Calc_func(self):
        self.RadiationEffect = MotorRadiation.TotalEffect
        self.MetaboreflexEffect = 0.32 * SkeletalMuscle_Metaboreflex.NerveActivity
        self.TotalEffect = self.RadiationEffect + self.MetaboreflexEffect

class MotorRadiation:
    def __init__(self):
        self.TotalEffect = None

    def TotalEffect_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 500.0, 1000.0], [0.0, 2.2, 2.6], [0.004, 0.002, 0.0])

    def Calc_func(self):
        self.TotalEffect = self.TotalEffect_curve( Exercise_Metabolism.TotalWatts )

class AdrenalNerve:
    def __init__(self):
        self.NA_Hz = None
        self.NA = None
        self.Switch = False
        self.Setting = 0.0
        self.Block_percent = 0.0

    def Calc_func(self):
        if self.Switch:
            self.NA_Hz = self.Setting
        else:
            self.NA_Hz = SympsCNS.NA_Hz * ( 1.0 - ( self.Block_percent / 100.0 ) )

        self.NA = 0.667 * self.NA_Hz

class LowPressureReceptors:
    def __init__(self):
        self.NA = None
        self.PressureChange = None
        self.Tau = 30.0
        self.Switch = False
        self.Level = 0.0
        self.AdaptedPressure = 6.0

    def PressureChangeOnNA_curve(self, x):
        return cubic_hermite_spline(x, [-4.0, 0.0, 12.0], [0.0, 1.0, 4.0], [0.0, 0.3, 0.0])

    def Parms_func(self):
        self.RateConst = ( 1 / ( 1440.0 * self.Tau ) )

    def Calc_func(self):
        self.AvePressure = ( RightAtrium.TMP + LeftAtrium.TMP ) / 2.0
        self.PressureChange = self.AvePressure - self.AdaptedPressure
        if RightHeart_Function.Failed or LeftHeart_Function.Failed:
            self.NA = 0.0
        elif self.Switch:
            self.NA = self.Level
        elif True:
            self.NA = self.PressureChangeOnNA_curve( self.PressureChange )
        self.AdaptedPressure = delay( self.RateConst, self.AvePressure, self.AdaptedPressure, System.Dx, 0.06)


class Baroreflex:
    def __init__(self):
        self.NA = None
        self.PressureChange = None
        self.PressureEffect = None
        self.TissueFunctionEffect = None
        self.Tau = 10.0
        self.Clamp = False
        self.Level = 0.0
        self.AdaptedPressure = 97.0

    def PressureEffect_curve(self, x):
        return cubic_hermite_spline(x, [-50.0, 0.0, 50.0], [0.0, 1.0, 2.0], [0.0, 0.02, 0.0])

    def Parms_func(self):
        self.RateConst = ( 1 / ( 60.0 * self.Tau ) )

    def Calc_func(self):
        self.PressureChange = CarotidSinus.Pressure - self.AdaptedPressure
        self.PressureEffect = self.PressureEffect_curve( self.PressureChange )
        self.TissueFunctionEffect = not OtherTissue_Function.Failed
        if self.Clamp:
            self.NA = self.Level
        else:
            self.NA = self.PressureEffect * self.TissueFunctionEffect


    def Dervs_func(self):
        self.SinusPressure = CarotidSinus.Pressure
        self.AdaptedPressure = delay( self.RateConst, self.SinusPressure, self.AdaptedPressure, System.Dx, 0.97)


class SympsChemo:
    def __init__(self):
        self.Effect = None

    def Calc_func(self):
        self.Effect = 1.0

class CushingResponse:
    def __init__(self):
        self.Effect = None

    def Calc_func(self):
        self.Effect = 0.0

class SystemicVeins_AlphaReceptors:
    def __init__(self):
        self.Activity = None
        self.TotalAgonism = None
        self.NeuralAgonism = None
        self.HumoralAgonism = None
        self.Switch = False
        self.Setting = 0.0
        self.NEURALK = 0.333
        self.HUMORALK = 0.5

    def Calc_func(self):
        self.NeuralAgonism = GangliaGeneral.NA_Hz
        self.HumoralAgonism = AlphaPool.Effect
        self.TotalAgonism = ( self.NEURALK * self.NeuralAgonism ) + ( self.HUMORALK * self.HumoralAgonism )
        if self.Switch:
            self.Activity = self.Setting
        else:
            self.Activity = self.TotalAgonism * AlphaBlockade.Effect


class ChemoreceptorAcclimation:
    def __init__(self):
        self.NA = None
        self.Tau = 20.0
        self.Effect = 1.0

    def SteadyState_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.0, 10.0], [0.0, 1.0, 2.0], [0.0, 0.3, 0.0])

    def Parms_func(self):
        self.K = ( 1 / ( 60.0 * self.Tau ) )

    def Calc_func(self):
        self.SteadyState = self.SteadyState_curve( Chemoreceptors.BasicFiringRate )
        self.Effect = delay( self.K, self.SteadyState, self.Effect, System.Dx, 0.1)


class VagusNerve:
    def __init__(self):
        self.NA_Hz = None
        self.NA = None
        self.Switch = False
        self.Setting = 0.0
        self.Block_percent = 0.0

    def NA_Hz_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.5, 4.5], [8.0, 2.0, 0.0], [0.0, -2.0, 0.0])

    def Calc_func(self):
        if self.Switch:
            self.NA_Hz = self.Setting
        else:
            self.NA_Hz = self.NA_Hz_curve( SympsCNS.NA_Hz ) * ( 1.0 - ( self.Block_percent / 100.0 ) )

        self.NA = 0.667 * self.NA_Hz

class Nerves:
    def __init__(self):
        pass
    
class OtherTissue_Vasculature:
    def __init__(self):
        self.Tau = 30.0
        self.Effect = 1.0

    def PO2OnStimulus_curve(self, x):
        return cubic_hermite_spline(x, [41.0, 51.0, 61.0], [1.2, 1.0, 0.8], [0.0, -0.03, 0.0])

    def Parms_func(self):
        self.K = 1.0 / ( self.Tau * 1440.0 )

    def Calc_func(self):
        if OtherTissue_Function.Failed:
            self.Stimulus = 0.0
        else:
            self.Stimulus = self.PO2OnStimulus_curve( OtherTissue_Flow.PO2 )

        self.Effect = delay( self.K, self.Stimulus, self.Effect, System.Dx, None)


class OtherTissue_Function:
    def __init__(self):
        self.Failed = False
        self.Effect = None
        self.PhEffect = None
        self.ProteinEffect = None
        self.FuelEffect = None
        self.TemperatureEffect = None

    def PhOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [6.6, 6.7], [0.0, 1.0], [0.0, 0.0])

    def ProteinOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [3000.0, 5200.0], [0.0, 1.0], [0.0, 0.0])

    def FuelOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.9], [0.0, 1.0], [0.0, 0.0])

    def TemperatureOnFunction_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 37.0, 40.0, 46.0], [0.0, 1.0, 1.5, 0.0], [0.0, 0.12, 0.0, 0.0])

    def Calc_func(self):
        self.PhEffect = self.PhOnFunction_curve( OtherTissue_Ph.Ph )
        self.ProteinEffect = self.ProteinOnFunction_curve( CellProtein.Mass_G )
        self.FuelEffect = self.FuelOnFunction_curve( OtherTissue_Fuel.FractUseDelay )
        self.TemperatureEffect = self.TemperatureOnFunction_curve( HeatCore.Temp_C )
        self.Effect = self.PhEffect * self.ProteinEffect * self.FuelEffect * self.TemperatureEffect * OtherTissue_Structure.Effect

    def Wrapup_func(self):
        if not self.Failed and ( self.Effect < 0.2 ):
            self.Failed = True
        elif self.Failed and ( self.Effect > 0.4 ):
            self.Failed = False

class OtherTissue_Fuel:
    def __init__(self):
        self.FADelivered = None
        self.GlucoseDelivered = None
        self.KR = 0.026
        self.Ratio = None
        self.FAFraction = None
        self.GlucoseFraction = None
        self.FA_GlucoseFraction = None
        self.LacFraction = None
        self.FAUsed_CalperMin = None
        self.AerobicGlucoseUsed_CalperMin = None
        self.AnaerobicGlucoseUsed_CalperMin = None
        self.LacUsed_CalperMin = None
        self.FAUsed_mGperMin = None
        self.AerobicGlucoseUsed_mGperMin = None
        self.AnaerobicGlucoseUsed_mGperMin = None
        self.LacUsed_mGperMin = None
        self.TotalGlucoseUsed_mGperMin = None
        self.AnaerobicGlucoseDelivered = None
        self.FAFractionalDelivery = None
        self.AerobicGlucoseFractionalDelivery = None
        self.AnaerobicGlucoseFractionalDelivery = None
        self.MinimumFractionalDelivery = None
        self.FractUseDelay = 1.0

    def LacFraction_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 100.0], [0.0, 0.3], [0.0, 0.0])

    def Dervs_func(self):
        self.FADelivered = ( max( ( FAPool.conc_FA * OtherTissue_Flow.PlasmaFlow ), 0.0) )
        self.GlucoseDelivered = ( max( ( GlucosePool.conc_Glucose * OtherTissue_Flow.PlasmaFlow ), 0.0) )
        self.LacFraction = self.LacFraction_curve( OtherTissue_Lactate.conc_Lac__mGperdL )
        self.FA_GlucoseFraction = 1.0 - self.LacFraction
        self.Ratio = FAPool.conc_FA_mGperdL / GlucosePool.conc_Glucose_mGperdL
        self.FAFraction = self.FA_GlucoseFraction * ( self.Ratio / ( self.Ratio + self.KR ) )
        self.GlucoseFraction = self.FA_GlucoseFraction - self.FAFraction
        self.FAUsed_CalperMin = self.FAFraction * OtherTissue_Metabolism.AerobicCals
        self.FAUsed_mGperMin = self.FAUsed_CalperMin * Metabolism_Tools.Fat_mGperCal
        self.AerobicGlucoseUsed_CalperMin = self.GlucoseFraction * OtherTissue_Metabolism.AerobicCals
        self.AerobicGlucoseUsed_mGperMin = self.AerobicGlucoseUsed_CalperMin * Metabolism_Tools.CarboAerobic_mGperCal
        self.LacUsed_CalperMin = self.LacFraction * OtherTissue_Metabolism.AerobicCals
        self.LacUsed_mGperMin = self.LacUsed_CalperMin * Metabolism_Tools.Lac__mGperCal
        self.AnaerobicGlucoseDelivered = self.GlucoseDelivered - self.AerobicGlucoseUsed_mGperMin
        self.AnaerobicGlucoseUsed_CalperMin = ( min( OtherTissue_Metabolism.AnaerobicCals, self.AnaerobicGlucoseDelivered) )
        self.AnaerobicGlucoseUsed_mGperMin = self.AnaerobicGlucoseUsed_CalperMin * Metabolism_Tools.CarboAnaerobic_mGperCal
        self.TotalGlucoseUsed_mGperMin = self.AerobicGlucoseUsed_mGperMin + self.AnaerobicGlucoseUsed_mGperMin
        if self.FAUsed_mGperMin > 0.0:
            self.FAFractionalDelivery = ( min( ( self.FADelivered / self.FAUsed_mGperMin ), 1.0) )
        else:
            self.FAFractionalDelivery = 1.0

        if self.AerobicGlucoseUsed_mGperMin > 0.0:
            self.AerobicGlucoseFractionalDelivery = ( min( ( self.GlucoseDelivered / self.AerobicGlucoseUsed_mGperMin ), 1.0) )
        else:
            self.AerobicGlucoseFractionalDelivery = 1.0

        if self.AnaerobicGlucoseUsed_mGperMin > 0.0:
            self.AnaerobicGlucoseFractionalDelivery = ( min( ( self.AnaerobicGlucoseDelivered / self.AnaerobicGlucoseUsed_mGperMin ), 1.0) )
        else:
            self.AnaerobicGlucoseFractionalDelivery = 1.0

        self.MinimumFractionalDelivery = ( min( ( min( self.FAFractionalDelivery, self.AerobicGlucoseFractionalDelivery) ), self.AnaerobicGlucoseFractionalDelivery) )
        self.K = 0.5
        self.DxMax = 1.0
        self.FractUse = self.MinimumFractionalDelivery
        self.FractUseDelay = delay( self.K, self.FractUse, self.FractUseDelay, System.Dx, 0.01)


class OtherTissue_Size:
    def __init__(self):
        self.Vol = None
        self.Mass = None
        self.InitialMass = None
        self.Density = None
        self.LiquidMass = None
        self.LiquidDensity = 1.00
        self.LiquidVol = None
        self.InitialLiquidVol = None
        self.SolidMass = None
        self.InitialSolidMass = None
        self.SolidDensity = 1.17
        self.SolidVol = None
        self.FractTotal = None
        self.IFV = None
        self.InitialIFV = None
        self.CellH2O = None
        self.InitialCellH2O = None
        self.MassFractBase = 0.165
        self.H2OFractMass = 0.67
        self.SolidsFractMass = None

    def Initialize_func(self):
        self.InitialMass = self.MassFractBase * Weight.InitialOtherMass
        self.InitialLiquidVol = self.H2OFractMass * self.InitialMass / self.LiquidDensity
        self.SolidsFractMass = 1.0 - self.H2OFractMass
        self.InitialSolidMass = self.SolidsFractMass * self.InitialMass

    def ScaleH2O_func(self):
        self.FractTotal = self.InitialLiquidVol / TissueH2O.InitialVol
        self.InitialIFV = self.FractTotal * InterstitialWater.InitialVol
        self.InitialCellH2O = self.FractTotal * CellH2O.InitialVol

    def Calc_func(self):
        self.IFV = self.FractTotal * InterstitialWater.Vol
        self.CellH2O = self.FractTotal * CellH2O.Vol
        self.LiquidVol = self.IFV + self.CellH2O
        self.LiquidMass = self.LiquidVol * self.LiquidDensity
        self.SolidMass = self.InitialSolidMass
        self.SolidVol = self.SolidMass / self.SolidDensity
        self.Mass = self.LiquidMass + self.SolidMass
        self.Vol = self.LiquidVol + self.SolidVol
        self.Density = self.Mass / self.Vol

class OtherTissue_Pressure:
    def __init__(self):
        self.ArtyPressure = None
        self.VeinPressure = None
        self.PressureGradient = None
        self.PumpSwitch = False
        self.PumpSetting = 0.0

    def Calc_func(self):
        if self.PumpSwitch:
            self.ArtyPressure = self.PumpSetting
        else:
            self.ArtyPressure = SystemicArtys.Pressure

        self.VeinPressure = SystemicVeins.Pressure
        self.PressureGradient = ( max( ( self.ArtyPressure - self.VeinPressure ), 0.0) )

class OtherTissue_Ph:
    def __init__(self):
        self.Ph = None
        self.conc_SID = None
        self.conc_SID_mEqperL = None

    def CalcSID_func(self):
        self.conc_SID = KCell.conc_K_ + CellSID.OtherCations - CellSID.StrongAnions - OtherTissue_Lactate.conc_Lac_
        self.conc_SID_mEqperL = 1000.0 * self.conc_SID

    def CalcPh_func(self):
        PhCells.pCO2 = OtherTissue_CO2.PCO2
        PhCells.SID = self.conc_SID_mEqperL
        PhCells.Calc_func()
        self.Ph = PhCells.pH

class OtherTissue:
    def __init__(self):
        pass
    
class OtherTissue_AlphaReceptors:
    def __init__(self):
        self.Activity = None
        self.TotalAgonism = None
        self.NeuralAgonism = None
        self.HumoralAgonism = None
        self.Switch = False
        self.Setting = 0.0
        self.NEURALK = 0.333
        self.HUMORALK = 0.5

    def Calc_func(self):
        self.NeuralAgonism = GangliaGeneral.NA_Hz
        self.HumoralAgonism = AlphaPool.Effect
        self.TotalAgonism = ( self.NEURALK * self.NeuralAgonism ) + ( self.HUMORALK * self.HumoralAgonism )
        if self.Switch:
            self.Activity = self.Setting
        else:
            self.Activity = self.TotalAgonism * AlphaBlockade.Effect


class OtherTissue_Lactate:
    def __init__(self):
        self.conc_Lac_ = None
        self.conc_Lac__mEqperL = None
        self.conc_Lac__mGperdL = None
        self.DC = 270.0
        self.Made = None
        self.Made_mGperMin = None
        self.Used = None
        self.Used_mGperMin = None
        self.Outflux = None
        self.Outflux_0 = None
        self.K = None
        self.Alpha = None
        self.MEQ_ML_TO_MG_DL = 9008.0
        self.GLUCOSE_TO_LACTATE = 0.99
        self.MG_TO_MEQ = 0.0112
        self.Mass = 3.17

    def CalcConc_func(self):
        self.conc_Lac_ = self.Mass / OtherTissue_Size.LiquidVol
        self.conc_Lac__mEqperL = 1000.0 * self.conc_Lac_
        self.conc_Lac__mGperdL = self.MEQ_ML_TO_MG_DL * self.conc_Lac_

    def CalcDervs_func(self):
        self.Made_mGperMin = self.GLUCOSE_TO_LACTATE * OtherTissue_Fuel.AnaerobicGlucoseUsed_mGperMin
        self.Made = self.MG_TO_MEQ * self.Made_mGperMin
        self.Used_mGperMin = OtherTissue_Fuel.LacUsed_mGperMin
        self.Used = self.MG_TO_MEQ * self.Used_mGperMin
        self.K = self.DC / OtherTissue_Size.LiquidVol
        if System.Dx >=0:
            self.Alpha = 0.0
        elif ( self.K * System.Dx ) >= 100.0:
            self.Alpha = 4E-44
        elif True:
            self.Alpha = ( math.e ** ( - self.K * System.Dx ) )
        self.Outflux_0 = self.DC * ( self.conc_Lac_ - LacPool.conc_Lac_ )
        self.Outflux = ( self.Alpha * self.Outflux_0 ) + ( ( 1 - self.Alpha ) * ( self.Made + self.Used ) )
        self.Change = self.Made - self.Used - self.Outflux
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.032)


class OtherTissue_Metabolism:
    def __init__(self):
        self.TotalCalsUsed = None
        self.NormalCalsUsed = None
        self.InitialNormalCalsUsed = None
        self.NormalCalsUsed__CalperMinperG = 0.0106
        self.CalMultiplier = 1.0
        self.AerobicCals = None
        self.AnaerobicCals = None
        self.O2Need = None
        self.O2Lack = None

    def ScaleCals_func(self):
        self.InitialNormalCalsUsed = self.CalMultiplier * self.NormalCalsUsed__CalperMinperG * OtherTissue_Size.InitialMass

    def CalcCals_func(self):
        self.NormalCalsUsed = self.CalMultiplier * self.NormalCalsUsed__CalperMinperG * OtherTissue_Size.Mass
        self.TotalCalsUsed = self.NormalCalsUsed * Thyroid.Effect * HeatMetabolism.Core * OtherTissue_Structure.Effect
        self.O2Need = Metabolism_Tools.CalToO2 * self.TotalCalsUsed

    def SplitCals_func(self):
        self.O2Lack = self.O2Need - OtherTissue_Flow.O2Use
        self.AerobicCals = Metabolism_Tools.O2ToCal * OtherTissue_Flow.O2Use
        self.AnaerobicCals = Metabolism_Tools.O2ToCal * self.O2Lack

class OtherTissue_CO2:
    def __init__(self):
        self.conc_HCO3 = None
        self.conc_HCO3_mEqperL = None
        self.PCO2 = None
        self.InflowGas = None
        self.InflowBase = None
        self.OutflowBase = None
        self.conc_BloodHCO3 = None
        self.Outflow_0 = None
        self.K = None
        self.Alpha = None
        self.Mass = 50.7

    def CalcConc_func(self):
        self.conc_HCO3 = self.Mass / OtherTissue_Size.LiquidVol
        self.conc_HCO3_mEqperL = 1000.0 * self.conc_HCO3
        Tissue_BaseToGas.conc_HCO3 = self.conc_HCO3
        Tissue_BaseToGas.conc_SID = OtherTissue_Ph.conc_SID
        Tissue_BaseToGas.Calc_func()
        self.PCO2 = Tissue_BaseToGas.pCO2

    def CalcDervs_func(self):
        self.K = OtherTissue_Flow.BloodFlow / OtherTissue_Size.LiquidVol
        if System.Dx >=0:
            self.Alpha = 0.0
        elif ( self.K * System.Dx ) >= 100.0:
            self.Alpha = 4E-44
        elif True:
            self.Alpha = ( math.e ** ( - self.K * System.Dx ) )
        self.InflowGas = Metabolism_RespiratoryQuotient.RQ * OtherTissue_Flow.O2Use
        self.InflowBase = CO2Tools.LitersToMols * self.InflowGas
        Blood_GasToBase.pCO2 = self.PCO2
        Blood_GasToBase.conc_SID = BloodIons.conc_SID
        Blood_GasToBase.Calc_func()
        self.conc_BloodHCO3 = Blood_GasToBase.conc_HCO3
        self.Outflow_0 = OtherTissue_Flow.BloodFlow * ( self.conc_BloodHCO3 - CO2Artys.conc_HCO3 )
        self.OutflowBase = ( self.Alpha * self.Outflow_0 ) + ( ( 1 - self.Alpha ) * self.InflowBase )
        self.Change = self.InflowBase - self.OutflowBase
        self.Mass = diffeq( self.Change, System.Dx, self.Mass, 0.51)


class OtherTissue_Flow:
    def __init__(self):
        self.Conductance = None
        self.BasicConductance = 4.2
        self.A2Effect = None
        self.SympsEffect = None
        self.ADHEffect = None
        self.PO2Effect = None
        self.AerobicFraction = None
        self.O2Use = None
        self.conc_O2 = None
        self.BloodFlow = None
        self.PlasmaFlow = None
        self.PO2 = 45.0
    def A2OnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.3, 3.5], [1.05, 1.0, 0.5], [0.0, -0.08, 0.0])

    def SympsOnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 1.0, 5.0], [1.3, 1.0, 0.1], [0.0, -0.3, 0.0])

    def PO2OnConductance_curve(self, x):
        return cubic_hermite_spline(x, [10.0, 30.0], [2.0, 1.0], [0.0, 0.0])

    def ADHOnConductance_curve(self, x):
        return cubic_hermite_spline(x, [0.8, 3.0], [1.0, 0.1], [0.0, 0.0])

    def PO2OnAerobicFraction_curve(self, x):
        return cubic_hermite_spline(x, [2.0, 10.0], [0.0, 1.0], [0.0, 0.0])

    def Calc_func(self):
        self.A2Effect = self.A2OnConductance_curve( A2Pool.Log10Conc )
        self.SympsEffect = self.SympsOnConductance_curve( OtherTissue_AlphaReceptors.Activity )
        self.ADHEffect = self.ADHOnConductance_curve( ADHPool.Log10Conc )
        self.SearchMax = PO2Artys.Pressure

        def PO2implicitfunc(PO2):
            self.PO2Effect = self.PO2OnConductance_curve( PO2 )
            self.Conductance = self.BasicConductance * self.A2Effect * self.SympsEffect * self.PO2Effect * self.ADHEffect * Viscosity.ConductanceEffect * Anesthesia.VascularConductance * OtherTissue_Vasculature.Effect
            self.BloodFlow = ( max( ( OtherTissue_Pressure.PressureGradient * self.Conductance ), 0.0) )
            self.AerobicFraction = self.PO2OnAerobicFraction_curve( PO2 )
            self.O2Use = OtherTissue_Metabolism.O2Need * self.AerobicFraction
            if self.BloodFlow > 0.0:
                self.conc_O2 = O2Artys.conc_O2 - ( self.O2Use / self.BloodFlow )
            else:
                self.conc_O2 = 0.0

            HgbTissue.conc_O2 = self.conc_O2
            HgbTissue.O2ToPO2_func()
            PO2End = HgbTissue.pO2

            return PO2End
        self.PO2 = impliciteq( PO2implicitfunc, self.PO2, 0.45)
        self.PlasmaFlow = self.BloodFlow * BloodVol.PVCrit

class OtherTissue_Structure:
    def __init__(self):
        self.PhFactor = None
        self.PhEffect = None
        self.PhMaximum = 0.1
        self.FuelFactor = None
        self.FuelEffect = None
        self.FuelMaximum = 0.05
        self.TemperatureFactor = None
        self.TemperatureEffect = None
        self.TemperatureMaximum = 0.05
        self.Effect = 1.0

    def PhFactor_curve(self, x):
        return cubic_hermite_spline(x, [6.5, 6.6], [1.0, 0.0], [0.0, 0.0])

    def FuelFactor_curve(self, x):
        return cubic_hermite_spline(x, [0.0, 0.3], [1.0, 0.0], [0.0, 0.0])

    def TemperatureFactor_curve(self, x):
        return cubic_hermite_spline(x, [44.0, 46.0], [0.0, 1.0], [0.0, 0.0])

    def Calc_func(self):
        self.PhFactor = self.PhFactor_curve( OtherTissue_Ph.Ph )
        self.PhEffect = self.PhFactor * self.PhMaximum
        self.FuelFactor = self.FuelFactor_curve( OtherTissue_Fuel.FractUseDelay )
        self.FuelEffect = self.FuelFactor * self.FuelMaximum
        self.TemperatureFactor = self.TemperatureFactor_curve( HeatCore.Temp_C )
        self.TemperatureEffect = self.TemperatureFactor * self.TemperatureMaximum
        self.F1 = 0.0
        self.F2 = self.PhEffect + self.FuelEffect + self.TemperatureEffect
        self.Effect = backwardeuler( self.F1, self.F2, System.Dx, self.Effect, None)


class IVDrip:
    def __init__(self):
        self.Switch = False
        self.H2OSetting = 0.0
        self.H2ORate = None
        self.ClinicalSaline = 0.0
        self.ClinicalSalineRate = None
        self.conc_NaCl = 0.0
        self.NaClRate = None
        self.conc_Bicarb = 0.0
        self.BicarbRate = None
        self.conc_NH4Cl = 0.0
        self.NH4ClRate = None
        self.conc_KCl = 0.0
        self.KClRate = None
        self.conc_Protein = 0.0
        self.ProteinRate = None
        self.NaRate = None
        self.KRate = None
        self.ClRate = None
        self.conc_Osm = None
        self.TotalH2O = 0.0

    def Parms_func(self):
        if self.Switch:
            self.H2ORate = self.H2OSetting
        else:
            self.H2ORate = 0.0

        self.ClinicalSalineRate = 0.001 * self.ClinicalSaline * self.H2ORate
        self.NaClRate = 0.001 * self.conc_NaCl * self.H2ORate
        self.BicarbRate = 0.001 * self.conc_Bicarb * self.H2ORate
        self.NH4ClRate = 0.001 * self.conc_NH4Cl * self.H2ORate
        self.KClRate = 0.001 * self.conc_KCl * self.H2ORate
        self.ProteinRate = 0.01 * self.conc_Protein * self.H2ORate
        self.NaRate = self.ClinicalSalineRate + self.NaClRate + self.BicarbRate
        self.KRate = self.KClRate
        self.ClRate = self.ClinicalSalineRate + self.NaClRate + self.NH4ClRate + self.KClRate
        self.conc_Osm = ( 2 * self.ClinicalSaline ) + ( 2 * self.conc_NaCl ) + ( 2 * self.conc_Bicarb ) + ( 2 * self.conc_NH4Cl ) + ( 2 * self.conc_KCl )

    def Dervs_func(self):
        self.H2OChange = self.H2ORate
        self.TotalH2O = diffeq( self.H2OChange, System.Dx, self.TotalH2O, None)


    def Reset_func(self):
        self.TotalH2O = 0.0

class Context:

    def Calc_func(self):
        Traits.Calc_func()
        Start.Calc_func()

class Traits:

    def Calc_func(self):
        Descriptors.Calc_func()
        Values.Calc_func()

class Values_Muscularity:
    def __init__(self):
        self.MALE_BELOWNORMAL = 18.0
        self.MALE_NORMAL = 27.4
        self.MALE_ABOVENORMAL = 40.0
        self.MALE_TRAINEDATHLETE = 58.0
        self.FEMALE_BELOWNORMAL = 12.0
        self.FEMALE_NORMAL = 17.9
        self.FEMALE_ABOVENORMAL = 23.0
        self.FEMALE_TRAINEDATHLETE = 34.0
        self.Mass_kG = None

    def Calc_func(self):
        if Descriptors_Gender.IsMale:
            self.Male_func()
        else:
            self.Female_func()

    def Male_func(self):
        if Descriptors_Muscularity.IsBelowNormal:
            self.Mass_kG = self.MALE_BELOWNORMAL
        elif Descriptors_Muscularity.IsNormal:
            self.Mass_kG = self.MALE_NORMAL
        elif Descriptors_Muscularity.IsAboveNormal:
            self.Mass_kG = self.MALE_ABOVENORMAL
        elif Descriptors_Muscularity.IsTrainedAthlete:
            self.Mass_kG = self.MALE_TRAINEDATHLETE
        elif True:
            pass

    def Female_func(self):
        if Descriptors_Muscularity.IsBelowNormal:
            self.Mass_kG = self.FEMALE_BELOWNORMAL
        elif Descriptors_Muscularity.IsNormal:
            self.Mass_kG = self.FEMALE_NORMAL
        elif Descriptors_Muscularity.IsAboveNormal:
            self.Mass_kG = self.FEMALE_ABOVENORMAL
        elif Descriptors_Muscularity.IsTrainedAthlete:
            self.Mass_kG = self.FEMALE_TRAINEDATHLETE
        elif True:
            pass

class Values:

    def Calc_func(self):
        Values_Gender.Calc_func()
        Values_Age.Calc_func()
        Values_Height.Calc_func()
        Values_Adiposity.Calc_func()
        Values_OtherMass.Calc_func()
        Values_Muscularity.Calc_func()

class Values_Gender:
    def __init__(self):
        self.IsMale = True
        self.IsFemale = False
        self.Value = 0

    def Calc_func(self):
        self.IsMale = Descriptors_Gender.IsMale
        self.IsFemale = Descriptors_Gender.IsFemale
        self.Value = Descriptors_Gender.Value

class Values_Adiposity:
    def __init__(self):
        self.MALE_UNDERWEIGHT = 10.0
        self.MALE_NORMALWEIGHT = 16.6
        self.MALE_OVERWEIGHT = 26.0
        self.MALE_OBESE = 44.0
        self.MALE_MORBIDLYOBESE = 110.0
        self.FEMALE_UNDERWEIGHT = 14.0
        self.FEMALE_NORMALWEIGHT = 20.2
        self.FEMALE_OVERWEIGHT = 32.0
        self.FEMALE_OBESE = 46.0
        self.FEMALE_MORBIDLYOBESE = 110.0
        self.Mass_kG = None

    def Calc_func(self):
        if Descriptors_Gender.IsMale:
            self.Male_func()
        else:
            self.Female_func()

    def Male_func(self):
        if Descriptors_Adiposity.IsUnderweight:
            self.Mass_kG = self.MALE_UNDERWEIGHT
        elif Descriptors_Adiposity.IsNormalWeight:
            self.Mass_kG = self.MALE_NORMALWEIGHT
        elif Descriptors_Adiposity.IsOverweight:
            self.Mass_kG = self.MALE_OVERWEIGHT
        elif Descriptors_Adiposity.IsObese:
            self.Mass_kG = self.MALE_OBESE
        elif Descriptors_Adiposity.IsMorbidlyObese:
            self.Mass_kG = self.MALE_MORBIDLYOBESE
        elif True:
            pass

    def Female_func(self):
        if Descriptors_Adiposity.IsUnderweight:
            self.Mass_kG = self.FEMALE_UNDERWEIGHT
        elif Descriptors_Adiposity.IsNormalWeight:
            self.Mass_kG = self.FEMALE_NORMALWEIGHT
        elif Descriptors_Adiposity.IsOverweight:
            self.Mass_kG = self.FEMALE_OVERWEIGHT
        elif Descriptors_Adiposity.IsObese:
            self.Mass_kG = self.FEMALE_OBESE
        elif Descriptors_Adiposity.IsMorbidlyObese:
            self.Mass_kG = self.FEMALE_MORBIDLYOBESE
        elif True:
            pass

class Values_OtherMass:
    def __init__(self):
        self.MALE_SMALL = 19.0
        self.MALE_NORMAL = 22.0
        self.MALE_LARGE = 30.0
        self.MALE_VERYLARGE = 44.0
        self.FEMALE_SMALL = 15.0
        self.FEMALE_NORMAL = 20.0
        self.FEMALE_LARGE = 28.0
        self.FEMALE_VERYLARGE = 36.0
        self.Mass = None
        self.Mass_kG = None

    def Calc_func(self):
        if Descriptors_Gender.IsMale:
            self.Male_func()
        else:
            self.Female_func()
        self.Mass = 1000.0 * self.Mass_kG

    def Male_func(self):
        if Descriptors_BodySize.IsSmall:
            self.Mass_kG = self.MALE_SMALL
        elif Descriptors_BodySize.IsNormal:
            self.Mass_kG = self.MALE_NORMAL
        elif Descriptors_BodySize.IsLarge:
            self.Mass_kG = self.MALE_LARGE
        elif Descriptors_BodySize.IsVeryLarge:
            self.Mass_kG = self.MALE_VERYLARGE
        elif True:
            pass

    def Female_func(self):
        if Descriptors_BodySize.IsSmall:
            self.Mass_kG = self.FEMALE_SMALL
        elif Descriptors_BodySize.IsNormal:
            self.Mass_kG = self.FEMALE_NORMAL
        elif Descriptors_BodySize.IsLarge:
            self.Mass_kG = self.FEMALE_LARGE
        elif Descriptors_BodySize.IsVeryLarge:
            self.Mass_kG = self.FEMALE_VERYLARGE
        elif True:
            pass

class Values_Height:
    def __init__(self):
        self.MALE_SHORT = 160.0
        self.MALE_NORMAL = 178.0
        self.MALE_TALL = 200.0
        self.MALE_VERYTALL = 230.0
        self.FEMALE_SHORT = 150.0
        self.FEMALE_NORMAL = 165.0
        self.FEMALE_TALL = 180.0
        self.FEMALE_VERYTALL = 200.0
        self.Height_cM = None

    def Calc_func(self):
        if Descriptors_Gender.IsMale:
            self.Male_func()
        else:
            self.Female_func()

    def Male_func(self):
        if Descriptors_BodySize.IsSmall:
            self.Height_cM = self.MALE_SHORT
        elif Descriptors_BodySize.IsNormal:
            self.Height_cM = self.MALE_NORMAL
        elif Descriptors_BodySize.IsLarge:
            self.Height_cM = self.MALE_TALL
        elif Descriptors_BodySize.IsVeryLarge:
            self.Height_cM = self.MALE_VERYTALL
        elif True:
            pass

    def Female_func(self):
        if Descriptors_BodySize.IsSmall:
            self.Height_cM = self.FEMALE_SHORT
        elif Descriptors_BodySize.IsNormal:
            self.Height_cM = self.FEMALE_NORMAL
        elif Descriptors_BodySize.IsLarge:
            self.Height_cM = self.FEMALE_TALL
        elif Descriptors_BodySize.IsVeryLarge:
            self.Height_cM = self.FEMALE_VERYTALL
        elif True:
            pass

class Values_Age:
    def __init__(self):
        self.YOUNG = 19.0
        self.YOUNGISH = 28.0
        self.MIDDLEAGED = 37.0
        self.OLD = 65.0
        self.VERYOLD = 89.0
        self.Age_Years = None

    def Calc_func(self):
        if Descriptors_Age.IsYoung:
            self.Age_Years = self.YOUNG
        elif Descriptors_Age.IsYoungish:
            self.Age_Years = self.YOUNGISH
        elif Descriptors_Age.IsMiddleaged:
            self.Age_Years = self.MIDDLEAGED
        elif Descriptors_Age.IsOld:
            self.Age_Years = self.OLD
        elif Descriptors_Age.IsVeryOld:
            self.Age_Years = self.VERYOLD
        elif True:
            pass

class Descriptors:

    def Calc_func(self):
        Descriptors_Gender.Calc_func()
        Descriptors_Age.Calc_func()
        Descriptors_BodySize.Calc_func()
        Descriptors_Adiposity.Calc_func()
        Descriptors_Muscularity.Calc_func()

class Male:
    def __init__(self):
        self.IsMale = True
        self.IsFemale = False
        self.Value = "MALE"
    
class Descriptors_Gender:
    def __init__(self):
        self.MALE = 0
        self.FEMALE = 1
        self.IsMale = False #changed from Hummod default of True
        self.IsFemale = True #changed from Hummod default of False
        self.Value = 1 #changed from Hummod default of 0

    def Calc_func(self):
        pass

class Female:
    def __init__(self):
        self.IsMale = False
        self.IsFemale = True
        self.Value = "FEMALE"
    
class Descriptors_Adiposity:
    def __init__(self):
        self.UNDERWEIGHT = 0
        self.NORMALWEIGHT = 1
        self.OVERWEIGHT = 2
        self.OBESE = 3
        self.MORBIDLYOBESE = 4
        self.IsUnderweight = False
        self.IsNormalWeight = True
        self.IsOverweight = False
        self.IsObese = False
        self.IsMorbidlyObese = False
        self.Value = 1

    def Calc_func(self):
        pass

class MorbidlyObese:
    def __init__(self):
        self.IsNormalWeight = False
        self.IsMorbidlyObese = True
        self.Value = "MORBIDLYOBESE"
    
class Overweight:
    def __init__(self):
        self.IsNormalWeight = False
        self.IsOverweight = True
        self.Value = "OVERWEIGHT"
    
class Underweight:
    def __init__(self):
        self.IsNormalWeight = False
        self.IsUnderweight = True
        self.Value = "UNDERWEIGHT"
    
class Obese:
    def __init__(self):
        self.IsNormalWeight = False
        self.IsObese = True
        self.Value = "OBESE"
    
class NormalWeight:
    def __init__(self):
        self.IsNormalWeight = True
        self.Value = "NORMALWEIGHT"
    
class Descriptors_Muscularity:
    def __init__(self):
        self.BELOWNORMAL = 0
        self.NORMAL = 1
        self.ABOVENORMAL = 2
        self.TRAINEDATHLETE = 3
        self.IsBelowNormal = False
        self.IsNormal = True
        self.IsAboveNormal = False
        self.IsTrainedAthlete = False
        self.Value = 1

    def Calc_func(self):
        pass

class AboveNormal:
    def __init__(self):
        self.IsNormal = False
        self.IsAboveNormal = True
        self.Value = "ABOVENORMAL"
    
class TrainedAthlete:
    def __init__(self):
        self.IsNormal = False
        self.IsTrainedAthlete = True
        self.Value = "TRAINEDATHLETE"
    
class Normal:
    def __init__(self):
        self.IsNormal = True
        self.Value = "NORMAL"
    
class BelowNormal:
    def __init__(self):
        self.IsNormal = False
        self.IsBelowNormal = True
        self.Value = "BELOWNORMAL"
    
class Descriptors_BodySize:
    def __init__(self):
        self.SMALL = 0
        self.NORMAL = 1
        self.LARGE = 2
        self.VERYLARGE = 3
        self.IsSmall = False
        self.IsNormal = True
        self.IsLarge = False
        self.IsVeryLarge = False
        self.Value = 1

    def Calc_func(self):
        pass

class VeryLarge:
    def __init__(self):
        self.IsNormal = False
        self.IsVeryLarge = True
        self.Value = "VERYLARGE"
    
class Large:
    def __init__(self):
        self.IsNormal = False
        self.IsLarge = True
        self.Value = "LARGE"
    
class Small:
    def __init__(self):
        self.IsNormal = False
        self.IsSmall = True
        self.Value = "SMALL"
    
class Normal:
    def __init__(self):
        self.IsNormal = True
        self.Value = "NORMAL"
    
class Descriptors_Age:
    def __init__(self):
        self.YOUNG = 0
        self.YOUNGISH = 1
        self.MIDDLEAGED = 2
        self.OLD = 3
        self.VERYOLD = 4
        self.IsYoung = False
        self.IsYoungish = False
        self.IsMiddleaged = True
        self.IsOld = False
        self.IsVeryOld = False
        self.Value = 2

    def Calc_func(self):
        pass

class Old:
    def __init__(self):
        self.IsMiddleaged = False
        self.IsOld = True
        self.Value = "OLD"
    
class Middleaged:
    def __init__(self):
        self.IsMiddleaged = True
        self.Value = "MIDDLEAGED"
    
class Youngish:
    def __init__(self):
        self.IsMiddleaged = False
        self.IsYoungish = True
        self.Value = "YOUNGISH"
    
class Young:
    def __init__(self):
        self.IsMiddleaged = False
        self.IsYoung = True
        self.Value = "YOUNG"
    
class VeryOld:
    def __init__(self):
        self.IsMiddleaged = False
        self.IsVeryOld = True
        self.Value = "VERYOLD"
    
class Start_OrganConductance:

    def Calc_func(self):
        Organs_ScaleConductance.Calc_func()

class Start:

    def Calc_func(self):
        Start_Morphology.Calc_func()
        Start_WholeBody.Calc_func()
        Start_Heat.Calc_func()
        Start_Electrolytes.Calc_func()
        Start_Metabolism.Calc_func()
        Start_Hormones.Calc_func()
        Start_OrganCalories.Calc_func()
        Start_OrganConductance.Calc_func()

class Start_OrganCalories:

    def Calc_func(self):
        Organs_ScaleCals.Calc_func()

class Start_Heat:

    def Calc_func(self):
        HeatCore.Initialize_func()
        HeatSkin.Initialize_func()
        HeatSkeletalMuscle.Initialize_func()

class Start_Height:

    def Calc_func(self):
        Height.Initialize_func()

class Start_Morphology:

    def Calc_func(self):
        Start_Age.Calc_func()
        Start_Height.Calc_func()
        Start_Gender.Calc_func()
        Start_Weight.Calc_func()
        Start_FatSize.Calc_func()
        Start_SkeletalMuscleSize.Calc_func()

class Start_FatSize:

    def Calc_func(self):
        Fat_Size.InitializeFatMass_func()

class Start_Weight:

    def Calc_func(self):
        Weight.InitializeOtherMass_func()

class Start_SkeletalMuscleSize:

    def Calc_func(self):
        SkeletalMuscle_Size.InitializeMuscleMass_func()

class Start_Gender:

    def Calc_func(self):
        Gender.IsMale = Values_Gender.IsMale
        Gender.IsFemale = Values_Gender.IsFemale
        Gender.Value = Values_Gender.Value

class Start_Age:

    def Calc_func(self):
        Age.Initialize_func()

class Start_BloodSize:

    def Calc_func(self):
        BloodVol.Initialize_func()
        PlasmaVol.Initialize_func()
        RBCVol.Initialize_func()
        RBCSolids.Initialize_func()
        RBCH2O.Initialize_func()

class Start_WholeBody:

    def Calc_func(self):
        Start_OrganSize.Calc_func()
        Start_General.Calc_func()
        Start_BloodSize.Calc_func()
        Start_BodyH2O.Calc_func()
        Start_BodySize.Calc_func()

class Start_BodyH2O:

    def Calc_func(self):
        TissueH2O.Initialize_func()
        ExternalH2O.Initialize_func()
        BodyH2O.Initialize_func()
        ECFV.Initialize_func()
        ICFV.Initialize_func()
        InterstitialWater.Initialize_func()
        CellH2O.Initialize_func()
        Organs_ScaleH2O.ScaleH2O_func()

class Start_General:
    def __init__(self):
        self.X_Textbook = None
        self.InitialLeanMass = None
        self.InitialFatMass = None
        self.LeanPart = None
        self.LeanFraction = 0.0000182
        self.FatPart = None
        self.FatFraction = 0.0000060

    def Calc_func(self):
        self.InitialLeanMass = Bone_Size.InitialMass + Brain_Size.InitialMass + GITract_Size.InitialMass + Kidney_Size.InitialMass + LeftHeart_Size.InitialMass + Liver_Size.InitialMass + OtherTissue_Size.InitialMass + RespiratoryMuscle_Size.InitialMass + RightHeart_Size.InitialMass + SkeletalMuscle_Size.InitialMass + Skin_Size.InitialMass
        self.InitialFatMass = Fat_Size.InitialMass
        self.LeanPart = self.LeanFraction * self.InitialLeanMass
        self.FatPart = self.FatFraction * self.InitialFatMass
        self.X_Textbook = self.LeanPart + self.FatPart

class Start_BodySize:

    def Calc_func(self):
        Weight.Initialize_func()
        Height.Initialize_func()

class Start_OrganSize:
    def __init__(self):
        self.SumMassFractBase = None

    def Calc_func(self):
        Fat_Size.Initialize_func()
        LipidDeposits.Initialize_func()
        Bone_Size.Initialize_func()
        Bone_Mineral.Initialize_func()
        Brain_Size.Initialize_func()
        GITract_Size.Initialize_func()
        Kidney_Size.Initialize_func()
        LeftHeart_Size.Initialize_func()
        LeftHeart_ContractileProtein.Initialize_func()
        Liver_Size.Initialize_func()
        OtherTissue_Size.Initialize_func()
        RespiratoryMuscle_Size.Initialize_func()
        RespiratoryMuscle_ContractileProtein.Initialize_func()
        RightHeart_Size.Initialize_func()
        RightHeart_ContractileProtein.Initialize_func()
        SkeletalMuscle_Size.Initialize_func()
        SkeletalMuscle_ContractileProtein.Initialize_func()
        Skin_Size.Initialize_func()
        self.SumMassFractBase = Bone_Size.MassFractBase + Brain_Size.MassFractBase + GITract_Size.MassFractBase + Kidney_Size.MassFractBase + LeftHeart_Size.MassFractBase + Liver_Size.MassFractBase + OtherTissue_Size.MassFractBase + RespiratoryMuscle_Size.MassFractBase + RightHeart_Size.MassFractBase + Skin_Size.MassFractBase

class Start_Creatinine:

    def Calc_func(self):
        CreatininePool.Init_func()

class Start_Creatine:

    def Calc_func(self):
        pass

class Start_Metabolism:

    def Calc_func(self):
        Start_Glucose.Calc_func()
        Start_FattyAcid.Calc_func()
        Start_AminoAcid.Calc_func()
        Start_KetoAcid.Calc_func()
        Start_Triglyceride.Calc_func()
        Start_Urea.Calc_func()
        Start_Creatine.Calc_func()
        Start_Creatinine.Calc_func()

class Start_Urea:

    def Calc_func(self):
        UreaPool.Init_func()

class Start_FattyAcid:

    def Calc_func(self):
        FAPool.Init_func()

class Start_AminoAcid:

    def Calc_func(self):
        AAPool.Init_func()

class Start_Triglyceride:

    def Calc_func(self):
        TriglyceridePool.Init_func()

class Start_Glucose:

    def Calc_func(self):
        GlucosePool.Init_func()

class Start_KetoAcid:

    def Calc_func(self):
        KAPool.Init_func()

class Start_Testosterone:

    def Calc_func(self):
        Testosterone.Init_func()

class Start_Progesterone:

    def Calc_func(self):
        Progesterone.Init_func()

class Start_Norepinephrine:

    def Calc_func(self):
        NEPool.Init_func()

class Start_Epinephrine:

    def Calc_func(self):
        EpiPool.Init_func()

class Start_ANP:

    def Calc_func(self):
        ANPPool.Init_func()

class Start_Aldosterone:

    def Calc_func(self):
        AldoPool.Init_func()

class Start_Renin:

    def Calc_func(self):
        ReninPool.Init_func()

class Start_FSH:

    def Calc_func(self):
        FSH_Circulating.Init_func()

class Start_Leptin:

    def Calc_func(self):
        LeptinPool.Init_func()

class Start_Insulin:

    def Calc_func(self):
        InsulinPool.Init_func()

class Start_Inhibin:

    def Calc_func(self):
        Inhibin.Init_func()

class Start_LH:

    def Calc_func(self):
        LH_Circulating.Init_func()

class Start_ADH:

    def Calc_func(self):
        ADHPool.Init_func()

class Start_Estradiol:

    def Calc_func(self):
        Estradiol.Init_func()

class Start_hCG:

    def Calc_func(self):
        hCG.Init_func()

class Start_Glucagon:

    def Calc_func(self):
        GlucagonPool.Init_func()

class Start_EPO:

    def Calc_func(self):
        EPOPool.Init_func()

class Start_Hormones:

    def Calc_func(self):
        Start_Epinephrine.Calc_func()
        Start_Norepinephrine.Calc_func()
        Start_ADH.Calc_func()
        Start_Aldosterone.Calc_func()
        Start_ANP.Calc_func()
        Start_EPO.Calc_func()
        Start_Estradiol.Calc_func()
        Start_FSH.Calc_func()
        Start_Glucagon.Calc_func()
        Start_hCG.Calc_func()
        Start_Inhibin.Calc_func()
        Start_Insulin.Calc_func()
        Start_Leptin.Calc_func()
        Start_LH.Calc_func()
        Start_Progesterone.Calc_func()
        Start_Renin.Calc_func()
        Start_Testosterone.Calc_func()
        Start_ThyroidHormone.Calc_func()

class Start_ThyroidHormone:

    def Calc_func(self):
        ThyroidPool.Init_func()

class Start_ExtracellularPotassium:

    def Calc_func(self):
        KPool.Init_func()

class Start_ExtracellularPhosphate:

    def Calc_func(self):
        PO4Pool.Init_func()

class Start_ExtracellularSodium:

    def Calc_func(self):
        NaPool.Init_func()

class Start_ExtracellularSulphate:

    def Calc_func(self):
        SO4Pool.Init_func()

class Start_ExtracellularChloride:

    def Calc_func(self):
        ClPool.Init_func()

class Start_CellularPotassium:

    def Calc_func(self):
        KCell.Init_func()

class Start_Electrolytes:

    def Calc_func(self):
        Start_ExtracellularSodium.Calc_func()
        Start_ExtracellularChloride.Calc_func()
        Start_ExtracellularPhosphate.Calc_func()
        Start_ExtracellularPotassium.Calc_func()
        Start_CellularPotassium.Calc_func()
        Start_ExtracellularSulphate.Calc_func()

class Start_OrganConductance:

    def Calc_func(self):
        Organs_ScaleConductance.Calc_func()

class Start:

    def Calc_func(self):
        Start_Morphology.Calc_func()
        Start_WholeBody.Calc_func()
        Start_Heat.Calc_func()
        Start_Electrolytes.Calc_func()
        Start_Metabolism.Calc_func()
        Start_Hormones.Calc_func()
        Start_OrganCalories.Calc_func()
        Start_OrganConductance.Calc_func()

class Start_OrganCalories:

    def Calc_func(self):
        Organs_ScaleCals.Calc_func()

class Start_Heat:

    def Calc_func(self):
        HeatCore.Initialize_func()
        HeatSkin.Initialize_func()
        HeatSkeletalMuscle.Initialize_func()

class Start_Height:

    def Calc_func(self):
        Height.Initialize_func()

class Start_Morphology:

    def Calc_func(self):
        Start_Age.Calc_func()
        Start_Height.Calc_func()
        Start_Gender.Calc_func()
        Start_Weight.Calc_func()
        Start_FatSize.Calc_func()
        Start_SkeletalMuscleSize.Calc_func()

class Start_FatSize:

    def Calc_func(self):
        Fat_Size.InitializeFatMass_func()

class Start_Weight:

    def Calc_func(self):
        Weight.InitializeOtherMass_func()

class Start_SkeletalMuscleSize:

    def Calc_func(self):
        SkeletalMuscle_Size.InitializeMuscleMass_func()

class Start_Gender:

    def Calc_func(self):
        Gender.IsMale = Values_Gender.IsMale
        Gender.IsFemale = Values_Gender.IsFemale
        Gender.Value = Values_Gender.Value

class Start_Age:

    def Calc_func(self):
        Age.Initialize_func()

class Start_BloodSize:

    def Calc_func(self):
        BloodVol.Initialize_func()
        PlasmaVol.Initialize_func()
        RBCVol.Initialize_func()
        RBCSolids.Initialize_func()
        RBCH2O.Initialize_func()

class Start_WholeBody:

    def Calc_func(self):
        Start_OrganSize.Calc_func()
        Start_General.Calc_func()
        Start_BloodSize.Calc_func()
        Start_BodyH2O.Calc_func()
        Start_BodySize.Calc_func()

class Start_BodyH2O:

    def Calc_func(self):
        TissueH2O.Initialize_func()
        ExternalH2O.Initialize_func()
        BodyH2O.Initialize_func()
        ECFV.Initialize_func()
        ICFV.Initialize_func()
        InterstitialWater.Initialize_func()
        CellH2O.Initialize_func()
        Organs_ScaleH2O.ScaleH2O_func()

class Start_General:
    def __init__(self):
        self.X_Textbook = None
        self.InitialLeanMass = None
        self.InitialFatMass = None
        self.LeanPart = None
        self.LeanFraction = 0.0000182
        self.FatPart = None
        self.FatFraction = 0.0000060

    def Calc_func(self):
        self.InitialLeanMass = Bone_Size.InitialMass + Brain_Size.InitialMass + GITract_Size.InitialMass + Kidney_Size.InitialMass + LeftHeart_Size.InitialMass + Liver_Size.InitialMass + OtherTissue_Size.InitialMass + RespiratoryMuscle_Size.InitialMass + RightHeart_Size.InitialMass + SkeletalMuscle_Size.InitialMass + Skin_Size.InitialMass
        self.InitialFatMass = Fat_Size.InitialMass
        self.LeanPart = self.LeanFraction * self.InitialLeanMass
        self.FatPart = self.FatFraction * self.InitialFatMass
        self.X_Textbook = self.LeanPart + self.FatPart

class Start_BodySize:

    def Calc_func(self):
        Weight.Initialize_func()
        Height.Initialize_func()

class Start_OrganSize:
    def __init__(self):
        self.SumMassFractBase = None

    def Calc_func(self):
        Fat_Size.Initialize_func()
        LipidDeposits.Initialize_func()
        Bone_Size.Initialize_func()
        Bone_Mineral.Initialize_func()
        Brain_Size.Initialize_func()
        GITract_Size.Initialize_func()
        Kidney_Size.Initialize_func()
        LeftHeart_Size.Initialize_func()
        LeftHeart_ContractileProtein.Initialize_func()
        Liver_Size.Initialize_func()
        OtherTissue_Size.Initialize_func()
        RespiratoryMuscle_Size.Initialize_func()
        RespiratoryMuscle_ContractileProtein.Initialize_func()
        RightHeart_Size.Initialize_func()
        RightHeart_ContractileProtein.Initialize_func()
        SkeletalMuscle_Size.Initialize_func()
        SkeletalMuscle_ContractileProtein.Initialize_func()
        Skin_Size.Initialize_func()
        self.SumMassFractBase = Bone_Size.MassFractBase + Brain_Size.MassFractBase + GITract_Size.MassFractBase + Kidney_Size.MassFractBase + LeftHeart_Size.MassFractBase + Liver_Size.MassFractBase + OtherTissue_Size.MassFractBase + RespiratoryMuscle_Size.MassFractBase + RightHeart_Size.MassFractBase + Skin_Size.MassFractBase

class Start_Creatinine:

    def Calc_func(self):
        CreatininePool.Init_func()

class Start_Creatine:

    def Calc_func(self):
        pass

class Start_Metabolism:

    def Calc_func(self):
        Start_Glucose.Calc_func()
        Start_FattyAcid.Calc_func()
        Start_AminoAcid.Calc_func()
        Start_KetoAcid.Calc_func()
        Start_Triglyceride.Calc_func()
        Start_Urea.Calc_func()
        Start_Creatine.Calc_func()
        Start_Creatinine.Calc_func()

class Start_Urea:

    def Calc_func(self):
        UreaPool.Init_func()

class Start_FattyAcid:

    def Calc_func(self):
        FAPool.Init_func()

class Start_AminoAcid:

    def Calc_func(self):
        AAPool.Init_func()

class Start_Triglyceride:

    def Calc_func(self):
        TriglyceridePool.Init_func()

class Start_Glucose:

    def Calc_func(self):
        GlucosePool.Init_func()

class Start_KetoAcid:

    def Calc_func(self):
        KAPool.Init_func()

class Start_Testosterone:

    def Calc_func(self):
        Testosterone.Init_func()

class Start_Progesterone:

    def Calc_func(self):
        Progesterone.Init_func()

class Start_Norepinephrine:

    def Calc_func(self):
        NEPool.Init_func()

class Start_Epinephrine:

    def Calc_func(self):
        EpiPool.Init_func()

class Start_ANP:

    def Calc_func(self):
        ANPPool.Init_func()

class Start_Aldosterone:

    def Calc_func(self):
        AldoPool.Init_func()

class Start_Renin:

    def Calc_func(self):
        ReninPool.Init_func()

class Start_FSH:

    def Calc_func(self):
        FSH_Circulating.Init_func()

class Start_Leptin:

    def Calc_func(self):
        LeptinPool.Init_func()

class Start_Insulin:

    def Calc_func(self):
        InsulinPool.Init_func()

class Start_Inhibin:

    def Calc_func(self):
        Inhibin.Init_func()

class Start_LH:

    def Calc_func(self):
        LH_Circulating.Init_func()

class Start_ADH:

    def Calc_func(self):
        ADHPool.Init_func()

class Start_Estradiol:

    def Calc_func(self):
        Estradiol.Init_func()

class Start_hCG:

    def Calc_func(self):
        hCG.Init_func()

class Start_Glucagon:

    def Calc_func(self):
        GlucagonPool.Init_func()

class Start_EPO:

    def Calc_func(self):
        EPOPool.Init_func()

class Start_Hormones:

    def Calc_func(self):
        Start_Epinephrine.Calc_func()
        Start_Norepinephrine.Calc_func()
        Start_ADH.Calc_func()
        Start_Aldosterone.Calc_func()
        Start_ANP.Calc_func()
        Start_EPO.Calc_func()
        Start_Estradiol.Calc_func()
        Start_FSH.Calc_func()
        Start_Glucagon.Calc_func()
        Start_hCG.Calc_func()
        Start_Inhibin.Calc_func()
        Start_Insulin.Calc_func()
        Start_Leptin.Calc_func()
        Start_LH.Calc_func()
        Start_Progesterone.Calc_func()
        Start_Renin.Calc_func()
        Start_Testosterone.Calc_func()
        Start_ThyroidHormone.Calc_func()

class Start_ThyroidHormone:

    def Calc_func(self):
        ThyroidPool.Init_func()

class Start_ExtracellularPotassium:

    def Calc_func(self):
        KPool.Init_func()

class Start_ExtracellularPhosphate:

    def Calc_func(self):
        PO4Pool.Init_func()

class Start_ExtracellularSodium:

    def Calc_func(self):
        NaPool.Init_func()

class Start_ExtracellularSulphate:

    def Calc_func(self):
        SO4Pool.Init_func()

class Start_ExtracellularChloride:

    def Calc_func(self):
        ClPool.Init_func()

class Start_CellularPotassium:

    def Calc_func(self):
        KCell.Init_func()

class Start_Electrolytes:

    def Calc_func(self):
        Start_ExtracellularSodium.Calc_func()
        Start_ExtracellularChloride.Calc_func()
        Start_ExtracellularPhosphate.Calc_func()
        Start_ExtracellularPotassium.Calc_func()
        Start_CellularPotassium.Calc_func()
        Start_ExtracellularSulphate.Calc_func()


System = System()
Structure = Structure()
ADHPump = ADHPump()
ADHPool = ADHPool()
ADHSecretion = ADHSecretion()
ADHClearance = ADHClearance()
ADH = ADH()
ADHSynthesis = ADHSynthesis()
ADHFastMass = ADHFastMass()
ADHSlowMass = ADHSlowMass()
ICFV = ICFV()
ECFV = ECFV()
H2O = H2O()
ExternalH2O = ExternalH2O()
BodyH2O = BodyH2O()
MetabolicH2O = MetabolicH2O()
RightHeartPumping_Pumping = RightHeartPumping_Pumping()
RightHeartPumping_Diastole = RightHeartPumping_Diastole()
RightHeartPumping_Systole = RightHeartPumping_Systole()
RightHeartPumping = RightHeartPumping()
RightHeartPumping_Valves = RightHeartPumping_Valves()
GlucosePump = GlucosePump()
Glucose = Glucose()
GlucosePool = GlucosePool()
GlucoseDecomposition = GlucoseDecomposition()
ThyroidClearance = ThyroidClearance()
ThyroidPump = ThyroidPump()
ThyroidTSH = ThyroidTSH()
ThyroidGland = ThyroidGland()
ThyroidPool = ThyroidPool()
ThyroidSecretion = ThyroidSecretion()
HgbConc = HgbConc()
HgbTissue = HgbTissue()
HgbProps = HgbProps()
Hemoglobin = Hemoglobin()
HgbLung = HgbLung()
Skin_Size = Skin_Size()
Skin_Function = Skin_Function()
Skin_Lactate = Skin_Lactate()
Skin_Pressure = Skin_Pressure()
Skin_Vasculature = Skin_Vasculature()
Skin_Fuel = Skin_Fuel()
Skin_Metabolism = Skin_Metabolism()
Skin_CO2 = Skin_CO2()
Skin_Flow = Skin_Flow()
Skin_Structure = Skin_Structure()
Skin_AlphaReceptors = Skin_AlphaReceptors()
Skin = Skin()
Skin_Ph = Skin_Ph()
CellSID = CellSID()
Electrolytes = Electrolytes()
PO4Pool = PO4Pool()
PO4 = PO4()
Na = Na()
NaPool = NaPool()
SO4 = SO4()
SO4Pool = SO4Pool()
ClPool = ClPool()
Cl = Cl()
KAldoEffect = KAldoEffect()
K = K()
KFluxToPool = KFluxToPool()
KCell = KCell()
KFluxToCell = KFluxToCell()
KPool = KPool()
KMembrane = KMembrane()
HeatStorage = HeatStorage()
HeatMetabolism = HeatMetabolism()
HeatSweating = HeatSweating()
HeatSkeletalMuscle = HeatSkeletalMuscle()
HeatIVDrip = HeatIVDrip()
TempTools = TempTools()
HeatRadiation = HeatRadiation()
Convulsing = Convulsing()
HeatSkin = HeatSkin()
HeatShivering = HeatShivering()
HeatInsensibleLung = HeatInsensibleLung()
HeatCore = HeatCore()
HeatInsensibleSkin = HeatInsensibleSkin()
HeatConduction = HeatConduction()
HeatSweatEvaporation = HeatSweatEvaporation()
HeatTransfusion = HeatTransfusion()
HeatSweatConvection = HeatSweatConvection()
HeatDialyzer = HeatDialyzer()
HeatHemorrhage = HeatHemorrhage()
Heat = Heat()
SpecificHeat = SpecificHeat()
HeatUrine = HeatUrine()
IVEpinephrineInjection = IVEpinephrineInjection()
CellProtein = CellProtein()
LungArtyO2 = LungArtyO2()
LungArtyCO2 = LungArtyCO2()
RightHemithorax = RightHemithorax()
ExcessLungWater = ExcessLungWater()
Thorax = Thorax()
LungO2 = LungO2()
Bronchi = Bronchi()
GasExchangeRatio = GasExchangeRatio()
PulmonaryMembrane = PulmonaryMembrane()
Ventilator = Ventilator()
LungVeinCO2 = LungVeinCO2()
Breathing = Breathing()
LeftHemithorax = LeftHemithorax()
LungCO2 = LungCO2()
Lungs = Lungs()
LungBloodFlow = LungBloodFlow()
LungVeinO2 = LungVeinO2()
BTPS_To_STPD = BTPS_To_STPD()
GasTools = GasTools()
STPD_To_BTPS = STPD_To_BTPS()
Posture = Posture()
PostureControl = PostureControl()
A2Pool = A2Pool()
ReninSynthesis = ReninSynthesis()
ReninClearance = ReninClearance()
ReninFree = ReninFree()
A2Pump = A2Pump()
ReninGranules = ReninGranules()
ReninPool = ReninPool()
ReninSecretion = ReninSecretion()
ReninTumor = ReninTumor()
Renin = Renin()
LegMusclePump = LegMusclePump()
Gravity = Gravity()
FattyAcid = FattyAcid()
FAPool = FAPool()
FADecomposition = FADecomposition()
Pericardium = Pericardium()
Pericardium_Drain = Pericardium_Drain()
Pericardium_Cavity = Pericardium_Cavity()
Pericardium_TMP = Pericardium_TMP()
Pericardium_Hemorrhage = Pericardium_Hemorrhage()
Pericardium_V0 = Pericardium_V0()
SkeletalMuscle_ContractileProtein = SkeletalMuscle_ContractileProtein()
SkeletalMuscle_Ph = SkeletalMuscle_Ph()
SkeletalMuscle_Fuel = SkeletalMuscle_Fuel()
SkeletalMuscle = SkeletalMuscle()
SkeletalMuscle_Structure = SkeletalMuscle_Structure()
SkeletalMuscle_Pressure = SkeletalMuscle_Pressure()
SkeletalMuscle_Work = SkeletalMuscle_Work()
SkeletalMuscle_Lactate = SkeletalMuscle_Lactate()
SkeletalMuscle_Metabolism = SkeletalMuscle_Metabolism()
SkeletalMuscle_Size = SkeletalMuscle_Size()
SkeletalMuscle_Metaboreflex = SkeletalMuscle_Metaboreflex()
SkeletalMuscle_Function = SkeletalMuscle_Function()
SkeletalMuscle_AlphaReceptors = SkeletalMuscle_AlphaReceptors()
SkeletalMuscle_MusclePumping = SkeletalMuscle_MusclePumping()
SkeletalMuscle_CO2 = SkeletalMuscle_CO2()
SkeletalMuscle_MetabolicVasodilation = SkeletalMuscle_MetabolicVasodilation()
SkeletalMuscle_Flow = SkeletalMuscle_Flow()
SkeletalMuscle_Vasculature = SkeletalMuscle_Vasculature()
SkeletalMuscle_Glycogen = SkeletalMuscle_Glycogen()
SkeletalMuscle_Insulin = SkeletalMuscle_Insulin()
InsulinInjection = InsulinInjection()
hCG = hCG()
Estradiol = Estradiol()
DailyPlannerControl = DailyPlannerControl()
DailyPlanner = DailyPlanner()
DailyPlannerSchedule = DailyPlannerSchedule()
TiltTable = TiltTable()
Heart_Tachyarrhythmia = Heart_Tachyarrhythmia()
Heart_VFib = Heart_VFib()
Heart_Asystole = Heart_Asystole()
SANode_Rate = SANode_Rate()
LeftHeart_Pain = LeftHeart_Pain()
Heart_Rhythm = Heart_Rhythm()
Heart_Ventricles = Heart_Ventricles()
Heart_Rate = Heart_Rate()
Heart_Intervals = Heart_Intervals()
Heart_Pacemaker = Heart_Pacemaker()
RightHeart_Pain = RightHeart_Pain()
Heart = Heart()
SANode_BetaReceptors = SANode_BetaReceptors()
Heart_ECG = Heart_ECG()
Heart_Defibrillator = Heart_Defibrillator()
Heart_Pain = Heart_Pain()
CPR_Lungs = CPR_Lungs()
CPR_Heart = CPR_Heart()
CPR = CPR()
Drugs = Drugs()
MidodrineSingleDose = MidodrineSingleDose()
MidodrinePool = MidodrinePool()
MidodrineGILumen = MidodrineGILumen()
MidodrineDailyDose = MidodrineDailyDose()
DesglymidodrinePool = DesglymidodrinePool()
DesglymidodrineKidney = DesglymidodrineKidney()
Midodrine = Midodrine()
DigoxinKidney = DigoxinKidney()
Digoxin = Digoxin()
DigoxinSingleDose = DigoxinSingleDose()
DigoxinPool = DigoxinPool()
DigoxinDailyDose = DigoxinDailyDose()
DigoxinGILumen = DigoxinGILumen()
FurosemideSingleDose = FurosemideSingleDose()
FurosemideKidney = FurosemideKidney()
FurosemidePool = FurosemidePool()
Furosemide = Furosemide()
ThiazideKidney = ThiazideKidney()
ThiazideGILumen = ThiazideGILumen()
Chlorothiazide = Chlorothiazide()
ThiazideDailyDose = ThiazideDailyDose()
ThiazidePool = ThiazidePool()
ThiazideSingleDose = ThiazideSingleDose()
CoronarySinus = CoronarySinus()
CardiacOutput = CardiacOutput()
Viscosity = Viscosity()
CarotidSinus = CarotidSinus()
VeinsVol = VeinsVol()
Circulation = Circulation()
OrganFlow = OrganFlow()
ArtysVol = ArtysVol()
CircyManager = CircyManager()
HepaticArty = HepaticArty()
PeripheralResistance = PeripheralResistance()
GILumen = GILumen()
GILumenSodium = GILumenSodium()
GILumenPotassium = GILumenPotassium()
GILumenChloride = GILumenChloride()
GILumenElectrolytes = GILumenElectrolytes()
GILumenVolume = GILumenVolume()
GILumenH2O = GILumenH2O()
GILumenTemperature = GILumenTemperature()
GILumenDiarrhea = GILumenDiarrhea()
GILumenVomitus = GILumenVomitus()
GILumenOther = GILumenOther()
GILumenCarbohydrates = GILumenCarbohydrates()
GILumenFood = GILumenFood()
GILumenProtein = GILumenProtein()
GILumenFat = GILumenFat()
GITract_Pressure = GITract_Pressure()
GITract = GITract()
GITract_Structure = GITract_Structure()
GITract_Metabolism = GITract_Metabolism()
GITract_CO2 = GITract_CO2()
GITract_Fuel = GITract_Fuel()
GITract_Ph = GITract_Ph()
GITract_Function = GITract_Function()
GITract_Size = GITract_Size()
GITract_AlphaReceptors = GITract_AlphaReceptors()
GITract_Vasculature = GITract_Vasculature()
GITract_Flow = GITract_Flow()
GITract_Lactate = GITract_Lactate()
AldoSecretion = AldoSecretion()
AldoDisposal = AldoDisposal()
AldoPool = AldoPool()
AldoTumor = AldoTumor()
AldoPump = AldoPump()
Aldosterone = Aldosterone()
PO2Veins = PO2Veins()
O2Total = O2Total()
O2Artys = O2Artys()
PO2Artys = PO2Artys()
O2Veins = O2Veins()
O2 = O2()
SweatDuct = SweatDuct()
Sweat = Sweat()
SweatGland = SweatGland()
SweatFuel = SweatFuel()
SweatAcclimation = SweatAcclimation()
Kidney_Alpha = Kidney_Alpha()
Kidney_Size = Kidney_Size()
Kidney_Lactate = Kidney_Lactate()
Kidney_O2 = Kidney_O2()
Kidney_MyogenicDelay = Kidney_MyogenicDelay()
Kidney_Fuel = Kidney_Fuel()
Kidney = Kidney()
Kidney_Ph = Kidney_Ph()
Kidney_Function = Kidney_Function()
Kidney_AfferentArtery = Kidney_AfferentArtery()
Kidney_CO2 = Kidney_CO2()
Kidney_Structure = Kidney_Structure()
Kidney_Metabolism = Kidney_Metabolism()
Kidney_BetaReceptors = Kidney_BetaReceptors()
Kidney_AlphaReceptors = Kidney_AlphaReceptors()
Kidney_EfferentArtery = Kidney_EfferentArtery()
Kidney_Pressure = Kidney_Pressure()
Kidney_ArcuateArtery = Kidney_ArcuateArtery()
Kidney_NephronCount = Kidney_NephronCount()
Kidney_Flow = Kidney_Flow()
Kidney_Myogenic = Kidney_Myogenic()
AnesthesiaGasBone = AnesthesiaGasBone()
AnesthesiaGas = AnesthesiaGas()
AnesthesiaGasBrain = AnesthesiaGasBrain()
AnesthesiaGasLiver = AnesthesiaGasLiver()
AnesthesiaGasGITract = AnesthesiaGasGITract()
AnesthesiaGasSkeletalMuscle = AnesthesiaGasSkeletalMuscle()
AnesthesiaGasFat = AnesthesiaGasFat()
AnesthesiaGasRespiratoryMuscle = AnesthesiaGasRespiratoryMuscle()
AnesthesiaGasVein = AnesthesiaGasVein()
AnesthesiaGasSkin = AnesthesiaGasSkin()
AnesthesiaGasLeftHeart = AnesthesiaGasLeftHeart()
AnesthesiaGasLung = AnesthesiaGasLung()
AnesthesiaGasSolubility = AnesthesiaGasSolubility()
AnesthesiaGasArty = AnesthesiaGasArty()
AnesthesiaGasOtherTissue = AnesthesiaGasOtherTissue()
AnesthesiaGasKidney = AnesthesiaGasKidney()
AnesthesiaGasRightHeart = AnesthesiaGasRightHeart()
CO = CO()
PhCells = PhCells()
PhBlood = PhBlood()
BloodPh = BloodPh()
PhGeneral = PhGeneral()
AcidBase = AcidBase()
InsulinSecretion = InsulinSecretion()
InsulinSynthesis = InsulinSynthesis()
InsulinPump = InsulinPump()
InsulinClearance = InsulinClearance()
InsulinPool = InsulinPool()
Insulin = Insulin()
InsulinStorage = InsulinStorage()
LeftHeartPumping_Valves = LeftHeartPumping_Valves()
LeftHeartPumping_Systole = LeftHeartPumping_Systole()
LeftHeartPumping_Diastole = LeftHeartPumping_Diastole()
LeftHeartPumping_Pumping = LeftHeartPumping_Pumping()
LeftHeartPumping = LeftHeartPumping()
Bone_Lactate = Bone_Lactate()
Bone_Size = Bone_Size()
Bone_Metabolism = Bone_Metabolism()
Bone_CO2 = Bone_CO2()
Bone_Fuel = Bone_Fuel()
Bone_Vasculature = Bone_Vasculature()
Bone_Structure = Bone_Structure()
Bone = Bone()
Bone_Function = Bone_Function()
Bone_Mineral = Bone_Mineral()
Bone_Flow = Bone_Flow()
Bone_Ph = Bone_Ph()
Bone_Pressure = Bone_Pressure()
Bone_AlphaReceptors = Bone_AlphaReceptors()
TissueH2O = TissueH2O()
UT_H2O = UT_H2O()
MT_H2O = MT_H2O()
LT_H2O = LT_H2O()
MT_CapillaryProtein = MT_CapillaryProtein()
CapillaryProtein = CapillaryProtein()
LT_CapillaryProtein = LT_CapillaryProtein()
UT_CapillaryProtein = UT_CapillaryProtein()
LT_LymphWater = LT_LymphWater()
MT_LymphWater = MT_LymphWater()
LymphWater = LymphWater()
UT_LymphWater = UT_LymphWater()
CellH2O = CellH2O()
UT_LymphProtein = UT_LymphProtein()
MT_LymphProtein = MT_LymphProtein()
LT_LymphProtein = LT_LymphProtein()
LymphProtein = LymphProtein()
LT_InterstitialWater = LT_InterstitialWater()
MT_InterstitialWater = MT_InterstitialWater()
UT_InterstitialWater = UT_InterstitialWater()
InterstitialWater = InterstitialWater()
MT_InterstitialProtein = MT_InterstitialProtein()
UT_InterstitialProtein = UT_InterstitialProtein()
LT_InterstitialProtein = LT_InterstitialProtein()
InterstitialProtein = InterstitialProtein()
UT_CapillaryWater = UT_CapillaryWater()
CapillaryWater = CapillaryWater()
LT_CapillaryWater = LT_CapillaryWater()
MT_CapillaryWater = MT_CapillaryWater()
PeritoneumSpace = PeritoneumSpace()
Peritoneum = Peritoneum()
PeritoneumProtein = PeritoneumProtein()
GlycerolPool = GlycerolPool()
Glycerol = Glycerol()
Metabolism_RespiratoryQuotient = Metabolism_RespiratoryQuotient()
Metabolism_MetabolicRate = Metabolism_MetabolicRate()
Metabolism_Tools = Metabolism_Tools()
Thyroid = Thyroid()
Metabolism = Metabolism()
Metabolism_FattyAcid = Metabolism_FattyAcid()
Metabolism_Glucose = Metabolism_Glucose()
Metabolism_FuelUse = Metabolism_FuelUse()
Metabolism_CaloriesUsed = Metabolism_CaloriesUsed()
OsmCell = OsmCell()
Osmoles = Osmoles()
OsmBody = OsmBody()
OsmECFV = OsmECFV()
conc_EPODelay = conc_EPODelay()
RBCSecretion = RBCSecretion()
PlasmaVol = PlasmaVol()
BloodVol = BloodVol()
BloodVolume = BloodVolume()
RBCVol = RBCVol()
RBCH2O = RBCH2O()
RBCClearance = RBCClearance()
RBCSolids = RBCSolids()
TriglycerideHydrolysis = TriglycerideHydrolysis()
TriglyceridePool = TriglyceridePool()
Triglyceride = Triglyceride()
TriglycerideDecomposition = TriglycerideDecomposition()
Organs_AlphaReceptors = Organs_AlphaReceptors()
Organs_Ph = Organs_Ph()
Organs_Flow = Organs_Flow()
Organs_ScaleH2O = Organs_ScaleH2O()
Organs_ScaleConductance = Organs_ScaleConductance()
Organs_Fuel = Organs_Fuel()
Organs_Pressure = Organs_Pressure()
Organs = Organs()
Organs_Lactate = Organs_Lactate()
Organs_Vasculature = Organs_Vasculature()
Organs_Function = Organs_Function()
Organs_Structure = Organs_Structure()
Organs_ScaleCals = Organs_ScaleCals()
Organs_Metabolism = Organs_Metabolism()
Organs_CO2 = Organs_CO2()
Organs_Size = Organs_Size()
Organs_BetaReceptors = Organs_BetaReceptors()
DietGoalElectrolytes = DietGoalElectrolytes()
DietIntakeElectrolytes = DietIntakeElectrolytes()
DietThirst = DietThirst()
DietFeeding = DietFeeding()
DietGoalH2O = DietGoalH2O()
DietIntakeNutrition = DietIntakeNutrition()
DietGoalNutrition = DietGoalNutrition()
Diet = Diet()
DietAppetite = DietAppetite()
DietIntakeH2O = DietIntakeH2O()
RightHeart_Pressure = RightHeart_Pressure()
RightHeart_Vasculature = RightHeart_Vasculature()
RightHeart_Work = RightHeart_Work()
RightHeart_Size = RightHeart_Size()
RightHeart_Function = RightHeart_Function()
RightHeart_Fuel = RightHeart_Fuel()
RightHeart_CO2 = RightHeart_CO2()
RightHeart_AlphaReceptors = RightHeart_AlphaReceptors()
RightHeart_ContractileProtein = RightHeart_ContractileProtein()
RightHeart_Ph = RightHeart_Ph()
RightHeart_Structure = RightHeart_Structure()
RightHeart_Metabolism = RightHeart_Metabolism()
RightHeart = RightHeart()
RightHeart_BetaReceptors = RightHeart_BetaReceptors()
RightHeart_Infarction = RightHeart_Infarction()
RightHeart_Flow = RightHeart_Flow()
RightHeart_Lactate = RightHeart_Lactate()
AminoAcid = AminoAcid()
AAPool = AAPool()
GnRH = GnRH()
Status = Status()
LipidDeposits = LipidDeposits()
LipidDeposits_Uptake = LipidDeposits_Uptake()
LipidDeposits_Release = LipidDeposits_Release()
OralH2OGlucoseLoad = OralH2OGlucoseLoad()
BVSeq = BVSeq()
SequesteredBlood = SequesteredBlood()
BVSeqVeins = BVSeqVeins()
BVSeqArtys = BVSeqArtys()
CardiacCycle = CardiacCycle()
DiastolicPressure = DiastolicPressure()
HypothalamusSweatingAcclimation = HypothalamusSweatingAcclimation()
HypothalamusShivering = HypothalamusShivering()
Hypothalamus = Hypothalamus()
HypothalamusTSH = HypothalamusTSH()
HypothalamusSkinFlow = HypothalamusSkinFlow()
HypothalamusSweating = HypothalamusSweating()
HypothalamusShiveringAcclimation = HypothalamusShiveringAcclimation()
RespiratoryCenter_Exercise = RespiratoryCenter_Exercise()
RespiratoryCenter_Metaboreflex = RespiratoryCenter_Metaboreflex()
RespiratoryCenter = RespiratoryCenter()
RespiratoryCenter_Chemical = RespiratoryCenter_Chemical()
RespiratoryCenter_Radiation = RespiratoryCenter_Radiation()
RespiratoryCenter_Output = RespiratoryCenter_Output()
RespiratoryCenter_Integration = RespiratoryCenter_Integration()
GlucagonSecretion = GlucagonSecretion()
Glucagon = Glucagon()
GlucagonPool = GlucagonPool()
GlucagonClearance = GlucagonClearance()
FractReab = FractReab()
Nephrons = Nephrons()
NephronANP = NephronANP()
NephronIFP = NephronIFP()
NephronGlucose = NephronGlucose()
NephronAldo = NephronAldo()
VasaRecta = VasaRecta()
NephronADH = NephronADH()
NephronKetoacids = NephronKetoacids()
GlomerulusKetoacid = GlomerulusKetoacid()
GlomerulusBicarbonate = GlomerulusBicarbonate()
GlomerulusUrea = GlomerulusUrea()
GlomerulusChloride = GlomerulusChloride()
GlomerulusSulphate = GlomerulusSulphate()
GlomerulusSodium = GlomerulusSodium()
Glomerulus = Glomerulus()
GlomerulusCreatinine = GlomerulusCreatinine()
GlomerulusGlucose = GlomerulusGlucose()
GlomerulusPhosphate = GlomerulusPhosphate()
GlomerulusProtein = GlomerulusProtein()
GlomerulusFiltrate = GlomerulusFiltrate()
TGF_Renin = TGF_Renin()
MD_Na = MD_Na()
MaculaDensa = MaculaDensa()
TGF_Vascular = TGF_Vascular()
MedullaUrea = MedullaUrea()
MedullaNa = MedullaNa()
Medulla = Medulla()
PT_Na = PT_Na()
PT_H2O = PT_H2O()
PT_NH3 = PT_NH3()
ProximalTubule = ProximalTubule()
CD_Urea = CD_Urea()
CD_K = CD_K()
CD_NH4 = CD_NH4()
CD_PO4 = CD_PO4()
CD_Glucose = CD_Glucose()
CD_Cl = CD_Cl()
CD_KA = CD_KA()
CD_HCO3 = CD_HCO3()
CD_SO4 = CD_SO4()
CD_Protein = CD_Protein()
CD_Creatinine = CD_Creatinine()
CD_H2OChannels = CD_H2OChannels()
CD_Na = CD_Na()
CollectingDuct = CollectingDuct()
CD_H2O = CD_H2O()
DT_Na = DT_Na()
DT_K = DT_K()
DT_H2O = DT_H2O()
DistalTubule = DistalTubule()
LoopOfHenle = LoopOfHenle()
LH_ = LH_()
LH_Na = LH_Na()
LH_H2O = LH_H2O()
Testosterone = Testosterone()
HeartValves = HeartValves()
TricuspidValve_Regurgitation = TricuspidValve_Regurgitation()
TricuspidValve = TricuspidValve()
TricuspidValve_Stenosis = TricuspidValve_Stenosis()
MitralValve = MitralValve()
MitralValve_Regurgitation = MitralValve_Regurgitation()
MitralValve_Stenosis = MitralValve_Stenosis()
AorticValve = AorticValve()
AorticValve_Regurgitation = AorticValve_Regurgitation()
AorticValve_Stenosis = AorticValve_Stenosis()
PulmonicValve_Stenosis = PulmonicValve_Stenosis()
PulmonicValve_Regurgitation = PulmonicValve_Regurgitation()
PulmonicValve = PulmonicValve()
DialyzerActivity = DialyzerActivity()
DialysateComposition = DialysateComposition()
DialysisShunt = DialysisShunt()
DialyzerControl = DialyzerControl()
Hemodialysis = Hemodialysis()
ANP = ANP()
ANPSecretion = ANPSecretion()
ANPPool = ANPPool()
ANPClearance = ANPClearance()
ANPPump = ANPPump()
BloodIons = BloodIons()
CreatininePool = CreatininePool()
Creatinine = Creatinine()
Anesthesia = Anesthesia()
NoAnesthesia = NoAnesthesia()
Transfusion = Transfusion()
Bladder = Bladder()
BladderChloride = BladderChloride()
BladderSulphate = BladderSulphate()
BladderKetoacid = BladderKetoacid()
BladderCreatinine = BladderCreatinine()
BladderGlucose = BladderGlucose()
BladderUrea = BladderUrea()
BladderPotassium = BladderPotassium()
BladderPhosphate = BladderPhosphate()
BladderSodium = BladderSodium()
BladderProtein = BladderProtein()
BladderBicarbonate = BladderBicarbonate()
BladderAmmonia = BladderAmmonia()
BladderVolume = BladderVolume()
Hemorrhage = Hemorrhage()
LeftHeart_Lactate = LeftHeart_Lactate()
LeftHeart_Metabolism = LeftHeart_Metabolism()
LeftHeart_Infarction = LeftHeart_Infarction()
LeftHeart_Flow = LeftHeart_Flow()
LeftHeart_Function = LeftHeart_Function()
LeftHeart_Size = LeftHeart_Size()
LeftHeart_Work = LeftHeart_Work()
LeftHeart_AlphaReceptors = LeftHeart_AlphaReceptors()
LeftHeart_Vasculature = LeftHeart_Vasculature()
LeftHeart_Ph = LeftHeart_Ph()
LeftHeart = LeftHeart()
LeftHeart_Pressure = LeftHeart_Pressure()
LeftHeart_BetaReceptors = LeftHeart_BetaReceptors()
LeftHeart_CO2 = LeftHeart_CO2()
LeftHeart_Structure = LeftHeart_Structure()
LeftHeart_Fuel = LeftHeart_Fuel()
LeftHeart_ContractileProtein = LeftHeart_ContractileProtein()
Exercise_Treadmill = Exercise_Treadmill()
Exercise_MusclePump = Exercise_MusclePump()
Exercise_Bike = Exercise_Bike()
Exercise_Motivation = Exercise_Motivation()
Exercise_Metabolism = Exercise_Metabolism()
Exercise = Exercise()
Exercise_Control = Exercise_Control()
EpiClearance = EpiClearance()
AlphaBlockade = AlphaBlockade()
NESecretion = NESecretion()
NEPump = NEPump()
Pheochromocytoma = Pheochromocytoma()
NEPool = NEPool()
EpiPump = EpiPump()
AlphaPool = AlphaPool()
BetaPool = BetaPool()
Catechols = Catechols()
EpiPool = EpiPool()
NEClearance = NEClearance()
EpiSecretion = EpiSecretion()
BetaBlockade = BetaBlockade()
Uterus = Uterus()
Testes_Inhibin = Testes_Inhibin()
Testes_Estradiol = Testes_Estradiol()
Testes = Testes()
Testes_Testosterone = Testes_Testosterone()
Testes_Progesterone = Testes_Progesterone()
Inhibin = Inhibin()
UreaPool = UreaPool()
Urea = Urea()
UreaCell = UreaCell()
EPOClearance = EPOClearance()
EPOPump = EPOPump()
EPOPool = EPOPool()
EPO = EPO()
EPOSecretion = EPOSecretion()
Lactate = Lactate()
LacPool = LacPool()
Infusions = Infusions()
LowerExternalPressure = LowerExternalPressure()
SplanchnicCirculation = SplanchnicCirculation()
HepaticVein = HepaticVein()
HepaticArtery = HepaticArtery()
PortalVein_Glucose = PortalVein_Glucose()
PortalVein = PortalVein()
PortalVein_Insulin = PortalVein_Insulin()
PortalVein_FattyAcid = PortalVein_FattyAcid()
PortalVein_Glucagon = PortalVein_Glucagon()
Wind = Wind()
Clothes = Clothes()
Altitude = Altitude()
RelativeHumidity = RelativeHumidity()
Environment = Environment()
AmbientTemperature = AmbientTemperature()
Barometer = Barometer()
EquivalentAltitude = EquivalentAltitude()
Symptoms = Symptoms()
Brain = Brain()
Brain_Ph = Brain_Ph()
Brain_Pressure = Brain_Pressure()
Brain_Flow = Brain_Flow()
Seizure = Seizure()
Brain_Function = Brain_Function()
Brain_CO2 = Brain_CO2()
Brain_Fuel = Brain_Fuel()
Brain_Lactate = Brain_Lactate()
Brain_Metabolism = Brain_Metabolism()
Brain_Structure = Brain_Structure()
GlasgowComaScale = GlasgowComaScale()
Brain_Vasculature = Brain_Vasculature()
Brain_Size = Brain_Size()
BrainInsult = BrainInsult()
BrainInsult_PO2 = BrainInsult_PO2()
BrainInsult_Temperature = BrainInsult_Temperature()
BrainInsult_Ph = BrainInsult_Ph()
BrainInsult_Structure = BrainInsult_Structure()
BrainInsult_Fuel = BrainInsult_Fuel()
BrainInsult_Highconc_Osm = BrainInsult_Highconc_Osm()
BrainInsult_Lowconc_Osm = BrainInsult_Lowconc_Osm()
AirSupply_PressureChamber = AirSupply_PressureChamber()
AirSupply = AirSupply()
AirSupply_GasTanks = AirSupply_GasTanks()
AirSupply_InspiredAir = AirSupply_InspiredAir()
LeftAtrium = LeftAtrium()
SplanchnicVeins = SplanchnicVeins()
PulmVeins = PulmVeins()
PulmArty = PulmArty()
RightVentricle = RightVentricle()
RightAtrium = RightAtrium()
LeftVentricle = LeftVentricle()
VascularCompartments = VascularCompartments()
SystemicArtys = SystemicArtys()
PulmCapys = PulmCapys()
SystemicVeins = SystemicVeins()
Inhibin_B = Inhibin_B()
Follicle_Estradiol = Follicle_Estradiol()
Inhibin_A = Inhibin_A()
Ovaries_CorpusLuteum = Ovaries_CorpusLuteum()
Ovaries_Follicle = Ovaries_Follicle()
CorpusLuteum_Involution = CorpusLuteum_Involution()
Follicle_Atresia = Follicle_Atresia()
CorpusLuteum_Estradiol = CorpusLuteum_Estradiol()
Ovaries = Ovaries()
Ovaries_Estradiol = Ovaries_Estradiol()
Ovaries_Inhibin = Ovaries_Inhibin()
Follicle_Growth = Follicle_Growth()
CorpusLuteum_Growth = CorpusLuteum_Growth()
Ovaries_Ovulation = Ovaries_Ovulation()
Ovaries_Testosterone = Ovaries_Testosterone()
Ovaries_Progesterone = Ovaries_Progesterone()
SurfaceArea = SurfaceArea()
BMI = BMI()
Age = Age()
Gender = Gender()
Morphology = Morphology()
Weight = Weight()
Weight_Fluids = Weight_Fluids()
Height = Height()
AnesthesiaIVRespiratoryMuscle = AnesthesiaIVRespiratoryMuscle()
AnesthesiaIVRightHeart = AnesthesiaIVRightHeart()
AnesthesiaIVSkin = AnesthesiaIVSkin()
AnesthesiaIVInjection = AnesthesiaIVInjection()
AnesthesiaIVBone = AnesthesiaIVBone()
AnesthesiaIV = AnesthesiaIV()
AnesthesiaIVLeftHeart = AnesthesiaIVLeftHeart()
AnesthesiaIVInfusion = AnesthesiaIVInfusion()
AnesthesiaIVSolubility = AnesthesiaIVSolubility()
AnesthesiaIVGITract = AnesthesiaIVGITract()
AnesthesiaIVSkeletalMuscle = AnesthesiaIVSkeletalMuscle()
AnesthesiaIVBlood = AnesthesiaIVBlood()
AnesthesiaIVLiver = AnesthesiaIVLiver()
AnesthesiaIVBrain = AnesthesiaIVBrain()
AnesthesiaIVKidney = AnesthesiaIVKidney()
AnesthesiaIVFat = AnesthesiaIVFat()
AnesthesiaIVOtherTissue = AnesthesiaIVOtherTissue()
Autopsy = Autopsy()
Orthostatics = Orthostatics()
RegionalPressure = RegionalPressure()
Hydrostatics = Hydrostatics()
A_VFistula = A_VFistula()
A_VFistula_Flow = A_VFistula_Flow()
A_VFistula_Pressure = A_VFistula_Pressure()
LH_AnteriorPituitary = LH_AnteriorPituitary()
LH = LH()
LH_Circulating = LH_Circulating()
Fat_Flow = Fat_Flow()
Fat_Ph = Fat_Ph()
Fat_Function = Fat_Function()
Fat_Lactate = Fat_Lactate()
Fat_CO2 = Fat_CO2()
Fat_Pressure = Fat_Pressure()
Fat_Vasculature = Fat_Vasculature()
Fat_AlphaReceptors = Fat_AlphaReceptors()
Fat = Fat()
Fat_Fuel = Fat_Fuel()
Fat_Structure = Fat_Structure()
Fat_Metabolism = Fat_Metabolism()
Fat_Size = Fat_Size()
Liver = Liver()
Liver_Metabolism = Liver_Metabolism()
Liver_Ph = Liver_Ph()
Liver_CO2 = Liver_CO2()
Liver_AlphaReceptors = Liver_AlphaReceptors()
Liver_Structure = Liver_Structure()
Liver_Size = Liver_Size()
Liver_O2 = Liver_O2()
Liver_Function = Liver_Function()
Liver_Lactate = Liver_Lactate()
Liver_Fuel = Liver_Fuel()
KAPump = KAPump()
Ketoacid = Ketoacid()
KAPool = KAPool()
KADecomposition = KADecomposition()
RespiratoryMuscle_Function = RespiratoryMuscle_Function()
RespiratoryMuscle_Size = RespiratoryMuscle_Size()
RespiratoryMuscle_Metabolism = RespiratoryMuscle_Metabolism()
RespiratoryMuscle_Work = RespiratoryMuscle_Work()
RespiratoryMuscle_Vasculature = RespiratoryMuscle_Vasculature()
RespiratoryMuscle_CO2 = RespiratoryMuscle_CO2()
RespiratoryMuscle_Pressure = RespiratoryMuscle_Pressure()
RespiratoryMuscle_ContractileProtein = RespiratoryMuscle_ContractileProtein()
RespiratoryMuscle_Fuel = RespiratoryMuscle_Fuel()
RespiratoryMuscle_Ph = RespiratoryMuscle_Ph()
RespiratoryMuscle_Lactate = RespiratoryMuscle_Lactate()
RespiratoryMuscle_AlphaReceptors = RespiratoryMuscle_AlphaReceptors()
RespiratoryMuscle_Structure = RespiratoryMuscle_Structure()
RespiratoryMuscle_Flow = RespiratoryMuscle_Flow()
RespiratoryMuscle = RespiratoryMuscle()
RespiratoryMuscle_Glycogen = RespiratoryMuscle_Glycogen()
RespiratoryMuscle_Insulin = RespiratoryMuscle_Insulin()
LM_Gluconeogenesis = LM_Gluconeogenesis()
LM_FA_Glucose = LM_FA_Glucose()
LM_Glycogenolysis = LM_Glycogenolysis()
LM_Insulin = LM_Insulin()
LM_FattyAcids = LM_FattyAcids()
LM_Ketoacids = LM_Ketoacids()
LM_Glycerol = LM_Glycerol()
LM_FA_AminoAcids = LM_FA_AminoAcids()
LM_AminoAcids = LM_AminoAcids()
LM_Lactate = LM_Lactate()
LM_Glucose = LM_Glucose()
LM_Glycogenesis = LM_Glycogenesis()
LiverMetabolism = LiverMetabolism()
LM_Glycogen = LM_Glycogen()
Progesterone = Progesterone()
FSH = FSH()
FSH_Circulating = FSH_Circulating()
FSH_AnteriorPituitary = FSH_AnteriorPituitary()
LeptinClearance = LeptinClearance()
LeptinPump = LeptinPump()
Leptin = Leptin()
LeptinPool = LeptinPool()
LeptinSecretion = LeptinSecretion()
HepaticFunction = HepaticFunction()
PlasmaProtein = PlasmaProtein()
CircyProtein = CircyProtein()
Colloids = Colloids()
CO2Veins = CO2Veins()
Blood_BaseToGas = Blood_BaseToGas()
CO2Total = CO2Total()
CO2Artys = CO2Artys()
CO2 = CO2()
Tissue_BaseToGas = Tissue_BaseToGas()
Muscle_BaseToGas = Muscle_BaseToGas()
Blood_GasToBase = Blood_GasToBase()
Muscle_GasToBase = Muscle_GasToBase()
CO2Tools = CO2Tools()
Tissue_GasToBase = Tissue_GasToBase()
CreatineSkeletalMuscle = CreatineSkeletalMuscle()
Creatine = Creatine()
CreatineCells = CreatineCells()
SympsKidy = SympsKidy()
GangliaKidney = GangliaKidney()
CNSTrophicFactor = CNSTrophicFactor()
Chemoreceptors = Chemoreceptors()
GangliaGeneral = GangliaGeneral()
SympsCNS = SympsCNS()
Mechanoreceptors = Mechanoreceptors()
ExerciseSymps = ExerciseSymps()
MotorRadiation = MotorRadiation()
AdrenalNerve = AdrenalNerve()
LowPressureReceptors = LowPressureReceptors()
Baroreflex = Baroreflex()
SympsChemo = SympsChemo()
CushingResponse = CushingResponse()
SystemicVeins_AlphaReceptors = SystemicVeins_AlphaReceptors()
ChemoreceptorAcclimation = ChemoreceptorAcclimation()
VagusNerve = VagusNerve()
Nerves = Nerves()
OtherTissue_Vasculature = OtherTissue_Vasculature()
OtherTissue_Function = OtherTissue_Function()
OtherTissue_Fuel = OtherTissue_Fuel()
OtherTissue_Size = OtherTissue_Size()
OtherTissue_Pressure = OtherTissue_Pressure()
OtherTissue_Ph = OtherTissue_Ph()
OtherTissue = OtherTissue()
OtherTissue_AlphaReceptors = OtherTissue_AlphaReceptors()
OtherTissue_Lactate = OtherTissue_Lactate()
OtherTissue_Metabolism = OtherTissue_Metabolism()
OtherTissue_CO2 = OtherTissue_CO2()
OtherTissue_Flow = OtherTissue_Flow()
OtherTissue_Structure = OtherTissue_Structure()
IVDrip = IVDrip()
Context = Context()
Traits = Traits()
Values_Muscularity = Values_Muscularity()
Values = Values()
Values_Gender = Values_Gender()
Values_Adiposity = Values_Adiposity()
Values_OtherMass = Values_OtherMass()
Values_Height = Values_Height()
Values_Age = Values_Age()
Descriptors = Descriptors()
Male = Male()
Descriptors_Gender = Descriptors_Gender()
Female = Female()
Descriptors_Adiposity = Descriptors_Adiposity()
MorbidlyObese = MorbidlyObese()
Overweight = Overweight()
Underweight = Underweight()
Obese = Obese()
NormalWeight = NormalWeight()
Descriptors_Muscularity = Descriptors_Muscularity()
AboveNormal = AboveNormal()
TrainedAthlete = TrainedAthlete()
Normal = Normal()
BelowNormal = BelowNormal()
Descriptors_BodySize = Descriptors_BodySize()
VeryLarge = VeryLarge()
Large = Large()
Small = Small()
Descriptors_Age = Descriptors_Age()
Old = Old()
Middleaged = Middleaged()
Youngish = Youngish()
Young = Young()
VeryOld = VeryOld()
Start_OrganConductance = Start_OrganConductance()
Start = Start()
Start_OrganCalories = Start_OrganCalories()
Start_Heat = Start_Heat()
Start_Height = Start_Height()
Start_Morphology = Start_Morphology()
Start_FatSize = Start_FatSize()
Start_Weight = Start_Weight()
Start_SkeletalMuscleSize = Start_SkeletalMuscleSize()
Start_Gender = Start_Gender()
Start_Age = Start_Age()
Start_BloodSize = Start_BloodSize()
Start_WholeBody = Start_WholeBody()
Start_BodyH2O = Start_BodyH2O()
Start_General = Start_General()
Start_BodySize = Start_BodySize()
Start_OrganSize = Start_OrganSize()
Start_Creatinine = Start_Creatinine()
Start_Creatine = Start_Creatine()
Start_Metabolism = Start_Metabolism()
Start_Urea = Start_Urea()
Start_FattyAcid = Start_FattyAcid()
Start_AminoAcid = Start_AminoAcid()
Start_Triglyceride = Start_Triglyceride()
Start_Glucose = Start_Glucose()
Start_KetoAcid = Start_KetoAcid()
Start_Testosterone = Start_Testosterone()
Start_Progesterone = Start_Progesterone()
Start_Norepinephrine = Start_Norepinephrine()
Start_Epinephrine = Start_Epinephrine()
Start_ANP = Start_ANP()
Start_Aldosterone = Start_Aldosterone()
Start_Renin = Start_Renin()
Start_FSH = Start_FSH()
Start_Leptin = Start_Leptin()
Start_Insulin = Start_Insulin()
Start_Inhibin = Start_Inhibin()
Start_LH = Start_LH()
Start_ADH = Start_ADH()
Start_Estradiol = Start_Estradiol()
Start_hCG = Start_hCG()
Start_Glucagon = Start_Glucagon()
Start_EPO = Start_EPO()
Start_Hormones = Start_Hormones()
Start_ThyroidHormone = Start_ThyroidHormone()
Start_ExtracellularPotassium = Start_ExtracellularPotassium()
Start_ExtracellularPhosphate = Start_ExtracellularPhosphate()
Start_ExtracellularSodium = Start_ExtracellularSodium()
Start_ExtracellularSulphate = Start_ExtracellularSulphate()
Start_ExtracellularChloride = Start_ExtracellularChloride()
Start_CellularPotassium = Start_CellularPotassium()
Start_Electrolytes = Start_Electrolytes()

components = {"System":System, "Structure":Structure, "ADHPump":ADHPump, "ADHPool":ADHPool, "ADHSecretion":ADHSecretion, "ADHClearance":ADHClearance, "ADH":ADH, "ADHSynthesis":ADHSynthesis, "ADHFastMass":ADHFastMass, "ADHSlowMass":ADHSlowMass, "ICFV":ICFV, "ECFV":ECFV, "H2O":H2O, "ExternalH2O":ExternalH2O, "BodyH2O":BodyH2O, "MetabolicH2O":MetabolicH2O, "RightHeartPumping_Pumping":RightHeartPumping_Pumping, "RightHeartPumping_Diastole":RightHeartPumping_Diastole, "RightHeartPumping_Systole":RightHeartPumping_Systole, "RightHeartPumping":RightHeartPumping, "RightHeartPumping_Valves":RightHeartPumping_Valves, "GlucosePump":GlucosePump, "Glucose":Glucose, "GlucosePool":GlucosePool, "GlucoseDecomposition":GlucoseDecomposition, "ThyroidClearance":ThyroidClearance, "ThyroidPump":ThyroidPump, "ThyroidTSH":ThyroidTSH, "ThyroidGland":ThyroidGland, "ThyroidPool":ThyroidPool, "ThyroidSecretion":ThyroidSecretion, "HgbConc":HgbConc, "HgbTissue":HgbTissue, "HgbProps":HgbProps, "Hemoglobin":Hemoglobin, "HgbLung":HgbLung, "Skin_Size":Skin_Size, "Skin_Function":Skin_Function, "Skin_Lactate":Skin_Lactate, "Skin_Pressure":Skin_Pressure, "Skin_Vasculature":Skin_Vasculature, "Skin_Fuel":Skin_Fuel, "Skin_Metabolism":Skin_Metabolism, "Skin_CO2":Skin_CO2, "Skin_Flow":Skin_Flow, "Skin_Structure":Skin_Structure, "Skin_AlphaReceptors":Skin_AlphaReceptors, "Skin":Skin, "Skin_Ph":Skin_Ph, "CellSID":CellSID, "Electrolytes":Electrolytes, "PO4Pool":PO4Pool, "PO4":PO4, "Na":Na, "NaPool":NaPool, "SO4":SO4, "SO4Pool":SO4Pool, "ClPool":ClPool, "Cl":Cl, "KAldoEffect":KAldoEffect, "K":K, "KFluxToPool":KFluxToPool, "KCell":KCell, "KFluxToCell":KFluxToCell, "KPool":KPool, "KMembrane":KMembrane, "HeatStorage":HeatStorage, "HeatMetabolism":HeatMetabolism, "HeatSweating":HeatSweating, "HeatSkeletalMuscle":HeatSkeletalMuscle, "HeatIVDrip":HeatIVDrip, "TempTools":TempTools, "HeatRadiation":HeatRadiation, "Convulsing":Convulsing, "HeatSkin":HeatSkin, "HeatShivering":HeatShivering, "HeatInsensibleLung":HeatInsensibleLung, "HeatCore":HeatCore, "HeatInsensibleSkin":HeatInsensibleSkin, "HeatConduction":HeatConduction, "HeatSweatEvaporation":HeatSweatEvaporation, "HeatTransfusion":HeatTransfusion, "HeatSweatConvection":HeatSweatConvection, "HeatDialyzer":HeatDialyzer, "HeatHemorrhage":HeatHemorrhage, "Heat":Heat, "SpecificHeat":SpecificHeat, "HeatUrine":HeatUrine, "IVEpinephrineInjection":IVEpinephrineInjection, "CellProtein":CellProtein, "LungArtyO2":LungArtyO2, "LungArtyCO2":LungArtyCO2, "RightHemithorax":RightHemithorax, "ExcessLungWater":ExcessLungWater, "Thorax":Thorax, "LungO2":LungO2, "Bronchi":Bronchi, "GasExchangeRatio":GasExchangeRatio, "PulmonaryMembrane":PulmonaryMembrane, "Ventilator":Ventilator, "LungVeinCO2":LungVeinCO2, "Breathing":Breathing, "LeftHemithorax":LeftHemithorax, "LungCO2":LungCO2, "Lungs":Lungs, "LungBloodFlow":LungBloodFlow, "LungVeinO2":LungVeinO2, "BTPS_To_STPD":BTPS_To_STPD, "GasTools":GasTools, "STPD_To_BTPS":STPD_To_BTPS, "Posture":Posture, "PostureControl":PostureControl, "A2Pool":A2Pool, "ReninSynthesis":ReninSynthesis, "ReninClearance":ReninClearance, "ReninFree":ReninFree, "A2Pump":A2Pump, "ReninGranules":ReninGranules, "ReninPool":ReninPool, "ReninSecretion":ReninSecretion, "ReninTumor":ReninTumor, "Renin":Renin, "LegMusclePump":LegMusclePump, "Gravity":Gravity, "FattyAcid":FattyAcid, "FAPool":FAPool, "FADecomposition":FADecomposition, "Pericardium":Pericardium, "Pericardium_Drain":Pericardium_Drain, "Pericardium_Cavity":Pericardium_Cavity, "Pericardium_TMP":Pericardium_TMP, "Pericardium_Hemorrhage":Pericardium_Hemorrhage, "Pericardium_V0":Pericardium_V0, "SkeletalMuscle_ContractileProtein":SkeletalMuscle_ContractileProtein, "SkeletalMuscle_Ph":SkeletalMuscle_Ph, "SkeletalMuscle_Fuel":SkeletalMuscle_Fuel, "SkeletalMuscle":SkeletalMuscle, "SkeletalMuscle_Structure":SkeletalMuscle_Structure, "SkeletalMuscle_Pressure":SkeletalMuscle_Pressure, "SkeletalMuscle_Work":SkeletalMuscle_Work, "SkeletalMuscle_Lactate":SkeletalMuscle_Lactate, "SkeletalMuscle_Metabolism":SkeletalMuscle_Metabolism, "SkeletalMuscle_Size":SkeletalMuscle_Size, "SkeletalMuscle_Metaboreflex":SkeletalMuscle_Metaboreflex, "SkeletalMuscle_Function":SkeletalMuscle_Function, "SkeletalMuscle_AlphaReceptors":SkeletalMuscle_AlphaReceptors, "SkeletalMuscle_MusclePumping":SkeletalMuscle_MusclePumping, "SkeletalMuscle_CO2":SkeletalMuscle_CO2, "SkeletalMuscle_MetabolicVasodilation":SkeletalMuscle_MetabolicVasodilation, "SkeletalMuscle_Flow":SkeletalMuscle_Flow, "SkeletalMuscle_Vasculature":SkeletalMuscle_Vasculature, "SkeletalMuscle_Glycogen":SkeletalMuscle_Glycogen, "SkeletalMuscle_Insulin":SkeletalMuscle_Insulin, "InsulinInjection":InsulinInjection, "hCG":hCG, "Estradiol":Estradiol, "DailyPlannerControl":DailyPlannerControl, "DailyPlanner":DailyPlanner, "DailyPlannerSchedule":DailyPlannerSchedule, "TiltTable":TiltTable, "Heart_Tachyarrhythmia":Heart_Tachyarrhythmia, "Heart_VFib":Heart_VFib, "Heart_Asystole":Heart_Asystole, "SANode_Rate":SANode_Rate, "LeftHeart_Pain":LeftHeart_Pain, "Heart_Rhythm":Heart_Rhythm, "Heart_Ventricles":Heart_Ventricles, "Heart_Rate":Heart_Rate, "Heart_Intervals":Heart_Intervals, "Heart_Pacemaker":Heart_Pacemaker, "RightHeart_Pain":RightHeart_Pain, "Heart":Heart, "SANode_BetaReceptors":SANode_BetaReceptors, "Heart_ECG":Heart_ECG, "Heart_Defibrillator":Heart_Defibrillator, "Heart_Pain":Heart_Pain, "CPR_Lungs":CPR_Lungs, "CPR_Heart":CPR_Heart, "CPR":CPR, "Drugs":Drugs, "MidodrineSingleDose":MidodrineSingleDose, "MidodrinePool":MidodrinePool, "MidodrineGILumen":MidodrineGILumen, "MidodrineDailyDose":MidodrineDailyDose, "DesglymidodrinePool":DesglymidodrinePool, "DesglymidodrineKidney":DesglymidodrineKidney, "Midodrine":Midodrine, "DigoxinKidney":DigoxinKidney, "Digoxin":Digoxin, "DigoxinSingleDose":DigoxinSingleDose, "DigoxinPool":DigoxinPool, "DigoxinDailyDose":DigoxinDailyDose, "DigoxinGILumen":DigoxinGILumen, "FurosemideSingleDose":FurosemideSingleDose, "FurosemideKidney":FurosemideKidney, "FurosemidePool":FurosemidePool, "Furosemide":Furosemide, "ThiazideKidney":ThiazideKidney, "ThiazideGILumen":ThiazideGILumen, "Chlorothiazide":Chlorothiazide, "ThiazideDailyDose":ThiazideDailyDose, "ThiazidePool":ThiazidePool, "ThiazideSingleDose":ThiazideSingleDose, "CoronarySinus":CoronarySinus, "CardiacOutput":CardiacOutput, "Viscosity":Viscosity, "CarotidSinus":CarotidSinus, "VeinsVol":VeinsVol, "Circulation":Circulation, "OrganFlow":OrganFlow, "ArtysVol":ArtysVol, "CircyManager":CircyManager, "HepaticArty":HepaticArty, "PeripheralResistance":PeripheralResistance, "GILumen":GILumen, "GILumenSodium":GILumenSodium, "GILumenPotassium":GILumenPotassium, "GILumenChloride":GILumenChloride, "GILumenElectrolytes":GILumenElectrolytes, "GILumenVolume":GILumenVolume, "GILumenH2O":GILumenH2O, "GILumenTemperature":GILumenTemperature, "GILumenDiarrhea":GILumenDiarrhea, "GILumenVomitus":GILumenVomitus, "GILumenOther":GILumenOther, "GILumenCarbohydrates":GILumenCarbohydrates, "GILumenFood":GILumenFood, "GILumenProtein":GILumenProtein, "GILumenFat":GILumenFat, "GITract_Pressure":GITract_Pressure, "GITract":GITract, "GITract_Structure":GITract_Structure, "GITract_Metabolism":GITract_Metabolism, "GITract_CO2":GITract_CO2, "GITract_Fuel":GITract_Fuel, "GITract_Ph":GITract_Ph, "GITract_Function":GITract_Function, "GITract_Size":GITract_Size, "GITract_AlphaReceptors":GITract_AlphaReceptors, "GITract_Vasculature":GITract_Vasculature, "GITract_Flow":GITract_Flow, "GITract_Lactate":GITract_Lactate, "AldoSecretion":AldoSecretion, "AldoDisposal":AldoDisposal, "AldoPool":AldoPool, "AldoTumor":AldoTumor, "AldoPump":AldoPump, "Aldosterone":Aldosterone, "PO2Veins":PO2Veins, "O2Total":O2Total, "O2Artys":O2Artys, "PO2Artys":PO2Artys, "O2Veins":O2Veins, "O2":O2, "SweatDuct":SweatDuct, "Sweat":Sweat, "SweatGland":SweatGland, "SweatFuel":SweatFuel, "SweatAcclimation":SweatAcclimation, "Kidney_Alpha":Kidney_Alpha, "Kidney_Size":Kidney_Size, "Kidney_Lactate":Kidney_Lactate, "Kidney_O2":Kidney_O2, "Kidney_MyogenicDelay":Kidney_MyogenicDelay, "Kidney_Fuel":Kidney_Fuel, "Kidney":Kidney, "Kidney_Ph":Kidney_Ph, "Kidney_Function":Kidney_Function, "Kidney_AfferentArtery":Kidney_AfferentArtery, "Kidney_CO2":Kidney_CO2, "Kidney_Structure":Kidney_Structure, "Kidney_Metabolism":Kidney_Metabolism, "Kidney_BetaReceptors":Kidney_BetaReceptors, "Kidney_AlphaReceptors":Kidney_AlphaReceptors, "Kidney_EfferentArtery":Kidney_EfferentArtery, "Kidney_Pressure":Kidney_Pressure, "Kidney_ArcuateArtery":Kidney_ArcuateArtery, "Kidney_NephronCount":Kidney_NephronCount, "Kidney_Flow":Kidney_Flow, "Kidney_Myogenic":Kidney_Myogenic, "AnesthesiaGasBone":AnesthesiaGasBone, "AnesthesiaGas":AnesthesiaGas, "AnesthesiaGasBrain":AnesthesiaGasBrain, "AnesthesiaGasLiver":AnesthesiaGasLiver, "AnesthesiaGasGITract":AnesthesiaGasGITract, "AnesthesiaGasSkeletalMuscle":AnesthesiaGasSkeletalMuscle, "AnesthesiaGasFat":AnesthesiaGasFat, "AnesthesiaGasRespiratoryMuscle":AnesthesiaGasRespiratoryMuscle, "AnesthesiaGasVein":AnesthesiaGasVein, "AnesthesiaGasSkin":AnesthesiaGasSkin, "AnesthesiaGasLeftHeart":AnesthesiaGasLeftHeart, "AnesthesiaGasLung":AnesthesiaGasLung, "AnesthesiaGasSolubility":AnesthesiaGasSolubility, "AnesthesiaGasArty":AnesthesiaGasArty, "AnesthesiaGasOtherTissue":AnesthesiaGasOtherTissue, "AnesthesiaGasKidney":AnesthesiaGasKidney, "AnesthesiaGasRightHeart":AnesthesiaGasRightHeart, "CO":CO, "PhCells":PhCells, "PhBlood":PhBlood, "BloodPh":BloodPh, "PhGeneral":PhGeneral, "AcidBase":AcidBase, "InsulinSecretion":InsulinSecretion, "InsulinSynthesis":InsulinSynthesis, "InsulinPump":InsulinPump, "InsulinClearance":InsulinClearance, "InsulinPool":InsulinPool, "Insulin":Insulin, "InsulinStorage":InsulinStorage, "LeftHeartPumping_Valves":LeftHeartPumping_Valves, "LeftHeartPumping_Systole":LeftHeartPumping_Systole, "LeftHeartPumping_Diastole":LeftHeartPumping_Diastole, "LeftHeartPumping_Pumping":LeftHeartPumping_Pumping, "LeftHeartPumping":LeftHeartPumping, "Bone_Lactate":Bone_Lactate, "Bone_Size":Bone_Size, "Bone_Metabolism":Bone_Metabolism, "Bone_CO2":Bone_CO2, "Bone_Fuel":Bone_Fuel, "Bone_Vasculature":Bone_Vasculature, "Bone_Structure":Bone_Structure, "Bone":Bone, "Bone_Function":Bone_Function, "Bone_Mineral":Bone_Mineral, "Bone_Flow":Bone_Flow, "Bone_Ph":Bone_Ph, "Bone_Pressure":Bone_Pressure, "Bone_AlphaReceptors":Bone_AlphaReceptors, "TissueH2O":TissueH2O, "UT_H2O":UT_H2O, "MT_H2O":MT_H2O, "LT_H2O":LT_H2O, "MT_CapillaryProtein":MT_CapillaryProtein, "CapillaryProtein":CapillaryProtein, "LT_CapillaryProtein":LT_CapillaryProtein, "UT_CapillaryProtein":UT_CapillaryProtein, "LT_LymphWater":LT_LymphWater, "MT_LymphWater":MT_LymphWater, "LymphWater":LymphWater, "UT_LymphWater":UT_LymphWater, "CellH2O":CellH2O, "UT_LymphProtein":UT_LymphProtein, "MT_LymphProtein":MT_LymphProtein, "LT_LymphProtein":LT_LymphProtein, "LymphProtein":LymphProtein, "LT_InterstitialWater":LT_InterstitialWater, "MT_InterstitialWater":MT_InterstitialWater, "UT_InterstitialWater":UT_InterstitialWater, "InterstitialWater":InterstitialWater, "MT_InterstitialProtein":MT_InterstitialProtein, "UT_InterstitialProtein":UT_InterstitialProtein, "LT_InterstitialProtein":LT_InterstitialProtein, "InterstitialProtein":InterstitialProtein, "UT_CapillaryWater":UT_CapillaryWater, "CapillaryWater":CapillaryWater, "LT_CapillaryWater":LT_CapillaryWater, "MT_CapillaryWater":MT_CapillaryWater, "PeritoneumSpace":PeritoneumSpace, "Peritoneum":Peritoneum, "PeritoneumProtein":PeritoneumProtein, "GlycerolPool":GlycerolPool, "Glycerol":Glycerol, "Metabolism_RespiratoryQuotient":Metabolism_RespiratoryQuotient, "Metabolism_MetabolicRate":Metabolism_MetabolicRate, "Metabolism_Tools":Metabolism_Tools, "Thyroid":Thyroid, "Metabolism":Metabolism, "Metabolism_FattyAcid":Metabolism_FattyAcid, "Metabolism_Glucose":Metabolism_Glucose, "Metabolism_FuelUse":Metabolism_FuelUse, "Metabolism_CaloriesUsed":Metabolism_CaloriesUsed, "OsmCell":OsmCell, "Osmoles":Osmoles, "OsmBody":OsmBody, "OsmECFV":OsmECFV, "conc_EPODelay":conc_EPODelay, "RBCSecretion":RBCSecretion, "PlasmaVol":PlasmaVol, "BloodVol":BloodVol, "BloodVolume":BloodVolume, "RBCVol":RBCVol, "RBCH2O":RBCH2O, "RBCClearance":RBCClearance, "RBCSolids":RBCSolids, "TriglycerideHydrolysis":TriglycerideHydrolysis, "TriglyceridePool":TriglyceridePool, "Triglyceride":Triglyceride, "TriglycerideDecomposition":TriglycerideDecomposition, "Organs_AlphaReceptors":Organs_AlphaReceptors, "Organs_Ph":Organs_Ph, "Organs_Flow":Organs_Flow, "Organs_ScaleH2O":Organs_ScaleH2O, "Organs_ScaleConductance":Organs_ScaleConductance, "Organs_Fuel":Organs_Fuel, "Organs_Pressure":Organs_Pressure, "Organs":Organs, "Organs_Lactate":Organs_Lactate, "Organs_Vasculature":Organs_Vasculature, "Organs_Function":Organs_Function, "Organs_Structure":Organs_Structure, "Organs_ScaleCals":Organs_ScaleCals, "Organs_Metabolism":Organs_Metabolism, "Organs_CO2":Organs_CO2, "Organs_Size":Organs_Size, "Organs_BetaReceptors":Organs_BetaReceptors, "DietGoalElectrolytes":DietGoalElectrolytes, "DietIntakeElectrolytes":DietIntakeElectrolytes, "DietThirst":DietThirst, "DietFeeding":DietFeeding, "DietGoalH2O":DietGoalH2O, "DietIntakeNutrition":DietIntakeNutrition, "DietGoalNutrition":DietGoalNutrition, "Diet":Diet, "DietAppetite":DietAppetite, "DietIntakeH2O":DietIntakeH2O, "RightHeart_Pressure":RightHeart_Pressure, "RightHeart_Vasculature":RightHeart_Vasculature, "RightHeart_Work":RightHeart_Work, "RightHeart_Size":RightHeart_Size, "RightHeart_Function":RightHeart_Function, "RightHeart_Fuel":RightHeart_Fuel, "RightHeart_CO2":RightHeart_CO2, "RightHeart_AlphaReceptors":RightHeart_AlphaReceptors, "RightHeart_ContractileProtein":RightHeart_ContractileProtein, "RightHeart_Ph":RightHeart_Ph, "RightHeart_Structure":RightHeart_Structure, "RightHeart_Metabolism":RightHeart_Metabolism, "RightHeart":RightHeart, "RightHeart_BetaReceptors":RightHeart_BetaReceptors, "RightHeart_Infarction":RightHeart_Infarction, "RightHeart_Flow":RightHeart_Flow, "RightHeart_Lactate":RightHeart_Lactate, "AminoAcid":AminoAcid, "AAPool":AAPool, "GnRH":GnRH, "Status":Status, "LipidDeposits":LipidDeposits, "LipidDeposits_Uptake":LipidDeposits_Uptake, "LipidDeposits_Release":LipidDeposits_Release, "OralH2OGlucoseLoad":OralH2OGlucoseLoad, "BVSeq":BVSeq, "SequesteredBlood":SequesteredBlood, "BVSeqVeins":BVSeqVeins, "BVSeqArtys":BVSeqArtys, "CardiacCycle":CardiacCycle, "DiastolicPressure":DiastolicPressure, "HypothalamusSweatingAcclimation":HypothalamusSweatingAcclimation, "HypothalamusShivering":HypothalamusShivering, "Hypothalamus":Hypothalamus, "HypothalamusTSH":HypothalamusTSH, "HypothalamusSkinFlow":HypothalamusSkinFlow, "HypothalamusSweating":HypothalamusSweating, "HypothalamusShiveringAcclimation":HypothalamusShiveringAcclimation, "RespiratoryCenter_Exercise":RespiratoryCenter_Exercise, "RespiratoryCenter_Metaboreflex":RespiratoryCenter_Metaboreflex, "RespiratoryCenter":RespiratoryCenter, "RespiratoryCenter_Chemical":RespiratoryCenter_Chemical, "RespiratoryCenter_Radiation":RespiratoryCenter_Radiation, "RespiratoryCenter_Output":RespiratoryCenter_Output, "RespiratoryCenter_Integration":RespiratoryCenter_Integration, "GlucagonSecretion":GlucagonSecretion, "Glucagon":Glucagon, "GlucagonPool":GlucagonPool, "GlucagonClearance":GlucagonClearance, "FractReab":FractReab, "Nephrons":Nephrons, "NephronANP":NephronANP, "NephronIFP":NephronIFP, "NephronGlucose":NephronGlucose, "NephronAldo":NephronAldo, "VasaRecta":VasaRecta, "NephronADH":NephronADH, "NephronKetoacids":NephronKetoacids, "GlomerulusKetoacid":GlomerulusKetoacid, "GlomerulusBicarbonate":GlomerulusBicarbonate, "GlomerulusUrea":GlomerulusUrea, "GlomerulusChloride":GlomerulusChloride, "GlomerulusSulphate":GlomerulusSulphate, "GlomerulusSodium":GlomerulusSodium, "Glomerulus":Glomerulus, "GlomerulusCreatinine":GlomerulusCreatinine, "GlomerulusGlucose":GlomerulusGlucose, "GlomerulusPhosphate":GlomerulusPhosphate, "GlomerulusProtein":GlomerulusProtein, "GlomerulusFiltrate":GlomerulusFiltrate, "TGF_Renin":TGF_Renin, "MD_Na":MD_Na, "MaculaDensa":MaculaDensa, "TGF_Vascular":TGF_Vascular, "MedullaUrea":MedullaUrea, "MedullaNa":MedullaNa, "Medulla":Medulla, "PT_Na":PT_Na, "PT_H2O":PT_H2O, "PT_NH3":PT_NH3, "ProximalTubule":ProximalTubule, "CD_Urea":CD_Urea, "CD_K":CD_K, "CD_NH4":CD_NH4, "CD_PO4":CD_PO4, "CD_Glucose":CD_Glucose, "CD_Cl":CD_Cl, "CD_KA":CD_KA, "CD_HCO3":CD_HCO3, "CD_SO4":CD_SO4, "CD_Protein":CD_Protein, "CD_Creatinine":CD_Creatinine, "CD_H2OChannels":CD_H2OChannels, "CD_Na":CD_Na, "CollectingDuct":CollectingDuct, "CD_H2O":CD_H2O, "DT_Na":DT_Na, "DT_K":DT_K, "DT_H2O":DT_H2O, "DistalTubule":DistalTubule, "LoopOfHenle":LoopOfHenle, "LH_":LH_, "LH_Na":LH_Na, "LH_H2O":LH_H2O, "Testosterone":Testosterone, "HeartValves":HeartValves, "TricuspidValve_Regurgitation":TricuspidValve_Regurgitation, "TricuspidValve":TricuspidValve, "TricuspidValve_Stenosis":TricuspidValve_Stenosis, "MitralValve":MitralValve, "MitralValve_Regurgitation":MitralValve_Regurgitation, "MitralValve_Stenosis":MitralValve_Stenosis, "AorticValve":AorticValve, "AorticValve_Regurgitation":AorticValve_Regurgitation, "AorticValve_Stenosis":AorticValve_Stenosis, "PulmonicValve_Stenosis":PulmonicValve_Stenosis, "PulmonicValve_Regurgitation":PulmonicValve_Regurgitation, "PulmonicValve":PulmonicValve, "DialyzerActivity":DialyzerActivity, "DialysateComposition":DialysateComposition, "DialysisShunt":DialysisShunt, "DialyzerControl":DialyzerControl, "Hemodialysis":Hemodialysis, "ANP":ANP, "ANPSecretion":ANPSecretion, "ANPPool":ANPPool, "ANPClearance":ANPClearance, "ANPPump":ANPPump, "BloodIons":BloodIons, "CreatininePool":CreatininePool, "Creatinine":Creatinine, "Anesthesia":Anesthesia, "NoAnesthesia":NoAnesthesia, "Transfusion":Transfusion, "Bladder":Bladder, "BladderChloride":BladderChloride, "BladderSulphate":BladderSulphate, "BladderKetoacid":BladderKetoacid, "BladderCreatinine":BladderCreatinine, "BladderGlucose":BladderGlucose, "BladderUrea":BladderUrea, "BladderPotassium":BladderPotassium, "BladderPhosphate":BladderPhosphate, "BladderSodium":BladderSodium, "BladderProtein":BladderProtein, "BladderBicarbonate":BladderBicarbonate, "BladderAmmonia":BladderAmmonia, "BladderVolume":BladderVolume, "Hemorrhage":Hemorrhage, "LeftHeart_Lactate":LeftHeart_Lactate, "LeftHeart_Metabolism":LeftHeart_Metabolism, "LeftHeart_Infarction":LeftHeart_Infarction, "LeftHeart_Flow":LeftHeart_Flow, "LeftHeart_Function":LeftHeart_Function, "LeftHeart_Size":LeftHeart_Size, "LeftHeart_Work":LeftHeart_Work, "LeftHeart_AlphaReceptors":LeftHeart_AlphaReceptors, "LeftHeart_Vasculature":LeftHeart_Vasculature, "LeftHeart_Ph":LeftHeart_Ph, "LeftHeart":LeftHeart, "LeftHeart_Pressure":LeftHeart_Pressure, "LeftHeart_BetaReceptors":LeftHeart_BetaReceptors, "LeftHeart_CO2":LeftHeart_CO2, "LeftHeart_Structure":LeftHeart_Structure, "LeftHeart_Fuel":LeftHeart_Fuel, "LeftHeart_ContractileProtein":LeftHeart_ContractileProtein, "Exercise_Treadmill":Exercise_Treadmill, "Exercise_MusclePump":Exercise_MusclePump, "Exercise_Bike":Exercise_Bike, "Exercise_Motivation":Exercise_Motivation, "Exercise_Metabolism":Exercise_Metabolism, "Exercise":Exercise, "Exercise_Control":Exercise_Control, "EpiClearance":EpiClearance, "AlphaBlockade":AlphaBlockade, "NESecretion":NESecretion, "NEPump":NEPump, "Pheochromocytoma":Pheochromocytoma, "NEPool":NEPool, "EpiPump":EpiPump, "AlphaPool":AlphaPool, "BetaPool":BetaPool, "Catechols":Catechols, "EpiPool":EpiPool, "NEClearance":NEClearance, "EpiSecretion":EpiSecretion, "BetaBlockade":BetaBlockade, "Uterus":Uterus, "Testes_Inhibin":Testes_Inhibin, "Testes_Estradiol":Testes_Estradiol, "Testes":Testes, "Testes_Testosterone":Testes_Testosterone, "Testes_Progesterone":Testes_Progesterone, "Inhibin":Inhibin, "UreaPool":UreaPool, "Urea":Urea, "UreaCell":UreaCell, "EPOClearance":EPOClearance, "EPOPump":EPOPump, "EPOPool":EPOPool, "EPO":EPO, "EPOSecretion":EPOSecretion, "Lactate":Lactate, "LacPool":LacPool, "Infusions":Infusions, "LowerExternalPressure":LowerExternalPressure, "SplanchnicCirculation":SplanchnicCirculation, "HepaticVein":HepaticVein, "HepaticArtery":HepaticArtery, "PortalVein_Glucose":PortalVein_Glucose, "PortalVein":PortalVein, "PortalVein_Insulin":PortalVein_Insulin, "PortalVein_FattyAcid":PortalVein_FattyAcid, "PortalVein_Glucagon":PortalVein_Glucagon, "Wind":Wind, "Clothes":Clothes, "Altitude":Altitude, "RelativeHumidity":RelativeHumidity, "Environment":Environment, "AmbientTemperature":AmbientTemperature, "Barometer":Barometer, "EquivalentAltitude":EquivalentAltitude, "Symptoms":Symptoms, "Brain":Brain, "Brain_Ph":Brain_Ph, "Brain_Pressure":Brain_Pressure, "Brain_Flow":Brain_Flow, "Seizure":Seizure, "Brain_Function":Brain_Function, "Brain_CO2":Brain_CO2, "Brain_Fuel":Brain_Fuel, "Brain_Lactate":Brain_Lactate, "Brain_Metabolism":Brain_Metabolism, "Brain_Structure":Brain_Structure, "GlasgowComaScale":GlasgowComaScale, "Brain_Vasculature":Brain_Vasculature, "Brain_Size":Brain_Size, "BrainInsult":BrainInsult, "BrainInsult_PO2":BrainInsult_PO2, "BrainInsult_Temperature":BrainInsult_Temperature, "BrainInsult_Ph":BrainInsult_Ph, "BrainInsult_Structure":BrainInsult_Structure, "BrainInsult_Fuel":BrainInsult_Fuel, "BrainInsult_Highconc_Osm":BrainInsult_Highconc_Osm, "BrainInsult_Lowconc_Osm":BrainInsult_Lowconc_Osm, "AirSupply_PressureChamber":AirSupply_PressureChamber, "AirSupply":AirSupply, "AirSupply_GasTanks":AirSupply_GasTanks, "AirSupply_InspiredAir":AirSupply_InspiredAir, "LeftAtrium":LeftAtrium, "SplanchnicVeins":SplanchnicVeins, "PulmVeins":PulmVeins, "PulmArty":PulmArty, "RightVentricle":RightVentricle, "RightAtrium":RightAtrium, "LeftVentricle":LeftVentricle, "VascularCompartments":VascularCompartments, "SystemicArtys":SystemicArtys, "PulmCapys":PulmCapys, "SystemicVeins":SystemicVeins, "Inhibin_B":Inhibin_B, "Follicle_Estradiol":Follicle_Estradiol, "Inhibin_A":Inhibin_A, "Ovaries_CorpusLuteum":Ovaries_CorpusLuteum, "Ovaries_Follicle":Ovaries_Follicle, "CorpusLuteum_Involution":CorpusLuteum_Involution, "Follicle_Atresia":Follicle_Atresia, "CorpusLuteum_Estradiol":CorpusLuteum_Estradiol, "Ovaries":Ovaries, "Ovaries_Estradiol":Ovaries_Estradiol, "Ovaries_Inhibin":Ovaries_Inhibin, "Follicle_Growth":Follicle_Growth, "CorpusLuteum_Growth":CorpusLuteum_Growth, "Ovaries_Ovulation":Ovaries_Ovulation, "Ovaries_Testosterone":Ovaries_Testosterone, "Ovaries_Progesterone":Ovaries_Progesterone, "SurfaceArea":SurfaceArea, "BMI":BMI, "Age":Age, "Gender":Gender, "Morphology":Morphology, "Weight":Weight, "Weight_Fluids":Weight_Fluids, "Height":Height, "AnesthesiaIVRespiratoryMuscle":AnesthesiaIVRespiratoryMuscle, "AnesthesiaIVRightHeart":AnesthesiaIVRightHeart, "AnesthesiaIVSkin":AnesthesiaIVSkin, "AnesthesiaIVInjection":AnesthesiaIVInjection, "AnesthesiaIVBone":AnesthesiaIVBone, "AnesthesiaIV":AnesthesiaIV, "AnesthesiaIVLeftHeart":AnesthesiaIVLeftHeart, "AnesthesiaIVInfusion":AnesthesiaIVInfusion, "AnesthesiaIVSolubility":AnesthesiaIVSolubility, "AnesthesiaIVGITract":AnesthesiaIVGITract, "AnesthesiaIVSkeletalMuscle":AnesthesiaIVSkeletalMuscle, "AnesthesiaIVBlood":AnesthesiaIVBlood, "AnesthesiaIVLiver":AnesthesiaIVLiver, "AnesthesiaIVBrain":AnesthesiaIVBrain, "AnesthesiaIVKidney":AnesthesiaIVKidney, "AnesthesiaIVFat":AnesthesiaIVFat, "AnesthesiaIVOtherTissue":AnesthesiaIVOtherTissue, "Autopsy":Autopsy, "Orthostatics":Orthostatics, "RegionalPressure":RegionalPressure, "Hydrostatics":Hydrostatics, "A_VFistula":A_VFistula, "A_VFistula_Flow":A_VFistula_Flow, "A_VFistula_Pressure":A_VFistula_Pressure, "LH_AnteriorPituitary":LH_AnteriorPituitary, "LH":LH, "LH_Circulating":LH_Circulating, "Fat_Flow":Fat_Flow, "Fat_Ph":Fat_Ph, "Fat_Function":Fat_Function, "Fat_Lactate":Fat_Lactate, "Fat_CO2":Fat_CO2, "Fat_Pressure":Fat_Pressure, "Fat_Vasculature":Fat_Vasculature, "Fat_AlphaReceptors":Fat_AlphaReceptors, "Fat":Fat, "Fat_Fuel":Fat_Fuel, "Fat_Structure":Fat_Structure, "Fat_Metabolism":Fat_Metabolism, "Fat_Size":Fat_Size, "Liver":Liver, "Liver_Metabolism":Liver_Metabolism, "Liver_Ph":Liver_Ph, "Liver_CO2":Liver_CO2, "Liver_AlphaReceptors":Liver_AlphaReceptors, "Liver_Structure":Liver_Structure, "Liver_Size":Liver_Size, "Liver_O2":Liver_O2, "Liver_Function":Liver_Function, "Liver_Lactate":Liver_Lactate, "Liver_Fuel":Liver_Fuel, "KAPump":KAPump, "Ketoacid":Ketoacid, "KAPool":KAPool, "KADecomposition":KADecomposition, "RespiratoryMuscle_Function":RespiratoryMuscle_Function, "RespiratoryMuscle_Size":RespiratoryMuscle_Size, "RespiratoryMuscle_Metabolism":RespiratoryMuscle_Metabolism, "RespiratoryMuscle_Work":RespiratoryMuscle_Work, "RespiratoryMuscle_Vasculature":RespiratoryMuscle_Vasculature, "RespiratoryMuscle_CO2":RespiratoryMuscle_CO2, "RespiratoryMuscle_Pressure":RespiratoryMuscle_Pressure, "RespiratoryMuscle_ContractileProtein":RespiratoryMuscle_ContractileProtein, "RespiratoryMuscle_Fuel":RespiratoryMuscle_Fuel, "RespiratoryMuscle_Ph":RespiratoryMuscle_Ph, "RespiratoryMuscle_Lactate":RespiratoryMuscle_Lactate, "RespiratoryMuscle_AlphaReceptors":RespiratoryMuscle_AlphaReceptors, "RespiratoryMuscle_Structure":RespiratoryMuscle_Structure, "RespiratoryMuscle_Flow":RespiratoryMuscle_Flow, "RespiratoryMuscle":RespiratoryMuscle, "RespiratoryMuscle_Glycogen":RespiratoryMuscle_Glycogen, "RespiratoryMuscle_Insulin":RespiratoryMuscle_Insulin, "LM_Gluconeogenesis":LM_Gluconeogenesis, "LM_FA_Glucose":LM_FA_Glucose, "LM_Glycogenolysis":LM_Glycogenolysis, "LM_Insulin":LM_Insulin, "LM_FattyAcids":LM_FattyAcids, "LM_Ketoacids":LM_Ketoacids, "LM_FA_AminoAcids":LM_FA_AminoAcids, "LM_AminoAcids":LM_AminoAcids, "LM_Glucose":LM_Glucose, "LM_Glycogenesis":LM_Glycogenesis, "LiverMetabolism":LiverMetabolism, "LM_Glycogen":LM_Glycogen, "Progesterone":Progesterone, "FSH":FSH, "FSH_Circulating":FSH_Circulating, "FSH_AnteriorPituitary":FSH_AnteriorPituitary, "LeptinClearance":LeptinClearance, "LeptinPump":LeptinPump, "Leptin":Leptin, "LeptinPool":LeptinPool, "LeptinSecretion":LeptinSecretion, "HepaticFunction":HepaticFunction, "PlasmaProtein":PlasmaProtein, "CircyProtein":CircyProtein, "Colloids":Colloids, "CO2Veins":CO2Veins, "Blood_BaseToGas":Blood_BaseToGas, "CO2Total":CO2Total, "CO2Artys":CO2Artys, "CO2":CO2, "Tissue_BaseToGas":Tissue_BaseToGas, "Muscle_BaseToGas":Muscle_BaseToGas, "Blood_GasToBase":Blood_GasToBase, "Muscle_GasToBase":Muscle_GasToBase, "CO2Tools":CO2Tools, "Tissue_GasToBase":Tissue_GasToBase, "CreatineSkeletalMuscle":CreatineSkeletalMuscle, "Creatine":Creatine, "CreatineCells":CreatineCells, "SympsKidy":SympsKidy, "GangliaKidney":GangliaKidney, "CNSTrophicFactor":CNSTrophicFactor, "Chemoreceptors":Chemoreceptors, "GangliaGeneral":GangliaGeneral, "SympsCNS":SympsCNS, "Mechanoreceptors":Mechanoreceptors, "ExerciseSymps":ExerciseSymps, "MotorRadiation":MotorRadiation, "AdrenalNerve":AdrenalNerve, "LowPressureReceptors":LowPressureReceptors, "Baroreflex":Baroreflex, "SympsChemo":SympsChemo, "CushingResponse":CushingResponse, "SystemicVeins_AlphaReceptors":SystemicVeins_AlphaReceptors, "ChemoreceptorAcclimation":ChemoreceptorAcclimation, "VagusNerve":VagusNerve, "Nerves":Nerves, "OtherTissue_Vasculature":OtherTissue_Vasculature, "OtherTissue_Function":OtherTissue_Function, "OtherTissue_Fuel":OtherTissue_Fuel, "OtherTissue_Size":OtherTissue_Size, "OtherTissue_Pressure":OtherTissue_Pressure, "OtherTissue_Ph":OtherTissue_Ph, "OtherTissue":OtherTissue, "OtherTissue_AlphaReceptors":OtherTissue_AlphaReceptors, "OtherTissue_Lactate":OtherTissue_Lactate, "OtherTissue_Metabolism":OtherTissue_Metabolism, "OtherTissue_CO2":OtherTissue_CO2, "OtherTissue_Flow":OtherTissue_Flow, "OtherTissue_Structure":OtherTissue_Structure, "IVDrip":IVDrip, "Context":Context, "Traits":Traits, "Values_Muscularity":Values_Muscularity, "Values":Values, "Values_Gender":Values_Gender, "Values_Adiposity":Values_Adiposity, "Values_OtherMass":Values_OtherMass, "Values_Height":Values_Height, "Values_Age":Values_Age, "Descriptors":Descriptors, "Male":Male, "Descriptors_Gender":Descriptors_Gender, "Female":Female, "Descriptors_Adiposity":Descriptors_Adiposity, "MorbidlyObese":MorbidlyObese, "Overweight":Overweight, "Underweight":Underweight, "Obese":Obese, "NormalWeight":NormalWeight, "Descriptors_Muscularity":Descriptors_Muscularity, "AboveNormal":AboveNormal, "TrainedAthlete":TrainedAthlete, "Normal":Normal, "BelowNormal":BelowNormal, "Descriptors_BodySize":Descriptors_BodySize, "VeryLarge":VeryLarge, "Large":Large, "Small":Small, "Descriptors_Age":Descriptors_Age, "Old":Old, "Middleaged":Middleaged, "Youngish":Youngish, "Young":Young, "VeryOld":VeryOld, "Start_OrganConductance":Start_OrganConductance, "Start":Start, "Start_OrganCalories":Start_OrganCalories, "Start_Heat":Start_Heat, "Start_Height":Start_Height, "Start_Morphology":Start_Morphology, "Start_FatSize":Start_FatSize, "Start_Weight":Start_Weight, "Start_SkeletalMuscleSize":Start_SkeletalMuscleSize, "Start_Gender":Start_Gender, "Start_Age":Start_Age, "Start_BloodSize":Start_BloodSize, "Start_WholeBody":Start_WholeBody, "Start_BodyH2O":Start_BodyH2O, "Start_General":Start_General, "Start_BodySize":Start_BodySize, "Start_OrganSize":Start_OrganSize, "Start_Creatinine":Start_Creatinine, "Start_Creatine":Start_Creatine, "Start_Metabolism":Start_Metabolism, "Start_Urea":Start_Urea, "Start_FattyAcid":Start_FattyAcid, "Start_AminoAcid":Start_AminoAcid, "Start_Triglyceride":Start_Triglyceride, "Start_Glucose":Start_Glucose, "Start_KetoAcid":Start_KetoAcid, "Start_Testosterone":Start_Testosterone, "Start_Progesterone":Start_Progesterone, "Start_Norepinephrine":Start_Norepinephrine, "Start_Epinephrine":Start_Epinephrine, "Start_ANP":Start_ANP, "Start_Aldosterone":Start_Aldosterone, "Start_Renin":Start_Renin, "Start_FSH":Start_FSH, "Start_Leptin":Start_Leptin, "Start_Insulin":Start_Insulin, "Start_Inhibin":Start_Inhibin, "Start_LH":Start_LH, "Start_ADH":Start_ADH, "Start_Estradiol":Start_Estradiol, "Start_hCG":Start_hCG, "Start_Glucagon":Start_Glucagon, "Start_EPO":Start_EPO, "Start_Hormones":Start_Hormones, "Start_ThyroidHormone":Start_ThyroidHormone, "Start_ExtracellularPotassium":Start_ExtracellularPotassium, "Start_ExtracellularPhosphate":Start_ExtracellularPhosphate, "Start_ExtracellularSodium":Start_ExtracellularSodium, "Start_ExtracellularSulphate":Start_ExtracellularSulphate, "Start_ExtracellularChloride":Start_ExtracellularChloride, "Start_CellularPotassium":Start_CellularPotassium, "Start_Electrolytes":Start_Electrolytes}

#the following are never referenced:
#LM_Glycerol
#LM_Lactate

all_ODEs = [{'type': 'diffeq', 'classname': 'ADHPool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.3}, {'type': 'diffeq', 'classname': 'ADHFastMass', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 32.0}, {'type': 'diffeq', 'classname': 'ADHSlowMass', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 170.0}, {'type': 'diffeq', 'classname': 'GlucosePool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 165.0}, {'type': 'diffeq', 'classname': 'ThyroidPool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 12.0}, {'type': 'diffeq', 'classname': 'Skin_Lactate', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.018}, {'type': 'delay', 'classname': 'Skin_Vasculature', 'outputname': 'Effect', 'k': 'K', 'inputname': 'Stimulus', 'errorlim': None}, {'type': 'stabledelay', 'classname': 'Skin_Fuel', 'outputname': 'FractUseDelay', 'k': 'K', 'inputname': 'FractUse', 'errorlim': 0.01}, {'type': 'diffeq', 'classname': 'Skin_CO2', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.28}, {'type': 'backwardeuler', 'classname': 'Skin_Structure', 'outputname': 'Effect', 'f1': 'F1', 'f2': 'F2', 'errorlim': None}, {'type': 'diffeq', 'classname': 'PO4Pool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.026}, {'type': 'diffeq', 'classname': 'NaPool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 21.7}, {'type': 'diffeq', 'classname': 'SO4Pool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.042}, {'type': 'diffeq', 'classname': 'ClPool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 16.1}, {'type': 'delay', 'classname': 'KAldoEffect', 'outputname': 'Delayed', 'k': 'RateConst', 'inputname': 'Immediate', 'errorlim': 0.01}, {'type': 'diffeq', 'classname': 'KCell', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 39.8}, {'type': 'diffeq', 'classname': 'KPool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.66}, {'type': 'diffeq', 'classname': 'HeatSkeletalMuscle', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 70.0}, {'type': 'diffeq', 'classname': 'HeatSkin', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 7.0}, {'type': 'diffeq', 'classname': 'HeatCore', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 123.0}, {'type': 'diffeq', 'classname': 'CellProtein', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 60000.0}, {'type': 'diffeq', 'classname': 'ExcessLungWater', 'outputname': 'Volume', 'dervname': 'Change', 'errorlim': 10.0}, {'type': 'delay', 'classname': 'ReninSynthesis', 'outputname': 'Rate', 'k': 'K', 'inputname': 'SteadyState', 'errorlim': 2.9}, {'type': 'diffeq', 'classname': 'ReninFree', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 870.0}, {'type': 'diffeq', 'classname': 'ReninGranules', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 8700.0}, {'type': 'diffeq', 'classname': 'ReninPool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 90.0}, {'type': 'diffeq', 'classname': 'FAPool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 25.0}, {'type': 'diffeq', 'classname': 'Pericardium_Cavity', 'outputname': 'Vol', 'dervname': 'Change', 'errorlim': 0.1}, {'type': 'diffeq', 'classname': 'Pericardium_V0', 'outputname': 'Vol', 'dervname': 'Change', 'errorlim': 5.0}, {'type': 'diffeq', 'classname': 'SkeletalMuscle_ContractileProtein', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 29.0}, {'type': 'stabledelay', 'classname': 'SkeletalMuscle_Fuel', 'outputname': 'FractUseDelay', 'k': 'K', 'inputname': 'FractUse', 'errorlim': 0.01}, {'type': 'backwardeuler', 'classname': 'SkeletalMuscle_Structure', 'outputname': 'Effect', 'f1': 'F1', 'f2': 'F2', 'errorlim': None}, {'type': 'diffeq', 'classname': 'SkeletalMuscle_Lactate', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.202}, {'type': 'diffeq', 'classname': 'SkeletalMuscle_CO2', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 3.24}, {'type': 'delay', 'classname': 'SkeletalMuscle_MetabolicVasodilation', 'outputname': 'Effect', 'k': 'K', 'inputname': 'SteadyState', 'errorlim': 0.01}, {'type': 'delay', 'classname': 'SkeletalMuscle_Vasculature', 'outputname': 'Effect', 'k': 'K', 'inputname': 'Stimulus', 'errorlim': None}, {'type': 'diffeq', 'classname': 'SkeletalMuscle_Glycogen', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 5.3}, {'type': 'delay', 'classname': 'SkeletalMuscle_Insulin', 'outputname': 'conc_InsulinDelayed', 'k': 'K', 'inputname': 'conc_Insulin', 'errorlim': 0.2}, {'type': 'diffeq', 'classname': 'hCG', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 1.0}, {'type': 'diffeq', 'classname': 'Estradiol', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.01}, {'type': 'diffeq', 'classname': 'MidodrinePool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 20.0}, {'type': 'diffeq', 'classname': 'MidodrineGILumen', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 5.0}, {'type': 'diffeq', 'classname': 'DesglymidodrinePool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 40.0}, {'type': 'diffeq', 'classname': 'DigoxinPool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.01}, {'type': 'diffeq', 'classname': 'DigoxinGILumen', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.01}, {'type': 'diffeq', 'classname': 'FurosemideSingleDose', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 1.0}, {'type': 'diffeq', 'classname': 'FurosemidePool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 1.0}, {'type': 'diffeq', 'classname': 'ThiazideGILumen', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 1.0}, {'type': 'diffeq', 'classname': 'ThiazidePool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 1.0}, {'type': 'diffeq', 'classname': 'GILumenSodium', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.8}, {'type': 'diffeq', 'classname': 'GILumenPotassium', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.25}, {'type': 'diffeq', 'classname': 'GILumenChloride', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.9}, {'type': 'diffeq', 'classname': 'GILumenVolume', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 10.0}, {'type': 'diffeq', 'classname': 'GILumenTemperature', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 1.6}, {'type': 'diffeq', 'classname': 'GILumenCarbohydrates', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 19.3}, {'type': 'diffeq', 'classname': 'GILumenProtein', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 16.0}, {'type': 'diffeq', 'classname': 'GILumenFat', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 19.9}, {'type': 'backwardeuler', 'classname': 'GITract_Structure', 'outputname': 'Effect', 'f1': 'F1', 'f2': 'F2', 'errorlim': None}, {'type': 'diffeq', 'classname': 'GITract_CO2', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.18}, {'type': 'stabledelay', 'classname': 'GITract_Fuel', 'outputname': 'FractUseDelay', 'k': 'K', 'inputname': 'FractUse', 'errorlim': 0.01}, {'type': 'delay', 'classname': 'GITract_Vasculature', 'outputname': 'Effect', 'k': 'K', 'inputname': 'Stimulus', 'errorlim': None}, {'type': 'diffeq', 'classname': 'GITract_Lactate', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.011}, {'type': 'diffeq', 'classname': 'AldoPool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 142.0}, {'type': 'stabledelay', 'classname': 'O2Artys', 'outputname': 'conc_O2', 'k': 'K', 'inputname': 'conc_O2_SteadyState', 'errorlim': 0.002}, {'type': 'stabledelay', 'classname': 'O2Veins', 'outputname': 'conc_O2', 'k': 'K', 'inputname': 'conc_O2_SteadyState', 'errorlim': 0.0015}, {'type': 'diffeq', 'classname': 'SweatFuel', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.01}, {'type': 'delay', 'classname': 'SweatAcclimation', 'outputname': 'Effect', 'k': 'K', 'inputname': 'SteadyState', 'errorlim': 0.01}, {'type': 'diffeq', 'classname': 'Kidney_Lactate', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.0026}, {'type': 'stabledelay', 'classname': 'Kidney_MyogenicDelay', 'outputname': 'PressureChange', 'k': 'K', 'inputname': 'PressureChange_Steady_State', 'errorlim': 0.1}, {'type': 'stabledelay', 'classname': 'Kidney_Fuel', 'outputname': 'FractUseDelay', 'k': 'K', 'inputname': 'FractUse', 'errorlim': 0.01}, {'type': 'diffeq', 'classname': 'Kidney_CO2', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.04}, {'type': 'backwardeuler', 'classname': 'Kidney_Structure', 'outputname': 'Effect', 'f1': 'F1', 'f2': 'F2', 'errorlim': None}, {'type': 'delay', 'classname': 'Kidney_Myogenic', 'outputname': 'AdaptedPressure', 'k': 'K', 'inputname': 'InterlobarPressure', 'errorlim': 0.1}, {'type': 'diffeq', 'classname': 'AnesthesiaGasBone', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.02}, {'type': 'diffeq', 'classname': 'AnesthesiaGasBrain', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.02}, {'type': 'diffeq', 'classname': 'AnesthesiaGasLiver', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.02}, {'type': 'diffeq', 'classname': 'AnesthesiaGasGITract', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.02}, {'type': 'diffeq', 'classname': 'AnesthesiaGasSkeletalMuscle', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.02}, {'type': 'diffeq', 'classname': 'AnesthesiaGasFat', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.02}, {'type': 'diffeq', 'classname': 'AnesthesiaGasRespiratoryMuscle', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.02}, {'type': 'stablediffeq', 'classname': 'AnesthesiaGasVein', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.1}, {'type': 'diffeq', 'classname': 'AnesthesiaGasSkin', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.02}, {'type': 'diffeq', 'classname': 'AnesthesiaGasLeftHeart', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.02}, {'type': 'stablediffeq', 'classname': 'AnesthesiaGasArty', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.1}, {'type': 'diffeq', 'classname': 'AnesthesiaGasOtherTissue', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.02}, {'type': 'diffeq', 'classname': 'AnesthesiaGasKidney', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.02}, {'type': 'diffeq', 'classname': 'AnesthesiaGasRightHeart', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.02}, {'type': 'diffeq', 'classname': 'CO', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 10.0}, {'type': 'delay', 'classname': 'InsulinSynthesis', 'outputname': 'Rate', 'k': 'K', 'inputname': 'SteadyState', 'errorlim': 0.17}, {'type': 'diffeq', 'classname': 'InsulinPool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 1.0}, {'type': 'diffeq', 'classname': 'InsulinStorage', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 20.0}, {'type': 'diffeq', 'classname': 'Bone_Lactate', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.035}, {'type': 'diffeq', 'classname': 'Bone_CO2', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.56}, {'type': 'stabledelay', 'classname': 'Bone_Fuel', 'outputname': 'FractUseDelay', 'k': 'K', 'inputname': 'FractUse', 'errorlim': 0.01}, {'type': 'delay', 'classname': 'Bone_Vasculature', 'outputname': 'Effect', 'k': 'K', 'inputname': 'Stimulus', 'errorlim': None}, {'type': 'backwardeuler', 'classname': 'Bone_Structure', 'outputname': 'Effect', 'f1': 'F1', 'f2': 'F2', 'errorlim': None}, {'type': 'diffeq', 'classname': 'Bone_Mineral', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 57.5}, {'type': 'diffeq', 'classname': 'UT_H2O', 'outputname': 'Vol', 'dervname': 'Change', 'errorlim': 98.0}, {'type': 'diffeq', 'classname': 'MT_H2O', 'outputname': 'Vol', 'dervname': 'Change', 'errorlim': 190.0}, {'type': 'diffeq', 'classname': 'LT_H2O', 'outputname': 'Vol', 'dervname': 'Change', 'errorlim': 98.0}, {'type': 'diffeq', 'classname': 'MT_InterstitialProtein', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.75}, {'type': 'diffeq', 'classname': 'UT_InterstitialProtein', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.75}, {'type': 'diffeq', 'classname': 'LT_InterstitialProtein', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.75}, {'type': 'diffeq', 'classname': 'PeritoneumSpace', 'outputname': 'Volume', 'dervname': 'Change', 'errorlim': 10.0}, {'type': 'diffeq', 'classname': 'PeritoneumProtein', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 10.0}, {'type': 'diffeq', 'classname': 'GlycerolPool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 15.0}, {'type': 'delay', 'classname': 'conc_EPODelay', 'outputname': 'Effect', 'k': 'K', 'inputname': 'SteadyState', 'errorlim': 0.01}, {'type': 'diffeq', 'classname': 'PlasmaVol', 'outputname': 'Vol', 'dervname': 'Change', 'errorlim': 30.0}, {'type': 'diffeq', 'classname': 'RBCVol', 'outputname': 'Vol', 'dervname': 'Change', 'errorlim': 24.0}, {'type': 'diffeq', 'classname': 'TriglyceridePool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 125.0}, {'type': 'delay', 'classname': 'RightHeart_Vasculature', 'outputname': 'Effect', 'k': 'K', 'inputname': 'Stimulus', 'errorlim': None}, {'type': 'stabledelay', 'classname': 'RightHeart_Fuel', 'outputname': 'FractUseDelay', 'k': 'K', 'inputname': 'FractUse', 'errorlim': 0.01}, {'type': 'diffeq', 'classname': 'RightHeart_CO2', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.01}, {'type': 'diffeq', 'classname': 'RightHeart_ContractileProtein', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.12}, {'type': 'backwardeuler', 'classname': 'RightHeart_Structure', 'outputname': 'Effect', 'f1': 'F1', 'f2': 'F2', 'errorlim': None}, {'type': 'delay', 'classname': 'RightHeart_Infarction', 'outputname': 'DeadTissueFraction', 'k': 'DeadTissueK', 'inputname': 'DamagedTissueFraction', 'errorlim': 0.01}, {'type': 'diffeq', 'classname': 'RightHeart_Lactate', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.0003}, {'type': 'diffeq', 'classname': 'AAPool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 75.0}, {'type': 'diffeq', 'classname': 'LipidDeposits', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 130.0}, {'type': 'diffeq', 'classname': 'OralH2OGlucoseLoad', 'outputname': 'TotalH2O', 'dervname': 'H2OChange', 'errorlim': None}, {'type': 'diffeq', 'classname': 'OralH2OGlucoseLoad', 'outputname': 'TotalGlucose', 'dervname': 'GlucoseChange', 'errorlim': None}, {'type': 'stablediffeq', 'classname': 'BVSeqVeins', 'outputname': 'Vol', 'dervname': 'Change', 'errorlim': 1.5}, {'type': 'stablediffeq', 'classname': 'BVSeqArtys', 'outputname': 'Vol', 'dervname': 'Change', 'errorlim': 0.5}, {'type': 'delay', 'classname': 'HypothalamusSweatingAcclimation', 'outputname': 'Offset', 'k': 'K', 'inputname': 'SteadyState', 'errorlim': 0.003}, {'type': 'delay', 'classname': 'HypothalamusShiveringAcclimation', 'outputname': 'Offset', 'k': 'K', 'inputname': 'SteadyState', 'errorlim': 0.003}, {'type': 'diffeq', 'classname': 'GlucagonPool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 15.0}, {'type': 'delay', 'classname': 'NephronANP', 'outputname': 'conc_ANPDelayed', 'k': 'K', 'inputname': 'conc_ANPPool', 'errorlim': None}, {'type': 'delay', 'classname': 'NephronAldo', 'outputname': 'conc_AldoDelayed', 'k': 'K', 'inputname': 'conc_AldoPool', 'errorlim': None}, {'type': 'delay', 'classname': 'NephronADH', 'outputname': 'conc_ADHDelayed', 'k': 'K', 'inputname': 'conc_ADHPool', 'errorlim': None}, {'type': 'stabledelay', 'classname': 'TGF_Vascular', 'outputname': 'Signal', 'k': 'K', 'inputname': 'Steady_State', 'errorlim': 0.01}, {'type': 'diffeq', 'classname': 'MedullaUrea', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 5.9}, {'type': 'diffeq', 'classname': 'MedullaNa', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.13}, {'type': 'delay', 'classname': 'PT_NH3', 'outputname': 'ChronicDelay', 'k': 'K', 'inputname': 'ChronicPhEffect', 'errorlim': None}, {'type': 'diffeq', 'classname': 'CD_H2OChannels', 'outputname': 'Inactive', 'dervname': 'Change', 'errorlim': 0.01}, {'type': 'diffeq', 'classname': 'Testosterone', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 2.0}, {'type': 'diffeq', 'classname': 'DialyzerActivity', 'outputname': 'TotalDialysateUsed', 'dervname': 'DialysateChange', 'errorlim': None}, {'type': 'diffeq', 'classname': 'DialyzerActivity', 'outputname': 'TotalUltrafiltration', 'dervname': 'UltrafiltrationChange', 'errorlim': None}, {'type': 'delay', 'classname': 'ANPSecretion', 'outputname': 'NaturalRate', 'k': 'K', 'inputname': 'SteadyState', 'errorlim': 0.67}, {'type': 'backwardeuler', 'classname': 'ANPPool', 'outputname': 'Mass', 'f1': 'F1', 'f2': 'F2', 'errorlim': 3.0}, {'type': 'diffeq', 'classname': 'CreatininePool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 3.1}, {'type': 'diffeq', 'classname': 'Transfusion', 'outputname': 'Volume', 'dervname': 'Rate', 'errorlim': 10.0}, {'type': 'diffeq', 'classname': 'BladderChloride', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': None}, {'type': 'diffeq', 'classname': 'BladderSulphate', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': None}, {'type': 'diffeq', 'classname': 'BladderKetoacid', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': None}, {'type': 'diffeq', 'classname': 'BladderCreatinine', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': None}, {'type': 'diffeq', 'classname': 'BladderGlucose', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': None}, {'type': 'diffeq', 'classname': 'BladderUrea', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': None}, {'type': 'diffeq', 'classname': 'BladderPotassium', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': None}, {'type': 'diffeq', 'classname': 'BladderPhosphate', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': None}, {'type': 'diffeq', 'classname': 'BladderSodium', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': None}, {'type': 'diffeq', 'classname': 'BladderProtein', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': None}, {'type': 'diffeq', 'classname': 'BladderBicarbonate', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': None}, {'type': 'diffeq', 'classname': 'BladderAmmonia', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': None}, {'type': 'diffeq', 'classname': 'BladderVolume', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 10.0}, {'type': 'diffeq', 'classname': 'Hemorrhage', 'outputname': 'Volume', 'dervname': 'Rate', 'errorlim': 10.0}, {'type': 'diffeq', 'classname': 'LeftHeart_Lactate', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.002}, {'type': 'delay', 'classname': 'LeftHeart_Infarction', 'outputname': 'DeadTissueFraction', 'k': 'DeadTissueK', 'inputname': 'DamagedTissueFraction', 'errorlim': 0.01}, {'type': 'delay', 'classname': 'LeftHeart_Vasculature', 'outputname': 'Effect', 'k': 'K', 'inputname': 'Stimulus', 'errorlim': None}, {'type': 'diffeq', 'classname': 'LeftHeart_CO2', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.04}, {'type': 'backwardeuler', 'classname': 'LeftHeart_Structure', 'outputname': 'Effect', 'f1': 'F1', 'f2': 'F2', 'errorlim': None}, {'type': 'stabledelay', 'classname': 'LeftHeart_Fuel', 'outputname': 'FractUseDelay', 'k': 'K', 'inputname': 'FractUse', 'errorlim': 0.01}, {'type': 'diffeq', 'classname': 'LeftHeart_ContractileProtein', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.38}, {'type': 'diffeq', 'classname': 'Exercise_Treadmill', 'outputname': 'DistanceTraveled_Feet', 'dervname': 'Velocity', 'errorlim': None}, {'type': 'delay', 'classname': 'Exercise_Metabolism', 'outputname': 'TotalWatts', 'k': 'TotalWattsK', 'inputname': 'TargetTotalWatts', 'errorlim': 3.0}, {'type': 'delay', 'classname': 'Exercise_Metabolism', 'outputname': 'MotionWatts', 'k': 'MotionWattsK', 'inputname': 'TargetMotionWatts', 'errorlim': 0.6}, {'type': 'delay', 'classname': 'Exercise_Metabolism', 'outputname': 'ContractionRate', 'k': 'ContractionRateK', 'inputname': 'TargetContractionRate', 'errorlim': 0.5}, {'type': 'diffeq', 'classname': 'Pheochromocytoma', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 50000.0}, {'type': 'backwardeuler', 'classname': 'NEPool', 'outputname': 'Mass', 'f1': 'F1', 'f2': 'F2', 'errorlim': 36.0}, {'type': 'backwardeuler', 'classname': 'EpiPool', 'outputname': 'Mass', 'f1': 'F1', 'f2': 'F2', 'errorlim': 6.0}, {'type': 'diffeq', 'classname': 'Inhibin', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.8}, {'type': 'diffeq', 'classname': 'UreaPool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 54.0}, {'type': 'diffeq', 'classname': 'UreaCell', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 101.0}, {'type': 'diffeq', 'classname': 'EPOPool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 1.2}, {'type': 'diffeq', 'classname': 'LacPool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.15}, {'type': 'diffeq', 'classname': 'Brain_CO2', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.14}, {'type': 'stabledelay', 'classname': 'Brain_Fuel', 'outputname': 'FractUseDelay', 'k': 'K', 'inputname': 'FractUse', 'errorlim': 0.01}, {'type': 'diffeq', 'classname': 'Brain_Lactate', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.008}, {'type': 'backwardeuler', 'classname': 'Brain_Structure', 'outputname': 'Effect', 'f1': 'F1', 'f2': 'F2', 'errorlim': None}, {'type': 'delay', 'classname': 'Brain_Vasculature', 'outputname': 'Effect', 'k': 'K', 'inputname': 'Stimulus', 'errorlim': None}, {'type': 'stabledelay', 'classname': 'BrainInsult_PO2', 'outputname': 'PO2Delay', 'k': 'K', 'inputname': 'PO2', 'errorlim': 0.37}, {'type': 'stablediffeq', 'classname': 'LeftAtrium', 'outputname': 'Vol', 'dervname': 'Change', 'errorlim': 10.0}, {'type': 'stablediffeq', 'classname': 'SplanchnicVeins', 'outputname': 'Vol', 'dervname': 'Change', 'errorlim': 10.0}, {'type': 'stablediffeq', 'classname': 'PulmVeins', 'outputname': 'Vol', 'dervname': 'Change', 'errorlim': 10.0}, {'type': 'stablediffeq', 'classname': 'PulmArty', 'outputname': 'Vol', 'dervname': 'Change', 'errorlim': 10.0}, {'type': 'stabledelay', 'classname': 'RightVentricle', 'outputname': 'Vol', 'k': 'K', 'inputname': 'Vol_SteadyState', 'errorlim': 0.9}, {'type': 'stablediffeq', 'classname': 'RightAtrium', 'outputname': 'Vol', 'dervname': 'Change', 'errorlim': 10.0}, {'type': 'stabledelay', 'classname': 'LeftVentricle', 'outputname': 'Vol', 'k': 'K', 'inputname': 'Vol_SteadyState', 'errorlim': 0.9}, {'type': 'stablediffeq', 'classname': 'SystemicArtys', 'outputname': 'Vol', 'dervname': 'Change', 'errorlim': 10.0}, {'type': 'stablediffeq', 'classname': 'PulmCapys', 'outputname': 'Vol', 'dervname': 'Change', 'errorlim': 10.0}, {'type': 'diffeq', 'classname': 'Ovaries_CorpusLuteum', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 1.0}, {'type': 'diffeq', 'classname': 'Ovaries_Follicle', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 1.0}, {'type': 'diffeq', 'classname': 'AnesthesiaIVRespiratoryMuscle', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 1.6}, {'type': 'diffeq', 'classname': 'AnesthesiaIVRightHeart', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.02}, {'type': 'diffeq', 'classname': 'AnesthesiaIVSkin', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 1.61}, {'type': 'diffeq', 'classname': 'AnesthesiaIVInjection', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 3.0}, {'type': 'diffeq', 'classname': 'AnesthesiaIVBone', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 2.4}, {'type': 'diffeq', 'classname': 'AnesthesiaIVLeftHeart', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.11}, {'type': 'diffeq', 'classname': 'AnesthesiaIVGITract', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 1.08}, {'type': 'diffeq', 'classname': 'AnesthesiaIVSkeletalMuscle', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 11.1}, {'type': 'diffeq', 'classname': 'AnesthesiaIVBlood', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 2.16}, {'type': 'diffeq', 'classname': 'AnesthesiaIVLiver', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.6}, {'type': 'diffeq', 'classname': 'AnesthesiaIVBrain', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.6}, {'type': 'diffeq', 'classname': 'AnesthesiaIVKidney', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.13}, {'type': 'diffeq', 'classname': 'AnesthesiaIVFat', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 6.4}, {'type': 'diffeq', 'classname': 'AnesthesiaIVOtherTissue', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 2.4}, {'type': 'delay', 'classname': 'LH_AnteriorPituitary', 'outputname': 'EstradiolEffectDelayed', 'k': 'K', 'inputname': 'EstradiolEffect', 'errorlim': 0.01}, {'type': 'diffeq', 'classname': 'LH_Circulating', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 1.0}, {'type': 'diffeq', 'classname': 'Fat_Lactate', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.025}, {'type': 'diffeq', 'classname': 'Fat_CO2', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.4}, {'type': 'delay', 'classname': 'Fat_Vasculature', 'outputname': 'Effect', 'k': 'K', 'inputname': 'Stimulus', 'errorlim': None}, {'type': 'stabledelay', 'classname': 'Fat_Fuel', 'outputname': 'FractUseDelay', 'k': 'K', 'inputname': 'FractUse', 'errorlim': 0.01}, {'type': 'backwardeuler', 'classname': 'Fat_Structure', 'outputname': 'Effect', 'f1': 'F1', 'f2': 'F2', 'errorlim': None}, {'type': 'diffeq', 'classname': 'Liver_CO2', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.23}, {'type': 'backwardeuler', 'classname': 'Liver_Structure', 'outputname': 'Effect', 'f1': 'F1', 'f2': 'F2', 'errorlim': None}, {'type': 'diffeq', 'classname': 'Liver_Lactate', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.014}, {'type': 'stabledelay', 'classname': 'Liver_Fuel', 'outputname': 'FractUseDelay', 'k': 'K', 'inputname': 'FractUse', 'errorlim': 0.01}, {'type': 'diffeq', 'classname': 'KAPool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.0075}, {'type': 'delay', 'classname': 'RespiratoryMuscle_Vasculature', 'outputname': 'Effect', 'k': 'K', 'inputname': 'Stimulus', 'errorlim': None}, {'type': 'diffeq', 'classname': 'RespiratoryMuscle_CO2', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.48}, {'type': 'diffeq', 'classname': 'RespiratoryMuscle_ContractileProtein', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 4.2}, {'type': 'stabledelay', 'classname': 'RespiratoryMuscle_Fuel', 'outputname': 'FractUseDelay', 'k': 'K', 'inputname': 'FractUse', 'errorlim': 0.01}, {'type': 'diffeq', 'classname': 'RespiratoryMuscle_Lactate', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.03}, {'type': 'backwardeuler', 'classname': 'RespiratoryMuscle_Structure', 'outputname': 'Effect', 'f1': 'F1', 'f2': 'F2', 'errorlim': None}, {'type': 'diffeq', 'classname': 'RespiratoryMuscle_Glycogen', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.46}, {'type': 'delay', 'classname': 'RespiratoryMuscle_Insulin', 'outputname': 'conc_InsulinDelayed', 'k': 'K', 'inputname': 'conc_Insulin', 'errorlim': 0.2}, {'type': 'delay', 'classname': 'LM_Insulin', 'outputname': 'conc_InsulinDelayed', 'k': 'K', 'inputname': 'conc_Insulin', 'errorlim': 0.5}, {'type': 'diffeq', 'classname': 'LM_Glycogen', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 1.0}, {'type': 'diffeq', 'classname': 'Progesterone', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.3}, {'type': 'diffeq', 'classname': 'FSH_Circulating', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.6}, {'type': 'delay', 'classname': 'FSH_AnteriorPituitary', 'outputname': 'EstradiolEffectDelayed', 'k': 'K', 'inputname': 'EstradiolEffect', 'errorlim': 0.01}, {'type': 'diffeq', 'classname': 'LeptinPool', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 1.2}, {'type': 'diffeq', 'classname': 'PlasmaProtein', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 2.1}, {'type': 'stabledelay', 'classname': 'CO2Veins', 'outputname': 'conc_HCO3', 'k': 'K', 'inputname': 'conc_HCO3_SteadyState', 'errorlim': 0.000256}, {'type': 'stabledelay', 'classname': 'CO2Artys', 'outputname': 'conc_HCO3', 'k': 'K', 'inputname': 'conc_HCO3_SteadyState', 'errorlim': 0.00024}, {'type': 'diffeq', 'classname': 'CNSTrophicFactor', 'outputname': 'Effect', 'dervname': 'EffectChange', 'errorlim': 0.01}, {'type': 'delay', 'classname': 'LowPressureReceptors', 'outputname': 'AdaptedPressure', 'k': 'RateConst', 'inputname': 'AvePressure', 'errorlim': 0.06}, {'type': 'delay', 'classname': 'Baroreflex', 'outputname': 'AdaptedPressure', 'k': 'RateConst', 'inputname': 'SinusPressure', 'errorlim': 0.97}, {'type': 'delay', 'classname': 'ChemoreceptorAcclimation', 'outputname': 'Effect', 'k': 'K', 'inputname': 'SteadyState', 'errorlim': 0.1}, {'type': 'delay', 'classname': 'OtherTissue_Vasculature', 'outputname': 'Effect', 'k': 'K', 'inputname': 'Stimulus', 'errorlim': None}, {'type': 'stabledelay', 'classname': 'OtherTissue_Fuel', 'outputname': 'FractUseDelay', 'k': 'K', 'inputname': 'FractUse', 'errorlim': 0.01}, {'type': 'diffeq', 'classname': 'OtherTissue_Lactate', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.032}, {'type': 'diffeq', 'classname': 'OtherTissue_CO2', 'outputname': 'Mass', 'dervname': 'Change', 'errorlim': 0.51}, {'type': 'backwardeuler', 'classname': 'OtherTissue_Structure', 'outputname': 'Effect', 'f1': 'F1', 'f2': 'F2', 'errorlim': None}, {'type': 'diffeq', 'classname': 'IVDrip', 'outputname': 'TotalH2O', 'dervname': 'H2OChange', 'errorlim': None}]

#also removed from here: LM_Glycerol

def save_state():
    store_vals = []
    for i, component_obj in enumerate(components.values()):
        for attr_str in vars(component_obj):
            store_vals.append([component_obj, attr_str, getattr(component_obj, attr_str)])
    return store_vals

def load_state(store_vals):
    for i, tupl in store_vals:
        component = tupl[0]
        attr_str = tupl[1]
        val = tupl[2]
        setattr(component, attr_str, val)

def step_with_timestep(timestep):
    System.Dx = timestep
    Structure.Dervs_func()
    Structure.Wrapup_func()

def calc_optimal_timestep():
    """
    calculates optimal timestep using truncation error

    need to evaluate one step with step of dt_tiny, to then calculate truncation error for every differential equation
    for each diffeq or backwardeuler, keep track of the output and its errolim
    this output is y?
    dydt is the first input to the differential equation
    get new value of every output
    Structure.Dervs_func
    """

    timesteps = []

    store_vals = save_state()
    #with state saved we can do tiny step to do truncation error stuff to get optimal timestep

    #record dydx in all_ODEs 

    #get current dydx for every ODE
    for ODE in all_ODEs:
        ODE_type = ODE["type"]
        classname = ODE["classname"]

        if ODE_type in ["delay", "stabledelay"]:
            #dydx is K * (A - B_pre)
            K_name = ODE["k"] #this will be the name of a variable
            A_name = ODE["inputname"]
            B_pre_name = ODE["outputname"]
            K = getattr(components[classname], K_name)
            A = getattr(components[classname], A_name)
            B_pre = getattr(components[classname], B_pre_name)
            dydt = K * (A - B_pre)
            ODE["dydt"] = dydt
        
        elif ODE_type in ["diffeq", "stablediffeq"]:
            dydt_name = ODE["dervname"]
            dydt = getattr(components[classname], dydt_name)
            ODE["dydt"] = dydt

        elif ODE_type == "backwardeuler":
            f1_name = ODE["f1"]
            f2_name = ODE["f2"]
            y0_name = ODE["outputname"]
            y0 = getattr(components[classname], y0_name)
            f1 = getattr(components[classname], f1_name)
            f2 = getattr(components[classname], f2_name)
            d2y_dt2 = abs(-f2 * (f1 - f2 * y0)) 
            ODE["d2y_dt2"] = d2y_dt2

    #take tiny step forward
    dt_tiny = 1e-6
    step_with_timestep(dt_tiny)

    #recalculate new dydx for every diffeq and delay in the system:
    for ODE in all_ODEs:
        ODE_type = ODE["type"]
        classname = ODE["classname"]

        if ODE_type in ["delay", "stabledelay"]:
            #dydx is K * (A - B_pre)
            K_name = ODE["k"] #this will be the name of a variable
            A_name = ODE["inputname"]
            B_pre_name = ODE["outputname"]
            K = getattr(components[classname], K_name)
            A = getattr(components[classname], A_name)
            B_pre = getattr(components[classname], B_pre_name)
            dydt = K * (A - B_pre)
        
        elif ODE_type in ["diffeq", "stablediffeq"]:
            dydt_name = ODE["dervname"]
            dydt = getattr(components[classname], dydt_name)

        if ODE_type != "backwardeuler":
            old_dydt = ODE["dydt"]
            d2y_dt2 = (dydt - old_dydt) / dt_tiny
            ODE["d2y_dt2"] = (d2y_dt2)

    all_max_timesteps = []

    for ODE in all_ODEs:
        d2y_dt2 = ODE["d2y_dt2"]
        if ODE["errorlim"] == None:
            ODE["errorlim"] = getattr(components[ODE["classname"]], ODE["outputname"])*0.03
        if abs(d2y_dt2) == 0:
            #will get /0 error if try this, just set max_dt to arbitrarily high number
            all_max_timesteps.append(math.inf)
        else:
            max_dt = np.sqrt(2 * ODE["errorlim"] / abs(d2y_dt2))
            all_max_timesteps.append(max_dt)

    return min(all_max_timesteps)

def run_sim(duration):
    Structure.Context_func() #maybe only need to do this once at start?
    Structure.Parms_func() #once at start too?
    Structure.Dervs_func() #once to initialise all the ODE vals
    Structure.Wrapup_func() #once because:?

    def step():
        timestep = calc_optimal_timestep()
        System.Dx = timestep
        Structure.Dervs_func()
        Structure.Wrapup_func()
        System.X += timestep
        print("ADHPool.mass:", ADHPool.Mass)

    while System.X < duration:
        step()


if __name__ == "__main__":
    run_sim(100000)

    """
    TODO: depending on Gender, Ovaries.derv_func() and Uterus.derv_func() might not run. So currently gender defaults to female
    TODO: needed to remove
    """