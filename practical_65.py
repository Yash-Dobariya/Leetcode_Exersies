def isNumber(self, s):
        try:
            i=float(s)
        except Exception:
            return False
        return True
isNumber(1,".")