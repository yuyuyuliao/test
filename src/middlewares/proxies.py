class ProxyFilterMiddleware:
    def process_request(self, request, spider):
        if request.meta.get("proxy", ""):
            request.headers["Connection"] = "close"
        return None
