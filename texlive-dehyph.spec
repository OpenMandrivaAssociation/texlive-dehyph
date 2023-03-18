Name:		texlive-dehyph
Version:	48599
Release:	2
Summary:	German hyphenation patterns for traditional orthography
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dehyph
License:	lppl1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dehyph.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-dehyph-exptl

%description
The package provides older hyphenation patterns for the German
language. Please note that by default only pdfLaTeX uses these
patterns (mainly for backwards compatibility). The older
packages ghyphen and gnhyph are now bundled together with
dehyph, and are no longer be updated. Both XeLaTeX and LuaLaTeX
use the current German hyphenation patterns taken from
Hyphenation patterns in UTF-8, and using the Experimental
hyphenation patterns for the German language package it is
possible to make pdfLaTeX use the new German patterns as well.

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/dehyph

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
