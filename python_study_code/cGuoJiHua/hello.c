#include <stdio.h>
#include <locale.h>
#include <libintl.h>

#define _(string) gettext(string)

#define LOCALEDIR "/usr/share/locale/"
#define PACKAGE "hello"

int main(int argc, char *argv[])
{
	setlocale(LC_ALL, "");
	bindtextdomain(PACKAGE, LOCALEDIR);
	textdomain(PACKAGE);

	printf(_("Hello world!\n"));

	return 0;
}

