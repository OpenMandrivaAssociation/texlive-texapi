Name:		texlive-texapi
Version:	54080
Release:	2
Summary:	Macros to write format-independent packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/texapi
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texapi.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texapi.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Texapi provides utility macros to write format-independent (and
-aware) packages. It is similar in spirit to the etoolbox,
except that it isn't tied to LaTeX. Tools include: engine and
format detection, expansion control, command definition and
manipulation, various testing macros, string operations, and
highly customizable while and for loops. The package requires
e-TeX (and, should you want to compile its documentation, the
pitex package is also needed).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/texapi/texapi.tex
%doc %{_texmfdistdir}/doc/generic/texapi/README
%doc %{_texmfdistdir}/doc/generic/texapi/texapi-doc.pdf
%doc %{_texmfdistdir}/doc/generic/texapi/texapi-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
