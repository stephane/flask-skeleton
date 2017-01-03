from flask import Response

class ContainsResponse(Response):

    def __contains__(a, b):
        return b in a.data.decode('utf-8')
