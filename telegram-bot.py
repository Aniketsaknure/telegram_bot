import telebot
bot = telebot.TeleBot('7297689164:AAFeTXfL49luNlnFPTOOgcGspYdPex1fO7M')
from telebot import types
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram.ext
from dotenv import load_dotenv
import os
load_dotenv()
token = os.getenv("token")

def start(update,context):
    update.message.reply_text(
            """
             Welcome to STUDYSAGE
            /SEM3 , /SEM4 , /SEM5
             /SEM5 , /SEM6, /sem7
             /SEM8
             /placementpreparation
            
            """
    )
def SEM3(update,context):
        update.message.reply_text(
                
                """
           /ElectronicCircuits
           /ElectricalCircuits
           /DigitalCircuits
           /DataStructure
           /EngineeringMathematicsIII   
           
                
                 
                """   
                              )
def placementpreparation(update,context):
        update.message.reply_text("aptitude preparation :https://drive.google.com/drive/folders/1u6TsWsA3GYJSkq2aFecV16Ny1tZa076v?usp=drive_link ")
        # context.bot.sendDocument(update.effective_chat.id,document = open ('ElectronicCircuits.pdf','rb'))
def ElectronicCircuits(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('ElectronicCircuits.pdf','rb'))

def ElectricalCircuits(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('ElecttricCircuits.pdf','rb'))
def DigitalCircuits(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('DC_decode.pdf','rb'))
def DataStructure(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Data_Structures.pdf','rb'))
def EngineeringMathematicsIII(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('M3_deocde.pdf','rb'))
def SEM4(update,context):
        update.message.reply_text(
                
                """
           /SignalSystems
           /ControlSystem
           /PrincipleofCommumicationSystem
           /ObjectOrientedProgramming
             
                
                
                """   
                              )
def SignalSystems(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('SS_decode.pdf','rb'))
def ControlSystem(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('control_system.pdf','rb'))
def PrincipleofCommumicationSystem(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('PCS_Decode.pdf','rb'))
def ObjectOrientedProgramming(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('oop_decode.pdf','rb'))
def SEM5(update,context):
        update.message.reply_text(
                
                """
           /DigitalCommunication
           /ElectomagneticFieldTheory
           /DatabaseManagement
           /Microcontroller
           /FundamentalaofJavaProgramming
           /ComputerNetworks
             
                
                
                """   
                              )
def DigitalCommunication(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Digital_communication.pdf','rb'))
def ElectomagneticFieldTheory(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('EFTdecode.pdf','rb'))
def DatabaseManagement(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Dbmsdecode.pdf','rb'))
def Microcontroller(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('microcontroller_decode.pdf','rb'))
def FundamentalaofJavaProgramming(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('FundamentalsofJAVAProgramming (2).pdf','rb'))
def ComputerNetworks(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Computernetwork.pdf','rb'))
def SEM6(update,context):
        update.message.reply_text(
                
                """
           /CellularNetworks
           /ProjectManagement
           /PowerDevicesCircuits
           /AdvancedJavaProgramming
           
           
             
                
                
                """   
                              )
def CellularNetworks(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('CN_Decode.pdf','rb'))
def ProjectManagement(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('PM decode.pdf','rb'))
def PowerDevicesCircuits(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('','rb'))
def AdvancedJavaProgramming(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('AJP.pdf','rb'))

def SEM7(update,context):
        update.message.reply_text(
                
                """
        /RadiationandMicrowaveTheory
        /VLSI
        /CloudComputing
        /JavaScript
        /IOT
        /DeepLearning
        /DataMining
           
           
             
                
                
                """   
                              )
def RadiationandMicrowaveTheory(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('RMT-1-2 notes (1).pdf','rb'))
def VLSI(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('VLSI Design & technology.pdf','rb'))
def CloudComputing(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Cloud_Computing.pdf','rb'))
def JavaScript(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('JS_Tech-Neo.pdf','rb'))
def DeepLearning(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Deep learning 1&2 unit (1).pdf','rb'))
def DataMining(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Aptitude Preparation Sheet.pdf','rb'))

updater = telegram.ext.Updater(token,use_context = True)
dispatch = updater.dispatcher


def content(update,context):
       
          
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Aptitude Preparation Sheet.pdf','rb'))
# def sharayu(update,context):
# update.message.reply_text("Ay Pankomb shamdhii Rusubai  ")
def SEM8 (update,context):
        update.message.reply_text(
                
                """
           /FiberOpticCommunication
           /MobileComputing
           /DigitalMarketing
           
             
                
                
                """   
               )
def FiberOpticCommunication(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('FOC Unit 1,2.pdf','rb'))
def MobileComputing(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('mobile computing unit 1.pdf','rb'))
        context.bot.sendDocument(update.effective_chat.id,document = open ('mobile computing unit 2.pdf','rb'))
def DigitalMarketing(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Digital marketing unit1.pdf','rb'))

        
        

  

dispatch.add_handler(telegram.ext.CommandHandler('start',start)) 
dispatch.add_handler(telegram.ext.CommandHandler('shamdhi',"shamdhi"))      
dispatch.add_handler(telegram.ext.CommandHandler('content',content))
dispatch.add_handler(telegram.ext.CommandHandler('SEM3',SEM3))
dispatch.add_handler(telegram.ext.CommandHandler('ElectronicCircuits',ElectronicCircuits))
dispatch.add_handler(telegram.ext.CommandHandler('ElectricalCircuits',ElectricalCircuits))
dispatch.add_handler(telegram.ext.CommandHandler('DigitalCircuits',DigitalCircuits))
dispatch.add_handler(telegram.ext.CommandHandler('DataStructure',DataStructure))
dispatch.add_handler(telegram.ext.CommandHandler('EngineeringMathematicsIII',EngineeringMathematicsIII))
dispatch.add_handler(telegram.ext.CommandHandler('SEM4',SEM4))
dispatch.add_handler(telegram.ext.CommandHandler('SignalSystems',SignalSystems))
dispatch.add_handler(telegram.ext.CommandHandler('ControlSystem',ControlSystem))
dispatch.add_handler(telegram.ext.CommandHandler('PrincipleofCommumicationSystem',PrincipleofCommumicationSystem))
dispatch.add_handler(telegram.ext.CommandHandler('ObjectOrientedProgramming',ObjectOrientedProgramming))
dispatch.add_handler(telegram.ext.CommandHandler('SEM5',SEM5))
dispatch.add_handler(telegram.ext.CommandHandler('DigitalCommunication',DigitalCommunication))
dispatch.add_handler(telegram.ext.CommandHandler('ElectomagneticFieldTheory',ElectomagneticFieldTheory))
dispatch.add_handler(telegram.ext.CommandHandler('DatabaseManagement',DatabaseManagement))
dispatch.add_handler(telegram.ext.CommandHandler('Microcontroller',Microcontroller))
dispatch.add_handler(telegram.ext.CommandHandler('FundamentalaofJavaProgramming',FundamentalaofJavaProgramming))
dispatch.add_handler(telegram.ext.CommandHandler('ComputerNetworks',ComputerNetworks))
dispatch.add_handler(telegram.ext.CommandHandler('SEM6',SEM6))
dispatch.add_handler(telegram.ext.CommandHandler('CellularNetworks',CellularNetworks))
dispatch.add_handler(telegram.ext.CommandHandler('ProjectManagement',ProjectManagement))
dispatch.add_handler(telegram.ext.CommandHandler('PowerDevicesCircuits',PowerDevicesCircuits))
dispatch.add_handler(telegram.ext.CommandHandler('AdvancedJavaProgramming',AdvancedJavaProgramming))
dispatch.add_handler(telegram.ext.CommandHandler('SEM7',SEM7))
dispatch.add_handler(telegram.ext.CommandHandler('RadiationandMicrowaveTheory',RadiationandMicrowaveTheory))
dispatch.add_handler(telegram.ext.CommandHandler('VLSI',VLSI))
dispatch.add_handler(telegram.ext.CommandHandler('CloudComputing',CloudComputing))
dispatch.add_handler(telegram.ext.CommandHandler('JavaScript',JavaScript))
dispatch.add_handler(telegram.ext.CommandHandler('DeepLearning',DeepLearning))
dispatch.add_handler(telegram.ext.CommandHandler('SEM8',SEM8))
dispatch.add_handler(telegram.ext.CommandHandler('FiberOpticCommunication',FiberOpticCommunication))
dispatch.add_handler(telegram.ext.CommandHandler('MobileComputing',MobileComputing))
dispatch.add_handler(telegram.ext.CommandHandler('DigitalMarketing',DigitalMarketing))



    
updater.start_polling()
updater.idle()

