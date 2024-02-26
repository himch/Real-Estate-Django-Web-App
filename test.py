import json

x = '"[{\"title\": {\"ru\": \"\u041b\u043e\u0431\u0431\u0438\", \"en\": \"Lobby\", \"ar\": \"\u0631\u062f\u0647\u0629\"}, \"images\": {\"image\": \"https://files.alnair.ae/uploads/2024/1/b4/3d/b43dee63d944dae957bf60f6002e4332.jpg\"}}, {\"title\": {\"ru\": \"\u0418\u043d\u0444\u0440\u0430\u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0430\", \"en\": \"Infrastructure\", \"ar\": \"\u0628\u0646\u064a\u0629 \u062a\u062d\u062a\u064a\u0629\"}, \"images\": {\"image\": [\"https://files.alnair.ae/uploads/2024/1/3a/c0/3ac0468f681bf9f526bf19a494e4702c.jpg\", \"https://files.alnair.ae/uploads/2024/1/3e/29/3e29abea2b55be3fd932bbba7e20e4e4.jpg\", \"https://files.alnair.ae/uploads/2024/1/9d/d9/9dd924cbd7e786b4a2478fbced3a1229.jpg\", \"https://files.alnair.ae/uploads/2024/1/83/b2/83b210ae7864d926b1966b589a089761.jpg\", \"https://files.alnair.ae/uploads/2024/1/36/db/36dbbd357c3271afa0cb7d7f31d32244.jpg\", \"https://files.alnair.ae/uploads/2024/1/40/d7/40d7b7a6a82a3456df8fc16ca5525bce.jpg\"]}}, {\"title\": {\"ru\": \"\u041f\u0440\u0438\u043c\u0435\u0440\u044b \u043e\u0442\u0434\u0435\u043b\u043a\u0438\", \"en\": \"Finishing examples\", \"ar\": \"\u0623\u0645\u062b\u0644\u0629 \u0639\u0644\u0649 \u0627\u0644\u062a\u0634\u0637\u064a\u0628\"}, \"images\": {\"image\": [\"https://files.alnair.ae/uploads/2024/1/f6/7e/f67e526f45e948f4ccc87510e3e9c640.jpg\", \"https://files.alnair.ae/uploads/2024/1/06/e0/06e0c352caaba54bdd15339e4ff8f70c.jpg\", \"https://files.alnair.ae/uploads/2024/1/0b/40/0b4035cf2d185ccfc8b0bcdf6ec3a317.jpg\", \"https://files.alnair.ae/uploads/2024/1/2f/66/2f6698917a7d2d752eb55f49fa8a57ef.jpg\", \"https://files.alnair.ae/uploads/2024/1/33/95/339513dfa41de45a17cb3944725c61e4.jpg\"]}}]"'

albums = json.loads(x)
for album in albums:
    album['title_ru'] = album['title']['ru']
    album['title_en'] = album['title']['en']
    album['title_ar'] = album['title']['ar']
    album.pop('title', None)
    images = album.pop('images', None)
    # new_album = self.albums.create(**album)
    print(type(images['image']))
    for image_url in images['image']:
        print(image_url)
        # new_image = new_album.images.create(photo=None)  # self.save_image_from_url(image)
        # self.save_image_from_url(image_url, new_image.photo)