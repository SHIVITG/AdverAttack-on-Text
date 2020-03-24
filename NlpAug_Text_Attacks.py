#!/usr/bin/env python
# coding: utf-8

# In[42]:


##------------------------------------------------------------------------------------##
#-----------------------Installing Required Libraries----------------------------------#
##------------------------------------------------------------------------------------##
import nlpaug.augmenter.char as nac
import nlpaug.augmenter.word as naw
import nlpaug.augmenter.sentence as nas
import nlpaug.flow as nafc
from nlpaug.util import Action
import nltk 
#nltk.download('all')


# In[54]:


text = "Product arrived labeled as Jumbo Salted Peanuts...the peanuts were actually small sized unsalted. Not sure if this was an error or if the vendor intended to represent the product as 'Jumbo'."


# In[55]:


text1 = "I have bought several of the Vitality canned dog food products and have found them all to be of good quality. The product looks more like a stew than a processed meat and it smells better."


# ### CHARACTER LEVEL ATTACK

# In[52]:


def char_level(text,n):
    #Augmenting data in character level.
    aug = nac.OcrAug()
    attacked_texts = aug.augment(text, n=n)
    # gives n forms of augmentation (n is the number of augmented forms a user wants)
    print("Attacked Text:")
    print(attacked_texts)


# In[53]:


def keyboard_attack(text):
    #Substitute character by keyboard distance
    aug = nac.KeyboardAug()
    attacked_text = aug.augment(text)
    print("Attacked Text:")
    print(attacked_text)


# In[61]:


def random_char_insert(text):
    # Insert character randomly
    aug = nac.RandomCharAug(action="insert")
    attacked_text = aug.augment(text)
    print("Attacked Text:")
    print(attacked_text)


# In[63]:


def random_char_subsi(text):
    # Substitute character randomly
    aug = nac.RandomCharAug(action="substitute")
    attacked_text = aug.augment(text)
    print("Attacked Text:")
    print(attacked_text)


# In[65]:


def random_char_swap(text):
    #Swap character randomly
    aug = nac.RandomCharAug(action="swap")
    attacked_text = aug.augment(text)
    print("Attacked Text:")
    print(attacked_text)


# In[67]:


def random_char_del(text):
    #Delete character randomly
    aug = nac.RandomCharAug(action="delete")
    attacked_text = aug.augment(text)
    print("Attacked Text:")
    print(attacked_text)


# In[56]:


char_level(text1,1)


# In[58]:


keyboard_attack(text1)


# In[62]:


random_char_insert(text1)


# In[64]:


random_char_subsi(text1)


# In[66]:


random_char_swap(text1)


# In[68]:


random_char_del(text1)


# ### WORD LEVEL ATTACK

# In[69]:


def spell_attack(text,n):
    #Spelling Augmenter
    #Substitute word by spelling mistake words dictionary
    aug = naw.SpellingAug('models/spelling_en.txt')
    attacked_texts = aug.augment(text, n=n)
    print("Attacked Texts:")
    print(attacked_texts)


# In[72]:


def synonym_wordnet(text):
    #Synonym Augmenter
    #Substitute word by WordNet's synonym
    aug = naw.SynonymAug(aug_src='wordnet')
    attacked_text = aug.augment(text)
    print("Attacked Text:")
    print(attacked_text)


# In[74]:


def antonym_subsi(text):
    #Antonym Augmenter
    #Substitute word by antonym
    aug = naw.AntonymAug()
    attacked_text = aug.augment(text)
    print("Attacked Text:")
    print(attacked_text)


# In[76]:


def random_word_swap(text):
    # Random Word Augmenter
    # Swap word randomly
    aug = naw.RandomWordAug(action="swap")
    attacked_text = aug.augment(text)
    print("Attacked Text:")
    print(attacked_text)


# In[78]:


def random_word_del(text):
    #Delete word randomly
    aug = naw.RandomWordAug()
    attacked_text = aug.augment(text)
    print("Attacked Text:")
    print(attacked_text)


# In[80]:


def split_word(text):
    #Split Augmenter
    #Split word to two tokens randomly
    aug = naw.SplitAug()
    attacked_text = aug.augment(text)
    print("Attacked Text:")
    print(attacked_text)


# In[71]:


spell_attack(text1,1)


# In[73]:


synonym_wordnet(text1)


# In[75]:


antonym_subsi(text1)


# In[77]:


random_word_swap(text1)


# In[82]:


split_word(text)


# In[79]:


random_word_del(text1)


# In[ ]:




