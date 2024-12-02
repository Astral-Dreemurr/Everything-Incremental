from tkinter import Tk
from tkinter import Button
from tkinter import Label
from tkinter import Frame
from tkinter import Scrollbar
import tkinter.ttk as ttk
from tkinter import messagebox
from random import randint

#Never Forget to make after Endorsements :skull:
########################################################################################################

EI = Tk()

EI.title("Everything Incremental Alpha")
EI.geometry("300x300")
EI.resizable(width=True,height=True)

########################################################################################################

messagebox.showinfo("Everything Incremental Alpha - Welcome!", "Welcome to Everything Incremental!")
messagebox.showinfo("Everything Incremental Alpha - Original Games List", "Original Games List \n1. Grass Cutting Incremental \n2. Really Grass Cutting Incremental \n3. Distance Incremental \n4. Antimatter Dimensions \n5. AD mods (NG+++, NG++++, NG-, NG-5, NG UD' etc) \n6. Merging Legends \n7. Circle Incremental \n8. Infinite Rarities \n9. Eternal Rarities 1 \n10. Eternal Rarities 2 \n11. Incremental Mass Rewritten \n12. Synergism \n13. Prestreestuck \n14. Prestige Tree \n15. ThetaCore Incremental \n16. Check Back Mod \n17. The Milestone Tree NG+ \n18. The Plant Tree \n19. The Tree Of Life \n20. The Operator Tree \n21. Le Underrated Forest \n22. APTMWYMTNWMMTTWATIEATASIJAPM (Another Prestige Tree Mod Where You Merge Things, Now With Much More Time To Waste! Also, There Isn’t Even A Tree Anymore So It’s Just A Prestige Mod) \nAnd more and more Incremental games unknown...")
messagebox.showwarning("Everything Incremental Alpha - Banned Players", "Banned players in this game : \n1. Baba Shelby (Discord : baba_shelby, Roblox : @TheDiamondCrew2000) \nPlease follow the rules on this game.")

########################################################################################################

MainContentFrame=Frame(EI, relief='solid', bd=2)
InfoSettingsFrame=Frame(EI, relief='solid', bd=2)

########################################################################################################

MainContentNoticeLabel=Label(MainContentFrame, text = 'Main Contents', background = 'yellow')
InfoSettingsNoticeLabel=Label(InfoSettingsFrame, text = 'Info & Settings', background = 'light grey')

MainContentNoticeLabel.pack()
InfoSettingsNoticeLabel.pack()

########################################################################################################

def Stattab():
    EIStattab = Tk()

    EIStattab.title("Everything Incremental Alpha - Stats")
    EIStattab.geometry("300x300")
    EIStattab.resizable(width=True,height=True)



    def NormalStattab():
        EINormalStattab = Tk()

        EINormalStattab.title("Everything Incremental Alpha - Normal Stats")
        EINormalStattab.geometry("300x300")
        EINormalStattab.resizable(width=True,height=True)


        def Sector1Stattab():
            EIS1Stattab = Tk()
            
            EIS1Stattab.title("Everything Incremental Alpha - Sector 1 Stats")
            EIS1Stattab.geometry("300x300")
            EIS1Stattab.resizable(width=True,height=True)

            EIS1Stattab.mainloop()

        
        def Sector2Stattab():
            EIS2Stattab = Tk()

            EIS2Stattab.title("Everything Incremental Alpha - Sector 2 Stats")
            EIS2Stattab.geometry("300x300")
            EIS2Stattab.resizable(width=True,height=True)

            EIS2Stattab.mainloop()

        
        def Sector3Stattab():
            EIS3Stattab = Tk()

            EIS3Stattab.title("Everything Incremental Alpha - Sector 3 Stats")
            EIS3Stattab.geometry("300x300")
            EIS3Stattab.resizable(width=True,height=True)

            EIS3Stattab.mainloop()

        def Sector4Stattab():
            EIS4Stattab = Tk()

            EIS4Stattab.title("Everything Incremental Alpha - Sector 4 Stats")
            EIS4Stattab.geometry("300x300")
            EIS4Stattab.resizable(width=True,height=True)

            EIS4Stattab.mainloop()
        
        
        def Sector5Stattab():
            EIS5Stattab = Tk()

            EIS5Stattab.title("Everything Incremental Alpha - Sector 5 Stats")
            EIS5Stattab.geometry("300x300")
            EIS5Stattab.resizable(width=True,height=True)

            EIS5Stattab.mainloop()

        
        def Sector6Stattab():
            EIS6Stattab = Tk()

            EIS6Stattab.title("Everything Incremental Alpha - Sector 6 Stats")
            EIS6Stattab.geometry("300x300")
            EIS6Stattab.resizable(width=True,height=True)

            EIS6Stattab.mainloop()


        def Sector7Stattab():
            EIS7Stattab = Tk()
            
            EIS7Stattab.title("Everything Incremental Alpha - Sector 7 Stats")
            EIS7Stattab.geometry("300x300")
            EIS7Stattab.resizable(width=True,height=True)

            EIS7Stattab.mainloop()

        
        def Sector8Stattab():
            EIS8Stattab = Tk()

            EIS8Stattab.title("Everything Incremental Alpha - Sector 8 Stats")
            EIS8Stattab.geometry("300x300")
            EIS8Stattab.resizable(width=True,height=True)

            EIS8Stattab.mainloop()


        S1Stats=Button(EINormalStattab, text = 'Sector 1 Stats', background = 'yellow', command=Sector1Stattab)
        S2Stats=Button(EINormalStattab, text = 'Sector 2 Stats', background = 'green', command=Sector2Stattab)
        S3Stats=Button(EINormalStattab, text = 'Sector 3 Stats', background = 'light grey', command=Sector3Stattab)
        S4Stats=Button(EINormalStattab, text = 'Sector 4 Stats', background = 'blue', command=Sector4Stattab)
        S5Stats=Button(EINormalStattab, text = 'Sector 5 Stats', background = 'dark grey', command=Sector5Stattab)
        S6Stats=Button(EINormalStattab, text = 'Sector 6 Stats', background = 'black', command=Sector6Stattab)
        S7Stats=Button(EINormalStattab, text = 'Sector 7 Stats', background = 'purple', command=Sector7Stattab)
        S8Stats=Button(EINormalStattab, text = 'Sector 8 Stats', background = 'orange', command=Sector8Stattab)

        S1Stats.pack()
        S2Stats.pack()
        S3Stats.pack()
        S4Stats.pack()
        S5Stats.pack()
        S6Stats.pack()
        S7Stats.pack()
        S8Stats.pack()

        EINormalStattab.mainloop()

########################################################################################################

    def Upgradetab():
        EIUpgradetab = Tk()

        EIUpgradetab.title("Everything Incremental Alpha - Upgrades")
        EIUpgradetab.geometry("300x300")
        EIUpgradetab.resizable(width=True,height=True)


        def NRUtab():
            EINRUtab = tk()

            EINRUtab.title("Everything Incremental Alpha - Normal Realm Upgrades")
            EINRUtab.geometry("300x300")
            EINRUtab.resizable(width=True,height=True)

            
            def S1Utab():
                EIS1Utab = tk()

                EIS1Utab.title("Everything Incremental Alpha - Sector 1 Upgrades")
                EIS1Utab.geometry("300x300")
                EIS1Utab.resizable(width=True,height=True)

                EIS1Utab.mainloop()

            
            def S2Utab():
                EIS2Utab = tk()
                
                EIS2Utab.title("Everything Incremental Alpha - Sector 2 Upgrades")
                EIS2Utab.geometry("300x300")
                EIS2Utab.resizable(width=True,height=True)

                EIS2Utab.mainloop()

            
            def S3Utab():
                EIS3Utab = tk()

                EIS3Utab.title("Everything Incremental Alpha - Sector 3 Upgrades")
                EIS3Utab.geometry("300x300")
                EIS3Utab.resizable(width=True,height=True)

                EIS3utab.mainloop()

            
            S1U=Button(EINRUtab, text = "Sector 1 Upgrades", background = 'yellow', command=S1Utab)
            S2U=Button(EINRUtab, text = "Sector 2 Upgrades", background = 'lime', command=S2Utab)
            S3U=Button(EINRUtab, text = "Sector 3 Upgrades", background = 'light grey', command=S3Utab)

            S1U.pack()
            S2U.pack()
            S3U.pack()

            EINRUtab.mainloop()

        
        NRU=Button(EIUpgradetab, text = "Normal Realm Upgrades", background = 'yellow', command=NRUtab)

        NRU.pack()


        EIUpgradetab.mainloop()

