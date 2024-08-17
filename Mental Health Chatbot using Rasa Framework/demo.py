'''
    if request.method == "POST":
    qtc_data = request.get_json()
    print(qtc_data)
 
 results = {'processed': 'true'}
 return jsonify(results)'''
    '''if request.method == 'GET':
                    test = []
                    val = str(request.args.get('text'))
                    print(val)
                    y = val
                    edu = TextBlob ( val )
                    x = edu.sentiment.polarity
                    negative_counter=0
                    neutral_counter=0
                    positive_counter=0
                    # Negative = x < 0 and Neutral = 0 and Positive x > 0 && x < = 1
                    if  x < 0 :
                        negative_counter+=1
                        a=" Negative "
                        test.append(a)
                    elif  x == 0 :
                        neutral_counter+=1
                        a="Neutral "
                        test.append(a)
                    elif  x > 0   :
                        positive_counter+=1
                        a=" Positive "
                        test.append(a)
                    data = json.dumps({"sender": "Rasa","message": val})
                    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
                    res = requests.post('http://localhost:5005/webhooks/rest/webhook', data= data, headers = headers)
                    res = res.json()
                    print(res[0]['text'])
                    val = res[0]['text']
                    print(test)'''
    