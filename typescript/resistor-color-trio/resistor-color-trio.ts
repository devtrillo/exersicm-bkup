const COLORS = [
	`black`,
	`brown`,
	`red`,
	`orange`,
	`yellow`,
	`green`,
	`blue`,
	`violet`,
	`grey`,
	`white`,
] as const;

export type Color = (typeof COLORS)[number];

const ohms = [
	[1_000_000_000, "giga"],
	[1_000_000, "mega"],
	[1_000, "kilo"],
] as const;

export function decodedResistorValue([band1, band2, band3]: Color[]): string {

	const power = 10 ** COLORS.indexOf(band3);
  const num = ((COLORS.indexOf(band1) * 10) + COLORS.indexOf(band2)) * (power)
	const [divisor, prefix] = ohms.find(([divisor]) => num >= divisor) ?? [1, ""];
	return `${num / divisor} ${prefix}ohms`;
}
