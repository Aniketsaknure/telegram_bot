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
def ElectronicCircuits(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Books\ElectronicCircuits.pdf','rb'))

def ElectricalCircuits(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Books\ElecttricCircuits.pdf','rb'))
def DigitalCircuits(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Books\DC_decode.pdf','rb'))
def DataStructure(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Books\Data_Structures.pdf','rb'))
def EngineeringMathematicsIII(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Books\M3_deocde.pdf','rb'))
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
        context.bot.sendDocument(update.effective_chat.id,document = open ('Books\SS_decode.pdf','rb'))
def ControlSystem(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Books\control_system.pdf','rb'))
def PrincipleofCommumicationSystem(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Books\PCS_Decode.pdf','rb'))
def ObjectOrientedProgramming(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Books\oop_decode.pdf','rb'))
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
        context.bot.sendDocument(update.effective_chat.id,document = open ('Books\Digital_communication.pdf','rb'))
def ElectomagneticFieldTheory(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Books\EFTdecode .pdf','rb'))
def DatabaseManagement(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Books\Dbmsdecode.pdf','rb'))
def Microcontroller(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Books\microcontroller_decode.pdf','rb'))
def FundamentalaofJavaProgramming(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Books\FundamentalsofJAVAProgramming (2).pdf','rb'))
def ComputerNetworks(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Books\Computer_network-1.pdf','rb'))
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
        context.bot.sendDocument(update.effective_chat.id,document = open ('Books\CN_Decode.pdf','rb'))
def ProjectManagement(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Books\PM decode.pdf','rb'))
def PowerDevicesCircuits(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('','rb'))
def AdvancedJavaProgramming(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Books\AJP.pdf','rb'))

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
        context.bot.sendDocument(update.effective_chat.id,document = open ('Books\RMT-1-2 notes (1).pdf','rb'))
def VLSI(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Books\Books\VLSI Design & technology.pdf','rb'))
def CloudComputing(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Books\Cloud_Computing.pdf','rb'))
def JavaScript(update,context):
        update.message.reply_text("Downloading...")
        context.bot.sendDocument(update.effective_chat.id,document = open ('Books\JS_Tech-Neo','rb'))
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
        
        

  

dispatch.add_handler(telegram.ext.CommandHandler('start',start))    
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


    
updater.start_polling()
updater.idle()

