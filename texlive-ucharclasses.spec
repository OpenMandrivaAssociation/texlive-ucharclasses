Name:		texlive-ucharclasses
Version:	64782
Release:	2
Summary:	Switch fonts in XeTeX according to what is being processed
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/ucharclasses
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucharclasses.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucharclasses.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
