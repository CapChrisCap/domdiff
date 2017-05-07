#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup, Tag


import domdiff

def test_additions():
    with open('tests/fixtures/index1.html', 'r') as f:
        html1 = f.read()
    with open('tests/fixtures/index2.html', 'r') as f:
        html2 = f.read()
    removals, additions = domdiff.diff(html1, html2)
    assert len(additions) == 5
    for addition in additions:
        assert isinstance(addition, Tag)
        print(addition)
    assert additions[0] == BeautifulSoup('<script src="_static/doctools.js" type="text/javascript"></script>').script
    assert additions[1] == BeautifulSoup('<p>A <tt class="docutils literal"><span class="pre">NavigableString</span></tt> is just like a Python Unicode string, except\nthat it also supports some of the features described in <a class="reference internal" href="#navigating-the-tree">Navigating\nthe tree</a> and <a class="reference internal" href="#searching-the-tree">Searching the tree</a>. You can convert a\n<tt class="docutils literal"><span class="pre">NavigableString</span></tt> to a Unicode string with <tt class="docutils literal"><span class="pre">unicode()</span></tt>:</p>').p
    assert additions[3] == BeautifulSoup('<span class="n">unicode_string</span>').span
    assert additions[4] == BeautifulSoup('<span class="c"># &lt;type \'unicode\'&gt;</span>').span
    for removal in removals:
        assert isinstance(removal, Tag)
        print(removal)
    assert len(removals) == 2
    assert removals[0] == BeautifulSoup('<script src="_static/jquery.js" type="text/javascript"></script>').script
    assert removals[1] == BeautifulSoup('<div class="section" id="beautifulsoup">\n<h2><tt class="docutils literal"><span class="pre">BeautifulSoup</span></tt><a class="headerlink" href="#beautifulsoup" title="Permalink to this headline">¶</a></h2>\n<p>The <tt class="docutils literal"><span class="pre">BeautifulSoup</span></tt> object itself represents the document as a\nwhole. For most purposes, you can treat it as a <a class="reference internal" href="#tag"><em>Tag</em></a>\nobject. This means it supports most of the methods described in\n<a class="reference internal" href="#navigating-the-tree">Navigating the tree</a> and <a class="reference internal" href="#searching-the-tree">Searching the tree</a>.</p>\n<p>Since the <tt class="docutils literal"><span class="pre">BeautifulSoup</span></tt> object doesn’t correspond to an actual\nHTML or XML tag, it has no name and no attributes. But sometimes it’s\nuseful to look at its <tt class="docutils literal"><span class="pre">.name</span></tt>, so it’s been given the special\n<tt class="docutils literal"><span class="pre">.name</span></tt> “[document]”:</p>\n<div class="highlight-python"><div class="highlight"><pre><span class="n">soup</span><span class="o">.</span><span class="n">name</span>\n<span class="c"># u\'[document]\'</span>\n</pre></div>\n</div>\n</div>').div


def test_stringify():
    soup = BeautifulSoup('<div><b class="boldest">Extremely bold</b></div>')
    assert domdiff._stringify(soup.div.b) == 'b/class=boldest'
    assert domdiff._stringify(soup.div) == 'div'


def test_path_representation():
    soup = BeautifulSoup('<div><b class="boldest thickest">Extremely bold</b></div>')
    assert domdiff._path_representation(soup.div.b) == 'html.body.div.b/class=boldest,thickest'
