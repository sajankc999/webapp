from django.dispatch import receiver
from django.db.models.signals import post_save,pre_delete
from .models import *


@receiver([post_save],sender=Interaction)
def update_count(sender,instance,*args, **kwargs):
    # raise Exception(instance)
    interaction = Interaction.objects.filter(id = instance.pk).first()
    post = Post.objects.filter(id=interaction.post.pk).first()
    if interaction.has_commented :
        if not len(interaction.comment)==0:
            print(len(interaction.comment))
            
            post.comment_count+=1
            post.save()
        else:
            interaction.has_commented=False
            # post.comment_count-=1
            interaction.save()
            # post.save()
    if interaction.has_liked:
        post.like_count+=1
        post.save()

    # if instance.has_liked:
@receiver(pre_delete,sender=Interaction)
def count(sender,instance,*args, **kwargs):
    print(instance.pk)
    interaction = Interaction.objects.filter(id = instance.pk).first()
    # raise Exception(interaction)
    post = Post.objects.filter(id=interaction.post.pk).first()
    if instance.has_liked :
        post.like_count-=1
        post.save()
    if instance.has_commented:
        post.comment_count-=1
        post.save()
    