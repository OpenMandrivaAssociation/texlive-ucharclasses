# revision 27820
# category Package
# catalog-ctan /macros/xetex/latex/ucharclasses
# catalog-date 2012-09-26 16:27:49 +0200
# catalog-license pd
# catalog-version 2.0
Name:		texlive-ucharclasses
Version:	2.0
Release:	11
Summary:	Switch fonts in XeTeX according to what is being processed
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/latex/ucharclasses
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucharclasses.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucharclasses.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package takes care of switching fonts when you switch from
one Unicode block to another in the text of a document. This
way, you can write a document with no explicit font selection,
but a series of rules of the form "when entering block ...,
switch font to use ...".

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xelatex/ucharclasses/ucharclasses.sty
%doc %{_texmfdistdir}/doc/xelatex/ucharclasses/README
%doc %{_texmfdistdir}/doc/xelatex/ucharclasses/ucharclasses.pdf
%doc %{_texmfdistdir}/doc/xelatex/ucharclasses/ucharclasses.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
