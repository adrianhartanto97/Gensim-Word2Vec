from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from django.contrib import messages

import gensim
import gzip
import logging
from gensim.models.word2vec import Word2Vec

def hello_world(request):
	# model = Word2Vec.load("C:/Users/User/word2vec/tes/newmodel")
	# w1 = "dirty"
	# result = model.wv.most_similar (positive=w1)

	# context = {
	# 	'content' : 'Hello world !!!',
	# 	'result' : result
	# }
	return render(request, 'index.html')

def submit_model_path(request):
	#path = "C:/Users/User/word2vec/tes/newmodel"
	try:
		path = request.POST['path']
		model = Word2Vec.load(path)
		status = True
		message = "Model Loaded Successfully"
	except Exception as e:
		status = False
		message = str(e)

	result = {
		'status' : status,
		'message' : message
	}

	return JsonResponse(result)

def submit_most_similar(request):
	try:
		path = request.POST['path']
		model = Word2Vec.load(path)

		word = request.POST['word']
		topn = int(request.POST['topn'])

		result = model.wv.most_similar (positive=word, topn = topn)

		status = True
		message = result
	except Exception as e:
		status = False
		message = str(e)

	context = {
		'status' : status,
		'message' : message
	}

	return render(request, 'most_similar.html', context)

def submit_similarity(request):
	try:
		path = request.POST['path']
		model = Word2Vec.load(path)

		word1 = request.POST['word1']
		word2 = request.POST['word2']

		result = model.wv.similarity(w1=word1,w2=word2)

		status = True
		message = result
	except Exception as e:
		status = False
		message = str(e)

	context = {
		'status' : status,
		'message' : message
	}

	return render(request, 'similarity.html', context)

def submit_dmatch(request):
	try:
		path = request.POST['path']
		model = Word2Vec.load(path)

		word_list = request.POST['word_list']
		delim = word_list.split()

		result = model.wv.doesnt_match(delim)

		status = True
		message = result
	except Exception as e:
		status = False
		message = str(e)

	context = {
		'status' : status,
		'message' : message
	}

	return render(request, 'dmatch.html', context)

def submit_analogy(request):
	try:
		path = request.POST['path']
		model = Word2Vec.load(path)

		arg1 = request.POST['arg1']
		arg2 = request.POST['arg2']
		arg3 = request.POST['arg3']
		pos = [arg3, arg2]
		neg = [arg1] 
		# print(pos)
		# print(neg)
		topn = int(request.POST['topn'])

		result = model.wv.most_similar(positive=pos, negative = neg, topn = topn)

		status = True
		message = result
	except Exception as e:
		status = False
		message = str(e)

	context = {
		'status' : status,
		'message' : message
	}

	return render(request, 'most_similar.html', context)

def read_input(input_file):  
    with gzip.open (input_file, 'rb') as f:
        for i, line in enumerate (f): 
            # do some pre-processing and return a list of words for each review text
            yield gensim.utils.simple_preprocess (line)

def submit_training(request):

	try :
		#data_file="C:/Users/User/word2vec/tes/reviews_data.txt.gz"
		dataset_path = request.POST['dataset_path']
		size = int(request.POST['size'])
		window= int(request.POST['window'])
		min_count = int(request.POST['min_count'])
		epoch = int(request.POST['epoch'])
		save_model_path = request.POST['save_model_path']

		#print(dataset_path, size, window, min_count, epoch, save_model_path)
		documents = list (read_input (dataset_path))
		model = gensim.models.Word2Vec (documents, size=size, window=window, min_count=min_count, workers=10)
		model.train(documents,total_examples=len(documents),epochs=epoch)
		model.save(save_model_path)

		messages.add_message(request, messages.SUCCESS, 'Model successfully saved at '+ save_model_path)
	except Exception as e:
		messages.add_message(request, messages.ERROR, str(e))

	return redirect(request.META.get('HTTP_REFERER', '/'))
