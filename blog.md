---
layout: page
title: Blog
permalink: /blog/
---

<div class="home">
    <h2><i class="fa fa-pencil"></i> Posts</h2>

  <ul class="posts">
    {% for post in site.posts %}
      <li>
        <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
        <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
      </li>
    {% endfor %}
  </ul>

  <p class="rss-subscribe"><i class="fa fa-rss"></i> subscribe <a href="{{ "/feed.xml" | prepend: site.baseurl }}">via RSS</a></p>


### <a class="page-link" href="/">Go Back!</a>

</div>
