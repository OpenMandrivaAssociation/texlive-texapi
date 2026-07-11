%global tl_name texapi
%global tl_revision 54080

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.04
Release:	%{tl_revision}.1
Summary:	Macros to write format-independent packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/texapi
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texapi.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texapi.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Texapi provides utility macros to write format-independent (and -aware)
packages. It is similar in spirit to the etoolbox, except that it isn't
tied to LaTeX. Tools include: engine and format detection, expansion
control, command definition and manipulation, various testing macros,
string operations, and highly customizable while and for loops. The
package requires e-TeX (and, should you want to compile its
documentation, the pitex package is also needed).

