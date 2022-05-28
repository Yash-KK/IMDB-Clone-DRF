# IMDB-Clone(In Progress)
This is the backend repository built on Django framework and utilises Django Rest Framework for a REST API.

### Status Codes:
200 : Success

204 : No Content

401 : Unauthorized

404 : Error

### The API Routes:
<ul>
  <li> watch/list/ - Movie List page </li>
  <li> watch/list/id/ - Movie detail page </li> 
  
  <li> watch/stream/ - Streaming Platform  List Page </li>
  <li> watch/stream/id/ - Streaming Platform Detail Page  </li>
  
  <li> stream/<int:pk>/review-create/ - Review Create for a particular Movie  </li>
  <li> stream/<int:pk>/review/ - Review Create for a particular Movie  </li>
  <li> stream/review/<int:pk>/ - Review Detail Page  </li>
</ul>  
