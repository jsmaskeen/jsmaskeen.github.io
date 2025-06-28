---
layout: default
permalink: /cv/
title: cv
nav: true
nav_order: 5
cv_pdf: cv_j.pdf
description: You can download a PDF of my CV by clicking the button on the right!
---

<style>
  .post {
    display: flex;
    flex-direction: column;
    height: 100vh;
    margin: 0;
  }
  .post-header {
    flex: 0 0 auto;
    padding: 1rem;
  }
  .cv-embed {
    flex: 1 1 auto;
  }
  .cv-embed iframe {
    width: 100%;
    height: 100%;
    border: none;
  }
</style>

<div class="post">
  <header class="post-header">
    <h1 class="post-title">
      {{ page.title }}
      {% if page.cv_pdf %}
        <a
          {% if page.cv_pdf contains '://' %}
            href="{{ page.cv_pdf }}"
          {% else %}
            href="{{ 'assets/pdf/' | append: page.cv_pdf | relative_url }}"
          {% endif %}
          target="_blank"
          rel="noopener noreferrer"
          class="float-right"
        >
          <i class="fa-solid fa-file-pdf"></i>
        </a>
      {% endif %}
    </h1>
    {% if page.description %}
      <p class="post-description">{{ page.description }}</p>
    {% endif %}
  </header>

  <article class="cv-embed">
    {% assign pdf_url = page.cv_pdf %}
    {% unless pdf_url contains '://' %}
      {% assign pdf_url = 'assets/pdf/' | append: pdf_url | relative_url %}
    {% endunless %}

    <!-- Google Docs viewer embed: -->
    <iframe
      src="https://docs.google.com/viewer?url={{ pdf_url | absolute_url | uri_escape }}&embedded=true"
      title="Curriculum Vitae (Google Viewer)"
    ></iframe>
  </article>
</div>
