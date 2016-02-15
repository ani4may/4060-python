# -*- coding: utf-8 -*-

print	'\nSTSCI	4060	HW1	Name:	Anirudh	Ashok	'	
print'\n               *****Question 1*****\n'

_name = 1
a_name= 1
#2name = 1 #invalid
name2= 1
Name= 1
NAME= 1
__name= 1
__name__= 1
_2name= 1
#$name= 1 # invalid
#%name= 1 #invalid
#–name= 1 #invalid
MyName= 1
print 'Invalid variable names are: \n 2name \n $name \n %name \n #-name' 
print'\n\n               *****Question 2*****\n'
text1='Call me Ishmael.'
text2 ='Some years ago, never mind how long precisely, having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world.'
text= text1+' '+text2
print text
textlength= len(text)
print '\nThe length of the string text is',textlength,'\n'
print 'The first 11 characters of the string text are:',text[:11],'\n'
index=text.find('money')
print 'The index of the string money is:',index,'\n'
length=len('money')
text3=text[0:index-1]+text[index+length:]
print 'text without the word money is:\n\n',text3,'\n'
tnw= len(text.split())
print 'The total number of words in the text are:',tnw,'\n'
print text.count('the')