const orbitalPeriods: Record<string, number> = {
  earth: 1.0,
  mercury: 0.2408467,
  venus: 0.61519726,
  mars: 1.8808158,
  jupiter: 11.862615,
  saturn: 29.447498,
  uranus: 84.016846,
  neptune: 164.79132,
};

export function age(planet: unknown, seconds: unknown): number {
  const SECONDS_IN_EARTH_YEAR = 31_557_600;
  if (typeof planet !== 'string' || !(planet in orbitalPeriods)) throw new Error('Invalid planet');
  if (typeof seconds !== 'number') throw new Error('Invalid seconds');
  const age = seconds / (SECONDS_IN_EARTH_YEAR * orbitalPeriods[planet]);
  return Math.round(age * 100) / 100;
}
