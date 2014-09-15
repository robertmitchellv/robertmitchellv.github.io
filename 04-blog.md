---
layout: page
title: Blog
permalink: "/blog/"
---

<div>
    <h2><i class="fa fa-pencil fa-rotate-270"></i> Posts</h2>

  <ul class="posts">
    {% for post in site.posts %}
      <li>
        <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
        <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
      </li>
    {% endfor %}
  </ul>

  <p class="rss-subscribe"><i class="fa fa-rss"></i> subscribe <a href="{{ "/feed.xml" | prepend: site.baseurl }}">via RSS</a></p>
</div>

### <a class="page-link" href="/"><i class="fa fa-arrow-circle-o-left fax2"></i>Go Back!</a>