########################################################################################################

    def TierStattab():
        EITierStattab = Tk()

        EITierStattab.title("Everything Incremental Alpha - Tier Stats")
        EITierStattab.geometry("300x300")
        EITierStattab.resizable(width=True,height=True)



        def Tiertab():
            EITiertab = Tk()
            
            EITiertab.title("Everything Incremental Alpha - Tiers")
            EITiertab.geometry("300x300")
            EITiertab.resizable(width=True,height=True)

            Tier1=Label(EITiertab, text = ('Tier 1 | Req : 100 Power | x2 Power per Tier'), background = 'grey')
            Tier2=Label(EITiertab, text = ('Tier 2 | Req : 10k Power | x2 Power, REBIRTH UNLOCK!'), background = 'grey')
            Tier3=Label(EITiertab, text = ('Tier 3 | Req : 100 Rebirths | x2 Rebirth per Tier, PRESTIGE UNLOCK!'), background = 'grey')
            Tier4=Label(EITiertab, text = ('Tier 4 | Req : 100 Prestige | x2 Power and Rebirth, ASCEND UNLOCK!'), background = 'grey')
            Tier5=Label(EITiertab, text = ('Tier 5 | Req : 100 Ascend | x2 Prestige per Tier, TRANSCEND UNLOCK!'), background = 'grey')
            Tier6=Label(EITiertab, text = ('Tier 6 | Req : 100 Transcend | x2 Power ~ Prestige, ULTRA UNLOCK!'), background = 'grey')
            Tier7=Label(EITiertab, text = ('Tier 7 | Req : 1k Ultra | x2 Ascend per Tier, MEGA UNLOCK!'), background = 'grey')
            Tier8=Label(EITiertab, text = ('Tier 8 | Req : 100 Power | x2 Power ~ Ascend, SACRIFICE UNLOCK!'), background = 'grey')
            Tier9=Label(EITiertab, text = ('Tier 9 | Req : 100 Sacrifice | x5 Power ~ Ascend'), background = 'grey')
            Tier10=Label(EITiertab, text = ('Tier 10 | Req : 10k Sacrifice | HYPER TIER UNLOCK!, REINCARNATIONS UNLOCK!'), background = 'grey')
            Tier11=Label(EITiertab, text = ('Tier 11 | Req : 10 Reins | x2 Transcend per Tier'), background = 'grey')
            Tier12=Label(EITiertab, text = ('Tier 12 | Req : 10k Reins | x2 Power ~ Transcend, MATTER UNLOCK!'), background = 'grey')
            Tier13=Label(EITiertab, text = ('Tier 13 | Req : 10 Matter | x2 Ultra per Tier'), background = 'grey')
            Tier14=Label(EITiertab, text = ('Tier 14 | Req : 1k Matter | x2 Power ~ Ultra'), background = 'grey')
            Tier15=Label(EITiertab, text = ('Tier 15 | Req : 100k Power | x2 Mega per Tier, DARK MATTER UNLOCK!'), background = 'grey')
            Tier16=Label(EITiertab, text = ('Tier 16 | Req : 10 Dark Matter | x2 Power ~ Mega'), background = 'grey')
            Tier17=Label(EITiertab, text = ('Tier 17 | Req : 1k Dark Matter | x5 Power ~ Mega'), background = 'grey')
            Tier18=Label(EITiertab, text = ('Tier 18 | Req : 100k Dark Matter | SECTOR 2 UNLOCK!'), background = 'grey')
            Tier19=Label(EITiertab, text = ('Tier 19 | Req : 100 Grass | GRASS HOP UNLOCK!'), background = 'grey')
            Tier20=Label(EITiertab, text = ('Tier 20 | Req : 10k Grass | x2 Sacrifice per Tier'), background = 'grey')
            Tier21=Label(EITiertab, text = ('Tier 21 | Req : 1m Grass | x2 Power ~ Sacrifice'), background = 'grey')
            Tier22=Label(EITiertab, text = ('Tier 22 | Req : 100 P.P | x2 Reins per Tier'), background = 'grey')
            Tier23=Label(EITiertab, text = ('Tier 23 | Req : 10k P.P | x2 Power ~ Reins'), background = 'grey')
            Tier24=Label(EITiertab, text = ('Tier 24 | Req : 1m P.P | x2 Matter per Tier'), background = 'grey')
            Tier25=Label(EITiertab, text = ('Tier 25 | Req : 100 Crystal | x2 Power ~ Matter'), background = 'grey')
            Tier26=Label(EITiertab, text = ('Tier 26 | Req : 10k Crystal | x2 Dark Matter per Tier'), background = 'grey')
            Tier27=Label(EITiertab, text = ('Tier 27 | Req : 1m Crystal | x2 Power ~ Dark Matter'), background = 'grey')

            Tier1.pack()
            Tier2.pack()
            Tier3.pack()
            Tier4.pack()
            Tier5.pack()
            Tier6.pack()
            Tier7.pack()
            Tier8.pack()
            Tier9.pack()
            Tier10.pack()
            Tier11.pack()
            Tier12.pack()
            Tier13.pack()
            Tier14.pack()
            Tier15.pack()
            Tier16.pack()
            Tier17.pack()
            Tier18.pack()
            Tier19.pack()
            Tier20.pack()
            Tier21.pack()
            Tier22.pack()
            Tier23.pack()
            Tier24.pack()
            Tier25.pack()
            Tier26.pack()
            Tier27.pack()

            EITiertab.mainloop()



        def HyperTiertab():
            EIHTtab = Tk()
            
            EIHTtab.title("Everything Incremental Alpha - Hyper Tiers")
            EIHTtab.geometry("300x300")
            EIHTtab.resizable(width=True,height=True)

            HT1=Label(EIHTtab, text = ('Hyper Tier 1 | Req : 10 Tiers | x5 Power ~ Sacrifice per HT!'), background = 'dark grey')
            
            HT1.pack()

            EIHTtab.mainloop()


        def SuperTiertab():
            EISTtab = Tk()

            EISTtab.title("Everything Incremental Alpha - Super Tiers")
            EISTtab.geometry("300x300")
            EISTtab.resizable(width=True,height=True)

            EISTtab.mainloop()


        def GrassHoptab():
            EIGHtab = Tk()

            EIGHtab.title("Everything Incremental Alpha - Grass Hops")
            EIGHtab.geometry("300x300")
            EIGHtab.resizable(width=True,height=True)

            GHInfo=Label(EIGHtab, text = '! THIS IS NOT 🦗 !\nDo you hate the lack of grasses?\nThen HOP ON THE GRASS TO EARN MORE GRASSES!\n(Dont do this on real life because you will look dumb.)\nEarn Grass to GRASSHOP!\nGrasshop boosts Grasses and other Grass-Related stats and EVEN OTHER SECTOR STATS!\nTho it resets Sector 1~2 Stats ;-;\nBUT THIS IS THE TEST SERVER SO THE STATS WONT RESET!', background = 'lime')

            GH1=Label(EIGHtab, text = ('Grass Hop 1 | Req : 100 Grass | x2 Grass per G.H'), background = 'lime')
            GH2=Label(EIGHtab, text = ('Grass Hop 2 | Req : 10k Grass | x2 Grass'), background = 'lime')
            GH3=Label(EIGHtab, text = ('Grass Hop 3 | Req : 1m Grass | x3 Sector 1 Stats per G.H'), background = 'lime')
            GH4=Label(EIGHtab, text = ('Grass Hop 4 | Req : 100m Grass | x3 Grass'), background = 'lime')
            GH5=Label(EIGHtab, text = ('Grass Hop 5 | Req : 10b Grass | +100% Grass per G.H'), background = 'lime')
            GH6=Label(EIGHtab, text = ('Grass Hop 6 | Req : 1T Grass | x4 Grass'), background = 'lime')
            GH7=Label(EIGHtab, text = ('Grass Hop 7 | Req : 100T Grass | +100% P.P per G.H'), background = 'lime')
            GH8=Label(EIGHtab, text = ('Grass Hop 8 | Req : 10Qd Grass | x5 Grass'), background = 'lime')
            GH9=Label(EIGHtab, text = ('Grass Hop 9 | Req : 1Qn Grass | +100% Crystals per G.H'), background = 'lime')
            GH10=Label(EIGHtab, text = ('Grass Hop 10 | Req : 100Qn Grass | Auto Grass Hop!'), background = 'lime')

            GHScale1=Label(EIGHtab, text = ('Because of getting 10+ Grass Hops, GH SCALING I is active.\nGH price formula is added +10% of the normal formula. (100% -> 110%)'), background = 'lime')

            GH11=Label(EIGHtab, text = ('Grass Hop 11 | Req : 11Sx Grass | +75% Aluminum per G.H'), background = 'lime')
            GH12=Label(EIGHtab, text = ('Grass Hop 12 | Req : 1.21Sp Grass | x6 Grass'), background = 'lime')
            GH13=Label(EIGHtab, text = ('Grass Hop 13 | Req : 133.1Sp Grass | +75% Flower per G.H'), background = 'lime')
            GH14=Label(EIGHtab, text = ('Grass Hop 14 | Req : 14.64Oc Grass | x7 Grass'), background = 'lime')
            GH15=Label(EIGHtab, text = ('Grass Hop 15 | Req : 1.61No Grass | +50% Steel per G.H'), background = 'lime')
            GH16=Label(EIGHtab, text = ('Grass Hop 16 | Req : 177.2No Grass | x8 Grass'), background = 'lime')
            GH17=Label(EIGHtab, text = ('Grass Hop 17 | Req : 19.5De Grass | +50% Charge MK.1 per G.H'), background = 'lime')
            GH18=Label(EIGHtab, text = ('Grass Hop 18 | Req : 2.144UDe Grass | x9 Grass'), background = 'lime')
            GH19=Label(EIGHtab, text = ('Grass Hop 19 | Req : 235.8UDe Grass | +25% Rocket Fuel MK.1 per G.H'), background = 'lime')
            GH20=Label(EIGHtab, text = ('Grass Hop 20 | Req : 26DDe Grass | Multi Grass Hop!'), background = 'lime')

            GHScale2=Label(EIGHtab, text = ('Because of getting 20+ Grass Hops, GH SCALING II is active.\nGH price formula is added +10% of the previous formula. (110% -> 120%)'), background = 'lime')

            GHInfo.pack()

            GH1.pack()
            GH2.pack()
            GH3.pack()
            GH4.pack()
            GH5.pack()
            GH6.pack()
            GH7.pack()
            GH8.pack()
            GH9.pack()
            GH10.pack()

            GHScale1.pack()

            GH11.pack()
            GH12.pack()
            GH13.pack()
            GH14.pack()
            GH15.pack()
            GH16.pack()
            GH17.pack()
            GH18.pack()
            GH19.pack()
            GH20.pack()

            GHScale2.pack()

            EIGHtab.mainloop()


        def GrassSkiptab():
            EIGStab = Tk()

            EIGStab.title("Everything Incremental Alpha - Grass Skips")
            EIGStab.geometry("300x300")
            EIGStab.resizable(width=True,height=True)

            GS1=Label(EIGStab, text = ('Grass Skip 1 | Req : 100 Anti-Grass | x2 Anti-Grass per G.S'), background = 'light blue')
            GS2=Label(EIGStab, text = ('Grass Skip 2 | Req : 10k Anti-Grass | x2 Anti-Grass'), background = 'light blue')
            GS3=Label(EIGStab, text = ('Grass Skip 3 | Req : 1m Anti-Grass | x10 Sector 1 Stats per G.S'), background = 'light blue')
            GS4=Label(EIGStab, text = ('Grass Skip 4 | Req : 100m Anti-Grass | x3 Anti-Grass'), background = 'light blue')
            GS5=Label(EIGStab, text = ('Grass Skip 5 | Req : 10b Anti-Grass | Grass Hops No Longer Resets Anything!'), background = 'light blue')
            GS6=Label(EIGStab, text = ('Grass Skip 6 | Req : 1T Anti-Grass | x4 Anti-Grass'), background = 'light blue')
            GS7=Label(EIGStab, text = ('Grass Skip 7 | Req : 100T Anti-Grass | x5 Sector 2 Stats per G.S'), background = 'light blue')
            GS8=Label(EIGStab, text = ('Grass Skip 8 | Req : 10Qd Anti-Grass | x5 Anti-Grass'), background = 'light blue')
            GS9=Label(EIGStab, text = ('Grass Skip 9 | Req : 1Qn Anti-Grass | x3 Sector 3 Stats per G.S'), background = 'light blue')
            GS10=Label(EIGStab, text = ('Grass Skip 10 | Req : 100Qn Anti-Grass | Auto Grass Skip Unlocked!'), background = 'light blue')

            GSScale1=Label(EIGStab, text = ('Because of getting 10+ Grass Skips, GS SCALING I is active.\nGS price formula is added +10% of the normal formula. (100% -> 110%)'), background = 'light blue')

            GS1.pack()
            GS2.pack()
            GS3.pack()
            GS4.pack()
            GS5.pack()
            GS6.pack()
            GS7.pack()
            GS8.pack()
            GS9.pack()
            GS10.pack()

            GSScale1.pack()

            EIGStab.mainloop()


        def GrassJumptab():
            EIGJtab = Tk()

            EIGJtab.title("Everything Incremental Alpha - Grass Jumps")
            EIGJtab.geometry("300x300")
            EIGJtab.resizable(width=True,height=True)

            GJ1=Label(EIGJtab, text = ('Grass Jump 1 | Req : 100 U-Grass | x2 U-Grass per G.J'), background = 'dark grey')
            GJ2=Label(EIGJtab, text = ('Grass Jump 2 | Req : 10k U-Grass | x2 U-Grass'), background = 'dark grey')
            GJ3=Label(EIGJtab, text = ('Grass Jump 3 | Req : 1m U-Grass | x50 Sector 1 Stats per G.J'), background = 'dark grey')
            GJ4=Label(EIGJtab, text = ('Grass Jump 4 | Req : 100m U-Grass | x3 U-Grass'), background = 'dark grey')
            GJ5=Label(EIGJtab, text = ('Grass Jump 5 | Req : 10b | Grass Skips No Longer Resets Anything!'), background = 'dark grey')

            GJ1.pack()
            GJ2.pack()
            GJ3.pack()
            GJ4.pack()
            GJ5.pack()

            EIGJtab.mainloop()


        def HopSkipJumptab():
            EIHSJtab = Tk()

            EIHSJtab.title("Everything Incremental Alpha - Hop Skip Jumps")
            EIHSJtab.geometry("300x300")
            EIHSJtab.resizable(width=True,height=True)

            EIHSJtab.mainloop()

        
        def ChargerTier1tab():
            EICT1tab = Tk()
            
            EICT1tab.title("Everything Incremental Alpha - Charger Tier 1")
            EICT1tab.geometry("300x300")
            EICT1tab.resizable(width=True,height=True)

            EICT1tab.mainloop()


        def ChargerTier2tab():
            EICT2tab = Tk()

            EICT2tab.title("Everything Incremental Alpha - Charger Tier 2")
            EICT2tab.geometry("300x300")
            EICT2tab.resizable(width=True,height=True)

            EICT2tab.mainloop()


        def ChargerTier3tab():
            EICT3tab = Tk()

            EICT3tab.title("Everything Incremental Alpha - Charger Tier 3")
            EICT3tab.geometry("300x300")
            EICT3tab.resizable(width=True,height=True)

            EICT3tab.mainloop()

        
        def HonorTiertab():
            EIHoTtab = Tk()

            EIHoTtab.title("Everything Incremental Alpha - Honor Tiers")
            EIHoTtab.geometry("300x300")
            EIHoTtab.resizable(width=True,height=True)

            EIHoTtab.mainloop()

        
        def StarPowerTiertab():
            EISPTtab = Tk()

            EISPTtab.title("Everything Incremental Alpha - Star Power Tiers")
            EISPTtab.geometry("300x300")
            EISPTtab.resizable(width=True,height=True)

            EISPTtab.mainloop()


        def CosmicTiertab():
            EICosTtab = Tk()
            
            EICosTtab.title("Everything Incremental Alpha - Cosmic Tiers")
            EICosTtab.geometry("300x300")
            EICosTtab.resizable(width=True,height=True)

            EICosTtab.mainloop()


        def TheRingTiertab():
            EITRTtab = Tk()

            EITRTtab.title("Everything Incremental Alpha - The Ring Tiers")
            EITRTtab.geometry("300x300")
            EITRTtab.resizable(width=True,height=True)

            EITRTtab.pack()


        def BreakTheRingtab():
            EIBTRtab = Tk()

            EIBTRtab.title("Everything Incremental Alpha - BREAK THE RING!")
            EIBTRtab.geometry("300x300")
            EIBTRtab.resizable(width=True,height=True)

            EIBTRtab.pack()

        
        def PlanetoidTiertab():
            EIPTtab = Tk()

            EIPTtab.title("Everything Incremental Alpha - Planetoid Tiers!")
            EIPTtab.geometry("300x300")
            EIPTtab.resizable(width=True,height=True)

            EIPTtab.pack()


        def LunarPowerTiertab():
            EILPTtab = Tk()

            EILPTtab.title("Everything Incremental Alpha - Lunar Power Tiers!")
            EILPTtab.geometry("300x300")
            EILPTtab.resizable(width=True,height=True)
            
            EILPTtab.pack()


        def DarkChargerTiertab():
            EIDCTtab = Tk()

            EIDCTtab.title("Everything Incremental Alpha - Dark Charger Tiers!")
            EIDCTtab.geometry("300x300")
            EIDCTtab.resizable(width=True,height=True)

            EIDCTtab.pack()


        def SupernovaTiertab():
            EISnTtab = Tk()

            EISnTtab.title("Everything Incremental Alpha - Supernova Tiers!")
            EISnTtab.geometry("300x300")
            EISnTtab.resizable(width=True,height=True)

            EISnTtab.pack()


        TierStats=Button(EITierStattab, text = 'Tiers', background = 'pink', command=Tiertab)
        HTStats=Button(EITierStattab, text = 'Hyper Tiers', background = 'orange', command=HyperTiertab)
        STStats=Button(EITierStattab, text = 'Super Tiers', background = 'red', command=SuperTiertab)
        GHStats=Button(EITierStattab, text = 'Grass Hops', background = 'light green', command=GrassHoptab)
        GSStats=Button(EITierStattab, text = 'Grass Skips', background = 'lime', command=GrassSkiptab)
        GJStats=Button(EITierStattab, text = 'Grass Jumps', background = 'green', command=GrassJumptab)
        HSJStats=Button(EITierStattab, text = 'Hop Skip Jumps', background = 'black', command=HopSkipJumptab)
        CT1Stats=Button(EITierStattab, text = 'Charger Tier 1', background = 'light yellow', command=ChargerTier1tab)
        CT2Stats=Button(EITierStattab, text = 'Charger Tier 2', background = 'yellow', command=ChargerTier2tab)
        CT3Stats=Button(EITierStattab, text = 'Charger Tier 3', background = 'orange', command=ChargerTier3tab)
        HoTStats=Button(EITierStattab, text = 'Honor Tiers', background = 'yellow', command=HonorTiertab)
        SPTStats=Button(EITierStattab, text = 'Star Power Tiers', background = 'blue', command=StarPowerTiertab)
        CosTStats=Button(EITierStattab, text = 'Cosmic Tiers', background = 'purple', command=CosmicTiertab)
        TRTStats=Button(EITierStattab, text = 'The Ring Tiers', background = 'light blue', command=TheRingTiertab)
        BTRStats=Button(EITierStattab, text = 'BREAK THE RING!', background = 'purple', command=BreakTheRingtab)
        PTStats=Button(EITierStattab, text = 'Planetoid Tiers', background = 'blue', command=PlanetoidTiertab)
        LPTStats=Button(EITierStattab, text = 'Lunar Power Tiers', background = 'light grey', command=LunarPowerTiertab)
        DCTStats=Button(EITierStattab, text = 'Dark Charger Tiers', background = 'black', command=DarkChargerTiertab)
        SnTStats=Button(EITierStattab, text = 'Supernova Tiers', background = 'orange', command=SupernovaTiertab)
    

        TierStats.pack()
        HTStats.pack()
        STStats.pack()
        GHStats.pack()
        GSStats.pack()
        GJStats.pack()
        HSJStats.pack()
        CT1Stats.pack()
        CT2Stats.pack()
        CT3Stats.pack()
        HoTStats.pack()
        SPTStats.pack()
        CosTStats.pack()
        TRTStats.pack()
        BTRStats.pack()
        PTStats.pack()
        LPTStats.pack()
        DCTStats.pack()
        SnTStats.pack()

        
        EITierStattab.mainloop()
    

    def Runetab():
        EIRunetab = Tk()

        EIRunetab.title("Everything Incremental - Runes")
        EIRunetab.geometry("300x300")
        EIRunetab.resizable(width=True,height=True)

        def NewbieRune():
            NewbRuneRNG = randint(0,100000)

            if NewbRuneRNG == (0):
                messagebox.showinfo("SUPER RARE DROP!", "YOU GOT A RUNE TOKEN! CONGRATULATIONS! (0.001%)")
                print("[SERVER] You got a RUNE TOKEN! (0.001%)")
                print("[GLOBAL] YOU GOT A RUNE TOKEN! (0.001%)")

            elif 1 <= NewbRuneRNG <= 60000:
                messagebox.showinfo("Common Drop!", "You got an Newbie Rune! (60%)")

            elif 60001 <= NewbRuneRNG <= 85000:
                messagebox.showinfo("Common Drop!", "You got an Noob Rune! (25%)")

            elif 85001 <= NewbRuneRNG <= 95000:
                messagebox.showinfo("Common Drop!", "You got an Apprentice Rune! (10%)")

            elif 95001 <= NewbRuneRNG <= 99000:
                messagebox.showinfo("Uncommon Drop!", "You got a Pro Rune! (4%)")

            elif 99001 <= NewbRuneRNG <= 99899:
                messagebox.showinfo("Uncommon Drop!", "You got a Master Rune! (1%)")

            elif 99900 <= NewbRuneRNG <= 99999:
                messagebox.showinfo("RARE DROP!", "You got a HACKER RUNE! Congratulations! (0.1%)")
                print("[SERVER] You got a HACKER RUNE! (0.1%)")

            else:
                messagebox.showinfo("SUPER RARE DROP!", "YOU GOT A GOD RUNE! CONGRATULATIONS! (0.001%)")
                print("[SERVER] You got a GOD RUNE! (0.001%)")
                print("[GLOBAL] YOU GOT A GOD RUNE! (0.001%)")


        def NormalRune():
            NormRuneRNG = randint(0,100000)

            if NormRuneRNG == (0):
                messagebox.showinfo("SUPER RARE DROP!", "YOU GOT A RUNE TOKEN! CONGRATULATIONS! (0.001%)")
                print("[SERVER] You got a RUNE TOKEN! (0.001%)")
                print("[GLOBAL] YOU GOT A RUNE TOKEN! (0.001%)")

            elif 1 <= NormRuneRNG <= 60000:
                messagebox.showinfo("Common Drop!", "You got a Strange Rune! (60%)")

            elif 60001 <= NormRuneRNG <= 85000:
                messagebox.showinfo("Common Drop!", "You got a Wrong Rune! (25%)")

            elif 85001 <= NormRuneRNG <= 95000:
                messagebox.showinfo("Common Drop!", "You got an Abnormal Rune! (10%)")

            elif 95001 <= NormRuneRNG <= 99000:
                messagebox.showinfo("Uncommon Drop!", "You got a Normal Rune! (4%)")

            elif 99001 <= NormRuneRNG <= 99899:
                messagebox.showinfo("Uncommon Drop!", "You got a Good Rune! (1%)")

            elif 99900 <= NormRuneRNG <= 99999:
                messagebox.showinfo("RARE DROP!", "You got a GREAT RUNE! Congratulations! (0.1%)")
                print("[SERVER] You got a GREAT RUNE! (0.1%)")

            else:
                messagebox.showinfo("SUPER RARE DROP!", "YOU GOT A PERFECT RUNE! CONGRATULATIONS! (0.001%)")
                print("[SERVER] You got a PERFECT RUNE! (0.001%)")
                print("[GLOBAL] YOU GOT A PERFECT RUNE! (0.001%)")


        def GrassRune():
            GrassRuneRNG = randint(0,100000)

            if GrassRuneRNG == (0):
                messagebox.showinfo("SUPER RARE DROP!", "YOU GOT A RUNE TOKEN! CONGRATULATIONS! (0.001%)")
                print("[SERVER] You got a RUNE TOKEN! (0.001%)")
                print("[GLOBAL] YOU GOT A RUNE TOKEN! (0.001%)")

            elif 1 <= GrassRuneRNG <= 60000:
                messagebox.showinfo("Common Drop!", "You got a Weeds Rune! (60%)")

            elif 60001 <= GrassRuneRNG <= 85000:
                messagebox.showinfo("Common Drop!", "You got a Bushes Rune! (25%)")

            elif 85001 <= GrassRuneRNG <= 95000:
                messagebox.showinfo("Common Drop!", "You got a Seeds Rune! (10%)")

            elif 95001 <= GrassRuneRNG <= 99000:
                messagebox.showinfo("Uncommon Drop!", "You got a Grass Rune! (4%)")

            elif 99001 <= GrassRuneRNG <= 99899:
                messagebox.showinfo("Uncommon Drop!", "You got a Field Rune! (1%)")

            elif 99900 <= GrassRuneRNG <= 99999:
                messagebox.showinfo("RARE DROP!", "You got a TREE RUNE! Congratulations! (0.1%)")
                print("[SERVER] You got a TREE RUNE! (0.1%)")

            else:
                messagebox.showinfo("SUPER RARE DROP!", "YOU GOT A GARDEN RUNE! CONGRATULATIONS! (0.001%)")
                print("[SERVER] You got a GARDEN RUNE! (0.001%)")
                print("[GLOBAL] YOU GOT A GARDEN RUNE! (0.001%)")


        def FactoryRune():
            FacRuneRNG = randint(0,100000)

            if FacRuneRNG == (0):
                messagebox.showinfo("SUPER RARE DROP!", "YOU GOT A RUNE TOKEN! CONGRATULATIONS! (0.001%)")
                print("[SERVER] You got a RUNE TOKEN! (0.001%)")
                print("[GLOBAL] YOU GOT A RUNE TOKEN! (0.001%)")

            elif 1 <= FacRuneRNG <= 60000:
                messagebox.showinfo("Common Drop!", "You got a Handmade Rune! (60%)")

            elif 60001 <= FacRuneRNG <= 85000:
                messagebox.showinfo("Common Drop!", "You got a Gears Rune! (25%)")

            elif 85001 <= FacRuneRNG <= 95000:
                messagebox.showinfo("Common Drop!", "You got a Bolts&Nuts Rune! (10%)")

            elif 95001 <= FacRuneRNG <= 99000:
                messagebox.showinfo("Uncommon Drop!", "You got a Machines Rune! (4%)")

            elif 99001 <= FacRuneRNG <= 99899:
                messagebox.showinfo("Uncommon Drop!", "You got an Energy Rune! (1%)")

            elif 99900 <= FacRuneRNG <= 99999:
                messagebox.showinfo("RARE DROP!", "You got a ROBOTS RUNE! Congratulations! (0.1%)")
                print("[SERVER] You got a ROBOTS RUNE! (0.1%)")

            else:
                messagebox.showinfo("SUPER RARE DROP!", "YOU GOT AN AI FACTORY RUNE! CONGRATULATIONS! (0.001%)")
                print("[SERVER] You got an AI FACTORY RUNE! (0.001%)")
                print("[GLOBAL] YOU GOT AN AI FACTORY RUNE! (0.001%)")


        def AutoRune():
            AutoRuneRNG = randint(0,100000)

            if AutoRuneRNG == (0):
                messagebox.showinfo("SUPER RARE DROP!", "YOU GOT A RUNE TOKEN! CONGRATULATIONS! (0.001%)")
                print("[SERVER] You got a RUNE TOKEN! (0.001%)")
                print("[GLOBAL] YOU GOT A RUNE TOKEN! (0.001%)")

            elif 1 <= AutoRuneRNG <= 60000:
                messagebox.showinfo("Common Drop!", "You got a DIY Rune! (60%)")

            elif 60001 <= AutoRuneRNG <= 85000:
                messagebox.showinfo("Common Drop!", "You got a Grinding Rune! (25%)")

            elif 85001 <= AutoRuneRNG <= 95000:
                messagebox.showinfo("Common Drop!", "You got an Afk Rune! (10%)")

            elif 95001 <= AutoRuneRNG <= 99000:
                messagebox.showinfo("Uncommon Drop!", "You got an Idle Rune! (4%)")

            elif 99001 <= AutoRuneRNG <= 99899:
                messagebox.showinfo("Uncommon Drop!", "You got an Automaion Rune! (1%)")

            elif 99900 <= AutoRuneRNG <= 99999:
                messagebox.showinfo("RARE DROP!", "You got an AUTO CLICKER RUNE! Congratulations! (0.1%)")
                print("[SERVER] You got an ROBOTS RUNE! (0.1%)")

            else:
                messagebox.showinfo("SUPER RARE DROP!", "YOU GOT AN AUTO GAMEPASS (💀) RUNE! CONGRATULATIONS! (0.001%)")
                print("[SERVER] You got an AUTO GAMEPASS (💀) RUNE! (0.001%)")
                print("[GLOBAL] YOU GOT AN AUTO GAMEPASS (💀) RUNE! (0.001%)")


        def HonorRune():
            HonorRuneRNG = randint(0,100000)

            if HonorRuneRNG == (0):
                messagebox.showinfo("SUPER RARE DROP!", "YOU GOT A RUNE TOKEN! CONGRATULATIONS! (0.001%)")
                print("[SERVER] You got a RUNE TOKEN! (0.001%)")
                print("[GLOBAL] YOU GOT A RUNE TOKEN! (0.001%)")

            elif 1 <= HonorRuneRNG <= 60000:
                messagebox.showinfo("Common Drop!", "You got a Disrespect Rune! (60%)")

            elif 60001 <= HonorRuneRNG <= 85000:
                messagebox.showinfo("Common Drop!", "You got an Unfamous Rune! (25%)")

            elif 85001 <= HonorRuneRNG <= 95000:
                messagebox.showinfo("Common Drop!", "You got a Normalized Rune! (10%)")

            elif 95001 <= HonorRuneRNG <= 99000:
                messagebox.showinfo("Uncommon Drop!", "You got a Famous Rune! (4%)")

            elif 99001 <= HonorRuneRNG <= 99899:
                messagebox.showinfo("Uncommon Drop!", "You got a Respectful Rune! (1%)")

            elif 99900 <= HonorRuneRNG <= 99999:
                messagebox.showinfo("RARE DROP!", "You got a NAMED RUNE! Congratulations! (0.1%)")
                print("[SERVER] You got a NAMED RUNE! (0.1%)")

            else:
                messagebox.showinfo("SUPER RARE DROP!", "YOU GOT A HONORED RUNE! CONGRATULATIONS! (0.001%)")
                print("[SERVER] You got a HONORED RUNE! (0.001%)")
                print("[GLOBAL] YOU GOT A HONORED RUNE! (0.001%)")


        def AntiRune():
            AntiRuneRNG = randint(0,100000)

            if AntiRuneRNG == (0):
                messagebox.showinfo("SUPER RARE DROP!", "YOU GOT A RUNE TOKEN! CONGRATULATIONS! (0.001%)")
                print("[SERVER] You got a RUNE TOKEN! (0.001%)")
                print("[GLOBAL] YOU GOT A RUNE TOKEN! (0.001%)")

            elif 1 <= AntiRuneRNG <= 60000:
                messagebox.showinfo("Common Drop!", "You got a Positive Rune! (60%)")

            elif 60001 <= AntiRuneRNG <= 85000:
                messagebox.showinfo("Common Drop!", "You got a Neautral Rune! (25%)")

            elif 85001 <= AntiRuneRNG <= 95000:
                messagebox.showinfo("Common Drop!", "You got a Depressed Rune! (10%)")

            elif 95001 <= AntiRuneRNG <= 99000:
                messagebox.showinfo("Uncommon Drop!", "You got a Sad Rune! (4%)")

            elif 99001 <= AntiRuneRNG <= 99899:
                messagebox.showinfo("Uncommon Drop!", "You got a Negative Rune! (1%)")

            elif 99900 <= AntiRuneRNG <= 99999:
                messagebox.showinfo("RARE DROP!", "You got a HATRED RUNE! Congratulations! (0.1%)")
                print("[SERVER] You got a HATRED RUNE! (0.1%)")

            else:
                messagebox.showinfo("SUPER RARE DROP!", "YOU GOT AN ANTI RUNE! CONGRATULATIONS! (0.001%)")
                print("[SERVER] You got an ANTI RUNE! (0.001%)")
                print("[GLOBAL] YOU GOT AN ANTI RUNE! (0.001%)")


        def FunnyRune():
            FunnyRuneRNG = randint(0,100000)

            if FunnyRuneRNG == (0):
                messagebox.showinfo("SUPER RARE DROP!", "YOU GOT A RUNE TOKEN! CONGRATULATIONS! (0.001%)")
                print("[SERVER] You got a RUNE TOKEN! (0.001%)")
                print("[GLOBAL] YOU GOT A RUNE TOKEN! (0.001%)")

            elif 1 <= FunnyRuneRNG <= 60000:
                messagebox.showinfo("Common Drop!", "You got a No Fun :( Rune! (60%)")

            elif 60001 <= FunnyRuneRNG <= 85000:
                messagebox.showinfo("Common Drop!", "You got a Bored :| Rune! (25%)")

            elif 85001 <= FunnyRuneRNG <= 95000:
                messagebox.showinfo("Common Drop!", "You got a Bit Fun :O Rune! (10%)")

            elif 95001 <= FunnyRuneRNG <= 99000:
                messagebox.showinfo("Uncommon Drop!", "You got a Fun :] Rune! (4%)")

            elif 99001 <= FunnyRuneRNG <= 99899:
                messagebox.showinfo("Uncommon Drop!", "You got a Funnier :) Rune! (1%)")

            elif 99900 <= FunnyRuneRNG <= 99999:
                messagebox.showinfo("RARE DROP!", "You got a FUNNIEST :> RUNE! Congratulations! (0.1%)")
                print("[SERVER] You got a FUNNIEST :> RUNE! (0.1%)")

            else:
                messagebox.showinfo("SUPER RARE DROP!", "YOU GOT A LAUGHING OUT LOUD :D RUNE! CONGRATULATIONS! (0.001%)")
                print("[SERVER] You got a LAUGHING OUT LOUD :D RUNE! (0.001%)")
                print("[GLOBAL] YOU GOT A LAUGHING OUT LOUD :D RUNE! (0.001%)")


        def StarRune():
            StarRuneRNG = randint(0,100000)

            if StarRuneRNG == (0):
                messagebox.showinfo("SUPER RARE DROP!", "YOU GOT A RUNE TOKEN! CONGRATULATIONS! (0.001%)")
                print("[SERVER] You got a RUNE TOKEN! (0.001%)")
                print("[GLOBAL] YOU GOT A RUNE TOKEN! (0.001%)")

            elif 1 <= StarRuneRNG <= 60000:
                messagebox.showinfo("Common Drop!", "You got a Red Star Rune! (60%)")

            elif 60001 <= StarRuneRNG <= 85000:
                messagebox.showinfo("Common Drop!", "You got an Orange Star Rune! (25%)")

            elif 85001 <= StarRuneRNG <= 95000:
                messagebox.showinfo("Common Drop!", "You got a Yellow Star Rune! (10%)")

            elif 95001 <= StarRuneRNG <= 99000:
                messagebox.showinfo("Uncommon Drop!", "You got a Green Star Rune! (4%)")

            elif 99001 <= StarRuneRNG <= 99899:
                messagebox.showinfo("Uncommon Drop!", "You got a Blue Star Rune! (1%)")

            elif 99900 <= StarRuneRNG <= 99999:
                messagebox.showinfo("RARE DROP!", "You got a WHITE STAR RUNE! Congratulations! (0.1%)")
                print("[SERVER] You got a WHITE STAR RUNE! (0.1%)")

            else:
                messagebox.showinfo("SUPER RARE DROP!", "YOU GOT A STAR CHART RUNE! CONGRATULATIONS! (0.001%)")
                print("[SERVER] You got a STAR CHART RUNE! (0.001%)")
                print("[GLOBAL] YOU GOT A STAR CHART RUNE! (0.001%)")


        def GalaxyRune():
            GalaxyRuneRNG = randint(0,100000)

            if GalaxyRuneRNG == (0):
                messagebox.showinfo("SUPER RARE DROP!", "YOU GOT A RUNE TOKEN! CONGRATULATIONS! (0.001%)")
                print("[SERVER] You got a RUNE TOKEN! (0.001%)")
                print("[GLOBAL] YOU GOT A RUNE TOKEN! (0.001%)")

            elif 1 <= GalaxyRuneRNG <= 60000:
                messagebox.showinfo("Common Drop!", "You got a Space Dust Rune! (60%)")

            elif 60001 <= GalaxyRuneRNG <= 85000:
                messagebox.showinfo("Common Drop!", "You got an Asteroid Rune! (25%)")

            elif 85001 <= GalaxyRuneRNG <= 95000:
                messagebox.showinfo("Common Drop!", "You got a Planet Rune! (10%)")

            elif 95001 <= GalaxyRuneRNG <= 99000:
                messagebox.showinfo("Uncommon Drop!", "You got a Stars Rune! (4%)")

            elif 99001 <= GalaxyRuneRNG <= 99899:
                messagebox.showinfo("Uncommon Drop!", "You got a Galaxy Rune! (1%)")

            elif 99900 <= GalaxyRuneRNG <= 99999:
                messagebox.showinfo("RARE DROP!", "You got a BLACK HOLE RUNE! Congratulations! (0.1%)")
                print("[SERVER] You got a BLACK HOLE RUNE! (0.1%)")

            else:
                messagebox.showinfo("SUPER RARE DROP!", "YOU GOT AN UNIVERSE RUNE! CONGRATULATIONS! (0.001%)")
                print("[SERVER] You got an UNIVERSE RUNE! (0.001%)")
                print("[GLOBAL] YOU GOT AN UNIVERSE RUNE! (0.001%)")


        def UnnaturalRune():
            UnnaturalRuneRNG = randint(0,100000)

            if UnnaturalRuneRNG == (0):
                messagebox.showinfo("SUPER RARE DROP!", "YOU GOT A RUNE TOKEN! CONGRATULATIONS! (0.001%)")
                print("[SERVER] You got a RUNE TOKEN! (0.001%)")
                print("[GLOBAL] YOU GOT A RUNE TOKEN! (0.001%)")

            elif 1 <= UnnaturalRuneRNG <= 60000:
                messagebox.showinfo("Common Drop!", "You got a Natural Rune! (60%)")

            elif 60001 <= UnnaturalRuneRNG <= 85000:
                messagebox.showinfo("Common Drop!", "You got an Unchanging Rune! (25%)")

            elif 85001 <= UnnaturalRuneRNG <= 95000:
                messagebox.showinfo("Common Drop!", "You got a Same Rune! (10%)")

            elif 95001 <= UnnaturalRuneRNG <= 99000:
                messagebox.showinfo("Uncommon Drop!", "You got a Changing Rune! (4%)")

            elif 99001 <= UnnaturalRuneRNG <= 99899:
                messagebox.showinfo("Uncommon Drop!", "You got a Fake Rune! (1%)")

            elif 99900 <= UnnaturalRuneRNG <= 99999:
                messagebox.showinfo("RARE DROP!", "You got an UNNATURAL RUNE! Congratulations! (0.1%)")
                print("[SERVER] You got an UNNATURAL RUNE! (0.1%)")

            else:
                messagebox.showinfo("SUPER RARE DROP!", "YOU GOT AN ARTIFICIAL RUNE! CONGRATULATIONS! (0.001%)")
                print("[SERVER] You got an ARTIFICIAL RUNE! (0.001%)")
                print("[GLOBAL] YOU GOT AN ARTIFICIAL RUNE! (0.001%)")


        Rune1=Button(EIRunetab, text = 'Newbie Rune', background = 'lime', command=NewbieRune)
        Rune2=Button(EIRunetab, text = 'Normal Rune', background = 'green', command=NormalRune)
        Rune3=Button(EIRunetab, text = 'Grass Rune', background = 'light green', command=GrassRune)
        Rune4=Button(EIRunetab, text = 'Factory Rune', background = 'grey', command=FactoryRune)
        Rune5=Button(EIRunetab, text = 'Auto Rune', background = 'orange', command=AutoRune)
        Rune6=Button(EIRunetab, text = 'Honor Rune', background = 'yellow', command=HonorRune)
        Rune7=Button(EIRunetab, text = 'Anti Rune', background = 'dark blue', command=AntiRune)
        Rune8=Button(EIRunetab, text = 'Funny Rune', background = 'yellow', command=FunnyRune)
        Rune9=Button(EIRunetab, text = 'Star Rune', command=StarRune)
        Rune10=Button(EIRunetab, text = 'Galaxy Rune', background = 'purple', command=GalaxyRune)
        Rune11=Button(EIRunetab, text = 'Unnatural Rune', background = 'black', command=UnnaturalRune)

        Rune1.pack()
        Rune2.pack()
        Rune3.pack()
        Rune4.pack()
        Rune5.pack()
        Rune6.pack()
        Rune7.pack()
        Rune8.pack()
        Rune9.pack()
        Rune10.pack()
        Rune11.pack()


        EIRunetab.mainloop()


    NormalStats=Button(EIStattab, text = 'Normal Stats', background = 'green', command=NormalStattab)
    Upgrades=Button(EIStattab, text = 'Upgrades', background = 'yellow', command=Upgradetab)
    TierStats=Button(EIStattab, text = 'Tier Stats', background = 'pink', command=TierStattab)
    RuneStats=Button(EIStattab, text = 'Runes', background = 'lime', command=Runetab)

    NormalStats.pack()
    Upgrades.pack()
    TierStats.pack()
    RuneStats.pack()

    EIStattab.mainloop()

