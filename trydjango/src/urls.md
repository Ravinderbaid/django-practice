Url ways to write-

<a href='/posts/{{ obj.pk }}/'>{{ obj.title}}</a><br>
<a href='{% url "detail" id=obj.pk %}'>{{ obj.title}}</a><br>