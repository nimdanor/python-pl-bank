    {% for type,num,text in feedback.tests %}
        {%  if type=="failure" %}#  Test {{ num }} échec <p style="background-color: Tomato;">{{text}}</p>
        {% endif %}
        {% if type=="success" %}# Test {{ num }} success <p style="background-color: lightgreen;">{{text}}</p>
        {%  endif %}
        {% if type=="error" %}#  Test {{ num }} Error Failure <p style="background-color: Tomato;">{{text}}</p>
        {%  endif %}
    {% endfor %}