########################################################################################################

def Coretab():
    EICoretab = Tk()

    EICoretab.title("Everything Incremental Alpha - Cores")
    EICoretab.geometry("300x300")
    EICoretab.resizable(width=True,height=True)

    CoreCount = '111,978'

    CoreStats=Label(EICoretab, text = ('Cores = ', CoreCount), background = 'yellow')

    def CoreRanktab():
        EICRtab = Tk()
        
        EICRtab.title("Everything Incremental Alpha - Core Ranks")
        EICRtab.geometry("300x300")
        EICRtab.resizable(width=True,height=True)

        EICRtab.mainloop()

    CRStats=Button(EICoretab, text = 'Core Ranks', background = 'yellow', command=CoreRanktab)

    CRStats.pack()
    CoreStats.pack()

    EICoretab.mainloop()

########################################################################################################

def Milestonetab():
    EIMilestonetab = Tk()

    EIMilestonetab.title("Everything Incremental Alpha - Milestones")
    EIMilestonetab.geometry("300x300")
    EIMilestonetab.resizable(width=True,height=True)
    
    EIMilestonetab.mainloop()

########################################################################################################

def Challengetab():
    EIChallengetab = Tk()

    EIChallengetab.title("Everything Incremental Alpha - Challenges")
    EIChallengetab.geometry("300x300")
    EIChallengetab.resizable(width=True,height=True)


    def NormalChaltab():
        EINormalChaltab = Tk()

        EINormalChaltab.title("Everything Incremental Alpha - Normal Challenges")
        EINormalChaltab.geometry("300x300")
        EINormalChaltab.resizable(width=True,height=True)

        EINormalChaltab.mainloop()

    
    def IDPDimtab():
        EIIDPDimtab = Tk()
        
        EIIDPDimtab.title("Everything Incremental Alpha - Impossible Doomed Purge Dimension")
        EIIDPDimtab.geometry("300x300")
        EIIDPDimtab.resizable(width=True,height=True)

        EIIDPDimtab.mainloop()


    def PreMassChaltab():
        EIPMChaltab = Tk()
        
        EIPMChaltab.title("Everything Incremental Alpha - Pre-Mass Challenges")
        EIPMChaltab.geometry("300x300")
        EIPMChaltab.resizable(width=True,height=True)

        EIPMChaltab.mainloop()


    def MassEraChaltab():
        EIMEChaltab = Tk()
        
        EIMEChaltab.title("Everything Incremental Alpha - Mass Era Challenges")
        EIMEChaltab.geometry("300x300")
        EIMEChaltab.resizable(width=True,height=True)


        def RageChaltab():
            EIRageChaltab = Tk()

            EIRageChaltab.title("Everything Incremental Alpha - Rage Challenges")
            EIRageChaltab.geometry("300x300")
            EIRageChaltab.resizable(width=True,height=True)

            EIRageChaltab.mainloop()

        
        def BHChaltab():
            EIBHChaltab = Tk()

            EIBHChaltab.title("Everything Incremental Alpha - Black Hole Challenges")
            EIBHChaltab.geometry("300x300")
            EIBHChaltab.resizable(width=True,height=True)

            EIBHChaltab.mainloop()

        
        def AtomChaltab():
            EIAtomChaltab = Tk()
            
            EIAtomChaltab.title("Everything Incremental Alpha - Atom Challenges")
            EIAtomChaltab.geometry("300x300")
            EIAtomChaltab.resizable(width=True,height=True)

            EIAtomChaltab.mainloop()


        RageChal=Button(EIMEChaltab, text = 'Rage Challenges', background = 'red', command=RageChaltab)
        BHChal=Button(EIMEChaltab, text = 'Black Hole Challenges', background = 'yellow', command=BHChaltab)
        AtomChal=Button(EIMEChaltab, text = 'Atom Challenges', background = 'blue', command=AtomChaltab)


        RageChal.pack()
        BHChal.pack()
        AtomChal.pack()

        EIMEChaltab.mainloop()


    def AMChaltab():
        EIAMChaltab = Tk()

        EIAMChaltab.title("Everything Incremental Alpha - Antimatter Challenges")
        EIAMChaltab.geometry("300x300")
        EIAMChaltab.resizable(width=True,height=True)

        EIAMChaltab.mainloop()

    
    def ICtab():
        EIICtab = Tk()

        EIICtab.title("Everything Incremental Alpha - Infinity Challenges")
        EIICtab.geometry("300x300")
        EIICtab.resizable(width=True,height=True)


    NormalChal=Button(EIChallengetab, text = 'Normal Challenges', background = 'yellow', command=NormalChaltab)
    IDPDim=Button(EIChallengetab, text = 'Impossible Doomed Purge Dimensions', background = 'dark blue', command=IDPDimtab)
    PMChal=Button(EIChallengetab, text = 'Pre-Mass Challenges', background = 'light grey', command=PreMassChaltab)
    MEChal=Button(EIChallengetab, text = 'Mass Era Challenges', background = 'grey', command=MassEraChaltab)
    AMChal=Button(EIChallengetab, text = 'Antimatter Dimension Challenges', background = 'black', command=AMChaltab)
    IC=Button(EIChallengetab, text = 'Infinity Challenges', background = 'orange', command=ICtab)


    NormalChal.pack()
    IDPDim.pack()
    PMChal.pack()
    MEChal.pack()
    AMChal.pack()
    IC.pack()


    EIChallengetab.mainloop()

########################################################################################################

def Labtab():
    EILabtab = Tk()

    EILabtab.title("Everything Incremental Alpha - The Lab")
    EILabtab.geometry("300x300")
    EILabtab.resizable(width=True,height=True)

    def Elementtab():
        EIElementtab = Tk()

        EIElementtab.title("Everything Incremental Alpha - Normal Elements")
        EIElementtab.geometry("300x300")
        EIElementtab.resizable(width=True,height=True)

        EIElementtab.mainloop()


    def MElementtab():
        EIMElementtab = Tk()

        EIMElementtab.title("Everything Incremental Alpha - Muonic Elements")
        EIMElementtab.geometry("300x300")
        EIMElementtab.resizable(width=True,height=True)

        EIMElementtab.mainloop()


    def BElementtab():
        EIBElementtab = Tk()

        EIBElementtab.title("Everything Incremental Alpha - Broken Elements")
        EIBElementtab.geometry("300x300")
        EIBElementtab.resizable(width=True,height=True)

        EIBElementtab.mainloop()


    def CElementtab():
        EICElementtab = Tk()

        EICElementtab.title("Everything Incremental Alpha - Crunched Elements")
        EICElementtab.geometry("300x300")
        EICElementtab.resizable(width=True,height=True)

        EICElementtab.mainloop()


    def MaElementtab():
        EIMaElementtab = Tk()

        EIMaElementtab.title("Everything Incremental Alpha - Matter Elements")
        EIMaElementtab.geometry("300x300")
        EIMaElementtab.resizable(width=True,height=True)

        EIMaElementtab.mainloop()


    def AElementtab():
        EIAElementtab = Tk()

        EIAElementtab.title("Everything Incremental Alpha - Antimatter Elements")
        EIAElementtab.geometry("300x300")
        EIAElementtab.resizable(width=True,height=True)

        EIAElementtab.mainloop()


    def Replicantistab():
        EIReplicantistab = Tk()

        EIReplicantistab.title("Everything Incremental Alpha - Replicantis")
        EIReplicantistab.geometry("300x300")
        EIReplicantistab.resizable(width=True,height=True)

        EIReplicantistab.mainloop()


    def Studiestab():
        EIStudiestab = Tk()

        EIStudiestab.title("Everything Incremental Alpha - Studies")
        EIStudiestab.geometry("300x300")
        EIStudiestab.resizable(width=True,height=True)

        def TimeStudiestab():
            EITimeStudiestab = Tk()

            EITimeStudiestab.title("Everything Incremental Alpha - Time Studies")
            EITimeStudiestab.geometry("300x300")
            EITimeStudiestab.resizable(width=True,height=True)

            EITimeStudiestab.mainloop()


        def MasteryStudiestab():
            EIMasteryStudiestab = Tk()

            EIMasteryStudiestab.title("Everything Incremental Alpha - Mastery Studies")
            EIMasteryStudiestab.geometry("300x300")
            EIMasteryStudiestab.resizable(width=True,height=True)

            EIMasteryStudiestab.mainloop()


        TimeStudies=Button(EIStudiestab, text = 'Time Studies', background = 'light blue', command=TimeStudiestab)
        MasteryStudies=Button(EIStudiestab, text = 'Mastery Studies', background = 'blue', command=MasteryStudiestab)
        
        TimeStudies.pack()
        MasteryStudies.pack()


        EIStudiestab.mainloop()

    
    def Electronstab():
        EIElectronstab = Tk()

        EIElectronstab.title("Everything Incremental Alpha - Electrons")
        EIElectronstab.geometry("300x300")
        EIElectronstab.resizable(width=True,height=True)

        EIElectronstab.mainloop()


    def Replicantstab():
        EIReplicantstab = Tk()

        EIReplicantstab.title("Everything Incremental Alpha - Replicants")
        EIReplicantstab.geometry("300x300")
        EIReplicantstab.resizable(width=True,height=True)

        EIReplicantstab.mainloop()


    def Nanofieldtab():
        EINanofieldtab = Tk()

        EINanofieldtab.title("Everything Incremental Alpha - Nanofield")
        EINanofieldtab.geometry("300x300")
        EINanofieldtab.resizable(width=True,height=True)

        EINanofieldtab.mainloop()


    def ToDtab():
        EIToDtab = Tk()

        EIToDtab.title("Everything Incremental Alpha - Tree of Decay")
        EIToDtab.geometry("300x300")
        EIToDtab.resizable(width=True,height=True)

        EIToDtab.mainloop()


    def Neutrinostab():
        EINeutrinostab = Tk()

        EINeutrinostab.title("Everything Incremental Alpha - Neutrinos")
        EINeutrinostab.geometry("300x300")
        EINeutrinostab.resizable(width=True,height=True)

        EINeutrinostab.mainloop()


    def GPhotonstab():
        EIGPhotonstab = Tk()

        EIGPhotonstab.title("Everything Incremental Alpha - Ghostly Photons")
        EIGPhotonstab.geometry("300x300")
        EIGPhotonstab.resizable(width=True,height=True)

        EIGPhotonstab.mainloop()


    def PerkPointTreetab():
        EIPerkPointTreetab = Tk()

        EIPerkPointTreetab.title("Everything Incremental Alpha - Perk Point Tree")
        EIPerkPointTreetab.geometry("300x300")
        EIPerkPointTreetab.resizable(width=True,height=True)

        EIPerkPointTreetab.mainloop()


    Elements=Button(EILabtab, text = 'Normal Elements', background = 'light blue', command=Elementtab)
    MElements=Button(EILabtab, text = 'Muonic Elements', background = 'orange', command=MElementtab)
    BElements=Button(EILabtab, text = 'Broken Elements', background = 'grey', command=BElementtab)
    CElements=Button(EILabtab, text = 'Crunched Elements', background = 'yellow', command=CElementtab)
    MaElements=Button(EILabtab, text = 'Matter Elements', background = 'light grey', command=MaElementtab)
    AElements=Button(EILabtab, text = 'Antimatter Elements', background = 'dark grey', command=AElementtab)
    Replicantis=Button(EILabtab, text = 'Replicantis', background = 'lime', command=Replicantistab)
    Studies=Button(EILabtab, text = 'Studies', background = 'blue', command=Studiestab)
    Electrons=Button(EILabtab, text = 'Electrons', background = 'green', command=Electronstab)
    Replicants=Button(EILabtab, text = 'Replicants', background = 'light green', command=Replicantstab)
    Nanofield=Button(EILabtab, text = 'Nanofield', background = 'purple', command=Nanofieldtab)
    ToD=Button(EILabtab, text = 'Tree of Decay', background = 'black', command=ToDtab)
    Neutrinos=Button(EILabtab, text = 'Neutrinos', command=Neutrinostab)
    GPhotons=Button(EILabtab, text = 'Ghostly Photons', command=GPhotonstab)
    PerkPointTree=Button(EILabtab, text = 'Perk Point Tree', command=PerkPointTreetab)

    Elements.pack()
    MElements.pack()
    BElements.pack()
    CElements.pack()
    MaElements.pack()
    AElements.pack()
    Replicantis.pack()
    Studies.pack()
    Electrons.pack()
    Replicants.pack()
    Nanofield.pack()
    ToD.pack()
    Neutrinos.pack()
    GPhotons.pack()
    PerkPointTree.pack()

    EILabtab.mainloop()

########################################################################################################

