const transcription: Record<string, string> = {
  'C': 'G',
  'G': 'C',
  'A': 'U',
  'T': 'A',
};

export function toRna(dna: string): string {
  return dna.split('').map(nucleotide => {
    if (!(nucleotide in transcription)) {
      throw new Error('Invalid input DNA.');
    }
    return transcription[nucleotide];
  }).join('');
}
