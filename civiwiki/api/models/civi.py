from __future__ import unicode_literals
from django.db import models
from hashtag import Hashtag

# Create your models here.
class Civi(models.Model):
    '''
    This is the model schema for the primary object in
    the application. Hold an id field and does not hold
    references to other objects. Maybe not the fastest
    implementation but it simplifies things such as searching.
    '''
    objects = models.Manager()
    author = models.ForeignKey('Account', default=None, null=True)
    article = models.ForeignKey('Article', default=None, null=True)
    hashtags = models.ManyToManyField(Hashtag)

    title = models.CharField(max_length=63, default='')
    body = models.TextField(max_length=4095)

    votes_negative2 = models.IntegerField(default=0, null=True)
    votes_negative1 = models.IntegerField(default=0, null=True)
    votes_neutral = models.IntegerField(default=0, null=True)
    votes_positive1 = models.IntegerField(default=0, null=True)
    votes_positive2 = models.IntegerField(default=0, null=True)

    visits = models.IntegerField(default=0, null=True)
    type = models.CharField(max_length=2, default='I')#Possible values of I, C, or S for
    #issue, cause, and solution
    REFERENCE = models.ForeignKey('Civi', related_name='REFERENCE_REL', default='', null=True)
    AT = models.ForeignKey('Civi', related_name='AT_REL', default='', null=True)
    AND_NEGATIVE = models.ForeignKey('Civi', related_name='AND_NEGATIVE_REL', default='', null=True)
    AND_POSITIVE = models.ForeignKey('Civi', related_name='AND_POSITIVE_REL', default='', null=True)

    def string(self):
        result = {
            "title": self.title,
            "body": self.body,
            "author": self.author.username,
            "visits": self.visits,
            "article": self.article.topic,
            "type": self.type,
            "id": self.id,
            "REF": self.REFERENCE_id,
            "AT": self.AT_id,
            "AND_NEGATIVE": self.AND_NEGATIVE_id,
            "AND_POSITIVE": self.AND_POSITIVE_id
	    }
        return result

    NEG2_WEIGHT = 2
    NEG1_WEIGHT = 1
    NEUTRAL_WEIGHT = 0
    POS1_WEIGHT = 1
    POS2_WEIGHT = 2
    SCALE_POLARITY = 2

    RANK_CUTOFF = -1

    def calcPolarity(self):
        '''
        :param civi: Calculates polarity of the inputted civi
        :return: polarity score
        '''
        score = self.votes_negative2 * self.NEG2_WEIGHT + self.votes_negative1 * self.NEG1_WEIGHT
        score += self.votes_positive1 * self.POS1_WEIGHT + self.votes_positive2 * self.POS2_WEIGHT
        score /= self.visits*1.0
        score /= self.SCALE_POLARITY #Scaling polarity so it is a value between 0 and 1 rather than 0 and 2
        return score


    def aveVote(self):
        '''
        Returns average vote of civi
        :param civi:
        :return:
        '''
        ave = self.votes_negative1 + self.votes_negative2 + self.votes_positive2 + self.votes_positive1
        ave /= self.visits
        return ave

    # def topNCivis(civis, N):
    #     '''
    #     Returns the top ranked N civis that are passed in
    #     :param civis:
    #     :return:
    #     '''
    #     # averages=aveVotes(civis)
    #     # for thing in averages:
    #     # 	if thing[ave] < -1.0:

    def rank(self):
        '''
        Ranks civis on a 0 to 1 scale based on polarity score,
        sets rank of civis with average votes to 0 (not polar)
        :return:
        '''
        result = self.calcPolarity()
        if self.aveVote() <= self.RANK_CUTOFF:
            result = 0.0
        return result