def Erastab():
    EIErastab = Tk()

    EIErastab.title("Everything Incremental Alpha - Eras")
    EIErastab.geometry("300x300")
    EIErastab.resizable(width=True,height=True)

    def MassEratab():
        EIMassEratab = Tk()
        
        EIMassEratab.title("Everything Incremental Alpha - Mass Era")
        EIMassEratab.geometry("300x300")
        EIMassEratab.resizable(width=True,height=True)

        EIMassEratab.mainloop()


    def SphereEratab():
        EISphereEratab = Tk()

        EISphereEratab.title("Everything Incremental Alpha - Sphere Era")
        EISphereEratab.geometry("300x300")
        EISphereEratab.resizable(width=True,height=True)

        EISphereEratab.mainloop()


    def MoneyEratab():
        EIMoneyEratab = Tk()

        EIMoneyEratab.title("Everything Incremental Alpha - Money Era")
        EIMoneyEratab.geometry("300x300")
        EIMoneyEratab.resizable(width=True,height=True)

        EIMoneyEratab.mainloop()


    def LBREratab():
        EILBREratab = Tk()

        EILBREratab.title("Everything Incremental Alpha - Leaf Blower Revolution Era")
        EILBREratab.geometry("300x300")
        EILBREratab.resizable(width=True,height=True)


        LBRFieldFrame=Frame(EILBREratab, relief='solid', bd=2)
        LBRResetFrame=Frame(EILBREratab, relief='solid', bd=2)

        LBRFieldNoticeLabel=Label(LBRFieldFrame, text = 'Leaf Fields', background = 'lime')
        LBRResetNoticeLabel=Label(LBRResetFrame, text = 'Reset Layers', background = 'grey')

        LBRFieldNoticeLabel.pack()
        LBRResetNoticeLabel.pack()

        def BasicLeafFieldtab():
            EIBasicLeafFieldtab = Tk()

            EIBasicLeafFieldtab.title("Everything Incremental Alpha - Basic Leaf Field")
            EIBasicLeafFieldtab.geometry("300x300")
            EIBasicLeafFieldtab.resizable(width=True,height=True)
            
            EIBasicLeafFieldtab.mainloop()


        def GoldLeafFieldtab():
            EIGoldLeafFieldtab = Tk()

            EIGoldLeafFieldtab.title("Everything Incremental Alpha - Gold Leaf Field")
            EIGoldLeafFieldtab.geometry("300x300")
            EIGoldLeafFieldtab.resizable(width=True,height=True)
            
            EIGoldLeafFieldtab.mainloop()


        def PlatinumLeafFieldtab():
            EIPlatinumLeafFieldtab = Tk()

            EIPlatinumLeafFieldtab.title("Everything Incremental Alpha - Platinum Leaf Field")
            EIPlatinumLeafFieldtab.geometry("300x300")
            EIPlatinumLeafFieldtab.resizable(width=True,height=True)
            
            EIPlatinumLeafFieldtab.mainloop()


        def BismuthLeafFieldtab():
            EIBismuthLeafFieldtab = Tk()

            EIBismuthLeafFieldtab.title("Everything Incremental Alpha - Bismuth Leaf Field")
            EIBismuthLeafFieldtab.geometry("300x300")
            EIBismuthLeafFieldtab.resizable(width=True,height=True)
            
            EIBismuthLeafFieldtab.mainloop()


        def CosmicLeafFieldtab():
            EICosmicLeafFieldtab = Tk()

            EICosmicLeafFieldtab.title("Everything Incremental Alpha - Cosmic Leaf Field")
            EICosmicLeafFieldtab.geometry("300x300")
            EICosmicLeafFieldtab.resizable(width=True,height=True)
            
            EICosmicLeafFieldtab.mainloop()


        def VoidLeafFieldtab():
            EIVoidLeafFieldtab = Tk()

            EIVoidLeafFieldtab.title("Everything Incremental Alpha - Gold Leaf Field")
            EIVoidLeafFieldtab.geometry("300x300")
            EIVoidLeafFieldtab.resizable(width=True,height=True)
            
            EIVoidLeafFieldtab.mainloop()


        def LeafFlaskLabtab():
            EILeafFlaskLabtab = Tk()

            EILeafFlaskLabtab.title("Everything Incremental Alpha - Leaf Flask Lab")
            EILeafFlaskLabtab.geometry("300x300")
            EILeafFlaskLabtab.resizable(width=True,height=True)

            def RedLeafFlasktab():
                EIRedLeafFlasktab = Tk()

                EIRedLeafFlasktab.title("Everything Incremental Alpha - Red Leaf Flasks")
                EIRedLeafFlasktab.geometry("300x300")
                EIRedLeafFlasktab.resizable(width=True,height=True)

                EIRedLeafFlasktab.mainloop()


            def GreenLeafFlasktab():
                EIGreenLeafFlasktab = Tk()

                EIGreenLeafFlasktab.title("Everything Incremental Alpha - Green Leaf Flasks")
                EIGreenLeafFlasktab.geometry("300x300")
                EIGreenLeafFlasktab.resizable(width=True,height=True)

                EIGreenLeafFlasktab.mainloop()


            def BlueLeafFlasktab():
                EIBlueLeafFlasktab = Tk()

                EIBlueLeafFlasktab.title("Everything Incremental Alpha - Blue Leaf Flasks")
                EIBlueLeafFlasktab.geometry("300x300")
                EIBlueLeafFlasktab.resizable(width=True,height=True)

                EIBlueLeafFlasktab.mainloop()


            def MagentaLeafFlasktab():
                EIMagentaLeafFlasktab = Tk()

                EIMagentaLeafFlasktab.title("Everything Incremental Alpha - Magenta Leaf Flasks")
                EIMagentaLeafFlasktab.geometry("300x300")
                EIMagentaLeafFlasktab.resizable(width=True,height=True)

                EIMagentaLeafFlasktab.mainloop()


            def OrangeLeafFlasktab():
                EIOrangeLeafFlasktab = Tk()

                EIOrangeLeafFlasktab.title("Everything Incremental Alpha - Orange Leaf Flasks")
                EIOrangeLeafFlasktab.geometry("300x300")
                EIOrangeLeafFlasktab.resizable(width=True,height=True)

                EIOrangeLeafFlasktab.mainloop()


            def BlackLeafFlasktab():
                EIBlackLeafFlasktab = Tk()

                EIBlackLeafFlasktab.title("Everything Incremental Alpha - Black Leaf Flasks")
                EIBlackLeafFlasktab.geometry("300x300")
                EIBlackLeafFlasktab.resizable(width=True,height=True)

                EIBlackLeafFlasktab.mainloop()


            def StrangeLeafFlasktab():
                EIStrangeLeafFlasktab = Tk()

                EIStrangeLeafFlasktab.title("Everything Incremental Alpha - Red Leaf Flasks")
                EIStrangeLeafFlasktab.geometry("300x300")
                EIStrangeLeafFlasktab.resizable(width=True,height=True)

                EIStrangeLeafFlasktab.mainloop()


            RedLeafFlask=Button(EILeafFlaskLabtab, text = 'Red Leaf Flasks', background = 'red', command=RedLeafFlasktab)
            GreenLeafFlask=Button(EILeafFlaskLabtab, text = 'Green Leaf Flasks', background = 'green', command=GreenLeafFlasktab)
            BlueLeafFlask=Button(EILeafFlaskLabtab, text = 'Blue Leaf Flasks', background = 'blue', command=BlueLeafFlasktab)
            MagentaLeafFlask=Button(EILeafFlaskLabtab, text = 'Magenta Leaf Flasks', background = 'magenta', command=MagentaLeafFlasktab)
            OrangeLeafFlask=Button(EILeafFlaskLabtab, text = 'Orange Leaf Flasks', background = 'orange', command=OrangeLeafFlasktab)
            BlackLeafFlask=Button(EILeafFlaskLabtab, text = 'Black Leaf Flasks', background = 'black', command=BlackLeafFlasktab)
            StrangeLeafFlask=Button(EILeafFlaskLabtab, text = 'Strange Leaf Flasks', background = 'dark red', command=StrangeLeafFlasktab)

            RedLeafFlask.pack()
            GreenLeafFlask.pack()
            BlueLeafFlask.pack()
            MagentaLeafFlask.pack()
            OrangeLeafFlask.pack()
            BlackLeafFlask.pack()
            StrangeLeafFlask.pack()

            EILeafFlaskLabtab.mainloop()


        def ExoticLeafFieldtab():
            EIExoticLeafFieldtab = Tk()

            EIExoticLeafFieldtab.title("Everything Incremental Alpha - Exotic Leaf Field")
            EIExoticLeafFieldtab.geometry("300x300")
            EIExoticLeafFieldtab.resizable(width=True,height=True)
            
            EIExoticLeafFieldtab.mainloop()


        def CelestialLeafFieldtab():
            EICelestialLeafFieldtab = Tk()

            EICelestialLeafFieldtab.title("Everything Incremental Alpha - Celestial Leaf Field")
            EICelestialLeafFieldtab.geometry("300x300")
            EICelestialLeafFieldtab.resizable(width=True,height=True)
            
            EICelestialLeafFieldtab.mainloop()


        def MythicalLeafFieldtab():
            EIMythicalLeafFieldtab = Tk()

            EIMythicalLeafFieldtab.title("Everything Incremental Alpha - Mythical Leaf Field")
            EIMythicalLeafFieldtab.geometry("300x300")
            EIMythicalLeafFieldtab.resizable(width=True,height=True)
            
            EIMythicalLeafFieldtab.mainloop()


        def LavaLeafFieldtab():
            EILavaLeafFieldtab = Tk()

            EILavaLeafFieldtab.title("Everything Incremental Alpha - Lava Leaf Field")
            EILavaLeafFieldtab.geometry("300x300")
            EILavaLeafFieldtab.resizable(width=True,height=True)
            
            EILavaLeafFieldtab.mainloop()


        def IceLeafFieldtab():
            EIIceLeafFieldtab = Tk()

            EIIceLeafFieldtab.title("Everything Incremental Alpha - Ice Leaf Field")
            EIIceLeafFieldtab.geometry("300x300")
            EIIceLeafFieldtab.resizable(width=True,height=True)
            
            EIIceLeafFieldtab.mainloop()


        def ObsidianLeafFieldtab():
            EIObsidianLeafFieldtab = Tk()

            EIObsidianLeafFieldtab.title("Everything Incremental Alpha - Obsidian Leaf Field")
            EIObsidianLeafFieldtab.geometry("300x300")
            EIObsidianLeafFieldtab.resizable(width=True,height=True)
            
            EIObsidianLeafFieldtab.mainloop()


        def SiliconLeafFieldtab():
            EISiliconLeafFieldtab = Tk()

            EISiliconLeafFieldtab.title("Everything Incremental Alpha - Silicon Leaf Field")
            EISiliconLeafFieldtab.geometry("300x300")
            EISiliconLeafFieldtab.resizable(width=True,height=True)
            
            EISiliconLeafFieldtab.mainloop()


        def BenitoiteLeafFieldtab():
            EIBenitoiteLeafFieldtab = Tk()

            EIBenitoiteLeafFieldtab.title("Everything Incremental Alpha - Benitoite Leaf Field")
            EIBenitoiteLeafFieldtab.geometry("300x300")
            EIBenitoiteLeafFieldtab.resizable(width=True,height=True)
            
            EIBenitoiteLeafFieldtab.mainloop()


        def AmberLeafFieldtab():
            EIAmberLeafFieldtab = Tk()

            EIAmberLeafFieldtab.title("Everything Incremental Alpha - Amber Leaf Field")
            EIAmberLeafFieldtab.geometry("300x300")
            EIAmberLeafFieldtab.resizable(width=True,height=True)
            
            EIAmberLeafFieldtab.mainloop()


        def AmethystLeafFieldtab():
            EIAmethystLeafFieldtab = Tk()

            EIAmethystLeafFieldtab.title("Everything Incremental Alpha - Amethyst Leaf Field")
            EIAmethystLeafFieldtab.geometry("300x300")
            EIAmethystLeafFieldtab.resizable(width=True,height=True)
            
            EIAmethystLeafFieldtab.mainloop()


        def EmeraldLeafFieldtab():
            EIEmeraldLeafFieldtab = Tk()

            EIEmeraldLeafFieldtab.title("Everything Incremental Alpha - Emerald Leaf Field")
            EIEmeraldLeafFieldtab.geometry("300x300")
            EIEmeraldLeafFieldtab.resizable(width=True,height=True)
            
            EIEmeraldLeafFieldtab.mainloop()


        def KyaniteLeafFieldtab():
            EIKyaniteLeafFieldtab = Tk()

            EIKyaniteLeafFieldtab.title("Everything Incremental Alpha - Kyanite Leaf Field")
            EIKyaniteLeafFieldtab.geometry("300x300")
            EIKyaniteLeafFieldtab.resizable(width=True,height=True)
            
            EIKyaniteLeafFieldtab.mainloop()


        def RhodoniteLeafFieldtab():
            EIRhodoniteLeafFieldtab = Tk()

            EIRhodoniteLeafFieldtab.title("Everything Incremental Alpha - Rhodonite Leaf Field")
            EIRhodoniteLeafFieldtab.geometry("300x300")
            EIRhodoniteLeafFieldtab.resizable(width=True,height=True)
            
            EIRhodoniteLeafFieldtab.mainloop()


        def RubyLeafFieldtab():
            EIRubyLeafFieldtab = Tk()

            EIRubyLeafFieldtab.title("Everything Incremental Alpha - Ruby Leaf Field")
            EIRubyLeafFieldtab.geometry("300x300")
            EIRubyLeafFieldtab.resizable(width=True,height=True)
            
            EIRubyLeafFieldtab.mainloop()


        def TektiteLeafFieldtab():
            EITektiteLeafFieldtab = Tk()

            EITektiteLeafFieldtab.title("Everything Incremental Alpha - Tektite Leaf Field")
            EITektiteLeafFieldtab.geometry("300x300")
            EITektiteLeafFieldtab.resizable(width=True,height=True)
            
            EITektiteLeafFieldtab.mainloop()


        def MoonstoneLeafFieldtab():
            EIMoonstoneLeafFieldtab = Tk()

            EIMoonstoneLeafFieldtab.title("Everything Incremental Alpha - Moonstone Leaf Field")
            EIMoonstoneLeafFieldtab.geometry("300x300")
            EIMoonstoneLeafFieldtab.resizable(width=True,height=True)
            
            EIMoonstoneLeafFieldtab.mainloop()


        def SandLeafFieldtab():
            EISandLeafFieldtab = Tk()

            EISandLeafFieldtab.title("Everything Incremental Alpha - Sand Leaf Field")
            EISandLeafFieldtab.geometry("300x300")
            EISandLeafFieldtab.resizable(width=True,height=True)
            
            EISandLeafFieldtab.mainloop()


        def AzuriteLeafFieldtab():
            EIAzuriteLeafFieldtab = Tk()

            EIAzuriteLeafFieldtab.title("Everything Incremental Alpha - Azurite Leaf Field")
            EIAzuriteLeafFieldtab.geometry("300x300")
            EIAzuriteLeafFieldtab.resizable(width=True,height=True)
            
            EIAzuriteLeafFieldtab.mainloop()


        def NiobiumLeafFieldtab():
            EINiobiumLeafFieldtab = Tk()

            EINiobiumLeafFieldtab.title("Everything Incremental Alpha - Niobium Leaf Field")
            EINiobiumLeafFieldtab.geometry("300x300")
            EINiobiumLeafFieldtab.resizable(width=True,height=True)
            
            EINiobiumLeafFieldtab.mainloop()


        def AncientLeafFieldtab():
            EIAncientLeafFieldtab = Tk()

            EIAncientLeafFieldtab.title("Everything Incremental Alpha - Ancient Leaf Field")
            EIAncientLeafFieldtab.geometry("300x300")
            EIAncientLeafFieldtab.resizable(width=True,height=True)
            
            EIAncientLeafFieldtab.mainloop()


        def SacredLeafFieldtab():
            EISacredLeafFieldtab = Tk()

            EISacredLeafFieldtab.title("Everything Incremental Alpha - Sacred Leaf Field")
            EISacredLeafFieldtab.geometry("300x300")
            EISacredLeafFieldtab.resizable(width=True,height=True)
            
            EISacredLeafFieldtab.mainloop()


        def BiotiteLeafFieldtab():
            EIBiotiteLeafFieldtab = Tk()

            EIBiotiteLeafFieldtab.title("Everything Incremental Alpha - Biotite Leaf Field")
            EIBiotiteLeafFieldtab.geometry("300x300")
            EIBiotiteLeafFieldtab.resizable(width=True,height=True)
            
            EIBiotiteLeafFieldtab.mainloop()


        def MalachiteLeafFieldtab():
            EIMalachiteLeafFieldtab = Tk()

            EIMalachiteLeafFieldtab.title("Everything Incremental Alpha - Malachite Leaf Field")
            EIMalachiteLeafFieldtab.geometry("300x300")
            EIMalachiteLeafFieldtab.resizable(width=True,height=True)
            
            EIMalachiteLeafFieldtab.mainloop()


        def HematiteLeafFieldtab():
            EIHematiteLeafFieldtab = Tk()

            EIHematiteLeafFieldtab.title("Everything Incremental Alpha - Hematite Leaf Field")
            EIHematiteLeafFieldtab.geometry("300x300")
            EIHematiteLeafFieldtab.resizable(width=True,height=True)
            
            EIHematiteLeafFieldtab.mainloop()


        def PlasmaLeafFieldtab():
            EIPlasmaLeafFieldtab = Tk()

            EIPlasmaLeafFieldtab.title("Everything Incremental Alpha - Plasma Leaf Field")
            EIPlasmaLeafFieldtab.geometry("300x300")
            EIPlasmaLeafFieldtab.resizable(width=True,height=True)
            
            EIPlasmaLeafFieldtab.mainloop()


        def CoalLeafFieldtab():
            EICoalLeafFieldtab = Tk()

            EICoalLeafFieldtab.title("Everything Incremental Alpha - Coal Leaf Field")
            EICoalLeafFieldtab.geometry("300x300")
            EICoalLeafFieldtab.resizable(width=True,height=True)
            
            EICoalLeafFieldtab.mainloop()


        def EmptySoulLeafFieldtab():
            EIEmptySoulLeafFieldtab = Tk()

            EIEmptySoulLeafFieldtab.title("Everything Incremental Alpha - Empty Soul Leaf Field")
            EIEmptySoulLeafFieldtab.geometry("300x300")
            EIEmptySoulLeafFieldtab.resizable(width=True,height=True)
            
            EIEmptySoulLeafFieldtab.mainloop()


        def SoulLeafFieldtab():
            EISoulLeafFieldtab = Tk()

            EISoulLeafFieldtab.title("Everything Incremental Alpha - Soul Leaf Field")
            EISoulLeafFieldtab.geometry("300x300")
            EISoulLeafFieldtab.resizable(width=True,height=True)
            
            EISoulLeafFieldtab.mainloop()


        def QuarkLeafFieldtab():
            EIQuarkLeafFieldtab = Tk()

            EIQuarkLeafFieldtab.title("Everything Incremental Alpha - Lava Leaf Field")
            EIQuarkLeafFieldtab.geometry("300x300")
            EIQuarkLeafFieldtab.resizable(width=True,height=True)
            
            EIQuarkLeafFieldtab.mainloop()


        BasicLeafField=Button(LBRFieldFrame, text = 'Basic Leaf Field', background = 'lime', command=BasicLeafFieldtab)
        GoldLeafField=Button(LBRFieldFrame, text = 'Gold Leaf Field', background = 'yellow', command=GoldLeafFieldtab)
        PlatinumLeafField=Button(LBRFieldFrame, text = 'Platinum Leaf Field', background = 'grey', command=PlatinumLeafFieldtab)
        BismuthLeafField=Button(LBRFieldFrame, text = 'Bismuth Leaf Field', background = 'orange', command=BismuthLeafFieldtab)
        CosmicLeafField=Button(LBRFieldFrame, text = 'Cosmic Leaf Field', background = 'red', command=CosmicLeafFieldtab)
        VoidLeafField=Button(LBRFieldFrame, text = 'Void Leaf Field', background = 'black', command=VoidLeafFieldtab)
        LeafFlaskLab=Button(LBRFieldFrame, text = 'Leaf Flask Lab', command=LeafFlaskLabtab)
        ExoticLeafField=Button(LBRFieldFrame, text = 'Exotic Leaf Field', background = 'brown', command=ExoticLeafFieldtab)
        CelestialLeafField=Button(LBRFieldFrame, text = 'Celestial Leaf Field', background = 'blue', command=CelestialLeafFieldtab)
        MythicalLeafField=Button(LBRFieldFrame, text = 'Mythical Leaf Field', background = 'light green', command=MythicalLeafFieldtab)
        LavaLeafField=Button(LBRFieldFrame, text = 'Lava Leaf Field', background = 'dark red', command=LavaLeafFieldtab)
        IceLeafField=Button(LBRFieldFrame, text = 'Ice Leaf Field', background = 'light blue', command=IceLeafFieldtab)
        ObsidianLeafField=Button(LBRFieldFrame, text = 'Obsidian Leaf Field', background = 'black', command=ObsidianLeafFieldtab)
        SiliconLeafField=Button(LBRFieldFrame, text = 'Silicon Leaf Field', background = 'light grey', command=SiliconLeafFieldtab)
        BenitoiteLeafField=Button(LBRFieldFrame, text = 'Benitoite Leaf Field', background = 'purple', command=BenitoiteLeafFieldtab)
        AmberLeafField=Button(LBRFieldFrame, text = 'Amber Leaf Field', background = 'yellow', command=AmberLeafFieldtab)
        AmethystLeafField=Button(LBRFieldFrame, text = 'Amethyst Leaf Field', background = 'pink', command=AmethystLeafFieldtab)
        EmeraldLeafField=Button(LBRFieldFrame, text = 'Emerald Leaf Field', background = 'lime', command=EmeraldLeafFieldtab)
        KyaniteLeafField=Button(LBRFieldFrame, text = 'Kyanite Leaf Field', background = 'pink', command=KyaniteLeafFieldtab)
        RhodoniteLeafField=Button(LBRFieldFrame, text = 'Rhodonite Leaf Field', background = 'brown', command=RhodoniteLeafFieldtab)
        RubyLeafField=Button(LBRFieldFrame, text = 'Ruby Leaf Field', background = 'red', command=RubyLeafFieldtab)
        TektiteLeafField=Button(LBRFieldFrame, text = 'Tektite Leaf Field', background = 'black', command=TektiteLeafFieldtab)
        MoonstoneLeafField=Button(LBRFieldFrame, text = 'Moonstone Leaf Field', command=MoonstoneLeafFieldtab)
        SandLeafField=Button(LBRFieldFrame, text = 'Sand Leaf Field', background = 'light yellow', command=SandLeafFieldtab)
        AzuriteLeafField=Button(LBRFieldFrame, text = 'Azurite Leaf Field', background = 'orange', command=AzuriteLeafFieldtab)
        NiobiumLeafField=Button(LBRFieldFrame, text = 'Niobium Leaf Field', background = 'cyan', command=NiobiumLeafFieldtab)
        AncientLeafField=Button(LBRFieldFrame, text = 'Ancient Leaf Field', background = 'pink', command=AncientLeafFieldtab)
        SacredLeafField=Button(LBRFieldFrame, text = 'Sacred Leaf Field', background = 'yellow', command=SacredLeafFieldtab)
        BiotiteLeafField=Button(LBRFieldFrame, text = 'Biotite Leaf Field', background = 'brown', command=BiotiteLeafFieldtab)
        MalachiteLeafField=Button(LBRFieldFrame, text = 'Malachite Leaf Field', background = 'light green', command=MalachiteLeafFieldtab)
        HematiteLeafField=Button(LBRFieldFrame, text = 'Hematite Leaf Field', background = 'brown', command=HematiteLeafFieldtab)
        PlasmaLeafField=Button(LBRFieldFrame, text = 'Plasma Leaf Field', background = 'light blue', command=PlasmaLeafFieldtab)
        CoalLeafField=Button(LBRFieldFrame, text = 'Coal Leaf Field', background = 'black', command=CoalLeafFieldtab)
        EmptySoulLeafField=Button(LBRFieldFrame, text = 'Empty Soul Leaf Field', command=EmptySoulLeafFieldtab)
        SoulLeafField=Button(LBRFieldFrame, text = 'Soul Leaf Field', background = 'dark blue', command=SoulLeafFieldtab)
        QuarkLeafField=Button(LBRFieldFrame, text = 'Quark Leaf Field', background = 'purple', command=QuarkLeafFieldtab)

        BasicLeafField.pack()
        GoldLeafField.pack()
        PlatinumLeafField.pack()
        BismuthLeafField.pack()
        CosmicLeafField.pack()
        VoidLeafField.pack()
        LeafFlaskLab.pack()
        ExoticLeafField.pack()
        CelestialLeafField.pack()
        MythicalLeafField.pack()
        LavaLeafField.pack()
        IceLeafField.pack()
        ObsidianLeafField.pack()
        SiliconLeafField.pack()
        BenitoiteLeafField.pack()
        AmberLeafField.pack()
        AmethystLeafField.pack()
        EmeraldLeafField.pack()
        KyaniteLeafField.pack()
        RhodoniteLeafField.pack()
        RubyLeafField.pack()
        TektiteLeafField.pack()
        MoonstoneLeafField.pack()
        SandLeafField.pack()
        AzuriteLeafField.pack()
        NiobiumLeafField.pack()
        AncientLeafField.pack()
        SacredLeafField.pack()
        BiotiteLeafField.pack()
        MalachiteLeafField.pack()
        HematiteLeafField.pack()
        PlasmaLeafField.pack()
        CoalLeafField.pack()
        EmptySoulLeafField.pack()
        SoulLeafField.pack()
        QuarkLeafField.pack()


        def TreeResettab():
            EITreeResettab = Tk()

            EITreeResettab.title("Everything Incremental Alpha - Tree Reset")
            EITreeResettab.geometry('300x300')
            EITreeResettab.resizable(width=True,height=True)

            EITreeResettab.mainloop()


        def ALBResettab():
            EIALBResettab = Tk()

            EIALBResettab.title("Everything Incremental Alpha - Automatic Leaf Blowers Reset")
            EIALBResettab.geometry("300x300")
            EIALBResettab.resizable(width=True,height=True)

            EIALBResettab.mainloop()


        def LeafPrestigetab():
            EILeafPrestigetab = Tk()

            EILeafPrestigetab.title("Everything Incremental Alpha - Leaf Prestige")
            EILeafPrestigetab.geometry("300x300")
            EILeafPrestigetab.resizable(width=True,height=True)

            EILeafPrestigetab.mainloop()


        def LeafFruitResettab():
            EILeafFruitResettab = Tk()
            
            EILeafFruitResettab.title("Everything Incremental Alpha - Leaf Fruit Reset")
            EILeafFruitResettab.geometry("300x300")
            EILeafFruitResettab.resizable(width=True,height=True)

            EILeafFruitResettab.mainloop()


        def LeafSeedResettab():
            EILeafSeedResettab = Tk()

            EILeafSeedResettab.title("Everything Incremental Alpha - Leaf Seed Reset")
            EILeafSeedResettab.geometry("300x300")
            EILeafSeedResettab.resizable(width=True,height=True)

            EILeafSeedResettab.mainloop()


        def LeafPrintertab():
            EILeafPrintertab = Tk()
            
            EILeafPrintertab.title("Everything Incremental Alpha - Leaf Printers")
            EILeafPrintertab.geometry("300x300")
            EILeafPrintertab.resizable(width=True,height=True)

            EILeafPrintertab.mainloop()


        def LeafConvertertab():
            EILeafConvertertab = Tk()

            EILeafConvertertab.title("Everything Incremental Alpha - Leaf Converters")
            EILeafConvertertab.geometry("300x300")
            EILeafConvertertab.resizable()


        TreeReset=Button(LBRResetFrame, text = 'Tree Reset', background = 'light green', command=TreeResettab)
        ALBReset=Button(LBRResetFrame, text = 'Automatic Leaf Blowers Reset', background = 'grey', command=ALBResettab)
        LeafPrestige=Button(LBRResetFrame, text = 'Leaf Prestige', background = 'yellow', command=LeafPrestigetab)
        LeafFruitReset=Button(LBRResetFrame, text = 'Leaf Fruit Reset', background = 'lime', command=LeafFruitResettab)
        LeafSeedReset=Button(LBRResetFrame, text = 'Leaf Seed Reset', background = 'brown', command=LeafSeedResettab)
        LeafPrinter=Button(LBRResetFrame, text = 'Leaf Printers', background = 'light grey', command=LeafPrintertab)

        TreeReset.pack()
        ALBReset.pack()
        LeafPrestige.pack()
        LeafFruitReset.pack()
        LeafSeedReset.pack()
        LeafPrinter.pack()

        LBRFieldFrame.pack(side='right', fill='both', expand=True)
        LBRResetFrame.pack(side='left', fill='both', expand=True)

        EILBREratab.mainloop()


    MassEra=Button(EIErastab, text = 'Mass Era', background = 'grey', command=MassEratab)
    SphereEra=Button(EIErastab, text = 'Sphere Era', background = 'yellow', command=SphereEratab)
    MoneyEra=Button(EIErastab, text = 'Money Era', background = 'green', command=MoneyEratab)
    LBREra=Button(EIErastab, text = 'Leaf Blower Revolution Era', background = 'lime', command=LBREratab)

    MassEra.pack()
    SphereEra.pack()
    MoneyEra.pack()
    LBREra.pack()

    EIErastab.mainloop()

