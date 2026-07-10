%global tl_name dehyph
%global tl_revision 48599

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	German hyphenation patterns for traditional orthography
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/hyphenation/dehyph
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dehyph.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides older hyphenation patterns for the German language.
Please note that by default only pdfLaTeX uses these patterns (mainly
for backwards compatibility). The older packages ghyphen and gnhyph are
now bundled together with dehyph, and are no longer be updated. Both
XeLaTeX and LuaLaTeX use the current German hyphenation patterns taken
from Hyphenation patterns in UTF-8, and using the Experimental
hyphenation patterns for the German language package it is possible to
make pdfLaTeX use the new German patterns as well.

