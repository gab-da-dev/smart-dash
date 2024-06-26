from enum import Enum


class CollectStatus(str, Enum):
    ASCENDING = "asc"
    DESCENDING = "desc"


class DeliveryStatus(str, Enum):
    ASCENDING = "asc"
    DESCENDING = "desc"


class OrderType(str, Enum):
    DELIVERY = "delivery"
    COLLECT = "collect"

class Rating(int, Enum):
    ONE_STAR = 1
    TWO_STARS = 2
    THREE_STARS = 3
    FOUR_STARS = 4
    FIVE_STARS = 5

class OrderStatus(str, Enum):
    ACCEPTED = "accepted"
    IN_PROGRESS = "collect"
    COMPLETE = "complete"


class DeliveryStatus(str, Enum):
    ON_THE_WAY = "accepted"
    IN_PROGRESS = "collect"
    ARRIVED = "complete"
    dELIVERED = "complete"