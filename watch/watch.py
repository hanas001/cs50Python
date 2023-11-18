import re
import sys


def main():
    # print(parse(input("HTML: ")))
    s = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    s = '<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>'
    # s = '<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'
    print(parse(s))

def parse(s):
    try:
        video_id = re.search(r'(?<=embed\/)[\w-]+(?=")', s).group()
        video_link = 'https://youtu.be/' + video_id
        return video_link
    except AttributeError:
        return None


if __name__ == "__main__":
    main()