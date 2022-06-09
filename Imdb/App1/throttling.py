from rest_framework.throttling import UserRateThrottle

class ReviewListThrottle(UserRateThrottle):
    scope = 'review-list'

class WatchListThrottle(UserRateThrottle):
    scope = 'watch-list'
       