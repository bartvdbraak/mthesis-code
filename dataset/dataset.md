# Dataset
This project is based on the RECOLA dataset, which is available for free to Academics and non-profit organisations under the terms of their EULA. There is also a commercial license.

Therefore, this codebase does not include the associated files. However, below will detail how the file structure should be for those who have access to RECOLA or want to use their data in the same format.

### File Tree

```
.
├── dataset.md
├── RECOLA-Annotation
│   ├── emotional_behaviour
│   │   ├── arousal
│   │   │   ├── P16.csv
│   │   │   ├── ...
│   │   │   └── P65.csv
│   │   └── valence
│   │       ├── P16.csv
│   │       ├── ...
│   │       └── P65.csv
│   └── social_behaviour
│       ├── agreement
│       │   ├── P16.csv
│       │   ├── ...
│       │   └── P65.csv
│       ├── dominance
│       │   ├── P16.csv
│       │   ├── ...
│       │   └── P65.csv
│       ├── engagement
│       │   ├── P16.csv
│       │   ├── ...
│       │   └── P65.csv
│       ├── performance
│       │   ├── P16.csv
│       │   ├── ...
│       │   └── P65.csv
│       └── rapport
│           ├── P16.csv
│           ├── ...
│           └── P65.csv
├── RECOLA-Audio-features
│   ├── P16.arff
│   ├── ...
│   └── P65.arff
├── RECOLA-Audio-probas
│   ├── P16.arff
│   ├── ...
│   └── P65.arff
├── RECOLA-Audio-recordings
│   ├── P16.wav
│   ├── ...
│   └── P65.wav
└── RECOLA-Audio_timings
    ├── P16.csv
    ├── ...
    └── P65.csv
```

### Document structures

#### CSV
Annotations have the following columns.
```
time;FM1 ;FM2 ;FM3 ;FF1 ;FF2 ;FF3
```
Audio timings have the following columns.
```
start;stop
```