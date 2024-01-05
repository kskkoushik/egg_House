import flask
import pymongo
from flask import Flask
from pymongo import MongoClient

mongo_url = "mongodb+srv://radhakrishn1811:radhekrishna@cluster0.knjvanw.mongodb.net/?retryWrites=true&w=majority"



member= MongoClient(mongo_url)

db = member['member_stats']

name = db['name']

def value_pred(type):
   if type == 'bo' :
      return 50
   elif type == 'boc' :
     return 60
   else :
     return 80


def take_tokens(taker_name , take_count , type):
   mem = name.find_one({'name' : taker_name})

   if mem is None:
     name.insert_one({'name' : taker_name , 'tokens' : 0 , 'bo' : 0 , 'boc' : 0 , 'boch' : 0 , 'chiegg' : 0 , 'sold' : 0 , 'sold_val' : 0 , 'hold_val' : 0})
     temp = name.find_one({'name' : taker_name})
     count = temp[type]
     count += take_count
     val = temp['hold_val']
     val = val + take_count*value_pred(type)
     name.update_one({'name' : taker_name} , {'$set' :{type : count}})
     name.update_one({'name' : taker_name} , {'$set' :{'value' : val }})
   else :
      temp = name.find_one({'name' : taker_name})
      count = temp[type]
      count += take_count
      val = temp['hold_val']
      val = val + take_count*value_pred(type)
      name.update_one({'name' : taker_name} , {'$set' :{type : count}})
      name.update_one({'name' : taker_name} , {'$set' :{'hold_val' : val }})
     

def sold_tokens(seller_name , type , sell_count):
   mem = name.find_one({'name' : seller_name})

   if mem is None:
      name.insert_one({'name' : seller_name , 'tokens' : 0 , 'bo' : 0 , 'boc' : 0 , 'boch' : 0 , 'chiegg' : 0 , 'sold' : 0 , 'sold_val' : 0 , 'hold_val' : 0})
      temp = name.find_one({'name' : seller_name})
      count = mem[type]
      count = count + sell_count
      sol_count = mem['sold'] + sell_count
      val = mem['hold_val'] - (value_pred(mem[type])*sell_count)
      sval = mem['sold_val'] + (value_pred(mem[type])*sell_count)
      if mem[type] > 0 : 
        name.update_one({'name' : seller_name} , {'$set' :{type : count}})  
      name.update_one({'name' : seller_name} , {'$set' :{'sold' : sol_count}})
      name.update_one({'name' : seller_name} , {'$set' :{'sold_val' : sval}})
     
      
   else :
     temp = mem
     count = mem[type]
     count = count + sell_count
     sol_count = mem['sold'] + sell_count
     val = mem['hold_val'] - (value_pred(mem[type])*sell_count)
     sval = mem['sold_val'] + (value_pred(mem[type])*sell_count)
     if mem[type] > 0 : 
       name.update_one({'name' : seller_name} , {'$set' :{type : count}})  
     name.update_one({'name' : seller_name} , {'$set' :{'sold' : sol_count}})
     name.update_one({'name' : seller_name} , {'$set' :{'sold_val' : sval}})
     
     

def data(find_name):
   return name.find_one({'name' : find_name})

def get_all_data():

  return name.find()


