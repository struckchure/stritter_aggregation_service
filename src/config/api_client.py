import typing

import requests


class APIClient:

    base_url: str | None = None

    def __init__(self, base_url: str | None = None) -> None:
        if base_url:
            self.base_url = base_url

    @staticmethod
    def join_url(*urls: str | None) -> str:
        _urls: list[str] = []

        for url in urls:
            if url is not None:
                if url.startswith("/"):
                    url = url[1:]
                if url.endswith("/"):
                    url = url[:-1]
                _urls.append(url)

        return "/".join(_urls) + "/"

    def send_req(
        self,
        method: str,
        url: str,
        *args: list[typing.Any],
        **kwargs: dict[str, typing.Any]
    ) -> requests.Response:
        try:
            return requests.request(
                method=method,
                url=APIClient.join_url(self.base_url, url),
                *args,
                **kwargs
            )
        except Exception as e:
            raise Exception(str(e))

    def get(
        self, url, *args: list[typing.Any], **kwargs: dict[str, typing.Any] | typing.Any
    ) -> requests.Response:
        return self.send_req("get", url=url, *args, **kwargs)

    def post(
        self, url, *args: list[typing.Any], **kwargs: dict[str, typing.Any] | typing.Any
    ) -> requests.Response:
        return self.send_req("post", url=url, *args, **kwargs)

    def put(
        self, url, *args: list[typing.Any], **kwargs: dict[str, typing.Any] | typing.Any
    ) -> requests.Response:
        return self.send_req("put", url=url, *args, **kwargs)

    def patch(
        self, url, *args: list[typing.Any], **kwargs: dict[str, typing.Any] | typing.Any
    ) -> requests.Response:
        return self.send_req("patch", url=url, *args, **kwargs)

    def delete(
        self, url, *args: list[typing.Any], **kwargs: dict[str, typing.Any] | typing.Any
    ) -> requests.Response:
        return self.send_req("delete", url=url, *args, **kwargs)
