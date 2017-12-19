def singleton(aClass):            # on @ decoration
    def onCall(*args, **kargs):   # on instance creation
        if onCall.instance == None:
            onCall.instance = aClass(*args, **kargs)
        return onCall.instance
    onCall.instance = None
    return onCall