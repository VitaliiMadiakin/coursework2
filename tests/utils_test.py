import pytest
from utils import get_posts_by_user, get_comments_by_post_id, get_post_by_pk


def test_get_posts_by_user_int():
    assert get_posts_by_user("1") == []


def test_get_posts_by_user_name():
    assert get_posts_by_user("leo") == [{'poster_name': 'leo', 'poster_avatar': 'https://randus.org/avatars/w/c1819dbdffffff18.png', 'pic': 'https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80', 'content': 'Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.', 'views_count': 376, 'likes_count': 154, 'pk': 1}, {'poster_name': 'leo', 'poster_avatar': 'https://randus.org/avatars/w/c1819dbdffffff18.png', 'pic': 'https://images.unsplash.com/photo-1570427968906-5a309bfd7de3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=880&q=80', 'content': 'Пурр-пурр! типичная инстарамная фотка с котом , книжкой и едой. Но не буду скрывать, что это я: а то вдруг у вас кот тоже такой, тогда вы не увидите этого в своих фото. #кот #котики #инста #инстаграм #любовькживотным #любимыйкот ... Как же я люблю этот момент, когда ты понимаешь, что ты ничего толком не умеешь делать и даже не знаешь, что с этим делать.', 'views_count': 287, 'likes_count': 99, 'pk': 5}]


def test_get_posts_by_user_caps_name():
    assert get_posts_by_user("LEO") == [{'poster_name': 'leo', 'poster_avatar': 'https://randus.org/avatars/w/c1819dbdffffff18.png', 'pic': 'https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80', 'content': 'Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.', 'views_count': 376, 'likes_count': 154, 'pk': 1}, {'poster_name': 'leo', 'poster_avatar': 'https://randus.org/avatars/w/c1819dbdffffff18.png', 'pic': 'https://images.unsplash.com/photo-1570427968906-5a309bfd7de3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=880&q=80', 'content': 'Пурр-пурр! типичная инстарамная фотка с котом , книжкой и едой. Но не буду скрывать, что это я: а то вдруг у вас кот тоже такой, тогда вы не увидите этого в своих фото. #кот #котики #инста #инстаграм #любовькживотным #любимыйкот ... Как же я люблю этот момент, когда ты понимаешь, что ты ничего толком не умеешь делать и даже не знаешь, что с этим делать.', 'views_count': 287, 'likes_count': 99, 'pk': 5}]


def test_get_comments_by_post_correct_id():
    assert get_comments_by_post_id("1") == [{'post_id': 1, 'commenter_name': 'hanna', 'comment': 'Очень здорово!', 'pk': 1}, {'post_id': 1, 'commenter_name': 'jlia', 'comment': ':)', 'pk': 2}, {'post_id': 1, 'commenter_name': 'ralf', 'comment': 'Класс!', 'pk': 3}, {'post_id': 1, 'commenter_name': 'leo', 'comment': 'Интересно. А где это?', 'pk': 4}]


def test_get_comments_by_wrong_id_in_post():
    with pytest.raises(ValueError, match="Нет поста с таким ID"):
        get_comments_by_post_id(5555)


def test_get_comments_by_string_id_in_post():
    with pytest.raises(ValueError, match="Вы ввели недопустимое значение"):
        get_comments_by_post_id("abc")


def test_get_post_by_correct_pk():
    assert get_post_by_pk(1) == {'poster_name': 'leo', 'poster_avatar': 'https://randus.org/avatars/w/c1819dbdffffff18.png', 'pic': 'https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80', 'content': 'Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.', 'views_count': 376, 'likes_count': 154, 'pk': 1}


def test_get_post_by_wrong_pk():
    with pytest.raises(ValueError, match="Нет поста с таким ID"):
        get_post_by_pk(5555)


def test_get_post_by_string_pk():
    with pytest.raises(ValueError, match="Вы ввели недопустимое значение"):
        get_post_by_pk("abc")
