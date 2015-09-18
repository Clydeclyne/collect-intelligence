'''
Created on 2015-6-12

@author: XXYF18
'''
from recommendations import critics,sim_distance,sim_pearson,topMatches,getRecommendations
#critics['Lisa Rose']['Lady in the Water']
#
#critics['Toby']['Snakes on a Plane']=4.5
#critics['Toby']
import pydelicious
pydelicious.get_popular(tag='programming')
print sim_distance(critics, 'Lisa Rose','Gene Seymour')

print sim_pearson(critics,'Lisa Rose','Gene Seymour')

print topMatches(critics,'Toby',n=3)
print getRecommendations(critics,'Toby')
print getRecommendations(critics,'Toby', similarity=sim_distance)