########################################################################################################

def Dimensiontab():
    EIDimensiontab = Tk()

    EIDimensiontab.title("Everything Incremental Alpha - Dimensions")
    EIDimensiontab.geometry("300x300")
    EIDimensiontab.resizable(width=True,height=True)

    def MDimensiontab():
        EIMDimensiontab = Tk()

        EIMDimensiontab.title("Everything Incremental Alpha - Matter Dimensions")
        EIMDimensiontab.geometry("300x300")
        EIMDimensiontab.resizable(width=True,height=True)
        
        EIMDimensiontab.mainloop()


    def AMDimensiontab():
        EIAMDimensiontab = Tk()

        EIAMDimensiontab.title("Everything Incremental Alpha - Antimatter Dimensions")
        EIAMDimensiontab.geometry("300x300")
        EIAMDimensiontab.resizable(width=True,height=True)

        EIAMDimensiontab.mainloop()


    def IDimensiontab():
        EIIDimensiontab = Tk()

        EIIDimensiontab.title("Everything Incremental Alpha - Infinity Dimensions")
        EIIDimensiontab.geometry("300x300")
        EIIDimensiontab.resizable(width=True,height=True)

        EIIDimensiontab.mainloop()


    def TDimensiontab():
        EITDimensiontab = Tk()

        EITDimensiontab.title("Everything Incremental Alpha - Time Dimensions")
        EITDimensiontab.geometry("300x300")
        EITDimensiontab.resizable(width=True,height=True)

        EITDimensiontab.mainloop()

    
    def MetaDimensiontab():
        EIMetaDimensiontab = Tk()

        EIMetaDimensiontab.title("Everything Incremental Alpha - Meta Dimensions")
        EIMetaDimensiontab.geometry("300x300")
        EIMetaDimensiontab.resizable(width=True,height=True)

        EIMetaDimensiontab.mainloop()

    
    def ABHDimensiontab():
        EIABHDimensiontab = Tk()
        
        EIABHDimensiontab.title("Everything Incremental Alpha - Anti Black Hole Dimensions")
        EIABHDimensiontab.geometry("300x300")
        EIABHDimensiontab.resizable(width=True,height=True)

        EIABHDimensiontab.mainloop()


    def EmpDimensiontab():
        EIEmpDimensiontab = Tk()

        EIEmpDimensiontab.title("Everything Incremental Alpha - Emperor Dimensions")
        EIEmpDimensiontab.geometry("300x300")
        EIEmpDimensiontab.resizable(width=True,height=True)

        EIEmpDimensiontab.mainloop()


    def GhostDimensiontab():
        EIGhostDimensiontab = Tk()

        EIGhostDimensiontab.tilte("Everything Incremental Alpha - Ghost Dimensions")
        EIGhostDimensiontab.geometry("300x300")
        EIGhostDimensiontab.resizable(width=True,height=True)

        EIGhostDimensiontab.mainloop()


    def PDimensiontab():
        EIPDimensiontab = Tk()

        EIPDimensiontab.title("Everything Incremental Alpha - Paradox Dimensions")
        EIPDimensiontab.geometry("300x300")
        EIPDimensiontab.resizable(width=True,height=True)

        EIPDimensiontab.mainloop()


    def GDimensiontab():
        EIGDimensiontab = Tk()

        EIGDimensiontab.title("Everything Incremental Alpha - Galactic Dimensions")
        EIGDimensiontab.geometry("300x300")
        EIGDimensiontab.resizable(width=True,height=True)

        EIGDimensiontab.mainloop()


    def SDimensiontab():
        EISDimensiontab = Tk()

        EISDimensiontab.title("Everything Incremental Alpha - Space Dimensions")
        EISDimensiontab.geometry("300x300")
        EISDimensiontab.resizable(width=True,height=True)

        EISDimensiontab.mainloop()


    def RDimensiontab():
        EIRDimensiontab = Tk()

        EIRDimensiontab.title("Everything Incremental Alpha - Reality Dimensions")
        EIRDimensiontab.geometry("300x300")
        EIRDimensiontab.resizable(width=True,height=True)

        EIRDimensiontab.mainloop()


    def WHDimensiontab():
        EIWHDimensiontab = Tk()

        EIWHDimensiontab.title("Everything Incremental Alpha - White Hole Dimensions")
        EIWHDimensiontab.geometry("300x300")
        EIWHDimensiontab.resizable(width=True,height=True)

        EIWHDimensiontab.mainloop()


    MDimensions=Button(EIDimensiontab, text = 'Matter Dimensions', background = 'light grey', command=MDimensiontab)
    AMDimensions=Button(EIDimensiontab, text = 'Antimatter Dimensions', background = 'dark grey', command=AMDimensiontab)
    IDimensions=Button(EIDimensiontab, text = 'Infinity Dimensions', background = 'orange', command=IDimensiontab)
    TDimensions=Button(EIDimensiontab, text = 'Time Dimensions', background = 'purple', command=TDimensiontab)
    MetaDimensions=Button(EIDimensiontab, text = 'Meta Dimensions', background = 'light blue', command=MetaDimensiontab)
    ABHDimensions=Button(EIDimensiontab, text = 'Anti Black Hole Dimensions', background = 'black', command=ABHDimensiontab)
    EmpDimensions=Button(EIDimensiontab, text = 'Emperor Dimensions', background = 'yellow', command=EmpDimensiontab)
    GhostDimensions=Button(EIDimensiontab, text = 'Ghost Dimensions', command=GhostDimensiontab)
    PDimensions=Button(EIDimensiontab, text = 'Paradox Dimensions', background = 'pink', command=PDimensiontab)
    GDimensions=Button(EIDimensiontab, text = 'Galactic Dimensions', background = 'purple', command=GDimensiontab)
    SDimensions=Button(EIDimensiontab, text = 'Space Dimensions', background = 'black', command=SDimensiontab)
    RDimensions=Button(EIDimensiontab, text = 'Reality Dimensions', background = 'green', command=RDimensiontab)
    WHDimensions=Button(EIDimensiontab, text = 'White Hole Dimensions', command=WHDimensiontab)

    MDimensions.pack()
    AMDimensions.pack()
    IDimensions.pack()
    TDimensions.pack()
    MetaDimensions.pack()
    EmpDimensions.pack()
    GhostDimensions.pack()
    PDimensions.pack()
    GDimensions.pack()
    SDimensions.pack()
    RDimensions.pack()
    WHDimensions.pack()

    EIDimensiontab.mainloop()

########################################################################################################

def TheHilltab():
    EITheHilltab = Tk()

    EITheHilltab.title("Everything Incremental Alpha - The Hill")
    EITheHilltab.geometry("300x300")
    EITheHilltab.resizable(width=True,height=True)

    def Climbingtab():
        EIClimbingtab = Tk()

        EIClimbingtab.title("Everything Incremental Alpha - Climbing The Hill")
        EIClimbingtab.geometry("300x300")
        EIClimbingtab.resizable(width=True,height=True)

        EIClimbingtab.mainloop()

    
    def Energizertab():
        EIEnergizertab = Tk()

        EIEnergizertab.title("Everything Incremental Alpha - The Energizer")
        EIEnergizertab.geometry("300x300")
        EIEnergizertab.resizable(width=True,height=True)

        def EnergeticUpgtab():
            EIEnergeticUpgtab = Tk()
            
            EIEnergeticUpgtab.title("Everything Incremental Alpha - Energetic Upgrades")
            EIEnergeticUpgtab.geometry("300x300")
            EIEnergeticUpgtab.resizable(width=True,height=True)

            EIEnergeticUpgtab.mainloop()


        def EnergeticGentab():
            EIEnergeticGentab = Tk()
            
            EIEnergeticGentab.title("Everything Incremental Alpha - Energetic Generators")
            EIEnergeticGentab.geometry("300x300")
            EIEnergeticGentab.resizable(width=True,height=True)

            EIEnergeticGentab.mainloop()


        EnergeticUpgs=Button(EIEnergizertab, text = 'Energetic Upgrades', background = 'yellow', command=EnergeticUpgtab)
        EnergeticGens=Button(EIEnergizertab, text = 'Energetic Generators', background = 'yellow', command=EnergeticGentab)

        EnergeticUpgs.pack()
        EnergeticGens.pack()

        EIEnergizertab.mainloop()


    def Furnacetab():
        EIFurnacetab = Tk()

        EIFurnacetab.title("Everything Incremental Alpha - The Furnace")
        EIFurnacetab.geometry("300x300")
        EIFurnacetab.resizable(width=True,height=True)

        def NFurnacetab():
            EINFurnacetab = Tk()

            EINFurnacetab.title("Everything Incremental Alpha - Normal Furnace")
            EINFurnacetab.geometry("300x300")
            EINFurnacetab.resizable(width=True,height=True)

            def CoalUpgstab():
                EICoalUpgstab = Tk()

                EICoalUpgstab.title("Everything Incremental Alpha - Coal Upgrades")
                EICoalUpgstab.geometry("300x300")
                EICoalUpgstab.resizable(width=True,height=True)

                EICoalUpgstab.mainloop()


            def BFlametab():
                EIBFlametab = Tk()

                EIBFlametab.title("Everything Incremental Alpha - Blue Flames")
                EIBFlametab.geometry("300x300")
                EIBFlametab.resizable(width=True,height=True)

                EIBFlametab.mainloop()


            def FurnaceChalstab():
                EIFurnaceChalstab = Tk()

                EIFurnaceChalstab.title("Everything Incremental Alpha - Furnace Challenges")
                EIFurnaceChalstab.geometry("300x300")
                EIFurnaceChalstab.resizable(width=True,height=True)

                EIFurnaceChalstab.mainloop()


            CoalUpgs=Button(EINFurnacetab, text = 'Coal Upgrades', background = 'orange', command=CoalUpgstab)
            BFlames=Button(EINFurnacetab, text = 'Blue Flames', background = 'light blue', command=BFlametab)
            FurnaceChals=Button(EINFurnacetab, text = 'Furnace Challenges', background = 'orange', command=FurnaceChalstab)

            CoalUpgs.pack()
            BFlames.pack()
            FurnaceChals.pack()

            EINFurnacetab.mainloop()


        def EFurnacetab():
            EIEFurnacetab = Tk()

            EIEFurnacetab.title("Everything Incremental Alpha - Enhanced Furnace")
            EIEFurnacetab.geometry("300x300")
            EIEFurnacetab.resizable(width=True,height=True)

            def ECoalUpgstab():
                EIECoalUpgstab = Tk()

                EIECoalUpgstab.title("Everything Incremental Alpha - Enhanced Coal Upgrades")
                EIECoalUpgstab.geometry("300x300")
                EIECoalUpgstab.resizable(width=True,height=True)

                EIECoalUpgstab.mainloop()


            def MoltenBrickstab():
                EIMoltenBrickstab = Tk()

                EIMoltenBrickstab.title("Everything Incremental Alpha - Molten Bricks")
                EIMoltenBrickstab.geometry("300x300")
                EIMoltenBrickstab.resizable(width=True,height=True)

                EIMoltenBrickstab.mainloop()


            ECoalUpgs=Button(EIEFurnacetab, text = 'Enhanced Coal Upgrades', background = 'yellow', command=ECoalUpgstab)
            MoltenBricks=Button(EIEFurnacetab, text = 'Molten Bricks', background = 'orange', command=MoltenBrickstab)

            ECoalUpgs.pack()
            MoltenBricks.pack()

            EIEFurnacetab.mainloop()


        def TheMagmatab():
            EITheMagmatab = Tk()

            EITheMagmatab.title("Everything Incremental Alpha - The Magma")
            EITheMagmatab.geometry("300x300")
            EITheMagmatab.resizable(width=True,height=True)

            def MagmaFoundrytab():
                EIMagmaFoundrytab = Tk()

                EIMagmaFoundrytab.title("Everything Incremental Alpha - Magma Foundry")
                EIMagmaFoundrytab.geometry("300x300")
                EIMagmaFoundrytab.resizable(width=True,height=True)

                EIMagmaFoundrytab.mainloop()


            def MagmaReformarytab():
                EIMagmaReformarytab = Tk()

                EIMagmaReformarytab.title("Everything Incremental Alpha - Magma Reformary")
                EIMagmaReformarytab.geometry("300x300")
                EIMagmaReformarytab.resizable(width=True,height=True)

                EIMagmaReformarytab.mainloop()


            MagmaFoundry=Button(EITheMagmatab, text = 'Magma Foundry', background = 'red', command=MagmaFoundrytab)
            MagmaReformary=Button(EITheMagmatab, text = 'Magma Reformary', background = 'black', command=MagmaReformarytab)

            MagmaFoundry.pack()
            MagmaReformary.pack()

            EITheMagmatab.mainloop()


        def ThePlasmatab():
            EIThePlasmatab = Tk()

            EIThePlasmatab.title("Everything Incremental Alpha - The Plasma")
            EIThePlasmatab.geometry("300x300")
            EIThePlasmatab.resizable(width=True,height=True)

            def PlasmaFormarytab():
                EIPlasmaFormarytab = Tk()

                EIPlasmaFormarytab.title("Everything Incremental Alpha - Plasma Formary")
                EIPlasmaFormarytab.geometry("300x300")
                EIPlasmaFormarytab.resizable(width=True,height=True)

                EIPlasmaFormarytab.mainloop()


            def WFlametab():
                EIWFlametab = Tk()

                EIWFlametab.title("Everything Incremental ALpha - White Flames")
                EIWFlametab.geometry("300x300")
                EIWFlametab.resizable(width=True,height=True)

                EIWFlametab.mainloop()


            def PlasmaticBooststab():
                EIPlasmaticBooststab = Tk()
                
                EIPlasmaticBooststab.title("Everything Incremental Alpha - Plasmatic Boosts")
                EIPlasmaticBooststab.geometry("300x300")
                EIPlasmaticBooststab.resizable(width=True,height=True)

                EIPlasmaticBooststab.mainloop()


            PlasmaFormary=Button(EIThePlasmatab, text = 'Plasma Formary', background = 'purple', command=PlasmaFormarytab)
            WFlames=Button(EIThePlasmatab, text = 'White Flames', command=WFlametab)
            PlasmaticBoosts=Button(EIThePlasmatab, text = 'Plasmatic Boosts', background = 'purple', command=PlasmaticBooststab)

            PlasmaFormary.pack()
            WFlames.pack()
            PlasmaticBoosts.pack()

            EIThePlasmatab.mainloop()


        NFurnace=Button(EIFurnacetab, text = 'Normal Furnace', background = 'orange', command=NFurnacetab)
        EFurnace=Button(EIFurnacetab, text = 'Enhanced Furnace', background = 'yellow', command=EFurnacetab)
        TheMagma=Button(EIFurnacetab, text = 'The Magma', background = 'red', command=TheMagmatab)
        ThePlasma=Button(EIFurnacetab, text = 'The Plasma', background = 'purple', command=ThePlasmatab)

        NFurnace.pack()
        EFurnace.pack()
        TheMagma.pack()
        ThePlasma.pack()

        EIFurnacetab.mainloop()


    def TimeReversetab():
        EITimeReversetab = Tk()

        EITimeReversetab.title("Everything Incremental Alpha - Time Reversal")
        EITimeReversetab.geometry("300x300")
        EITimeReversetab.resizable(width=True,height=True)

        EITimeReversetab.mainloop()


    def Cadavertab():
        EICadavertab = Tk()

        EICadavertab.title("Everything Incremental Alpha - Cadavers")
        EICadavertab.geometry("300x300")
        EICadavertab.resizable(width=True,height=True)

        def TheDeadtab():
            EITheDeadtab = Tk()

            EITheDeadtab.title("Everything Incremental Alpha - The Dead")
            EITheDeadtab.geometry("300x300")
            EITheDeadtab.resizable(width=True,height=True)

            EITheDeadtab.mainloop()


        def TheLivetab():
            EITheLivetab = Tk()

            EITheLivetab.title("Everything Incremental Alpha - The Live")
            EITheLivetab.geometry("300x300")
            EITheLivetab.resizable(width=True,height=True)

            EITheLivetab.mainloop()


        TheDead=Button(EICadavertab, text = 'The Dead', background = 'black', command=TheDeadtab)
        TheLive=Button(EICadavertab, text = 'The Live', background = 'lime', command=TheLivetab)

        TheDead.pack()
        TheLive.pack()

        EICadavertab.mainloop()

    
    def Pathogentab():
        EIPathogentab = Tk()

        EIPathogentab.title("Everything Incremental Alpha - Pathogens")
        EIPathogentab.geometry("300x300")
        EIPathogentab.resizable(width=True,height=True)

        EIPathogentab.mainloop()


    def DarkCoretab():
        EIDarkCoretab = Tk()

        EIDarkCoretab.title("Everything Incremental Alpha - Dark Cores")
        EIDarkCoretab.geometry("300x300")
        EIDarkCoretab.resizable(width=True,height=True)

        EIDarkCoretab.mainloop()

    
    def Endorsementtab():
        EIEndorsementtab = Tk()

        EIEndorsementtab.title("Everything Incremental Alpha - Endorsements")
        EIEndorsementtab.geometry("300x300")
        EIEndorsementtab.resizable(width=True,height=True)

        def EPUpgTreetab():
            EIEPUpgTreetab = Tk()
            
            EIEPUpgTreetab.title("Everything Incremental Alpha - Endorsement Points Upgrade Tree")
            EIEPUpgTreetab.geometry("300x300")
            EIEPUpgTreetab.resizable(width=True,height=True)

            EIEPUpgTreetab.mainloop()


        def Perkstab():
            EIPerkstab = Tk()

            EIPerkstab.title("Everything Incremental Alpha - Perks")
            EIPerkstab.geometry("300x300")
            EIPerkstab.resizable(width=True,height=True)

            EIPerkstab.mainloop()


        def TheStadiumtab():
            EITheStadiumtab = Tk()

            EITheStadiumtab.title("Everything Incremental Alpha - The Stadium")
            EITheStadiumtab.geometry("300x300")
            EITheStadiumtab.resizable(width=True,height=True)

            EITheStadiumtab.mainloop()


        def ThePantheontab():
            EIThePantheontab = Tk()

            EIThePantheontab.title("Everything Incremental Alpha - The Pantheon")
            EIThePantheontab.geometry("300x300")
            EIThePantheontab.resizable(width=True,height=True)

            def SpectralGemstab():
                EISpectralGemstab = Tk()

                EISpectralGemstab.title("Everything Incremental Alpha - Spectral Gems")
                EISpectralGemstab.geometry("300x300")
                EISpectralGemstab.resizable(width=True,height=True)

                EISpectralGemstab.mainloop()


            def PurgeRunstab():
                EIPurgeRunstab = Tk()

                EIPurgeRunstab.title("Everything Incremental Alpha - Purge Runs")
                EIPurgeRunstab.geometry("300x300")
                EIPurgeRunstab.resizable(width=True,height=True)

                EIPurgeRunstab.mainloop()


            SpectralGems=Button(EIThePantheontab, text = 'Spectral Gems', command=SpectralGemstab)
            PurgeRuns=Button(EIThePantheontab, text = 'Purge Runs', background = 'blue', command=PurgeRunstab)

            SpectralGems.pack()
            PurgeRuns.pack()

            EIThePantheontab.mainloop()


        def Derivativetab():
            EIDerivativetab = Tk()

            EIDerivativetab.title("Everything Incremental Alpha - Derivatives")
            EIDerivativetab.geometry("300x300")
            EIDerivativetab.resizable(width=True,height=True)

            EIDerivativetab.mainloop()


        EPUpgTree=Button(EIEndorsementtab, text = 'Endorsement Points Upgrade Tree', command=EPUpgTreetab)
        Perks=Button(EIEndorsementtab, text = 'Perks', background = 'yellow', command=Perkstab)
        TheStadium=Button(EIEndorsementtab, text = 'The Stadium', background = 'orange', command=TheStadiumtab)
        ThePantheon=Button(EIEndorsementtab, text = 'The Pantheon', background = 'light blue', command=ThePantheontab)
        Derivatives=Button(EIEndorsementtab, text = 'Derivatives', background = 'green', command=Derivativetab)

        EPUpgTree.pack()
        Perks.pack()
        TheStadium.pack()
        ThePantheon.pack()
        Derivatives.pack()

        EIEndorsementtab.mainloop()


    def Elementarytab():
        EIElementarytab = Tk()

        EIElementarytab.title("Everything Incremental Alpha - Elementary")
        EIElementarytab.geometry("300x300")
        EIElementarytab.resizable(width=True,height=True)

        def Fermionstab():
            EIFermionstab = Tk()

            EIFermionstab.title("Everything Incremental Alpha - Fermions")
            EIFermionstab.geometry("300x300")
            EIFermionstab.resizable(width=True,height=True)

            EIFermionstab.mainloop()


        def Bosonstab():
            EIBosonstab = Tk()
            
            EIBosonstab.title("Everything Incremental Alpha - Bosons")
            EIBosonstab.geometry("300x300")
            EIBosonstab.resizable(width=True,height=True)

            def GaugeBosonstab():
                EIGaugeBosonstab = Tk()

                EIGaugeBosonstab.title("Everything Incremental Alpha - Gauge Bosons")
                EIGaugeBosonstab.geometry("300x300")
                EIGaugeBosonstab.resizable(width=True,height=True)

                EIGaugeBosonstab.mainloop()


            def ScalarBosonstab():
                EIScalarBosonstab = Tk()

                EIScalarBosonstab.title("Everything Incremental Alpha - Scalar Bosons")
                EIScalarBosonstab.geometry("300x300")
                EIScalarBosonstab.resizable(width=True,height=True)
                
                EIScalarBosonstab.mainloop()


            GaugeBosons=Button(EIBosonstab, text = 'Gauge Bosons', background = 'light green', command=GaugeBosonstab)
            ScalarBosons=Button(EIBosonstab, text = 'Scalar Bosons', background = 'yellow', command=ScalarBosonstab)

            GaugeBosons.pack()
            ScalarBosons.pack()

            EIBosonstab.mainloop()


        def Theoriversetab():
            EITheoriversetab = Tk()

            EITheoriversetab.title("Everything Incremental Alpha - The Theoriverse")
            EITheoriversetab.geometry("300x300")
            EITheoriversetab.resizable(width=True,height=True)

            def TheoriverseDepthstab():
                EITheoriverseDepthstab = Tk()

                EITheoriverseDepthstab.title("Everything Incremental Alpha - Theoriverse Depths")
                EITheoriverseDepthstab.geometry("300x300")
                EITheoriverseDepthstab.resizable(width=True,height=True)

                EITheoriverseDepthstab.mainloop()


            def SymetricParticlestab():
                EISymetricParticlestab = Tk()

                EISymetricParticlestab.title("Everything Incremental Alpha - Symetric Particles")
                EISymetricParticlestab.geometry("300x300")
                EISymetricParticlestab.resizable(width=True,height=True)

                EISymetricParticlestab.mainloop()


            def TheoriversePointsUpgTreetab():
                EITheoriversePointsUpgTreetab = Tk()

                EITheoriversePointsUpgTreetab.title("Everything Incremental Alpha - Theoriverse Points Upgrade Tree")
                EITheoriversePointsUpgTreetab.geometry("300x300")
                EITheoriversePointsUpgTreetab.resizable(width=True,height=True)

                EITheoriversePointsUpgTreetab.mainloop()


            def Stringstab():
                EIStringstab = Tk()

                EIStringstab.title("Everything Incremental Alpha - Strings")
                EIStringstab.geometry("300x300")
                EIStringstab.resizable(width=True,height=True)

                EIStringstab.mainloop()


            def Preonstab():
                EIPreonstab = Tk()

                EIPreonstab.title("Everything Incremental Alpha - Preons")
                EIPreonstab.geometry("300x300")
                EIPreonstab.resizable(width=True,height=True)

                EIPreonstab.mainloop()


            def Acceleronstab():
                EIAcceleronstab = Tk()

                EIAcceleronstab.title("Everything Incremental Alpha - Accelerons")
                EIAcceleronstab.geometry("300x300")
                EIAcceleronstab.resizable(width=True,height=True)

                EIAcceleronstab.mainloop()


            def Inflateronstab():
                EIInflateronstab = Tk()

                EIInflateronstab.title("Everything Incremental Alpha - Inflaterons")
                EIInflateronstab.geometry("300x300")
                EIInflateronstab.resizable(width=True,height=True)

                EIInflateronstab.mainloop()


            TheoriverseDepths=Button(EITheoriversetab, text = 'Theoriverse Depths', background = 'black', command=TheoriverseDepthstab)
            SymetricParticles=Button(EITheoriversetab, text = 'Symetric Particles', command=SymetricParticlestab)
            TheoriversePointsUpgTree=Button(EITheoriversetab, text = 'Theoriverse Points Upgrade Tree', background = 'black', command=TheoriversePointsUpgTreetab)
            Strings=Button(EITheoriversetab, text = 'Strings', command=Stringstab)
            Preons=Button(EITheoriversetab, text = 'Preons', background = 'light blue', command=Preonstab)
            Accelerons=Button(EITheoriversetab, text = 'Accelerons', background = 'yellow', command=Acceleronstab)
            Inflaterons=Button(EITheoriversetab, text = 'Inflaterons', command=Inflateronstab)

            TheoriverseDepths.pack()
            SymetricParticles.pack()
            TheoriversePointsUpgTree.pack()
            Strings.pack()
            Preons.pack()
            Accelerons.pack()
            Inflaterons.pack()

            EITheoriversetab.mainloop()


        def HadronicChalstab():
            EIHadronicChalstab = Tk()

            EIHadronicChalstab.title("Everything Incremental Alpha - Hadronic Challenges")
            EIHadronicChalstab.geometry("300x300")
            EIHadronicChalstab.resizable(width=True,height=True)

            EIHadronicChalstab.mainloop()


        def Quantumizertab():
            EIQuantumizertab = Tk()

            EIQuantumizertab.title("Everything Incremental Alpha - The Quantumizer")
            EIQuantumizertab.geometry("300x300")
            EIQuantumizertab.resizable(width=True,height=True)

            def QuantumFoamtab():
                EIQuantumFoamtab = Tk()

                EIQuantumFoamtab.title("Everything Incremental Alpha - Quantum Foams")
                EIQuantumFoamtab.geometry("300x300")
                EIQuantumFoamtab.resizable(width=True,height=True)

                EIQuantumFoamtab.mainloop()


            def Entropytab():
                EIEntropytab = Tk()

                EIEntropytab.title("Everything Incremental Alpha - Entropy")
                EIEntropytab.geometry("300x300")
                EIEntropytab.resizable(width=True,height=True)

                EIEntropytab.mainloop()


            def Skyrmionstab():
                EISkyrmionstab = Tk()

                EISkyrmionstab.title("Everything Incremental Alpha - Skyrmions")
                EISkyrmionstab.geometry("300x300")
                EISkyrmionstab.resizable(width=True,height=True)

                def Pionstab():
                    EIPionstab = Tk()

                    EIPionstab.title("Everything Incremental Alpha - Pions")
                    EIPionstab.geometry("300x300")
                    EIPionstab.resizable(width=True,height=True)

                    EIPionstab.mainloop()


                def Spinorstab():
                    EISpinorstab = Tk()
                    
                    EISpinorstab.title("Everything Incremental Alpha - Spinors")
                    EISpinorstab.geometry("300x300")
                    EISpinorstab.resizable(width=True,height=True)

                    EISpinorstab.mainloop()


                Pions=Button(EISkyrmionstab, text = 'Pions', background = 'purple', command=Pionstab)
                Spinors=Button(EISkyrmionstab, text = 'Spinors', background = 'purple', command=Spinorstab)

                Pions.pack()
                Spinors.pack()

                EISkyrmionstab.mainloop()

            
            QuantumFoam=Button(EIQuantumizertab, text = 'Quantum Foam', command=QuantumFoamtab)
            Entropy=Button(EIQuantumizertab, text = 'Entropy', command=Entropytab)
            Skyrmions=Button(EIQuantumizertab, text = 'Skyrmions', background = 'purple', command=Skyrmionstab)

            QuantumFoam.pack()
            Entropy.pack()
            Skyrmions.pack()

            EIQuantumizertab.mainloop()


        Fermions=Button(EIElementarytab, text = 'Fermions', background = 'light grey', command=Fermionstab)
        Bosons=Button(EIElementarytab, text = 'Bosons', background = 'light grey', command=Bosonstab)
        Theoriverse=Button(EIElementarytab, text = 'Theoriverse', background = 'black', command=Theoriversetab)
        HadronicChals=Button(EIElementarytab, text = 'Hadronic Challenges', background = 'grey', command=HadronicChalstab)
        Quantumizer=Button(EIElementarytab, text = 'Quantumizer', command=Quantumizertab)

        Fermions.pack()
        Bosons.pack()
        Theoriverse.pack()
        HadronicChals.pack()
        Quantumizer.pack()

        EIElementarytab.mainloop()


    def Multiversaltab():
        EIMultiversaltab = Tk()

        EIMultiversaltab.title("Everything Incremental Alpha - Multiverse!")
        EIMultiversaltab.geometry("300x300")
        EIMultiversaltab.resizable(width=True,height=True)

        def MultiversalChalstab():
            EIMultiversalChalstab = Tk()

            EIMultiversalChalstab.title("Everything Incremental Alpha - Multiversal Challenges")
            EIMultiversalChalstab.geometry("300x300")
            EIMultiversalChalstab.resizable(width=True,height=True)

            EIMultiversalChalstab.mainloop()


        def MultiversalQuiltstab():
            EIMultiversalQuiltstab = Tk()

            EIMultiversalQuiltstab.title("Everything Incremental Alpha - Multiversal Quilts")
            EIMultiversalQuiltstab.geometry("300x300")
            EIMultiversalQuiltstab.resizable(width=True,height=True)

            EIMultiversalQuiltstab.mainloop()


        MultiversalChals=Button(EIMultiversaltab, text = 'Multiversal Challenges', background = 'purple', command=MultiversalChalstab)
        MultiversalQuilts=Button(EIMultiversaltab, text = 'Multiversal Quilts', background = 'purple', command=MultiversalQuiltstab)

        MultiversalChals.pack()
        MultiversalQuilts.pack()

        EIMultiversaltab.mainloop()

    
    Climbing=Button(EITheHilltab, text = 'Climb The Hill', background = 'lime', command=Climbingtab)
    Energizer=Button(EITheHilltab, text = 'The Energizer', background = 'yellow', command=Energizertab)
    Furnace=Button(EITheHilltab, text = 'The Furnace', background = 'orange', command=Furnacetab)
    TimeReverse=Button(EITheHilltab, text = 'Time Reversal', background = 'pink', command=TimeReversetab)
    Cadavers=Button(EITheHilltab, text = 'Cadavers', background = 'grey', command=Cadavertab)
    Pathogens=Button(EITheHilltab, text = 'Pathogens', background = 'green', command=Pathogentab)
    DarkCores=Button(EITheHilltab, text = 'Dark Cores', background = 'black', command=DarkCoretab)
    Endorsements=Button(EITheHilltab, text = 'Endorsements', background = 'orange', command=Endorsementtab)
    Elementary=Button(EITheHilltab, text = 'Elementary', background = 'light blue', command=Elementarytab)
    Multiverse=Button(EITheHilltab, text = 'Multiverse', background = 'purple', command=Multiversaltab)

    Climbing.pack()
    Energizer.pack()
    Furnace.pack()
    TimeReverse.pack()
    Cadavers.pack()
    Pathogens.pack()
    DarkCores.pack()
    Endorsements.pack()
    Elementary.pack()
    Multiverse.pack()

    EITheHilltab.mainloop()

########################################################################################################

def TheFormulatab():
    EITheFormulatab = Tk()

    EITheFormulatab.title("Everything Incremental Alpha - The Formula")
    EITheFormulatab.geometry("300x300")
    EITheFormulatab.resizable(width=True,height=True)


    def SubFormulatab():
        EISubFormulatab = Tk()

        EISubFormulatab.title("Everything Incremental Alpha - Sub-Formula")
        EISubFormulatab.geometry("300x300")
        EISubFormulatab.resizable(width=True,height=True)

        EISubFormulatab.mainloop()
    

    def ZoneAtab():
        EIZoneAtab = Tk()

        EIZoneAtab.title("Everything Incremental Alpha - A")
        EIZoneAtab.geometry("300x300")
        EIZoneAtab.resizable(width=True,height=True)


        def ZoneAMaintab():
            EIZoneAMaintab = Tk()

            EIZoneAMaintab.title("Everything Incremental Alpha - A - Main")


            def APowertab():
                EIAPowertab = Tk()

                EIAPowertab.title("Everything Incremental Alpha - A Power")
                EIAPowertab.geometry("300x300")
                EIAPowertab.resizable(width=True,height=True)

                EIAPowertab.mainloop()


            def Alphatab():
                EIAlphatab = Tk()

                EIAlphatab.title("Everything Incremental Alpha - Alpha")
                EIAlphatab.geometry("300x300")
                EIAlphatab.resizable(width=True,height=True)

                EIAlphatab.mainloop()


            def Abolitytab():
                EIAbolitytab = Tk()

                EIAbolitytab.title("Everything Incremental Alpha - Abolity")
                EIAbolitytab.geometry("300x300")
                EIAbolitytab.resizable(width=True,height=True)

                EIAbolitytab.mainloop()

            APower=Button(EIZoneAMaintab, text = 'A Power', command=APowertab)
            Alpha=Button(EIZoneAMaintab, text = 'Alpha', command=Alphatab)
            Abolity=Button(EIZoneAMaintab, text = 'Abolity', command=Abolitytab)

            APower.pack()
            Alpha.pack()
            Abolity.pack()

            EIZoneAMaintab.mainloop()

        ZoneAMain=Button(EIZoneAMaintab, text = 'Main of A', command=ZoneAMaintab)
        ZoneASub=Button(EIZoneASubtab, text = 'Sub of A', command=ZoneASubtab)
        ZoneAReset=Button(EIZoneAResettab, text = 'Reset of A', command=ZoneAResettab)

        ZoneAMain.pack()
        ZoneASub.pack()
        ZoneAReset.pack()

        EIZoneAtab.mainloop()

    
    def ZoneBtab():
        EIZoneBtab = Tk()

        EIZoneBtab.title("Everything Incremental Alpha - B")
        EIZoneBtab.geometry("300x300")
        EIZoneBtab.resizable(width=True,height=True)


        def BPowertab():
            EIBPowertab = Tk()

            EIBPowertab.title("Everything Incremental Alpha - B Power")
            EIBPowertab.geometry("300x300")
            EIBPowertab.resizable(width=True,height=True)

            EIBPowertab.mainloop()


        def Betatab():
            EIBetatab = Tk()

            EIBetatab.title("Everything Incremental Alpha - Beta")
            EIBetatab.geometry("300x300")
            EIBetatab.resizable(width=True,height=True)

            EIBetatab.mainloop()


        def Batteriestab():
            EIBatteriestab = Tk()

            EIBatteriestab.title("Everything Incremental Alpha - Batteries")
            EIBatteriestab.geometry("300x300")
            EIBatteriestab.resizable(width=True,height=True)

            ba1=Label(Batteriestab, text = ('ba1 : 0'))
            ba2=Label(Batteriestab, text = ('ba2 : 0'))
            ba3=Label(Batteriestab, text = ('ba3 : 0'))

            ba1.pack()
            ba2.pack()
            ba3.pack()


            EIBatteriestab.mainloop()


        def Brickstab():
            EIBrickstab = Tk()
            
            EIBrickstab.title("Everything Incremental Alpha - Bricks")
            EIBrickstab.geometry("300x300")
            EIBrickstab.resizable(width=True,height=True)

            EIBrickstab.mainloop()


        def Buttonstab():
            EIButtonstab = Tk()

            EIButtonstab.title("Everything Incremental Alpha - Buttons")
            EIButtonstab.geometry("300x300")
            EIButtonstab.resizable(width=True,height=True)

            EIButtonstab.mainloop()


        def Blockstab():
            EIBlockstab = Tk()

            EIBlockstab.title("Everything Incremental Alpha - Blocks")
            EIBlockstab.geometry("300x300")
            EIBlockstab.resizable(width=True,height=True)

            EIBlockstab.mainloop()


        BPower=Button(EIZoneBtab, text = 'B Power', command=BPowertab)
        Beta=Button(EIZoneBtab, text = 'Beta', command=Betatab)
        Batteries=Button(EIZoneBtab, text = 'Batteries', command=Batteriestab)
        Bricks=Button(EIZoneBtab, text = 'Bricks', command=Brickstab)
        Buttons=Button(EIZoneBtab, text = 'Buttons', command=Buttonstab)
        Blocks=Button(EIZoneBtab, text = 'Blocks', command=Blockstab)

        BPower.pack()
        Beta.pack()
        Batteries.pack()
        Bricks.pack()
        Buttons.pack()
        Blocks.pack()

        EIZoneBtab.mainloop()



    def Spinstab():
        EISpinstab = Tk()
        
        EISpinstab.title("Everything Incremental Alpha - Spins")
        EISpinstab.geometry("300x300")
        EISpinstab.resizable(width=True,height=True)

        ROa=Label(Spinstab, text = ('ROa : 0'))
        ROb=Label(Spinstab, text = ('ROb : 0'))
        ROc=Label(Spinstab, text = ('ROc : 0'))

        ROa.pack()
        ROb.pack()
        ROc.pack()


        EISpinstab.mainloop()



    def ZoneCtab():
        EIZoneCtab = Tk()

        EIZoneCtab.title("Everything Incremental Alpha - C")
        EIZoneCtab.geometry("300x300")
        EIZoneCtab.resizable(width=True,height=True)

        def CPowertab():
            EICPowertab = Tk()

            EICPowertab.title("Everything Incremental Alpha - C Power")
            EICPowertab.geometry("300x300")
            EICPowertab.resizable(width=True,height=True)
            
            EICPowertab.mainloop()


        def Cetatab():
            EICetatab = Tk()
            
            EICetatab.title("Everything Incremental Alpha - Ceta")
            EICetatab.geometry("300x300")
            EICetatab.resizable(width=True,height=True)

            EICetatab.mainloop()


        def Candytab():
            EICandytab = Tk()

            EICandytab.title("Everything Incremental Alpha - Candy!!!!!")
            EICandytab.geometry("300x300")
            EICandytab.resizable(width=True,height=True)

            def Candies():
                EICandiestab = Tk()

                EICandiestab.title("Everything Incremental Alpha - Candies")
                EICandiestab.geometry("300x300")
                EICandiestab.resizable(width=True,height=True)

                EICandiestab.mainloop()


            def Chocolates():
                EIChocolatestab = Tk()

                EIChocolatestab.title("Everything Incremental Alpha - Chocolates")
                EIChocolatestab.geometry("300x300")
                EIChocolatestab.resizable(width=True,height=True)

                EIChocolatestab.mainloop()


            def Taffies():
                EITaffiestab = Tk()

                EITaffiestab.title("Everything Incremental Alpha - Taffies")
                EITaffiestab.geometry("300x300")
                EITaffiestab.resizable(width=True,height=True)

                EITaffiestab.mainloop()


            Candies=Button(EICandytab, text = 'Candies', command=Candies)
            Chocolates=Button(EICandytab, text = 'Chocolates', command=Chocolates)
            Taffies=Button(EICandytab, text = 'Taffies', command=Taffies)

            Candies.pack()
            Chocolates.pack()
            Taffies.pack()

            EICandytab.mainloop()

        
        def Clockstab():
            EIClockstab = Tk()

            EIClockstab.title("Everything Incremental Alpha - Clocks")
            EIClockstab.geometry("300x300")
            EIClockstab.resizable(width=True,height=True)

            TimeResetsFrame=Frame(Clockstab, relief='solid', bd=2)
            TimeAmountInfoFrame=Frame(Clockstab, relief='solid', bd=2)

            SecondAmount = 0
            MinuteAmount = 0
            HourAmount = 0
            DayAmount = 0
            WeekAmount = 0
            MonthAmount = 0
            YearAmount = 0
            DecadeAmount = 0
            MilleniumAmount = 0
            Eons = 0
            QuantumCycles = 0
            UniversalLengths = 0
            MultiversalLengths = 0

            def TimeUpgradestab():
                EITimeUpgradestab = Tk()
                
                EITimeUpgradestab.title("Everything Incremental Alpha - Time Upgrades")
                EITimeUpgradestab.geometry("300x300")
                EITimeUpgradestab.resizable(width=True,height=True)

                EITimeUpgradestab.mainloop()

            
            def MinutesResetButtonClicked():
                MinutesResetresponse = messagebox.askyesnocancel("Minutes Reset", "Do you want to Reset your Seconds to Minutes?! | RequirementsL 60+ Seconds | 60 Seconds -> 1 Minute")

                if MinutesResetresponse == 1:
                    if SecondAmount >= 60:
                        messagebox.showinfo("Reset Done!", "Your", SecondAmount, "Seconds are converted to", SecondAmount/60, "Minutes!")
                elif SecondAmount < 60:
                    messagebox.showerror("Failed", "Not enough Seconds!")
                elif response == 0:
                    messagebox.showinfo("Cancelled", "You cancelled the performation of Minutes Reset.")
                else:
                    messagebox.showinfo("Cancelled", "You cancelled the performation of Minutes Reset.")
            
            TimeUpgrades=Button(TimeResetsFrame, text = 'Time Upgrades', command=TimeUpgradestab)
            MinutesReset=Button(TimeResetsFrame, text = 'Reset For Minutes', command=MinutesResetButtonClicked)

            TimeUpgrades.pack()
            MinutesReset.pack()

            EIClockstab.mainloop()
        
        CPower=Button(EIZoneCtab, text = 'C Power', command=CPowertab)
        Ceta=Button(EIZoneCtab, text = 'Ceta', command=Cetatab)
        Candy=Button(EIZoneCtab, text = 'Candy!!!!', command=Candytab)
        Clocks=Button(EIZoneCtab, text = 'Clocks', command=Clockstab)

        CPower.pack()
        Ceta.pack()
        Candy.pack()
        Clocks.pack()

        EIZoneCtab.mainloop()


    def ZoneDtab():
        EIZoneDtab = Tk()

        EIZoneDtab.title("Everything Incremental Alpha - D")
        EIZoneDtab.geometry("300x300")
        EIZoneDtab.resizable(width=True,height=True)

        EIZoneDtab.mainloop()


    def ZoneEtab():
        EIZoneEtab = Tk()

        EIZoneEtab.title("Everything Incremental Alpha - E")
        EIZoneEtab.geometry("300x300")
        EIZoneEtab.resizable(width=True,height=True)

        EIZoneEtab.mainloop()


    def ZoneFtab():
        EIZoneFtab = Tk()

        EIZoneFtab.title("Everything Incremental Alpha - F")
        EIZoneFtab.geometry("300x300")
        EIZoneFtab.resizable(width=True,height=True)

        EIZoneFtab.mainloop()


    def ZoneGtab():
        EIZoneGtab = Tk()

        EIZoneGtab.title("Everything Incremental Alpha - G")
        EIZoneGtab.geometry("300x300")
        EIZoneGtab.resizable(width=True,height=True)

        EIZoneGtab.mainloop()


    def ZoneHtab():
        EIZoneHtab = Tk()

        EIZoneHtab.title("Everything Incremental Alpha - H")
        EIZoneHtab.geometry("300x300")
        EIZoneHtab.resizable(width=True,height=True)

        EIZoneHtab.mainloop()


    def ZoneItab():
        EIZoneItab = Tk()

        EIZoneItab.title("Everything Incremental Alpha - I")
        EIZoneItab.geometry("300x300")
        EIZoneItab.resizable(width=True,height=True)

        EIZoneItab.mainloop()


    def ZoneJtab():
        EIZoneJtab = Tk()

        EIZoneJtab.title("Everything Incremental Alpha - J")
        EIZoneJtab.geometry("300x300")
        EIZoneJtab.resizable(width=True,height=True)

        EIZoneJtab.mainloop()


    def ZoneKtab():
        EIZoneKtab = Tk()

        EIZoneKtab.title("Everything Incremental Alpha - K")
        EIZoneKtab.geometry("300x300")
        EIZoneKtab.resizable(width=True,height=True)

        EIZoneKtab.mainloop()


    def ZoneLtab():
        EIZoneLtab = Tk()

        EIZoneLtab.title("Everything Incremental Alpha - L")
        EIZoneLtab.geometry("300x300")
        EIZoneLtab.resizable(width=True,height=True)

        EIZoneLtab.mainloop()


    def ZoneMtab():
        EIZoneMtab = Tk()

        EIZoneMtab.title("Everything Incremental Alpha - M")
        EIZoneMtab.geometry("300x300")
        EIZoneMtab.resizable(width=True,height=True)

        EIZoneMtab.mainloop()


    def ZoneNtab():
        EIZoneNtab = Tk()

        EIZoneNtab.title("Everything Incremental Alpha - N")
        EIZoneNtab.geometry("300x300")
        EIZoneNtab.resizable(width=True,height=True)

        EIZoneNtab.mainloop()


    def ZoneOtab():
        EIZoneOtab = Tk()

        EIZoneOtab.title("Everything Incremental Alpha - O")
        EIZoneOtab.geometry("300x300")
        EIZoneOtab.resizable(width=True,height=True)

        EIZoneOtab.mainloop()


    def ZonePtab():
        EIZonePtab = Tk()

        EIZonePtab.title("Everything Incremental Alpha - P")
        EIZonePtab.geometry("300x300")
        EIZonePtab.resizable(width=True,height=True)

        EIZonePtab.mainloop()


    def ZoneQtab():
        EIZoneQtab = Tk()

        EIZoneQtab.title("Everything Incremental Alpha - Q")
        EIZoneQtab.geometry("300x300")
        EIZoneQtab.resizable(width=True,height=True)

        EIZoneQtab.mainloop()


    def ZoneRtab():
        EIZoneRtab = Tk()

        EIZoneRtab.title("Everything Incremental Alpha - R")
        EIZoneRtab.geometry("300x300")
        EIZoneRtab.resizable(width=True,height=True)

        EIZoneRtab.mainloop()


    def ZoneStab():
        EIZoneStab = Tk()

        EIZoneStab.title("Everything Incremental Alpha - S")
        EIZoneStab.geometry("300x300")
        EIZoneStab.resizable(width=True,height=True)

        EIZoneStab.mainloop()


    def ZoneTtab():
        EIZoneTtab = Tk()

        EIZoneTtab.title("Everything Incremental Alpha - T")
        EIZoneTtab.geometry("300x300")
        EIZoneTtab.resizable(width=True,height=True)

        EIZoneTtab.mainloop()


    def ZoneUtab():
        EIZoneUtab = Tk()

        EIZoneUtab.title("Everything Incremental Alpha - U")
        EIZoneUtab.geometry("300x300")
        EIZoneUtab.resizable(width=True,height=True)

        EIZoneUtab.mainloop()


    def ZoneVtab():
        EIZoneVtab = Tk()

        EIZoneVtab.title("Everything Incremental Alpha - V")
        EIZoneVtab.geometry("300x300")
        EIZoneVtab.resizable(width=True,height=True)

        EIZoneVtab.mainloop()


    def ZoneWtab():
        EIZoneWtab = Tk()

        EIZoneWtab.title("Everything Incremental Alpha - W")
        EIZoneWtab.geometry("300x300")
        EIZoneWtab.resizable(width=True,height=True)

        EIZoneWtab.mainloop()


    def ZoneXtab():
        EIZoneXtab = Tk()

        EIZoneXtab.title("Everything Incremental Alpha - X")
        EIZoneXtab.geometry("300x300")
        EIZoneXtab.resizable(width=True,height=True)

        EIZoneXtab.mainloop()


    def ZoneYtab():
        EIZoneYtab = Tk()

        EIZoneYtab.title("Everything Incremental Alpha - Y")
        EIZoneYtab.geometry("300x300")
        EIZoneYtab.resizable(width=True,height=True)

        EIZoneYtab.mainloop()


    def ZoneZtab():
        EIZoneZtab = Tk()

        EIZoneZtab.title("Everything Incremental Alpha - Z")
        EIZoneZtab.geometry("300x300")
        EIZoneZtab.resizable(width=True,height=True)

        EIZoneZtab.mainloop()


    SubFormula=Button(EITheFormulatab, text = 'Sub-Formula', command=SubFormulatab)
    ZoneA=Button(EITheFormulatab, text = 'Zone A', command=ZoneAtab)
    ZoneB=Button(EITheFormulatab, text = 'Zone B', command=ZoneBtab)
    Spins=Button(EITheFormulatab, text = 'Spins', command=Spinstab)
    ZoneC=Button(EITheFormulatab, text = 'Zone C', command=ZoneCtab)
    ZoneD=Button(EITheFormulatab, text = 'Zone D', command=ZoneDtab)
    ZoneE=Button(EITheFormulatab, text = 'Zone E', command=ZoneEtab)
    ZoneF=Button(EITheFormulatab, text = 'Zone F', command=ZoneFtab)
    ZoneG=Button(EITheFormulatab, text = 'Zone G', command=ZoneGtab)
    ZoneH=Button(EITheFormulatab, text = 'Zone H', command=ZoneHtab)
    ZoneI=Button(EITheFormulatab, text = 'Zone I', command=ZoneItab)
    ZoneJ=Button(EITheFormulatab, text = 'Zone J', command=ZoneJtab)
    ZoneK=Button(EITheFormulatab, text = 'Zone K', command=ZoneKtab)
    ZoneL=Button(EITheFormulatab, text = 'Zone L', command=ZoneLtab)
    ZoneM=Button(EITheFormulatab, text = 'Zone M', command=ZoneMtab)
    ZoneN=Button(EITheFormulatab, text = 'Zone N', command=ZoneNtab)
    ZoneO=Button(EITheFormulatab, text = 'Zone O', command=ZoneOtab)
    ZoneP=Button(EITheFormulatab, text = 'Zone P', command=ZonePtab)
    ZoneQ=Button(EITheFormulatab, text = 'Zone Q', command=ZoneQtab)
    ZoneR=Button(EITheFormulatab, text = 'Zone R', command=ZoneRtab)
    ZoneS=Button(EITheFormulatab, text = 'Zone S', command=ZoneStab)
    ZoneT=Button(EITheFormulatab, text = 'Zone T', command=ZoneTtab)
    ZoneU=Button(EITheFormulatab, text = 'Zone U', command=ZoneUtab)
    ZoneV=Button(EITheFormulatab, text = 'Zone V', command=ZoneVtab)
    ZoneW=Button(EITheFormulatab, text = 'Zone W', command=ZoneWtab)
    ZoneX=Button(EITheFormulatab, text = 'Zone X', command=ZoneXtab)
    ZoneY=Button(EITheFormulatab, text = 'Zone Y', command=ZoneYtab)
    ZoneZ=Button(EITheFormulatab, text = 'Zone Z', command=ZoneZtab)


    SubFormula.pack()
    ZoneA.pack()
    ZoneB.pack()
    Spins.pack()
    ZoneC.pack()
    ZoneD.pack()
    ZoneE.pack()
    ZoneF.pack()
    ZoneG.pack()
    ZoneH.pack()
    ZoneI.pack()
    ZoneJ.pack()
    ZoneK.pack()
    ZoneL.pack()
    ZoneM.pack()
    ZoneN.pack()
    ZoneO.pack()
    ZoneP.pack()
    ZoneQ.pack()
    ZoneR.pack()
    ZoneS.pack()
    ZoneT.pack()
    ZoneU.pack()
    ZoneV.pack()
    ZoneW.pack()
    ZoneX.pack()
    ZoneY.pack()
    ZoneZ.pack()



    EITheFormulatab.mainloop()

