import string
import os


class Element:
    data = None;
    Next = None;
    Previous = None;

class LinkedList:
    root = None;

def insertFirst(linkedList, element):
    if(linkedList.root == None):
        linkedList.root = element;
    else:
        element.next = linkedList.root;
        linkedList.root = element;

def insertLast(linkedList, element):
    if(linkedList.root == None):
        linkedList.root = element;
    else:
        courant = linkedList.root;
        while(courant.next != None):
            courant = courant.next;
            courant.next = element;
            
def removeFirst(linkedList):
    if(linkedList.root == None):
        return None;
    else:
        linkedList.root = linkedList.root.next;

def removeLast(linkedList):
    if(linkedList.root == None):
        return None;
    else:
        previous = None;
        courant = linkedList.root
        while(courant.next != None):
            previous = courant;
            courant = courant.next;
        if(previous == None):
            linkedList.root = None;
            courant.next = None;

def compteur(linkedList):
    if(linkedList.root == None):
        compteur=0;
    else:
        courant = linkedList.root
        while(courant.next != None):
            courant = courant.Next;
            compteur += 1;