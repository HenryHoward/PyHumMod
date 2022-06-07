from src import hummod

#set params here:
hummod.BetaBlockade.Block_percent = 50

for n in range(0, 1000):
    hummod.step()
    print("at time: {} seconds:\n    SV is: {}\n    heart rate is: {}\n    carotid sinus pressure is: {}\n    resp rate is {}".format(
        hummod.System.X * 60, 
        hummod.LeftHeartPumping_Pumping.StrokeVolume,
        hummod.Heart_Ventricles.Rate,
        hummod.CarotidSinus.Pressure,
        hummod.Breathing.RespRate))