########################################################################################################

def Informationtab():
    EIInfotab = Tk()

    EIInfotab.title("Everything Incremental Alpha - Informations")
    EIInfotab.geometry("300x300")
    EIInfotab.resizable(width=True,height=True)

    def Developers():
        messagebox.showinfo("Everything Incremental Alpha - Devs", "Made With Love By Astral! (Discord = rondogreat#0000 , Astral#7101)")

    def VersionInfo():
        messagebox.showinfo("Everything Incremental Alpha - Versions", "Current Version : v0.0.2.py [Moving To Python II]")

    def ModVersionInfo():
        messagebox.showinfo("Everything Incremental Alpha - Mods", "Current Mod : v13.2.13.c [Another Fighting Patch]")

    def SpecialThanks():
        messagebox.showinfo("Everything Incremental Alpha - Special Thanks", "Special Thanks to *Loads of Game Developers from all over the world!*")

    def DiscordLinks():
        messagebox.showinfo("Everything Incremental Alpha - Discord Links", "Everything Incremental Main Server : https://discord.gg/uda8J9ABtm, Global Games Club Server : https://discord.gg/B2he8NsnV4")

    def DonationLinks():
        messagebox.showerror("Everything Incremental Alpha - ???", "Uhh.. No thanks???? I am not developing games for money you know...")

    def NotationsInfo():
        Nresponse = messagebox.askyesno("Everything Incremental Alpha - Notations Info", "We are now using the normal(Not the scientific.) notations. Do you want to know about *HUGE* and *ENORMOUS* numbers?")

        if Nresponse == 1:
            HNresponse = messagebox.askyesno("Everything Incremental Alpha - *HUGE* and *ENORMOUS* numbers", "Here are some *HUGE* and *ENORMOUS* numbers.\n1. G^64(4) : Graham's Number - ε.0.1.0 function \n2. Tar(10) : Dekotar \n3. Σ(1919) : Busy beaver function \nDo you want to see *INFINITY-RELATED* Numbers? then, Click yes. or else. Click no.")

            if HNresponse == 1:
                messagebox.showinfo("Everything Incremental Alpha - *INFINITY-RELATED* numbers", "Here are some *INFINITY-RELATED* numbers.\n1. ℵ0 : Aleph zero \n2. ℶ1 : Beth one \n3. ℶ2 : Beth two \n4. ℶω : Beth omega \n5. I : Inaccessible cardinal \n6. M : Mahlo cardinal \n7. K : Weakly compact cardinal \n8. Πmn : Indescribable cardinal \n9. I0 : rank-into-rank cardinals \n10. Ω : Absolute Infinite \nThanks for watching these Numbers! Bye!")

            elif HNresponse == 0:
                messagebox.showinfo("Everything Incremental Alpha - Cancelled", "Thanks for watching the *HUGE* and *ENORMOUS* numbers!")

        elif Nresponse == 0:
            messagebox.showinfo("Everything Incremental Alpha - Cancelled", "So, Seems that you didn't wanted to see *HUGE* and *ENORMOUS* numbers... Welp, bye then!")

    def SupportersInfo():
        messagebox.showinfo("Everything Incremental Alpha - Supporters!", "These are my GENEROUS SUPPORTERS who supported me so much! \nthe rabbit, H̷̆̈ĕ̵̈l̵̂̿ṕ̷͘y̸͂̾, Aether, Catattack, Seby, bruh, fdgdgfdatr, mrs.rogue_, Awmen, gizmodank, applesince, OMG, rndzz, Tempest, hangchhay2009 and other peoples in EI server and GGC server!")
    

    Devs=Button(EIInfotab, text = 'Developers', background = 'pink', command=Developers)
    Versions=Button(EIInfotab, text = 'Current Version', background = 'light blue', command=VersionInfo)
    ModVersions=Button(EIInfotab, text = 'Current Mod Version', background = 'blue', command=ModVersionInfo)
    SpecialThank=Button(EIInfotab, text = 'Special Thanks', background = 'yellow', command=SpecialThanks)
    Discord=Button(EIInfotab, text = 'Link to Discord!', background = 'dark blue', command=DiscordLinks)
    Donation=Button(EIInfotab, text = 'Donation!', background = 'lime', command=DonationLinks)
    NotationInfo=Button(EIInfotab, text = 'Notations', background = 'light green', command=NotationsInfo)
    Supporters=Button(EIInfotab, text= 'Supporters!', background = 'green', command=SupportersInfo)


    Devs.pack()
    Versions.pack()
    ModVersions.pack()
    SpecialThanks.pack()
    Discord.pack()
    Donation.pack()
    NotationInfo.pack()
    Supporters.pack()

    EIInfotab.mainloop()

########################################################################################################

def Settingtab():
    EISettingtab = Tk()

    EISettingtab.title("Everything Incremental Alpha - Settings")
    EISettingtab.geometry("300x300")
    EISettingtab.resizable(width=True,height=True)

    def LanguageSetting():
        response = messagebox.askyesno("Everything Incremental Alpha - Change Language", "Do you want to change your language to Korean (한국어)?")

        if response == 1:
            messagebox.showerror("Everything Incremental Alpha - Change Language Failed", "Cannot change language to Korean (한국어) because the developer has poor programming skills.")
        
        elif response == 0:
            messagebox.showinfo("Everything Incremental Alpha - Change Language Cancelled", "Changing language is cancelled.")

    def FontSetting():
        messagebox.showinfo("Everything Incremental Alpha - Change Fonts", "Sadly, There are only 1 fonts availiable now. Wait until the developer adds more fonts! (or wait until the dev has enough programming skills to add a new font.)")
    
    def NotationSetting():
        messagebox.showinfo("Everything Incremental Alpha - Change Notations", "Sadly, You can only use 1 Notation (Normal) now. Wait until the developer adds more Notations! (Please add Emoji Notations- *Gets Shot by Softcap*)")

    def ConfermSetting():
        messagebox.showinfo("Everything Incremental Alpha - Confermations", "There are no Confermations to enable or to disable in this game. Just double check before clicking the reset layer buttons. Please.")

    def HotkeySetting():
        messagebox.showinfo("Everything Incremental Alpha - Hotkeys", "There are no Hotkeys in this game by now. Hope the dev adds more Hotkeys cause QoL..")
    
    def AnimationSetting():
        messagebox.showinfo("Everything Incremental Alpha - Animatons", "This game has NO Animations. remind that. NO Animations. It might be added in 100 Dimensional Epoches.")

    def LeaveAReview():
        messagebox.showinfo("Everything Incremental Alpha - Reviews", "Leave a Review to me! DM me to [rondogreat#0000, Astral#7101]")

    def ResetAllProgress():
        WipeSave = messagebox.askyesnocancel("Everything Incremental Alpha - WIPE YOUR SAVE", "Do you really want to wipe your save..?")

        if WipeSave == 1:
            WipeSaveResponse = messagebox.askyesno("Everything Incremental Alpha - WIPE YOUR SAVE", "WARNING. THIS ACTION CANNOT BE CANCELLED. YOU WON'T GET ANY REWARDS. YOU WILL LOSE ALL YOUR PROGRESS IF YOU CONTINUE.")

            if WipeSaveResponse == 1:
                WipeSaveResponse2 = messagebox.askyesno("Everything Incremental Alpha - WIPE YOUR SAVE", "THIS IS YOUR LAST WARNING. I RECOMMEND YOU TO RESET IF THERE IS A CRITICAL ERROR IN THIS GAME. CONTINUE?")

                if WipeSaveResponse2 == 1:
                    messagebox.showerror("Everything Incremental Alpha - ERROR WHILE WIPING SAVE", "ERROR : RESETTING FUNCTION IS DENIED BY DEVELOPER.")

                elif WipeSaveResponse2 == 0:
                    messagebox.showinfo("Everything Incremental Alpha - Wiping Save Cancelled", "Wiping Save Cancelled!")

            elif WipeSaveResponse == 0:
                messagebox.showinfo("Everything Incremental Alpha - Wiping Save Cancelled", "Wiping Save Cancelled!")
        
        elif WipeSave == 0:
            messagebox.showinfo("Everything Incremental Alpha - Wiping Save Cancelled", "Wiping Save Cancelled!")

            
        else:
            messagebox.showinfo("Everything Incremental Alpha - Wiping Save Cancelled", "Wiping Save Cancelled!")



    Language=Button(EISettingtab, text = 'Change Language', background = 'grey', command=LanguageSetting)
    Fonts=Button(EISettingtab, text = 'Change Fonts', background = 'grey', command=FontSetting)
    Notations=Button(EISettingtab, text = 'Change Notations', background = 'grey', command=NotationSetting)
    Conferms=Button(EISettingtab, text = 'Turn On/Off Confermations', background = 'grey', command=ConfermSetting)
    Hotkeys=Button(EISettingtab, text = 'Hotkey Settings', background = 'grey', command=HotkeySetting)
    Animations=Button(EISettingtab, text = 'Animation Settings', background = 'grey', command=AnimationSetting)
    Reviews=Button(EISettingtab, text = 'Leave A Review!', background = 'yellow', command=LeaveAReview)
    WIPESAVE=Button(EISettingtab, text = 'WIPE YOUR SAVE', background = 'red', command=ResetAllProgress)


    Language.pack()
    Fonts.pack()
    Notations.pack()
    Conferms.pack()
    Hotkeys.pack()
    Reviews.pack()
    WIPESAVE.pack()

    EISettingtab.mainloop()

########################################################################################################

