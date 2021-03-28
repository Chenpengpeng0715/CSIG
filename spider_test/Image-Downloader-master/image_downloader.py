# -*- coding: utf-8 -*-

from __future__ import print_function

import argparse

import crawler
import downloader
import sys
import hashlib

def main(argv):
    parser = argparse.ArgumentParser(description="Image Downloader")
    #parser.add_argument("keywords", type=str,
    #                    help='Keywords to search. ("in quotes")')
    parser.add_argument("--engine", "-e", type=str, default="Google",
                        help="Image search engine.", choices=["Google", "Bing", "Baidu"])
    parser.add_argument("--max-number", "-n", type=int, default=50000,
                        help="Max number of images download for the keywords.")
    parser.add_argument("--num-threads", "-j", type=int, default=16,
                        help="Number of threads to concurrently download images.")
    parser.add_argument("--timeout", "-t", type=int, default=20,
                        help="Seconds to timeout when download an image.")
    parser.add_argument("--output", "-o", type=str, default="./download_images",
                        help="Output directory to save downloaded images.")
    parser.add_argument("--safe-mode", "-S", action="store_true", default=True,
                        help="Turn on safe search mode. (Only effective in Google)")
    parser.add_argument("--face-only", "-F", action="store_true", default=False,
                        help="Only search for ")
    parser.add_argument("--proxy_http", "-ph", type=str, default='web-proxy.tencent.com:8080',
                        help="Set http proxy (e.g. 192.168.0.2:8080)")
    parser.add_argument("--proxy_socks5", "-ps", type=str, default=None,
                        help="Set socks5 proxy (e.g. 192.168.0.2:1080)")

    args = parser.parse_args(args=argv)

    proxy_type = None
    proxy = None
    if args.proxy_http is not None:
        proxy_type = "http"
        proxy = args.proxy_http
    elif args.proxy_socks5 is not None:
        proxy_type = "socks5"
        proxy = args.proxy_socks5
    for _keywords in ['阅兵', '国庆大阅兵', '天安门阅兵', '队伍', '美国阅兵', '俄罗斯阅兵', '军队', '英国阅兵', '德国阅兵', '法国阅兵', '日本阅兵', '中国阅兵', '伊拉克阅兵']:
    #for _keywords in ['阅兵', '国庆大阅兵', '天安门阅兵', '队伍', '美国阅兵', '俄罗斯阅兵', '军队', '英国阅兵', '德国阅兵', '法国阅兵', '日本阅兵', '中国阅兵', '伊拉克阅兵']:

        for _engine in ["Google", "Bing", "Baidu"]:
            crawled_urls = crawler.crawl_image_urls(_keywords,
                                                    engine=_engine, max_number=args.max_number,
                                                    face_only=args.face_only, safe_mode=args.safe_mode,
                                                    proxy_type=proxy_type, proxy=proxy)
            downloader.download_images(image_urls=crawled_urls, dst_dir=args.output,
                                       concurrency=args.num_threads, timeout=args.timeout,
                                       proxy_type=proxy_type, proxy=proxy,
                                       file_prefix=_engine + '_' + hashlib.md5(_keywords.encode()).hexdigest())

    print("Finished.")

if __name__ == '__main__':
    main(sys.argv[1:])
