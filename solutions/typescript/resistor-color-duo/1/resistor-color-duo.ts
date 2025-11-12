const COLORS = [
	"black",
	"brown",
	"red",
	"orange",
	"yellow",
	"green",
	"blue",
	"violet",
	"grey",
	"white",
];

const colorCode = (color: string): number => {
	const res = COLORS.indexOf(color);
	return res === -1 ? 0 : res;
};

export function decodedValue([tens, ones]: string[]): number {
	return colorCode(tens) * 10 + colorCode(ones);
}