def TuStTaQutab():
    EITuStTaQutab = Tk()

    EITuStTaQutab.title("Everything Incremental Alpha - Tutorials & Stories & Tasks & Quests")
    EITuStTaQutab.geometry("300x300")
    EITuStTaQutab.resizable(width=True,height=True)

    def Tutorial():
        messagebox.showinfo("Everything Incremental Alpha - Tutorial!", "Welcome to Everything Incremental! \nThis game is an enormous fangame which includes many original incremental games! \nThis game is made by Astral! \nIt is simple. You can learn how to play this game by watching Stories (At the Stories tab), and completing Tasks which I give to you! \nThis game is *ever-expanding* game, so there are no goals! \nJust grind as much as you can and be the top of the leaderboards! \nGood Luck!")

    def Story():
        EIStory = Tk()

        EIStory.title("Everything Incremental Alpha - ★Stories★")
        EIStory.geometry("300x300")
        EIStory.resizable(width=True,height=True)


        def DevStory():
            EIDevStory = Tk()

            EIDevStory.title("Everything Incremental Alpha - Developer's Story")
            EIDevStory.geometry("300x300")
            EIDevStory.resizable(width=True,height=True)

            def DSC1():
                messagebox.showinfo("Everything Incremental Alpha - Developer's Story Chapter 1", "Chapter 1. \nOnce upon a time, there was a girl named Astral. \nShe liked playing games. \nShe wanted to be a programmer to develop games. \nOne day, she played Grass Cutting Incremental and Infinite Rarities and other Incremental games. \nThen, she got an idea; \n'How about making a huge fangame which includes lots of incremental game features?' \nShe started to work on that game. \n(Continues at Chapter 2...)")

            
            def DSC2():
                messagebox.showinfo("Everything Incremental Alpha - Developer's Story Chapter 2", "Chapter 2. \nShe searched more incremental games and added lots of features and content and layers in her ida note, but there was no way to make this game alive! \nShe learned Python and how to code, and she started to make her game with it...! \n(Continues at Chapter 3...)")


            def DSC3():
                messagebox.showinfo("Everything Incremental Alpha - Developer's Story Chapter 3", "Chapter 3. \nAfter fixing some bugs and errors in her game, She finally made a GUI. \nShe was so happy so she wanted to add a Story about her! \nThis is the story! \nAfter adding her story in her game, She continues updating her game...")


            def DSC4():
                messagebox.showerror("Everything Incremental Alpha - Developer's Story Chapter 4", "Coming Soon!")
            
            
            DSChapter1=Button(EIDevStory, text = 'Chapter 1', background = 'yellow', command=DSC1)
            DSChapter2=Button(EIDevStory, text = 'Chapter 2', background = 'orange', command=DSC2)
            DSChapter3=Button(EIDevStory, text = 'Chapter 3', background = 'pink', command=DSC3)
            DSChapter4=Button(EIDevStory, text = 'Chapter 4', background = 'red', command=DSC4)

            DSChapter1.pack()
            DSChapter2.pack()
            DSChapter3.pack()
            DSChapter4.pack()

            EIDevStory.mainloop()

        
        def GameStory():
            EIGameStory = Tk()

            EIGameStory.title("Everything Incremental Alpha - Main Game Story")
            EIGameStory.geometry("300x300")
            EIGameStory.resizable(width=True,height=True)

            def GSPrgue():
                messagebox.showinfo("Everything Incremental Alpha - Prologue", "Prologue \nIt was just a dark void. \nThere is only You and some old, rusty machine. \nIt says 'Turn me on!'. \nYou hesitated for a while but clicked the 'Turn me on!' button. \nThe machine turned on and started to produce something! \nIt was a strange, yellow material which flows! \nThis is a start of your journey... \n(Go to the Chapter A tab and Watch Chapter A-1...)")

            
            def GSCA():
                EIGSCA = Tk()

                EIGSCA.title("Everything Incremental Alpha - Chapter A Section")
                EIGSCA.geometry("500x500")
                EIGSCA.resizable(width=True,height=True)
                
                def GSCA1():
                    GSCA1res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to watch this chapter after watching prologue. \nDo you want to proceed?")
                        
                    if GSCA1res == 1:
                        messagebox.showinfo("Everything Incremental Alpha - Chapter A-1", "Chapter A-1 \nAfter a while, something appeared near you. \nIt was a girl. \n'Do Not fear me!' \nI am Astral, maker of this game!' \n'I will help you to unlock more features!' \nAstral said that you can gain *powers* with that machine, and upgrade it with generated powers! \nShe said that there are lots of *Reset Layers*, and You require some *Special Stats* to get them. \n'First of all, You have to get some *Tiers*.' \n'Get 100 Power and come back to me!' \n(Get 100 Power and Watch Chapter A-2...)")
                    
                    elif GSCA1res == 0:
                        messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")
                
                
                def GSCA2():
                    GSCA2res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to watch this chapter after watching chapter A-1, and after reached 100 Power. \nDo you want to proceed?")
                    
                    if GSCA2res == 1:
                        messagebox.showinfo("Everything Incremental Alpha - Chapter A-2", "After a moment, You got 100 power. \nYou told Astral that You already got 100 Power. \nAstral was delighted. \n'Now You can get your first Tier!' \n'It will reset most of your progress, but you will get some OP boosts.' \nYou proceed... And you got your first Tier! \n'Congratulations! I will give you the next task.' \n'The next task is to get Tier 2 and 10,000 Power!' \n'Tier 2 requires 10,000 Power!' \n'Complete this task for a New Reset Layer!' \n(Get Tier 2 and 10,000 Power and Watch Chapter A-3...)")

                    elif GSCA2res == 0:
                        messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")

                
                def GSCA3():
                    GSCA3res = messagebox.askyesno("Everything Incremental Alpha - Comfirmation", "It is recommended to watch this chapter after watching chapter A-2, and after reaching Tier 2 and 10,000 Power. \nDo you want to proceed?")

                    if GSCA3res == 1:
                        messagebox.showinfo("Everything Incremental Alpha - Chapter A-3", "Will be soon added.")

                    elif GSCA3res == 0:
                        messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")


                def GSCA4():
                    GSCA4res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to watch this chapter after watching chapter A-3, and after reaching Tier 3. \nDo you want to proceed?")

                    if GSCA4res == 1:
                        messagebox.showinfo("Everything Incremental Alpha - Chapter A-4", "Will be soon added.")

                    elif GSCA4res == 0:
                        messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")


                def GSCA5():
                    GSCA5res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to watch this chapter after watching chapter A-4, and after reaching Tier 4. \nDo you want to proceed?")

                    if GSCA5res == 1:
                        messagebox.showinfo("Everything Incremental Alpha - Chapter A-5", "Will be soon added.")

                    elif GSCA5res == 0:
                        messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")

                    
                def GSCA6():
                    GSCA6res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to watch this chapter after watching chapter A-5, and after reaching Tier 5. \nDo you want to proceed?")

                    if GSCA6res == 1:
                        messagebox.showinfo("Everything Incremental Alpha - Chapter A-6", "Will be soon added.")

                    elif GSCA6res == 0:
                        messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")


                def GSCA7():
                    GSCA7res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to watch this chapter after watching chapter A-6, and after reaching Tier 6. \nDo you want to proceed?")

                    if GSCA7res == 1:
                        messagebox.showinfo("Everything Incremental Alpha - Chapter A-7", "Will be soon added.")

                    elif GSCA7res == 0:
                        messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")


                def GSCA8():
                    GSCA8res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to watch this chapter after watching chapter A-7, and after reaching Tier 7. \nDo you want to proceed?")

                    if GSCA8res == 1:
                        messagebox.showinfo("Everything Incremental Alpha - Chapter A-8", "Will be soon added.")

                    elif GSCA8res == 0:
                        messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")


                def GSCA9():
                    GSCA9res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to watch this chapter after watching chapter A-8, and after reaching Tier 8. \nDo you want to proceed?")

                    if GSCA9res == 1:
                        messagebox.showinfo("Everything Incremental Alpha - Chapter A-9", "Will be soon added.")

                    elif GSCA9res == 0:
                        messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")

                    
                def GSCAH():
                    GSCAHres = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to watch this chapter after watching chapter A-9, and after reaching Tier 10. \nDo you want to proceed?")

                    if GSCAHres == 1:
                        messagebox.showinfo("Everything Incremental Alpha - Chapter A-h", "Will be soon added.")

                    elif GSCAHres == 0:
                        messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")

                
                def GSCA10():
                    GSCA10res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to watch this chapter after watching chapter A-h, and after reaching Hyper Tier 1 and Tier 10. \nDo you want to proceed?")

                    if GSCA10res == 1:
                        messagebox.showinfo("Everything Incremental Alpha - Chapter A-10", "Will be soon added.")

                    elif GSCA10res == 0:
                        messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")

                
                def GSCA11():
                    GSCA11res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to watch this chapter after watching chapter A-10, and after reaching Tier 12. \nDo you want to proceed?")

                    if GSCA11res == 1:
                        messagebox.showinfo("Everything Incremental Alpha - Chapter A-11", "Will be soon added.")

                    elif GSCA11res == 0:
                        messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")

                
                def GSCA12():
                    GSCA12res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to watch this chapter after watching chapter A-11, and after reaching Tier 15. \nDo you want to proceed?")

                    if GSCA12res == 1:
                        messagebox.showinfo("Everything Incremental Alpha - Chapter A-12", "Will be soon added.")

                    elif GSCA12res == 0:
                        messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action in cancelled.")

                
                def GSCAF():
                    GSCAFres = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to watch this chapter after watching chapter A-12, and after reaching Tier 18. \nDo you want to proceed?")

                    if GSCAFres == 1:
                        messagebox.showinfo("Everything Incremental Alpha - Chafter A-fin", "Will be soon added.")

                    elif GSCAFres == 0:
                        messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")

                
                GSChapterA1=Button(EIGSCA, text = "Chapter A-1", background = 'yellow', command=GSCA1)
                GSChapterA2=Button(EIGSCA, text = "Chapter A-2", background = 'light grey', command=GSCA2)
                GSChapterA3=Button(EIGSCA, text = "Chapter A-3", background = 'light blue', command=GSCA3)
                GSChapterA4=Button(EIGSCA, text = "Chapter A-4", background = 'blue', command=GSCA4)
                GSChapterA5=Button(EIGSCA, text = "Chapter A-5", command=GSCA5)
                GSChapterA6=Button(EIGSCA, text = "Chapter A-6", background = 'green', command=GSCA6)
                GSChapterA7=Button(EIGSCA, text = "Chapter A-7", background = 'orange', command=GSCA7)
                GSChapterA8=Button(EIGSCA, text = "Chapter A-8", background = 'red', command=GSCA8)
                GSChapterA9=Button(EIGSCA, text = "Chapter A-9", background = 'dark blue', command=GSCA9)
                GSChapterAH=Button(EIGSCA, text = "Chapter A-h", background = 'grey', command=GSCAH)
                GSChapterA10=Button(EIGSCA, text = "Chapter A-10", background = 'purple', command=GSCA10)
                GSChapterA11=Button(EIGSCA, text = "Chapter A-11", background = 'dark grey', command=GSCA11)
                GSChapterA12=Button(EIGSCA, text = "Chapter A-12", background = 'black', command=GSCA12)
                GSChapterAF=Button(EIGSCA, text = "Chapter A-fin", background = 'lime', command=GSCAF)

                GSChapterA1.pack()
                GSChapterA2.pack()
                GSChapterA3.pack()
                GSChapterA4.pack()
                GSChapterA5.pack()
                GSChapterA6.pack()
                GSChapterA7.pack()
                GSChapterA8.pack()
                GSChapterA9.pack()
                GSChapterAH.pack()
                GSChapterA10.pack()
                GSChapterA11.pack()
                GSChapterA12.pack()
                GSChapterAF.pack()
                
                EIGSCA.mainloop()

            
            def GSCB():
                EIGSCB = Tk()

                EIGSCB.title("Everything Incremental Alpha - Chapter B Section")
                EIGSCB.geometry("500x500")
                EIGSCB.resizable(width=True,height=True)


                def GSCB0():
                    GSCB0res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to watch this chapter after watching chapter A-fin. \nDo you want to proceed?")

                    if GSCB0res == 1:
                        messagebox.showinfo("Everything Incremental Alpha - Chapter B-0", "Will be soon added.")

                    elif GSCB0res == 0:
                        messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")


                def GSCB1():
                    GSCB1res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to watch this chapter after watching chapter B-0, and after getting 100 Grass and Tier 19. \nDo you want to proceed?")

                    if GSCB1res == 1:
                        messagebox.showinfo("Everything Incremental Alpha - Chapter B-1", "Will be soon added.")

                    elif GSCB1res == 0:
                        messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")


                def GSCB2():
                    GSCB2res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to watch this chapter after watching chapter B-1, and after getting Grasshop 1 and Tier 20. \nDo you want to proceed?")

                    if GSCB2res == 1:
                        messagebox.showinfo("Everything Incremental Alpha - Chapter B-2", "Will be soon added.")

                    elif GSCB2res == 0:
                        messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")

                
                GSChapterB0=Button(EIGSCB, text = "Chapter B-0", background = 'lime', command=GSCB0)
                GSChapterB1=Button(EIGSCB, text = "Chapter B-1", background = 'light grey', command=GSCB1)
                GSChapterB2=Button(EIGSCB, text = "Chapter B-2", background = 'light green', command=GSCB2)

                GSChapterB0.pack()
                GSChapterB1.pack()
                GSChapterB2.pack()


                EIGSCB.mainloop()


            GSPrologue=Button(EIGameStory, text = "Prologue", background = 'grey', command=GSPrgue)
            GSChapterA=Button(EIGameStory, text = "Chapter A Selection", background = 'yellow', command=GSCA)
            GSChapterB=Button(EIGameStory, text = "Chapter B Selection", background = 'light green', command=GSCB)

            GSPrologue.pack()
            GSChapterA.pack()
            GSChapterB.pack()


            EIGameStory.mainloop()


        def TaskQuest():
            EITaskQuest = Tk()

            EITaskQuest.title("Everything Incremental Alpha - Tasks & Quests")
            EITaskQuest.geometry("500x500")
            EITaskQuest.resizable(width=True,height=True)

            def Task1():
                Task1res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to see this Task information after watching Chapter A-1. \nDo you want to proceed?")
                
                if Task1res == 1:
                    messagebox.showinfo("Everything Incremental Alpha - First Task", "Task 1. \nGet 100 Power. \nUnlockable at Chapter A-1. \nRewards - New static reset : Tiers!")

                elif Task1res == 0:
                    messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")


            def Task2():
                Task2res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to see this Task information after watching Chapter A-2. \nDo you want to proceed?")

                if Task2res == 1:
                    messagebox.showinfo("Everything Incremental Alpha - Second Task", "Task 2. \nGet Tier 2 and 10,000 Power. \nUnlockable at Chapter A-2. \nRewards - New reset layer : Rebirths!")
            
                elif Task2res == 0:
                    messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")


            def Task3():
                Task3res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to see this Task information after watching Chapter A-3. \nDo you want to proceed?")

                if Task3res == 1:
                    messagebox.showinfo("Everything Incremental Alpha - Third Task", "Task 3. \nGet Tier 3 and 100 RP. \nUnlockable at Chapter A-3. \nRewards - New reset layer : Prestige!")

                elif Task3res == 0:
                    messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")


            def Task4():
                Task4res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to see this Task information after watching Chapter A-4. \nDo you want to proceed?")

                if Task4res == 1:
                    messagebox.showinfo("Everything Incremental Alpha - Fourth Task", "Task 4. \nGet Tier 4. \nUnlockable at Chapter A-4. \nRewards - New reset layer : Ascension!")


                elif Task4res == 0:
                    messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")

            
            def Task5():
                Task5res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to see this Task information after watching Chapter A-5. \nDo you want to proceed?")

                if Task5res == 1:
                    messagebox.showinfo("Everything Incremental Alpha - Fifth Task", "Task 5. \nGet Tier 5. \nUnlockable at Chapter A-5. \nRewards - New reset layer : Transcension!")

                elif Task5res == 0:
                    messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")


            def Task6():
                Task6res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to see this Task information after watching Chapter A-6. \nDo you want to proceed?")

                if Task6res == 1:
                    messagebox.showinfo("Everything Incremental Alpha - Sixth Task", "Task 6. \nGet Tier 6. \nUnlockable at Chapter A-6. \nRewards - New reset layer : Ultra!")

                elif Task6res == 0:
                    messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")

            
            def Task7():
                Task7res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to see this Task information after watching Chapter A-7. \nDo you want to proceed?")

                if Task7res == 1:
                    messagebox.showinfo("Everything Incremental Alpha - Seventh Task", "Task 7. \nGet Tier 7. \nUnlockable at Chapter A-7. \nRewards - New reset layer : Mega!")

                elif Task7res == 0:
                    messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")


            def Task8():
                Task8res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to see this Task information after watching Chapter A-8. \nDo you want to proceed?")

                if Task8res == 1:
                    messagebox.showinfo("Everything Incremental Alpha - Eighth Task", "Task 8. \nGet Tier 8. \nUnlockable at Chapter A-8. \nRewards - New reset layer : Sacrifice!")

                elif Task8res == 0:
                    messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")

            
            def Task9():
                Task9res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to see this Task information after watching Chapter A-9. \nDo you want to proceed?")

                if Task9res == 1:
                    messagebox.showinfo("Everything Incremental Alpha - Ninth Task", "Task 9. \nGet Tier 10. \nUnlockable at Chapter A-9. \nRewards - New static reset : Hyper Tier!")

                elif Task9res == 0:
                    messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")


            def Task10():
                Task10res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to see this Task information after watching Chapter A-h. \nDo you want to proceed?")

                if Task10res == 1:
                    messagebox.showinfo("Everything Incremental Alpha - Tenth Task", "Task 10. \nGet Hyper Tier 1, Reach Tier 10 Again. \nUnlockable at Chapter A-h. \nRewards - New reset layer : Reincarnations!")

                elif Task10res == 0:
                    messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")

            
            def Task11():
                Task11res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to see this Task information after watching Chapter A-10. \nDo you want to proceed?")

                if Task11res == 1:
                    messagebox.showinfo("Everything Incremental Alpha - Eleventh Task", "Task 11. \nGet Tier 12. \nUnlockable at Chapter A-10. \nRewards - New reset layer : Matter!")

                elif Task11res == 0:
                    messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")


            def Task12():
                Task12res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to see this Task information after watching Chapter A-11. \nDo you want to proceed?")

                if Task12res == 1:
                    messagebox.showinfo("Everything Incremental Alpha - Twelvth Task", "Task 12. \nGet Tier 15. \nUnlockable at Chapter A-11. \nRewards - New reset layer : Dark Matter!")

                elif Task12res == 0:
                    messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")

                
            def Task13():
                Task13res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to see this Task information after watching Chapter A-12. \nDo you want to proceed?")
                if Task13res == 1:
                    messagebox.showinfo("Everything Incremental Alpha - Thirteenth Task", "Task 13. \nGet Tier 18. \nUnlockable at Chapter A-12. \nRewards - New sector : Sector 2!")

                elif Task13res == 0:
                    messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")

                    
            def S2Task():
                Sector2Task = Tk()
                
                Sector2Task.title("Everything Incremental Alpha - Sector 2 Tasks")
                Sector2Task.geometry("300x300")
                Sector2Task.resizable(width=True,height=True)

                def Task14():
                    Task14res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to see this Task information after watching Chapter B-0. \nDo you want to proceed?")
                    
                    if Task14res == 1:
                        messagebox.showinfo("Everything Incremental Alpha - Fourteenth Task", "Task 14. \nGet 100 Grass, Get Tier 19. \nUnlockable at Chapter B-0. \nRewards - New static reset : Grass Hop!")

                    elif Task14res == 0:
                        messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")

                
                def Task15():
                    Task15res = messagebox.askyesno("Everything Incremental Alpha - Confirmation", "It is recommended to see this Task information after watching Chapter B-1. \nDo you want to proceed?")

                    if Task15res == 1:
                        messagebox.showinfo("Everything Incremental Alpha - Fifteenth Task", "Task 15. \nGet Grasshop 1, Get Tier 20. \nUnlockable at Chapter B-1. \nRewards - Hyper Tier 2!")

                    elif Task15res == 0:
                        messagebox.showinfo("Everything Incremental Alpha - Cancelled", "This action is cancelled.")

                
                Task14Btn=Button(Sector2Task, text = "Fourteenth Task", background = 'lime', command=Task14)
                Task15Btn=Button(Sector2Task, text = "Fifteenth Task", background = 'light grey', command=Task15)

                Task14Btn.pack()
                Task15Btn.pack()

                Sector2Task.mainloop()

            
            Task1Btn=Button(EITaskQuest, text = "First Task", background = 'yellow', command=Task1)
            Task2Btn=Button(EITaskQuest, text = "Second Task", background = 'light grey', command=Task2)
            Task3Btn=Button(EITaskQuest, text = "Third Task", background = 'light blue', command=Task3)
            Task4Btn=Button(EITaskQuest, text = "Fourth Task", background = 'blue', command=Task4)
            Task5Btn=Button(EITaskQuest, text = "Fifth Task", command=Task5)
            Task6Btn=Button(EITaskQuest, text = "Sixth Task", background = 'green', command=Task6)
            Task7Btn=Button(EITaskQuest, text = "Seventh Task", background = 'orange', command=Task7)
            Task8Btn=Button(EITaskQuest, text = "Eighth Task", background = 'red', command=Task8)
            Task9Btn=Button(EITaskQuest, text = "Ninth Task", background = 'dark blue', command=Task9)
            Task10Btn=Button(EITaskQuest, text = "Tenth Task", background = 'grey', command=Task10)
            Task11Btn=Button(EITaskQuest, text = "Eleventh Task", background = 'purple', command=Task11)
            Task12Btn=Button(EITaskQuest, text = "Twelvth Task", background = 'dark grey', command=Task12)
            Task13Btn=Button(EITaskQuest, text = "Thirteenth Task", background = 'black', command=Task13)
            S2Tasks=Button(EITaskQuest, text = "Sector 2 Tasks", background = 'lime', command=S2Task)

            Task1Btn.pack()
            Task2Btn.pack()
            Task3Btn.pack()
            Task4Btn.pack()
            Task5Btn.pack()
            Task6Btn.pack()
            Task7Btn.pack()
            Task8Btn.pack()
            Task9Btn.pack()
            Task10Btn.pack()
            Task11Btn.pack()
            Task12Btn.pack()
            Task13Btn.pack()
            S2Tasks.pack()

            EITaskQuest.mainloop()

        
        DevStories=Button(EIStory, text = "Developer's Story", background = 'yellow', command=DevStory)
        GameStories=Button(EIStory, text = "Main Game Story", background = 'purple', command=GameStory)
        TasksQuests=Button(EIStory, text = "Tasks & Quests", background = 'lime', command=TaskQuest)

        DevStories.pack()
        GameStories.pack()
        TasksQuests.pack()

        EIStory.mainloop()

    Tutorials=Button(EITuStTaQutab, text = 'Tutorial', background = 'lime', command=Tutorial)
    Stories=Button(EITuStTaQutab, text = '★Stories★', background = 'yellow', command=Story)

    Tutorials.pack()
    Stories.pack()

    EITuStTaQutab.mainloop()

########################################################################################################

def OriginGameInfo():
    messagebox.showinfo("Everything Incremental Alpha - Original Games List", "Original Games List \n1. Grass Cutting Incremental \n2. Really Grass Cutting Incremental \n3. Distance Incremental \n4. Antimatter Dimensions \n5. AD mods (NG+++, NG++++, NG-, NG-5, NG UD' etc) \n6. Merging Legends \n7. Circle Incremental \n8. Infinite Rarities \n9. Eternal Rarities 1 \n10. Eternal Rarities 2 \n11. Incremental Mass Rewritten \n12. Synergism \n13. Prestreestuck \n14. Prestige Tree \n15. ThetaCore Incremental \n16. Check Back Mod \n17. The Milestone Tree NG+ \n18. The Plant Tree \n19. The Tree Of Life \n20. The Operator Tree \n21. Le Underrated Forest \n22. APTMWYMTNWMMTTWATIEATASIJAPM (Another Prestige Tree Mod Where You Merge Things, Now With Much More Time To Waste! Also, There Isn’t Even A Tree Anymore So It’s Just A Prestige Mod) \nAnd more and more Incremental games unknown...")

########################################################################################################

Stats=Button(MainContentFrame, text = 'Stats', background = 'green', command=Stattab)
Cores=Button(MainContentFrame, text = 'Cores', background = 'yellow', command=Coretab)
Milestones=Button(MainContentFrame, text = 'Milestones', background = 'yellow', command=Milestonetab)
Challenges=Button(MainContentFrame, text = 'Challenges', background = 'blue', command=Challengetab)
Lab=Button(MainContentFrame, text = 'The Lab', background = 'light blue', command=Labtab)
Eras=Button(MainContentFrame, text = 'Eras', command=Erastab)
Dimensions=Button(MainContentFrame, text = 'Dimensions?!', background = 'purple', command=Dimensiontab)
TheHill=Button(MainContentFrame, text = 'The Hill', background = 'lime', command=TheHilltab)
TheFormula=Button(MainContentFrame, text = 'The Formula', command=TheFormulatab)
Informations=Button(InfoSettingsFrame, text = 'Informations', background = 'grey', command=Informationtab)
Settings=Button(InfoSettingsFrame, text = 'Settings', background = 'dark grey', command=Settingtab)
TuStTaQu=Button(MainContentFrame, text = 'Tutorials & Stories & Tasks & Quests', background = 'pink', command=TuStTaQutab)
OriginGame=Button(InfoSettingsFrame, text = 'Original Games List', background = 'light blue', command=OriginGameInfo)

Stats.pack()
Cores.pack()
Milestones.pack()
Challenges.pack()
Lab.pack()
Eras.pack()
Dimensions.pack()
TheHill.pack()
TheFormula.pack()
Informations.pack()
Settings.pack()
TuStTaQu.pack()
OriginGame.pack()

########################################################################################################

MainContentFrame.pack(side='left', fill='both', expand=True)
InfoSettingsFrame.pack(side='right', fill='both', expand=True)

########################################################################################################

EI.mainloop()

########################################################################################################
